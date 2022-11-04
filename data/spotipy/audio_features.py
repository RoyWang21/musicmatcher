
'''
 Extract track features using Spotify API, given playists data in .json format
'''

from __future__ import print_function    # (at top of module)
from spotipy.oauth2 import SpotifyClientCredentials
import json
import spotipy
import time
import sys
import pandas as pd
import json


# Read Spotify playlist Json File
dr = 'C:\\million_spotify_playlist\\'
file_json = 'challenge_set.json'

with open(dr + file_json) as json_file: 
    data = json.load(json_file)
playlists = data['playlists']

client_credentials_manager = SpotifyClientCredentials(client_id="cbe799bc34534312995a6fef92ee25f8",
                                                           client_secret="373fa05a5baa41399658e69285117387")
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace = False

## READ TRACK LIST, WITH TRACK ID ONLY 

#ids_pd = pd.read_csv( dr + 'track_list.csv', header = 0)
#ids_pd = ids_pd[:10000]
#ids_pd = ids_pd[:10]

## READ TRACK LIST PREPARED BY MARK, WITH FULL TRACK INFO

sample = pd.read_csv( dr + 'sample_tracks_from_fulllist.csv', header = 0)
track_id = sample.iloc[:,-1].drop_duplicates() # get unique songs by id
sample_unique_track = sample.loc[track_id.index] # filter sample to keep unique tracks only
ids_pd = track_id.str.split(":").str[-1] # get the last item after splitting with ':'

# extract the first 10000 tracks
ids_pd = ids_pd[:10000]


start = time.time()
features = []
for ind, tids in enumerate(ids_pd):
    if ind%100 == 0:
        print(ind)
    features.append(sp.audio_features(tids)[0])
    
delta = time.time() - start    
print("features retrieved in %.2f seconds" % (delta,))

df = pd.DataFrame(features)

# Reorder df column headers, move 'id' to the front
cols = list(df)
# move the column to head of list using index, pop and insert
cols.insert(0, cols.pop(cols.index('id')))
df = df.loc[:, cols]

df.to_csv(dr + 'extracted_tracks.csv', header = True, index = False)



# original code below
# shows acoustic features for tracks for the given artist

#if len(sys.argv) > 1:
#    artist_name = ' '.join(sys.argv[1:])
#else:
#    artist_name = ''
#
#results = sp.search(q=artist_name, limit=50)
#tids = []
#for i, t in enumerate(results['tracks']['items']):
##    print(' ', i, t['name'])
#    tids.append(t['uri'])

#    for feature in features:
#        print(json.dumps(feature, indent=4))
#        print()
#        print(features[0]['uri'])
#        analysis = sp._get(feature['analysis_url'])
#        print(json.dumps(analysis, indent=4))
#        print()
#delta = time.time() - start    
#print("features retrieved in %.2f seconds" % (delta,))
