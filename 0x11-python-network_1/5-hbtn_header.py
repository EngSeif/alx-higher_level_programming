#!/usr/bin/python3
"""
a Python script that takes in a URL,
sends a request to the URL and displays
the value of the variable X-Request-Id
in the response header
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    if len(argv) != 2:
        print("Usage: python script.py <url>")

    url = argv[1]

    if type(url) is not str:
        print("Error in Url Entered")

    r = requests.get(url)
    header_name = 'X-Request-Id'
    header_value = r.headers.get(header_name)
    print(header_value)
