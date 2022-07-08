from importlib.resources import path
import pathlib

HERE = pathlib.Path(".").absolute()
REPO_ROOT = HERE.parent()
data = REPO_ROOT / "data"
results = REPO_ROOT / "results"
checkpoints = results / "models"
figures = results / "figures"