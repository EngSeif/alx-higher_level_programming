#!/usr/bin/python3
"""
a Python script that takes your GitHub
credentials (username and password)
and uses the GitHub API to display your id
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    username = argv[2]
    Repo_name = argv[1]
    url = f"https://api.github.com/repos/{username}/{Repo_name}/commits"
    r = requests.get(url)

    commits = r.json()
    i = 0
    for commit in commits:
        if i == 10:
            break
        sha = commit.get("sha")
        author_name = commit.get('commit').get('author').get('name')
        print(f"{sha}: {author_name}")
        i = i + 1
