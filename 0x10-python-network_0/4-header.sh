#!/bin/bash
#script that takes in a URL as an argument, header variable X-School-User-Id must be sent with the value 98
curl -sL -H "X-School-User-Id: 98" "$1"
