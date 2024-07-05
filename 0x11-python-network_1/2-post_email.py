#!/usr/bin/python3
"""
a Python script that takes in a URL and an email,
sends a POST request to the passed URL with the
email as a parameter, and displays the body of
the response (decoded in utf-8)
"""
if __name__ == "__main__":
    from urllib import request, parse
    from sys import argv

    if len(argv) != 3:
        print("Usage: python script.py <url> <email>")

    url = argv[1]
    input_email = argv[2]

    if type(url) is not str:
        print("Error in Type Url Entered")

    if type(input_email) is not str:
        print("Error in Type Email Entered")

    data = {}
    data['email'] = input_email
    email = parse.urlencode(data)
    email = email.encode('utf-8')
    req = request.Request(url, email)
    with request.urlopen(req) as response:
        body = response.read().decode('utf-8')
        print(body)
