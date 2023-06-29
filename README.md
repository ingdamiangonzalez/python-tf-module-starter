# python-tf-module-starter

This repository is a python package to deploy my terraform module template

## How to build and upload a new version

Change the version in pyproject.toml

[project]
version = "VERSION_NAME"  0.0.10

pip install build 
pip install twine

python -m build
python3 -m twine upload --repository testpypi dist/*