import numpy as np
import pandas as pd
from matcher import data, train, predict, utils
from argparse import Namespace
import joblib
from config import config
from pathlib import Path

class Matcher():
    def __init__(self):
        # Params
        self.args_fp = "config/args.json"
        self.args = Namespace(**utils.load_dict(filepath=self.args_fp))
        self.num_recs = 1 + self.args.k_neighbors
        # Data
        self.df_tracks, self.train_X = data.etl_data()
        # Training and persisting model
        artifacts = train.train(self.args, self.train_X)
        joblib.dump(artifacts["model"], 
                    Path(config.STORES_DIR, "model.pkl"))

    def predict_tracks(self, seed_index):
        # Predict
        seed_index = int(seed_index)
        self.model = joblib.load(Path(config.STORES_DIR, "model.pkl"))
        print('seed track:',
              self.df_tracks.loc[seed_index,'track_name'],
              ',  by:',
              self.df_tracks.loc[seed_index,'artist_name'])
        seed_vector = self.train_X[seed_index].reshape(-1,1).T
        df_output = predict.predict(
                    self.args,
                    self.model,
                    seed_vector,
                    self.df_tracks)
        return df_output
