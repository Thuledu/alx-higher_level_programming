#!/bin/bash
# A Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response.
URL=$1
curl -s -X DELETE $URL
