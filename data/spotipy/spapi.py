from spotipy.oauth2 import SpotifyClientCredentials
import json
import spotipy


client_credentials_manager = SpotifyClientCredentials(client_id="cbe799bc34534312995a6fef92ee25f8",
                                                           client_secret="373fa05a5baa41399658e69285117387")
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace = False

# Audio Features
sp.audio_features(tids)[0]

# Search Artist
sp.search(q=artist_name, limit=50)

#
sp._get(feature['analysis_url'])
