# Aim: To improve user experience from earlier version of app.py from Week 1

import os       # Helpful to clear terminal
import time     # Helpful to add waiting times
from logo import logo     # Collects my logo from 'logo.py'
from file_handler import read_file, write_file
from list_handler import print_list

PRODUCTS_FILE_NAME = 'products.txt'
COURIERS_FILE_NAME = 'couriers.txt'
ORDERS_FILE_NAME = 'orders.json'

main_menu_options = [
    'Exit', 
    'Products Menu',
    'Couriers Menu',
    'Orders Menu'
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

order_menu_options = [
    'Main Menu',
    'Print Orders List',
    'Create New Order',
    'Update an Existing Order',
    'Delete Order'
]

order_keys = [
    "customer\'s name",
    "customer\'s address",
    "customer\'s phone number",
    "courier\'s name",
    "status"
]

class Item:
    def __init__(self, item_type: str, item_keys = ['name'], item_values = None):
        self.type = item_type
        self.keys = item_keys
        self.content = dict()
        if item_values == None:
            for key in self.keys:
                self.content[key] = input(f'For this {item_type}, enter the {key}: ').strip().title()
        else:
            self.content = dict(zip(item_keys, item_values))

    def update(self):
        for key in self.keys:
            updated_input = input(f'For this {self.type}, enter the updated {key} or leave blank: ').strip().title()
            if updated_input:
                self.content[key] = updated_input

    def print(self, time_gap):
        if len(self.keys) > 1:
            for key, value in self.content.items():
                print(f'  {key}: {value}')
            print()
        else:
            print(f"  {self.content.get('name')}")
        time.sleep(time_gap)

    def exists_in(self, items: list['Item']) -> bool:
        exists_in = False
        for item in items:
            exists_in = True
            for key in item.keys:
                if self.content.get(key) != item.content.get(key):
                    exists_in = False
                    break
            if exists_in:
                return True
        return False

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
    def __init__(self, menu_type: str, menu_options: list[str], file_name: str, item_keys = ['name']):
        super().__init__(menu_type, menu_options)
        self.file_name = file_name
        self.file_type = file_name.split('.')[-1]
        contents = read_file(file_name)
        self.items = []
        # In python 3.10.4, there is a 'match-case' approach 
        if self.file_type == 'txt':
            self.items = [Item(self.type, item_values = [item]) for item in contents]
        elif self.file_type == 'json':
            self.items = [Item(self.type, item.keys(), item.values()) for item in contents]
        else:
            print('Did not recognise file type')
        self.item_keys = item_keys
    
    def save(self):
        if self.file_type == 'txt':
            contents = [item.content['name'] for item in self.items]
        elif self.file_type == 'json':
            contents = [item.content for item in self.items]
        write_file(self.file_name, contents)

    def print_items(self, is_indexed: bool, time_gap: float, final_delay: float):
        for i, item in enumerate(self.items):
            if is_indexed:
                print(f'  [{i}]', end="")
            item.print(time_gap)
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

    def add_item(self):
        item = Item(self.type, self.item_keys)
        if not(item.exists_in(self.items)):
            self.items.append(item)
        else:
            print(f'{item} is already in our {self.type} list')

    def update_item(self):
        index = self.get_item_index()
        if isinstance(index, int):
            self.items[index].update()

    def delete_item(self):
        index = self.get_item_index()
        if isinstance(index, int):
            del self.items[index]

def get_active(menus: list[Menu]) -> int:
    for index, is_active in enumerate([menu.is_active for menu in menus]):
        if is_active:
            return index
    return None

# Clear terminal
def clear_terminal():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

# Clear terminal and print logo
def display_logo():
    clear_terminal()
    # print(logo) # Comment out when debugging

# Close application after a delay
def close_app(menus: list[Menu]):
    '''Close application after saving files'''
    display_logo()
    print('Saving files and closing application...')
    for menu in menus[1:]:
        menu.save()
    time.sleep(1)
    clear_terminal()
    print('\n     See you next time!\n')

# App runs from here onwards
if __name__ == "__main__":
    main_menu = Menu('main', main_menu_options, True)
    product_menu = ItemsMenu('product', product_menu_options, PRODUCTS_FILE_NAME)
    courier_menu = ItemsMenu('courier', couriers_menu_options, COURIERS_FILE_NAME)
    order_menu = ItemsMenu('order', order_menu_options, ORDERS_FILE_NAME, order_keys)
    menus = (main_menu, product_menu, courier_menu) # irreplacable objects 
    menu_index = 0

    while menu_index != None:
        current_menu = menus[menu_index]
        current_option = current_menu.get_option()
        if menu_index == 0 and current_option == 0:
            main_menu.is_active = False
        elif menu_index == 0:
            current_menu.switch_to(menus[current_option])
        elif current_option == 0:
            current_menu.switch_to(main_menu)
        elif current_option == 1:
            current_menu.print_items(False, 0.5, 2)
        elif current_option == 2:
            current_menu.add_item()
            current_menu.save()
        elif current_option == 3:
            current_menu.update_item()
            current_menu.save()
        elif current_option == 4:
            current_menu.delete_item()
            current_menu.save()

        menu_index = get_active(menus)
        if menu_index != None:
            menus[menu_index].delay_loading_menu(1.5)

    close_app(menus)     