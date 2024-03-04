#!/bin/bash
# A Bash script that takes in a URL and displays all HTTP methods the server will accept.
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Send an OPTIONS request to the URL and display the allowed methods
allowed_methods=$(curl -s -i -X OPTIONS "$1" | awk '/Allow:/ {print $2}')
echo "$allowed_methods"
