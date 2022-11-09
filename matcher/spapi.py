from spotipy.oauth2 import SpotifyClientCredentials
import json
import spotipy
from argparse import Namespace
from pathlib import Path
from config import config
from matcher import utils

args_fp = "config/args.json"
args = Namespace(**utils.load_dict(filepath=args_fp))
client_id = args.client_id
client_secret = args.client_secret

client_credentials_manager = SpotifyClientCredentials(client_id=client_id,
                                                           client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace = False

# test:
tid = "6cb0HzFQPN4BGADOmSzPCw"
# Audio Features
#print(sp.audio_features(tid)[0])
print(sp.track(tid, market=None))

# Search Artist
#sp.search(q=artist_name, limit=50)

#
#sp._get(feature['analysis_url'])
