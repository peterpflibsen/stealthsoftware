#!/bin/bash

for file in *
do
    echo "Processing file: $file"
    NUMBER=$(echo $file | tr -dc '0-9')

    MODULUS=$(($NUMBER % 2))

    if [ $MODULUS -eq 0 ]; then
        rm $file
    fi    
done

