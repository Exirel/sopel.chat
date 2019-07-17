#!/bin/bash
set -e

echo "Starting custom build script..."

echo "Generating changelogs & latest.json file"
python document_versions.py --news=_sopel/NEWS

echo "Installing Sopel globally for module autodoc script"
grep -v "pyenchant" _sopel/requirements.txt > _sopel/requirements.noenchant
mv _sopel/requirements.noenchant _sopel/requirements.txt
pip install ./_sopel

echo "Generating module command/config pages"
python document_sopel_modules.py --sopel=_sopel

echo "Building Jekyll site"
jekyll build

echo "Installing Sopel's dev dependencies"
pip install -r ./_sopel/dev-requirements.txt

echo "Building Sphinx docs"
cd _sopel/docs
make html
cd ../../

echo "Moving Sphinx docs to Jekyll output folder"
mv _sopel/docs/build/html _site/docs

echo "Finished custom build script!"
