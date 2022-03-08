#!/usr/bin/python3
"""Python script that fetches a url"""

import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
    print(html)
