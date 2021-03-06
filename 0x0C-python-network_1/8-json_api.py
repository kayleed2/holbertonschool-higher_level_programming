#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
"""

import requests
import sys


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) > 1 and type(sys.argv[1]) != int:
        q = sys.argv[1]
    else:
        q = ""
    r = requests.post(url, data={'q': q})
    try:
        res = r.json()
        if res == {}:
            print("No result")
        else:
            print("[{}] {}".format(res.get('id'), res.get('name')))
    except:
        print("Not a valid JSON")
