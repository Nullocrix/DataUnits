#!/bin/bash

# Build the package
python setup.py sdist bdist_wheel

# Install the package locally
pip install dist/*.whl
