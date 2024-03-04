#!/bin/bash
# A Bash script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.
if [ -z "$1" ] || [ -z "$2" ]; then
  echo "Usage: $0 <URL> <filename>"
  exit 1
fi

json_data=$(cat "$2")

response_body=$(curl -s -X POST -H "Content-Type: application/json" -d "$json_data" "$1")
echo "$response_body"
