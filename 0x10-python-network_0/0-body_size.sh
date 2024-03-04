#!/bin/bash
# A Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response.
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Send a request to the URL and get the size of the response body in bytes
response_size=$(curl -sI "$1" | awk '/Content-Length/ {print $2}' | tr -d '\r')

# Display the size of the response body in bytes
echo "$response_size bytes"
