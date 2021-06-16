#!/bin/bash

TOPRINT=1
while [ $TOPRINT -le 99 ]
do
    echo $TOPRINT
    TOPRINT=$((TOPRINT+2))
done