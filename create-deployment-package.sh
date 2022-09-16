#!/bin/bash

if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

source ./venv/bin/activate
pip3 install -r requirements.txt
deactivate

cd venv/lib/python3.8/site-packages
zip -q -r ../../../../deployment.zip .
cd ../../../../
zip -q -g deployment-package.zip lambda_function.py bot.py quotes.json .env
