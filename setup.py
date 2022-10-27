# setup.py
from pathlib import Path

from setuptools import find_namespace_packages, setup

# load requirements.txt
BASE_DIR = Path(__file__).parent
with open(Path(BASE_DIR, "requirements.txt"), "r") as file:
    required_packages = [ln.strip() for ln in file.readlines()]

style_packages = ["black==22.3.0", "flake8==3.9.2", "isort==5.10.1"]

# setup.py
setup(
    name="musicmatcher",
    version=0.1,
    description="A fast music recommender to match your preference",
    author="Roy Wang",
    author_email="royyi2012@gmail.com",
    url="https://to be finished",
    python_requires="==3.7.13",
    install_requires=[required_packages],
    extras_require={"dev": style_packages},
)
