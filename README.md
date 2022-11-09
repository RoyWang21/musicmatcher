# musicmatcher
A fast music recommender to match your preference

Create a new environment:
```
pyenv install 3.7.13
pyenv global 3.7.13
python3 -m venv venv
source venv/bin/activate
python3 -m pip install pip setuptools wheel
python3 -m pip install -e .
```

Usage:
- To run on local machine: uvicorn app:app --host 0.0.0.0 --port 8000

Demo:

Check live [DEMO](https://musicmatcher21.herokuapp.com/).

TODO:

- Feature:

	- enable searching by artist name, return artist's hot tracks
	- allow user to construct a seedlist, then auto-populate it with recs of similar and latest tracks.
	- allow user to give feedback to generated rec (one by one?) and follow up with new recs
- UI:
	- search result list with 'add' and 'play' button
	- list showing added seed tracks + generated recs
- Data:
	- use popular songs in library.
	- incorporate spotify API to fetch more recent musics.
	- candidate generation?
		- use spotify recommend api
		- use pre-loaded candidate tracks
		- combine
	- use fastAPI background task to load latest tracks via API?
