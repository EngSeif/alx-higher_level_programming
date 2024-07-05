#!/usr/bin/python3
"""
a Python script that fetches https://alx-intranet.hbtn.io/status
"""
if __name__ == "__main__":
    from urllib import request
    url = 'https://alx-intranet.hbtn.io/status'
    with request.urlopen(url) as response:
        body = response.read()
        decode = body.decode('utf-8')
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(decode))
