#!/usr/bin/python3
"""A Python script that takes in a URL and an email, sends a POST request to
the passed URL with the email as a parameter, and displays the body of the
response (decoded in utf-8)"""
import urllib.parse
import urllib.request
import sys


if __name__ == "__main__":
    link = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    req = urllib.request.Request(link, data)
    with urllib.request.urlopen(req) as page:
        print(page.read().decode("utf-8"))
