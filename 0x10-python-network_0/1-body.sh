#!/bin/bash
# a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
S=$(curl -so /dev/null -w '%{http_code}' "$1"); if [ "$S" -eq 200 ]; then curl -s "$1"; fi
