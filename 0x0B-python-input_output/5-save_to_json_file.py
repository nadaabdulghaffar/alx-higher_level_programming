#!/usr/bin/python3
"""Define save_to_json_file Methode"""
import json


def save_to_json_file(my_obj, filename):
    """function writes an Object to a text file"""
    str_obj = json.dumps(my_obj)
    with open(filename, "w") as file:
        file.write(str_obj)
