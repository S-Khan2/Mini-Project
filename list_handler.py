# list_handler.py
# The module handles how to print a list for a user and how to select an option from it

import time

def print_list(items_list: list, is_indexed: bool, time_gap: float):
    '''items_list could be a list of menu options, list of products or list of couriers'''
    for i, item in enumerate(items_list):
        if is_indexed:
            print(f'  [{i}]  {item}')
        else:
            print(f'  {item}')
        # time_delay is the number of seconds between displaying successive items
        time.sleep(time_gap)

def print_dict():
    pass

def get_index(num: int, with_empty_str: bool) -> int:
    try:
        str_index = input("Enter an index: ").strip()
        if str_index:
            if int(str_index) in range(num):
                return int(str_index)
            else:
                print("Invalid Index: Please enter a valid integer\n")
                return get_index(num, with_empty_str)
        else:
            if with_empty_str:
                return None
            else:
                print("Invalid Index: Please enter a valid integer\n")
                return get_index(num, with_empty_str)
    except:
        print("Invalid Index: Please enter a valid integer\n")
        return get_index(num, with_empty_str)

# 5: 0 1 2 3 4 
def get_indices(num: int) -> list[int]:
    str_indices = input('Enter indices, separated by commas: ').split(",")

    def make_int(string: str) -> int:
        try:
            return int(string)
        except:
            return None

    def is_index(string) -> bool:
        return make_int(string) in range(num) 

    return [make_int(string) for string in str_indices if is_index(string)]

# print(get_indices(4))

def get_item_from(items_list: list):
    print_list(items_list, True, 0)
    try:
        index = int(input('Enter index: ').strip()) # TODO: handle invalid input
        return items_list[int(index)]
    except:
        print('InvalidIndex: Not a valid index')
        return None


def get_item_from2(items_list: list, with_empty_str: bool):
    # A valid_index is either an index of the list or the empty string
    valid_indices = [str(num) for num in range(len(items_list))]
    if with_empty_str:
        valid_indices.append("")
    print_list(items_list, True, 0)
    while True:
        index = input('Enter index: ').strip()  # TODO: handle invalid input
        if index in valid_indices:
            if index == "":
                return None
            else:
                return items_list[int(index)]
        else:
            print('InvalidIndex: Not a valid index')
