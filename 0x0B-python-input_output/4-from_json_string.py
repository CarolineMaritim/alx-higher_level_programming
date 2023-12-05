#!/usr/bin/python3
"""function that returns an object rep by JSON"""
import json


def from_json_string(my_str):
    """Main function"""
    return json.loads(my_str)
