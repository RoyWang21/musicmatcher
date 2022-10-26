import numpy as np
import pandas as pd
from matcher import data, train, predict, utils
from argparse import Namespace
import joblib
from config import config
from pathlib import Path

if __name__ == "__main__":
    # Params
    args_fp = "config/args.json"
    args = Namespace(**utils.load_dict(filepath=args_fp))
    num_recs = 1 + args.k_neighbors

    # Data
    df_tracks, train_X = data.etl_data()

    # Training
    artifacts = train.train(args, train_X)
    joblib.dump(artifacts["model"], Path(config.STORES_DIR, "model.pkl"))

    # Random seed vector
    seed_index = 3419
    seed_vector = train_X[seed_index].reshape(-1,1).T
    print(df_tracks.loc[seed_index])

    # Predict
    df_output = predict.predict(
                args,
                artifacts['model'],
                seed_vector,
                df_tracks)
    print(df_output)
