#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
"""

from json import JSONDecodeError
import requests
import sys


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) == 3:
        q = sys.argv[2]
    else:
        q = ""
    r = requests.post(url, data={q: q})
    try:
        res = r.json()
        if res == {}:
            print("No result")
        else:
            print("[{}] {}".format(res['id'], res['name']))
    except JSONDecodeError as er:
        print("Not a valid JSON")
