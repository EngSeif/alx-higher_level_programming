#!/usr/bin/python3
"""
a Python script that takes in a URL,
sends a request to the URL and displays
the body of the response.
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
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
