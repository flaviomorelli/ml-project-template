#!/bin/zsh
source /Users/gnexx/opt/miniconda3/etc/profile.d/conda.sh
conda activate base
repo="{{ cookiecutter.repo_name }}"
mamba env create -f $repo.yml