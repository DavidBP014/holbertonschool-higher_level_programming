#!/usr/bin/python3
"""
Script that adds all arguments to a
Python list, and then save them to a file
"""


import sys
import os
my_list = []
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

if __name__ == "__main__":
    validator = os.path.exists("add_item.json")
    if validator is True:
        my_list = load_from_json_file("add_item.json")
    for i in sys.argv[1:]:
        my_list.append(i)

    save_to_json_file(my_list, "add_item.json")
