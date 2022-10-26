import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors
from typing import Dict
from argparse import Namespace

def train(args, train_X) -> Dict:
    # Params
    num_recs = args.k_neighbors + 1

    # Model
    model_knn = NearestNeighbors(
        metric='cosine', 
        algorithm='brute', 
        n_neighbors=num_recs)

    # Training
    model_knn.fit(train_X)

    return {"model":model_knn}
