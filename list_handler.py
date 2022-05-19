# list_handler.py
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

def get_item_from(items_list: list):
    print_list(items_list, True, 0)
    try:
        index = int(input('Enter index: ').strip()) # TODO: handle invalid input
        return items_list[int(index)]
    except:
        print('InvalidIndex: Not a valid index')
        return None
