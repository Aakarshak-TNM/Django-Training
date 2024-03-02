#!/usr/bin/env bash

# kill any servers that may be running in the background 
sudo pkill -f runserver

# kill frontend servers if you are deploying any frontend
# sudo pkill -f tailwind
# sudo pkill -f node

cd /home/ubuntu/Django-Training/

# # activate virtual environment
# python3 -m venv venv
# source venv/bin/activate

# install requirements.txt
# pip install -r /home/ubuntu/Django-Training/requirements.txt
# # run server
# screen -d -m python3 manage.py runserver 0:8000
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install

aws --version
aws configure

export AWS_ACCESS_KEY_ID=AKIAYS2NV6GEEGQGLJGM
export AWS_SECRET_ACCESS_KEY=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
export AWS_DEFAULT_REGION=ap-south-1

aws ecr get-login-password --region ap-south-1 | docker login --username AWS --password-stdin 590184051080.dkr.ecr.ap-south-1.amazonaws.com
sudo docker pull 590184051080.dkr.ecr.ap-south-1.amazonaws.com/django:latest
if [ $? -eq 0 ]; then
    echo "Docker image pulled successfully"
    # Run your Docker container with appropriate options
    # You can add more options like port mappings, volumes, environment variables, etc., as needed
sudo docker-compose build
sudo docker-compose up

else
    echo "Failed to pull Docker image from Amazon ECR"
    exit 1
fi