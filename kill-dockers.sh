#!/bin/bash

for x in $(sudo docker ps -a | tail --lines=+2 | cut -c -12)
do
    sudo docker rm -f $x
done
