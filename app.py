from fastapi import FastAPI, Request
from http import HTTPStatus
from matcher import main
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import numpy as np

# Define Application
app = FastAPI(
    title="MusicMatcher",
    description="A simple music recommender.",
    version="0.1",
)
templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.on_event("startup")
def _initialize():
    global matcher 
    matcher = main.Matcher()
    print('Initialized!')

@app.get("/", tags=["General"])
def _index(request: Request):
    """Health check."""
    response = {
        "message": HTTPStatus.OK.phrase,
        "status-code": HTTPStatus.OK,
        "data": {},
    }
    # Generate seed tracks
    n_tracks = matcher.df_tracks.shape[0]
    seed_list = np.random.choice(n_tracks,5)
#    return response
    return templates.TemplateResponse(
        "home.html", 
        {"request": request, 
         "track_name": list(matcher.df_tracks.loc[seed_list,'track_name'].values)})

@app.post("/recommend", tags=["recommendation"])
def _recommend(request: Request, seed_index):
    """Recommend the matched items given seed item"""
    recs = matcher.predict_tracks(seed_index)
    #recs = pd.Series(
    #    df_tracks.track_name.values, 
    #    index=df_tracks.track_id).to_dict()
    tracks = list(recs['track_name'].values)
    artists = list(recs['artist_name'].values)
    albums = list(recs['album_name'].values)
    response = {
        "message": HTTPStatus.OK.phrase,
        "status-code":HTTPStatus.OK,
        "data":{"tracks":tracks,
                "artists":artists,
                "alumbs":albums}
    }
    return response
