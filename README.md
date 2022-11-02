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

- UI:
- Data:
	- use popular songs in library.
	- incorporate spotify API to fetch more recent musics.
