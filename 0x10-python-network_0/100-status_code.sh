#!/bin/bash
# A Bash script that sends a request to a URL passed as an argument, and displays only the status code of the response.
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Send a request to the URL and display only the status code of the response
curl -s -o /dev/null -w "%{http_code}" "$1"
