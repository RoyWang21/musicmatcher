import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors

def predict(args, model, seed_vector, df_tracks):
    # Params
    num_recs = args.k_neighbors + 1
    output_cols = args.output_cols

    # Model Prediction
    distances, indices = model.kneighbors(
        seed_vector, 
        n_neighbors = num_recs)

    # Organize output
    df_output = df_tracks.loc[indices[0][1:],output_cols]
    df_output['score'] = 1-distances[0][1:]*10

    return df_output
