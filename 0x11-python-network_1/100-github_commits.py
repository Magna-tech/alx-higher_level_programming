#!/usr/bin/python3
"""A python script that prints the latest 10 commits on github"""
import sys
import requests


if __name__ == "__main__":
    req = requests.get("https://api.github.com/repos/{}/{}/commits"
                       .format(sys.argv[2], sys.argv[1]))
    commits = req.json()
    for commit in commits[:10]:
        print(commit.get('sha'), end=": ")
        print(commit.get('commit').get('author').get('name'))
