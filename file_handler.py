# file_handler.py
# Read/write a list of str from/to a textfile
# TODO: Read/write a list of dict from/into a CSV file
import json

def read_file(file_name: str):
    file_extension = get_extension(file_name)
    if file_extension == 'txt':
        return read_textfile(file_name)
    elif file_extension == 'json':
        return read_jsonfile(file_name)
    else:
        print('Cannot recognise file extension')
        return None


def write_file(file_name: str, contents):
    file_extension = get_extension(file_name)
    if file_extension == 'txt':
        write_textfile(file_name, contents)
    elif file_extension == 'json':
        write_jsonfile(file_name, contents)
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

def get_extension(file_name: str) -> str:
    return file_name.split('.')[-1].lower()
