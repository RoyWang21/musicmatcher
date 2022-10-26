import numpy as np
import pandas as pd
from matcher import main
from argparse import Namespace
import joblib
from config import config
from pathlib import Path

if __name__ == "__main__":
    matcher = main.Matcher()
    recs = matcher.predict_tracks(seed_index=1465)
    print(recs)
