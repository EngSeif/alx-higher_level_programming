#!/usr/bin/python3
"""
a Python script that takes in a URL,
sends a request to the URL and displays
the value of the X-Request-Id variable
found in the header of the response.
"""
if __name__ == "__main__":
    from urllib import request
    from sys import argv

    if len(argv) != 2:
        print("Usage: python script.py <url>")

    url = argv[1]

    if type(url) is not str:
        print("Error in Url Entered")

    with request.urlopen(url) as response:
        header_name = "X-Request-Id"
        header_value = response.getheader(header_name)
        print(header_value)
