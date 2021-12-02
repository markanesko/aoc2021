#!/bin/bash

FOLDER_PATH="$(pwd)/${1}"
README_PATH="$FOLDER_PATH/README.md"
SRC_TEMPLATE="$(pwd)/template.py"
DST_TEPMLATE="${FOLDER_PATH}/main.py"

if [ ! -d $FOLDER_PATH ]; then
    mkdir $FOLDER_PATH;
    touch $README_PATH;
    cp $SRC_TEMPLATE $DST_TEPMLATE;
    echo "created new day"
fi