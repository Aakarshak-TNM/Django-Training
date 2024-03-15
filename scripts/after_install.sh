#!/usr/bin/env bash

# Kill any servers that may be running in the background
sudo pkill -f runserver

# Change directory to the Django project root
cd /home/ubuntu/Django-Training/

# Install the AWS CLI
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install

# Verify AWS CLI installation and configure if needed
aws --version
# aws configure  # Uncomment this line if you need to configure AWS CLI

# Set AWS credentials and region (consider using secure methods)
export AWS_ACCESS_KEY_ID=AKIAYS2NV6GEEGQGLJGM
export AWS_SECRET_ACCESS_KEY=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
export AWS_DEFAULT_REGION=ap-south-1

# Log in to Amazon ECR registry
aws ecr get-login-password --region ap-south-1 | docker login --username AWS --password-stdin 590184051080.dkr.ecr.ap-south-1.amazonaws.com
# Pull the Docker image from Amazon ECR (if needed)
sudo docker pull 590184051080.dkr.ecr.ap-south-1.amazonaws.com/django-ecr:latest
# Build and start the Docker Compose services
sudo docker-compose up -d

# Docker Done!