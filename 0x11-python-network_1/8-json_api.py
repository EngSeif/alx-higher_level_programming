#!/usr/bin/python3
"""
a Python script that takes in a letter
and sends a POST request to
http://0.0.0.0:5000/search_user with the
letter as a parameter.
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    url = "http://0.0.0.0:5000/search_user"

    if len(argv) < 2:
        q = ""
    else:
        q = argv[1]
    Data = {}
    Data['q'] = q
    try:
        r = requests.post(url, data=Data)
        cont = r.json()
        if len(cont) > 0:
            id = cont['id']
            name = cont['name']
            print("[{}] {}".format(id, name))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
