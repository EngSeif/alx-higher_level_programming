#!/usr/bin/python3
"""
a Python script that takes your GitHub
credentials (username and password)
and uses the GitHub API to display your id
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    username = argv[1]
    passwd = argv[2]
    url = 'https://api.github.com/user'
    headers = {
        "Authorization": f"{username} {passwd}"
    }
    r = requests.get(url, headers=headers)

    if r.status_code == 200:
        cont = r.json()
        print("hi")
        id = cont['id']
        print(id)
    else:
        print("None")
