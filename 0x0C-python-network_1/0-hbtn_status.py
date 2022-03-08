#!/usr/bin/python3
"""Python script that fetches a url"""

import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        print("Body response:")
        print('\t- type: {}'.format(type(response.text)))
        print('\t- content: {}'.format(response.text))
