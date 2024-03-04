#!/bin/bash
# A Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response.
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Send a GET request to the URL with the header variable X-School-User-Id set to 98 and display the body of the response
response_body=$(curl -s -H "X-School-User-Id: 98" "$1")
echo "$response_body"
