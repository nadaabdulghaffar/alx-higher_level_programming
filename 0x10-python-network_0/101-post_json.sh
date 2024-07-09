#!/bin/bash
# Script that takes in a URL, sends a POST request to the passed URL
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
