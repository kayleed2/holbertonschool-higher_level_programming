#!/usr/bin/python3
"""Script that adds all arguments to a Python list
and then saves them to a file"""

import json
import sys
save = __import__("5-save_to_json_file").save_to_json_file
load = __import__("6-load_from_json_file").load_from_json_file

python_list = []

# save(python_list, 'add_item.json')

for arg in sys.argv[1:]:
    python_list.append(arg)

with open('add_item.json', 'a') as f:
    json.dump(python_list, f)
