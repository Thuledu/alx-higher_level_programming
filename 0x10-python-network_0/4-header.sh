#!/bin/bash
# A Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response.
URL=$1
curl -s -H "X-School-User-Id: 98" $URL
