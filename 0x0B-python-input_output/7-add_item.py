#!/usr/bin/python3
"""
This Script Contains : adds all arguments to a Python list, and then save them to a file
"""

import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

if __name__ == "__main__":
    args = sys.argv[1:]

    try:
        existing_items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        existing_items = []
    existing_items.extend(args)
    save_to_json_file(existing_items, "add_item.json")
