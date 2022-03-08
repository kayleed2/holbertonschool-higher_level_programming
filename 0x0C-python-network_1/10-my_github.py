#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
"""

import requests
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    pwd = sys.argv[2]
    r = requests.get('https://api.github.com/user', auth=(user, pwd))
    if r.status_code > 400:
        print("None")
    else:
        new = r.json()
        print(new['id'])
