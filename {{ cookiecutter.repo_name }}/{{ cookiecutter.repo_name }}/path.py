from importlib.resources import path
import pathlib

HERE = pathlib.Path(__file__).absolute().parent
REPO_ROOT = HERE.parent
data = REPO_ROOT / "data"
results = REPO_ROOT / "results"
figures = results / "figures"
checkpoints = results / "models"
scripts = REPO_ROOT / "scripts"
runs = REPO_ROOT / "runs"