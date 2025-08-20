#!/bin/bash

# Deploy script for GitHub Pages
# This script builds both language versions and prepares them for deployment

echo "🚀 Building Multilingual Jupyter Book for Deployment"

# Clean previous builds
echo "🧹 Cleaning previous builds..."
rm -rf _build_fr _build_en docs/

# Build both versions
echo "🔨 Building both language versions..."
python build_multilingual.py

# Create docs directory for GitHub Pages
echo "📁 Preparing GitHub Pages deployment..."
mkdir -p docs

# Copy built files to docs
cp -r _build_fr/_build/html docs/fr
cp -r _build_en/_build/html docs/en
cp index.html docs/

# remove unnecessary files
rm -rf _build_fr _build_en

# Create .nojekyll file to prevent Jekyll processing
touch docs/.nojekyll

# Create CNAME file if domain is specified
if [ ! -z "$1" ]; then
    echo "$1" > docs/CNAME
    echo "🌐 Created CNAME file for domain: $1"
fi

echo "✅ Deployment ready!"
echo "📁 Files are in docs/ directory"
echo "🌐 Upload docs/ to GitHub Pages or serve locally with:"
echo "   cd docs && python -m http.server 8000"