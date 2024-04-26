#!/usr/bin/python3
"""
A Python script that receives a URL, sends a
request to it,and shows the body of the response.
"""
import requests
from sys import argv

if __name__ == "__main__":
    resp = requests.get(argv[1])
    code = resp.status_code
    if code >= 400:
        print("Error code: {}".format(code))
    else:
        print(resp.text)
