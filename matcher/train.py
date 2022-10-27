from typing import Dict

import numpy as np
from sklearn.neighbors import NearestNeighbors


def train(args, train_X: np.ndarray) -> Dict:
    """
    Train the KNN model to calculate cosine similarities between tracks

    Args:
        args: input parameters from config
        train_X: (np.ndarray) numerical features of tracks in library

    Returns:
        Dict: artifact containing the trained model
    """
    # Params
    num_recs = args.k_neighbors + 1

    # Model
    model_knn = NearestNeighbors(metric="cosine", algorithm="brute", n_neighbors=num_recs)

    # Training
    model_knn.fit(train_X)

    return {"model": model_knn}
