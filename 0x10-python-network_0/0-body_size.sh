#!/usr/bin/env bash
#script that takes in a URL and displays the size of the body of the response
wc stands for word count. As the name implies, it is mainly used for counting purpose.
curl -s "$1" | wc -c
