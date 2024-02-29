#!/bin/bash

if[-d 'env']
then
echo "Virtual env exists"
else
    python3 -m venv env
fi

echo $PWD
source env\bin\activate

if[-d 'logs']
then
echo "Log Folder exists"
else
    mkdir logs
    touch logs/error.log logs/access.log
fi

sudo chmod -R 777 logs
echo "envsetup finishes"