#!/bin/bash
# A Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response.
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Send a DELETE request to the URL and display the body of the response
response_body=$(curl -s -X DELETE "$1")
echo "$response_body"
