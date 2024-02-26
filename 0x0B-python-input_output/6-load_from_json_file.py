#!/usr/bin/python3
"""Define load_from_json_file Methode"""
import json


def load_from_json_file(filename):
    """ function that creates an Object from a “JSON file"""
    with open(filename, "r", encoding="uft-8") as file:
        return json.load(file)
