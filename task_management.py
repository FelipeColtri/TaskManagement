#!/usr/bin/env python

import os
import sys
import json
import time
import argparse
import datetime as dt

# Install location
file_path = os.getcwd()

# Global variables
data = None

# Open json file
with open('{}/data.json'.format(file_path)) as file:
    data = json.load(file)
    file.close()

if __name__ == '__main__':
    # All arguments available
    parser = argparse.ArgumentParser()
    
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-l", "--list", help="List All Tasks")
    group.add_argument("-a", "--add", help="Add Task")
    group.add_argument("-e", "--edit", help="Edit Task")
    group.add_argument("-r", "--remove", help="Remove Tesk")
    group.add_argument("-o", "--order", help="Shows Tasks in Chronological Order")
    group.add_argument("-L", "--List", help="List All Headers")
    group.add_argument("-A", "--Add", help="Add Header")
    group.add_argument("-E", "--Edit", help="Edit Header")
    group.add_argument("-R", "--Remove", help="Remove Header")
    #group.add_argument("-", "--", help="")
    parser.add_argument("-n", "--name", help="Name of Task or Header")
    parser.add_argument("-d", "--date", help="Date of Task")
    #parser.add_argument("-", "--", help="")

    args = parser.parse_args()
    print(args) 
    if args.add:
        print(args.add)
        if args.name:
            print(args.name)
        if args.date:
            print(args.date)
