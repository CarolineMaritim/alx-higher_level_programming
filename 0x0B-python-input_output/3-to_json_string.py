#!/usr/bin/python3
"""function that returns the JSON representation of an obj"""
import json


def to_json_string(my_obj):
    """Main function"""
    return json.dumps(my_obj)
