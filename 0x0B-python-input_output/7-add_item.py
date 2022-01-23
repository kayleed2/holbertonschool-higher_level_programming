#!/usr/bin/python3
"""Script that adds all arguments to a Python list
and then saves them to a file"""

import json
import sys
import os.path
save = __import__("5-save_to_json_file").save_to_json_file
load = __import__("6-load_from_json_file").load_from_json_file

python_list = []

for arg in sys.argv[1:]:
    python_list.append(arg)

flag = os.path.exists('add_item.json')

if flag is False:
    save(python_list, 'add_item.json')

if flag is True:
    existing = load('add_item.json')
    existing.extend(python_list)
    with open('add_item.json', 'w') as f:
        json.dump(existing, f)
