#!/bin/bash
set -e

echo "Starting custom build script..."

echo "Generating changelogs & latest.json file"
python3 document_versions.py --news=_sopel/NEWS

echo "Installing Sopel globally for plugin autodoc script"
grep -v "pyenchant" _sopel/requirements.txt > _sopel/requirements.noenchant
mv _sopel/requirements.noenchant _sopel/requirements.txt
pip3 install ./_sopel

echo "Generating plugin command/config pages"
python3 document_sopel_plugins.py --sopel=_sopel

echo "Building Jekyll site"
jekyll build

echo "Installing Sphinx"
pip3 install sphinx

echo "Building Sphinx docs"
cd _sopel/docs
make html
cd ../../

echo "Moving Sphinx docs to Jekyll output folder"
mv _sopel/docs/build/html _site/docs

echo "Finished custom build script!"
