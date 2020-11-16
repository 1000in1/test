#!/bin/bash

cd ../test
while true
do
    python3 ../test_github/getIp.py > data.txt
    git add data.txt
    git commit -m "update data"
    git push

    sleep 60
done
