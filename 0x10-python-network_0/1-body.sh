#!/bin/bash
# A Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response.
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Send a GET request to the URL and display the body if the status code is 200
response_code=$(curl -s -o /dev/null -w "%{http_code}" "$1")
if [ "$response_code" -eq 200 ]; then
  curl -s "$1"
fi
