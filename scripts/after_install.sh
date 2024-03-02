#!/usr/bin/env bash

# kill any servers that may be running in the background 
sudo pkill -f runserver

# kill frontend servers if you are deploying any frontend
# sudo pkill -f tailwind
# sudo pkill -f node

cd ${PROJECT_DIR}

# activate virtual environment
python3 -m venv ${VIRTUAL_ENV}
source ${VIRTUAL_ENV}/bin/activate

# install requirements.txt
pip install -r ${REQUIREMENTS_FILE}
# run server
screen -d -m python3 manage.py runserver 0:8000