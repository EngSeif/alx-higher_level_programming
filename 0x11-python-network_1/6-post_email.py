#!/usr/bin/python3
"""
a Python script that takes in a URL
and an email address, sends a POST
request to the passed URL with the
email as a parameter, and finally
displays the body of the response.
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    if len(argv) != 3:
        print("Usage: python script.py <url> <email>")

    url = argv[1]
    input_email = argv[2]

    if type(url) is not str:
        print("Error in Type Url Entered")

    if type(input_email) is not str:
        print("Error in Type Email Entered")

    email = {}
    email['email'] = input_email
    r = requests.post(url, data=email)
    print(r.text)
