# Aim: To improve user experience from earlier version of app.py from Week 1

import os       # Helpful to clear terminal
import time     # Helpful to add waiting times
from logo import logo     # Collects my logo from 'logo.py'
from file_handler import * # read_file and write_file
from list_handler import print_list

PRODUCTS_FILE_NAME = 'products.txt'
COURIERS_FILE_NAME = 'couriers.txt'

main_menu_options = [
    'Exit', 
    'Products Menu',
    'Couriers Menu'
    ]

product_menu_options = [
    'Main Menu', 
    'Print Product List', 
    'Create New Product',
    'Update Existing Product', 
    'Delete Product'
    ]

couriers_menu_options = [
    'Main Menu',
    'Print Couriers List',
    'Create New Courier',
    'Update Existing Courier',
    'Delete Courier'
]

class Menu:
    def __init__(self, menu_type: str, menu_options: list[str], is_active=False):
        self.type = menu_type
        self.options = menu_options
        self.is_active = is_active
        # self.valid_options = range(len(menu_options))

    def switch_to(self, next_menu: 'Menu'):
        self.is_active = False
        next_menu.is_active = True

    def print_options(self):
        print(f'{self.type.title()} Menu:')
        print_list(self.options, True, 0)

    def get_option(self) -> int:
        display_logo()
        self.print_options()
        try:
            option = int(input(f'Enter option: ').strip())
            if option in range(len(self.options)):
                return option
            else:
                print('\nInputError: Please enter a valid integer')
                time.sleep(1)
                return self.get_option()
        except:
            print('\nInputError: Please enter a valid integer')
            time.sleep(1)
            return self.get_option()

    def delay_loading_menu(self, time_delay):
        time.sleep(time_delay / 2)
        # display_logo()
        print(f'\nLoading {self.type.title()} Menu ...')
        time.sleep(time_delay / 2)

class ItemsMenu(Menu):
    def __init__(self, menu_type: str, menu_options: list[str], file_name: str):
        super().__init__(menu_type, menu_options)
        self.file_name = file_name
        self.items = read_file(file_name)
    
    def save(self):
        write_file(self.file_name, self.items)

    def print_items(self, is_indexed: bool, time_delay: float, final_delay: float):
        print_list(self.items, is_indexed, time_delay)
        time.sleep(final_delay)
    
    def get_item_index(self) -> int:
        self.print_items(True, 0, 0.5)
        try:
            index = int(input(f'Enter the {self.type} number: '))
            if index in range(len(self.items)):
                return index
            else:
                print(f'InputError: Not a valid {self.type} number')
                return None
        except:
            print(f'InputError: Not a valid {self.type} number')
            return None

    def append_item(self):
        item = input(f'Enter the name of new {self.type}: ').strip().title()
        if not(item in self.items):
            self.items.append(item)
        else:
            print(f'{item} is already in our {self.type} list')

    def update_item(self):
        index = self.get_item_index()
        self.items[index] = input(
            f'Enter the updated {self.type} name: '
        ).strip().title()

    def delete_item(self):
        del self.items[self.get_item_index()]

def get_active(menus: list[Menu]) -> int:
    for index, is_active in enumerate([menu.is_active for menu in menus]):
        if is_active:
            return index
    return None


state_dict = {
    '0': [
        'Main Menu',
        main_menu_options
    ],
    '1': [
        'Products Menu',
        product_menu_options,
        PRODUCTS_FILE_NAME,  # Not needed, but could be handy if we update continuously
        [],  # list of products has index 3
        'Enter new product name: ',
        'Enter product number: '
    ],
    '2': [
        'Couriers Menu',
        couriers_menu_options,
        COURIERS_FILE_NAME,  # Not needed, but could be handy if we update continuously
        [],  # list of couriers has index 3
        'Enter new courier name: ',
        'Enter courier number: '
    ]
}

def display_menu_options(menu_key):
    print(state_dict[menu_key][0])
    for i, choice in enumerate(state_dict[menu_key][1]):
        print(f'  [{i}]  {choice}')

def get_menu_option(state_key):
    display_logo()
    display_menu_options(state_key)
    option = input(f'Enter option: ').strip()
    if int(option) in range(len(state_dict[state_key][1])):
        return option
    else:
        print('\nInputError: Please enter a valid integer')
        time.sleep(1)
        return get_menu_option(state_key)

def print_items(state_key, delay):
    for item in state_dict[state_key][3]:
        print(f'  {item}')
        time.sleep(delay)
    time.sleep(1)

def get_item_index(state_key):  # for state_key in ['1', '2']
    for i, item in enumerate(state_dict[state_key][3]):
        print(f'  [{i}]  {item}')
    index = int(input(state_dict[state_key][5]))
    if index in range(len(state_dict[state_key][3])):
        return index

def delay_loading_menu(state_key, time_delay):
    time.sleep(time_delay / 2)
    print(f'\nLoading {state_dict[state_key][0]} ...')
    time.sleep(time_delay / 2)

# Clear terminal
def clear_terminal():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

# Clear terminal and print logo
def display_logo():
    clear_terminal()
    print(logo)

# Close application after a delay
def close_app():
    display_logo()
    print('Closing application...')
    # Thought: Now we could store the product list update
    time.sleep(1)
    clear_terminal()
    print('Application closed')
    exit()

# App runs from here onwards
# Load products and couriers into lists
state_dict['1'][3] = read_file(PRODUCTS_FILE_NAME)
state_dict['2'][3] = read_file(COURIERS_FILE_NAME)

# Start at main menu
state_key = '0'
# menu_changed = False
while state_key != None:
    menu_option = get_menu_option(state_key)

    if state_key == '0' and menu_option == '0':
        state_key = None
        # menu_changed = False
    elif state_key == '0':
        state_key = menu_option
        # menu_changed = True
    elif menu_option == '0':  # Go to main menu
        state_key = '0'
        # menu_changed = True
    elif menu_option == '1':
        print()
        print_items(state_key, 0.5)
        # After printing add a delay: (i) Press enter (ii) Sleep for a little
        # input('Press ENTER to return to main menu')
        # menu_changed = False
    elif menu_option == '2':  # add item and save file
        # Add only if item is not in list
        item = input(state_dict[state_key][4]).strip().title()
        if not(item in state_dict[state_key][3]):
            state_dict[state_key][3].append(item)
            write_file(state_dict[state_key][2], state_dict[state_key][3])
        else:
            print(f'{item} is already in the list')
        # menu_changed = False
    elif menu_option == '3':  # update item and save file
        index = get_item_index(state_key)
        state_dict[state_key][3][index] = input(
            state_dict[state_key][4]).strip().title()
        write_file(state_dict[state_key][2], state_dict[state_key][3])
        # menu_changed = False
    elif menu_option == '4':  # delete item and save file
        del state_dict[state_key][3][get_item_index(state_key)]
        write_file(state_dict[state_key][2], state_dict[state_key][3])
        # menu_changed = False

    # Add a delay time from loading
    if state_key != None:
        delay_loading_menu(state_key, 1.5)

close_app()       