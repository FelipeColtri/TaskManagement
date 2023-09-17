#!/usr/bin/env python

import os
import sys
import json
import time
import argparse
import datetime as dt

# Install location
file_path = os.getcwd()
file_name = "example.json"

# Global variables
dataset = None

# If file not exist, crate base json
if not os.path.exists(file_name):
    with open('{}/{}'.format(file_path, file_name), 'w') as file:
        file.write('{}\n')

# Open json file
with open('{}/{}'.format(file_path, file_name)) as file:
    dataset = json.load(file)

# PART OF GENERIC FUNCTIONS
def dataset_save():
    with open('{}/{}'.format(file_path, file_name), 'w') as file:
        json.dump(dataset, file)

# PART OF HEADERS
def header_list():
    print('{}\t {:{}} {}\n{}'.format('ID', 'ACRONYM', 10, 'QUANTITY', '-' * 28))

    count = 1
    for key in dataset:
        print('{:02d}\t {:{}} {}'.format(count, key, 10, len(dataset[key])))
        count += 1

def header_add(header):
    if header not in dataset:
        dataset[header] = {}
        dataset_save()
    else:
        print("Error: Header Already Exist!")

def header_remove(header):
    if header in dataset:
        del dataset[header]
        dataset_save()
    else:
        print("Error: Header not Exist!")

def header_edit(header_old, header_new):
    if header_old == header_new:
        print("Same Names!")
        exit()

    if header_new == 'NONE':
        print("Error: New Name Required! \n[-E <old_header_name> -n <new_header_name>]")
        exit()
        
        if header_new in dataset:
        print("Error: Name Conflicts!")
        exit()

    if header_old in dataset:
        dataset[header_new] = dataset[header_old]
        del dataset[header_old]
        dataset_save()
    else:
        print("Error: Header not Exist!")

# PART OF TASKS
def task_list(header):    
    try:
        print('{}\t {:{}} {}\n{}'.format('ID', 'DESCRIPITION', 35, 'DATE [DD/MM/YYYY]', '-' * 62))
        count = 1
        for key in dataset[header]:
            print('{:02d}\t {:{}} {}'.format(count, key, 35, dataset[header][key]))
            count += 1
    except:
        print("Error: Header not Exist!")

# PART OF MAIN FUNCION
if __name__ == '__main__':
    # All arguments available
    parser = argparse.ArgumentParser()
    
    # Exclusive and Required group of arguments
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-l", "--list", action='store_true', help="List All Tasks")
    group.add_argument("-a", "--add", help="Add Task")
    group.add_argument("-e", "--edit", help="Edit Task")
    group.add_argument("-r", "--remove", help="Remove Tesk")
    group.add_argument("-o", "--order", help="Shows Tasks in Chronological Order")
    group.add_argument("-A", "--Add", help="Add Header")
    group.add_argument("-E", "--Edit", help="Edit Header")
    group.add_argument("-R", "--Remove", help="Remove Header")
    #group.add_argument("-", "--", help="")
    
    # Optional arguments
    parser.add_argument("-n", "--name", help="Name of Task or Header")
    parser.add_argument("-d", "--date", help="Date of Task")
    #parser.add_argument("-", "--", help="")

    # Atribute all arguments
    args = parser.parse_args()

    # Actions with arguments
    if args.list:
        if args.name:
            task_list(str(args.name).upper())
        else:
            header_list()
    elif args.Add:
        header_add(str(args.Add).upper())
    elif args.Remove:
        header_remove(str(args.Remove).upper())
    elif args.Edit:
        header_edit(str(args.Edit).upper(), str(args.name).upper())
