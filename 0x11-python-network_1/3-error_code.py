#!/usr/bin/python3
"""
Write a Python script that takes in a URL,
sends a request to the URL and displays the
body of the response (decoded in utf-8).
"""
if __name__ == "__main__":
    from urllib import request
    import urllib
    from sys import argv

    try:
        if len(argv) != 2:
            print("Usage: python script.py <url>")

        url = argv[1]

        if type(url) is not str:
            print("Error in Url Entered")

        with request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
