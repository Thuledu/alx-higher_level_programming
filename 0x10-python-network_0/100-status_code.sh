#!/bin/bash
# A Bash script that sends a request to a URL passed as an argument, and displays only the status code of the response.
URL=$1
curl -s -o /dev/null -w "%{http_code}" $URL
