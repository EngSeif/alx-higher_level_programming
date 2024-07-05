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
    Repo_name = argv[2]
    url = f"https://api.github.com/repos/{username}/{Repo_name}/commits"
    r = requests.get(url)

    for coms in r.json():
        sha = coms['sha']
        name = coms['commit']['author']['name']
        print(f"{sha}: {name}")
