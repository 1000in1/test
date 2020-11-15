#!/bin/bash

while true
do
    python3 getIp.py > data.txt
    git add data.txt
    git commit -m "update data"
    git push

    sleep 60
done
