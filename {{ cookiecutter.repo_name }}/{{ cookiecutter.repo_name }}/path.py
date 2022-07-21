from importlib.resources import path
import pathlib

REPO_ROOT = pathlib.Path(".").absolute()
data = REPO_ROOT / "data"
results = REPO_ROOT / "results"
figures = results / "figures"
checkpoints = results / "models"
scripts = REPO_ROOT / "scripts"
runs = REPO_ROOT / "runs"