from importlib.resources import path
import pathlib

HERE = pathlib.Path(".")
REPO_ROOT = HERE.parent()
data = REPO_ROOT / "data"
results = REPO_ROOT / "results"
figures = results / "figures"
checkpoints = results / "models"
scripts = REPO_ROOT / "scripts"