#!/bin/bash
# A Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response.
URL=$1
FILENAME=$(mktemp)
curl -s -o $FILENAME -w "%{http_code}" $URL | {
    read status
    if [ $status -eq 200 ]; then
        cat $FILENAME
    fi
    rm $FILENAME
}
