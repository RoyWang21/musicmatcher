import logging
import sys
from argparse import Namespace
from pathlib import Path

import joblib
import pandas as pd

from config import config
from matcher import data, predict, train, utils

logging.basicConfig(stream=sys.stdout, level=logging.INFO)


class Matcher:
    """The main object of the app contains data and model."""

    def __init__(self):
        """
        Initialization: Load datasets, train and persist the model.
        """
        # Params
        self.args_fp = "config/args.json"
        self.args = Namespace(**utils.load_dict(filepath=self.args_fp))
        self.num_recs = 1 + self.args.k_neighbors
        # Data
        try:
            self.df_tracks, self.train_X = data.etl_data()
            logging.info("Data extracted successfully.")
        except Exception as e:
            logging.error(("Data extraction failed, due to:", e))
        # Training and persisting model
        try:
            artifacts = train.train(self.args, self.train_X)
            logging.info("Model trained successfully.")
            joblib.dump(artifacts["model"], Path(config.STORES_DIR, "model.pkl"))
            logging.info("Model persisted successfully.")
        except Exception as e:
            logging.error(("Model training and saving failed, due to:", e))

    def predict_tracks(self, seed_index: int = 0) -> pd.DataFrame:
        """
        Inference for recommendation ouput
        Args:
            seed_index(int): the index of seed track in the library dataframe
        Returns:
            pd.DataFrame: output info of recommended tracks
        """
        # Predict
        self.model = joblib.load(Path(config.STORES_DIR, "model.pkl"))
        seed_vector = self.train_X[seed_index].reshape(1, -1)
        logging.info("Predicting neighbors of seed track.")
        df_output = predict.predict(self.args, self.model, seed_vector, self.df_tracks)
        return df_output
