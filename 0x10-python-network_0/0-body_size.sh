#!/bin/bash
# a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -so /dev/null "$1" -w '%{size_download}\n'
