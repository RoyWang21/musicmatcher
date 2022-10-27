from argparse import Namespace
from pathlib import Path

import joblib
import numpy as np
import pandas as pd

from config import config
from matcher import main

if __name__ == "__main__":
    matcher = main.Matcher()
    recs = matcher.predict_tracks(seed_index=1465)
    print(recs)
