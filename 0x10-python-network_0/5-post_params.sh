#!/bin/bash
# A Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Send a POST request to the URL with the specified variables and their values and display the body of the response
response_body=$(curl -s -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1")
echo "$response_body"
