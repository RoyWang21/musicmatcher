from fastapi import FastAPI, Request
from http import HTTPStatus
from matcher import main

# Define Application
app = FastAPI(
    title="MusicMatcher",
    description="A simple music recommender.",
    version="0.1",
)

@app.on_event("startup")
def initialize():
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
    return response
@app.post("/recommend", tags=["recommendation"])
def _recommend(request: Request, seed_index):
    recs = matcher.predict_tracks(seed_index)
    response = {
        "message": HTTPStatus.OK.phrase,
        "status-code":HTTPStatus.OK,
        "data":{"rec1":recs['track_name'].values[0]}
    }
    return response
