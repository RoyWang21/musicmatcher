import logging
import sys
from http import HTTPStatus

import numpy as np
from fastapi import FastAPI, Form, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from matcher import main

# Define Application
app = FastAPI(
    title="MusicMatcher",
    description="A simple music recommender.",
    version="0.1",
)
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")
logging.basicConfig(stream=sys.stdout, level=logging.INFO)


@app.on_event("startup")
def _initialize():
    """initialize model&data object when app start"""
    global matcher
    matcher = main.Matcher()
    logging.info("App initialized!")


@app.post("/")
@app.get("/", tags=["General"])
def _index(request: Request):
    """Home Page"""
    response = {
        "message": HTTPStatus.OK.phrase,
        "status-code": HTTPStatus.OK,
        "data": {},
    }
    return templates.TemplateResponse(
        "home.html",
        {
            "request": request,
        },
    )


@app.post("/recommend", tags=["recommendation"])
def _recommend(request: Request, artist_input: str = Form(), track_input: str = Form()):
    """Recommend the matched items given seed item"""
    logging.info(("user input:", artist_input, track_input))
    # find the seed track from library
    try:
        seed_index = matcher.df_tracks.loc[
            (matcher.df_tracks["track_name"] == track_input)
            & (matcher.df_tracks["artist_name"] == artist_input)
        ].index.values[0]
        assert type(seed_index) is np.int64, "Warning: seed_index is not int type."
        seed_uri = str(matcher.df_tracks.loc[[seed_index], "track_id"].values[0])
    except Exception as e:
        logging.error(("Seed track not found, due to:", e))
    # generate recommendation based on the seed track
    try:
        recs = matcher.predict_tracks(seed_index)
        posts = recs.to_dict(orient="records")
    except Exception as e:
        logging.error(("Prediction failed due to:", e))
    return templates.TemplateResponse(
        "recommend.html",
        {
            "request": request,
            "posts": posts,
            "artist_input": artist_input,
            "track_input": track_input,
            "track_uri": seed_uri,
            "liked": "",
        },
    )
