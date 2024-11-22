#!/bin/bash

# Ensure the script is executed with 2 arguments
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <URL> <TITLE>"
    exit 1
fi

URL=$1
TITLE=$2

# Check if the virtual environment exists
if [ ! -d ".venv" ]; then
    echo "Error: Virtual environment '.venv' not found."
    echo "Create one using 'python -m venv .venv' and install dependencies."
    exit 1
fi

# Activate the virtual environment
source .venv/bin/activate

# Run the Python script with arguments
python create_ebook.py "$URL" "$TITLE"

# Deactivate the virtual environment
deactivate
