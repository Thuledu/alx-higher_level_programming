#!/bin/bash
# A Bash script that takes in a URL and displays all HTTP methods the server will accept.
URL=$1
curl -sI $URL | grep -i Allow | cut -d ' ' -f 2-
