# file_handler.py
# Read/write a list of str from/to a TXT/JSON/CSV file

import json
import csv

def read_file(file_name: str):
    file_extension = get_extension(file_name)
    if file_extension == 'txt':
        return read_textfile(file_name)
    elif file_extension == 'json':
        return read_jsonfile(file_name)
    elif file_extension == 'csv':
        return read_csvfile(file_name)
    else:
        print('Cannot recognise file extension')
        return None


def write_file(file_name: str, contents, fieldnames=None):
    file_extension = get_extension(file_name)
    if file_extension == 'txt':
        write_textfile(file_name, contents)
    elif file_extension == 'json':
        write_jsonfile(file_name, contents)
    elif file_extension == 'csv':
        write_csvfile(file_name, contents, fieldnames)
    else:
        print('Cannot recognise file extension')


def read_textfile(file_name: str) -> list[str]:
    try:
        with open(file_name, 'r') as f:
            return [line.strip() for line in f.readlines()]
    except:
        return []
        # Could instead raise an exception, then handle in the main app file
        # Raising an exception isn't a good idea


def write_textfile(file_name: str, our_list: list[str]):
    try:
        with open(file_name, 'w') as f:
            for item in our_list:
                f.write(f'{item}\n')
    except Exception as e:
        print(e)

def read_jsonfile(file_name: str) -> list[dict]:
    try:
        with open(file_name, 'r') as f:
            return json.load(f)
    except:
        return []

def write_jsonfile(file_name: str, json_list: list[dict]):
    try:
        with open(file_name, 'w') as json_file:
            json.dump(json_list, json_file, indent=4) # human readable json file
    except Exception as e:
        print(e)

def read_csvfile(file_name: str) -> list[dict[str, str]]:
    try:
        list_dicts = []
        with open(file_name, "r") as f:
            csv_reader = csv.DictReader(f)
            for row in csv_reader:
                list_dicts.append(row)
    except FileNotFoundError:
        list_dicts = []
    return list_dicts

def write_csvfile(
    file_name: str, list_dicts: list[dict[str, str]], fieldnames: list[str]
):
    with open(file_name, "w") as file:
        csv_writer = csv.DictWriter(file, fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(list_dicts)

def get_extension(file_name: str) -> str:
    return file_name.split('.')[-1].lower()
