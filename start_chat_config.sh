#!/usr/bin/env bash

# Script to inizializated project and run all migrations and 
# install requirements
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
echo $DIR
echo "Install enviroment..."
sudo apt-get -y install python3-pip
sudo pip3 install virtualenv
virtualenv -p python3 .env
echo "Activate enviroment"
source .env/bin/activate

echo "Install Requiremets"
pip install -r requirements.txt


echo "Make migrations"
python3 manage.py makemigrations
python3 manage.py migrate

echo "Run Docker redis"
sudo docker run -p 6379:6379 -d redis:5


echo "Run project"
python3 manage.py runserver 8000
