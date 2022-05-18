# Aim: To improve user experience from earlier version of app.py from Week 1

import os       # Helpful to clear terminal
import time     # Helpful to add waiting times
from logo import logo     # Collects my logo from 'logo.py'
from file_handler import * # read_file and write_file

PRODUCTS_FILE_NAME = 'products.txt'
COURIERS_FILE_NAME = 'couriers.txt'

# Load list of products and couriers
products = read_file(PRODUCTS_FILE_NAME)
couriers = read_file(COURIERS_FILE_NAME)

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
    print(state_dict(menu_key)[0])
    for i, choice in enumerate(state_dict(menu_key)[1]):
        print(f'  [{i}]  {choice}')

def get_menu_option(state_key):
    display_logo()
    display_menu_options(state_key)
    option = input(f'Enter option: ').strip()
    if int(option) in range(len(state_dict[state_key])):
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

# Clear terminal
def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

# Clear terminal and print logo
def display_logo():
    clear_console()
    print(logo)

# Close application after a delay
def close_app():
    display_logo()
    print('Closing application...')
    # Thought: Now we could store the product list update
    time.sleep(1)
    clear_console()
    print('Application closed')
    exit()

# Take a list, find max length, find how many can fit per line,
# keep the items aligned
def multi_print(our_list, line_length):
    return None

# Display main menu and return input
def get_main_menu_choice():
    display_logo()
    print('Main Menu:\n  [0]  Exit Application\n  [1]  Product Menu')
    return input('Enter option: ')

# Display product menu and return option
def get_product_menu_choice():
    display_logo()
    print('Product Menu:')
    for i, option in enumerate(product_menu_options):
        print(f'  [{i}]  {option}')
    return input('Enter option: ')

# Print products with index, and return index as an int
def get_product_index():
    for i, product in enumerate(products):
            print(f'  [{i}]  {product}')
    return int(input('Enter index of product: '))

# Run until we exit app
while True:
    user_input = get_main_menu_choice()
    if user_input == '0': # exit
        close_app()
    else:
        user_input = get_product_menu_choice()
        if user_input == '2': # add new product
            new_product = input('Enter new product: ').title()
            products.append(new_product)
        elif user_input == '3': # update old product
            index = get_product_index()
            products[index] = input('Enter update of product: ')
        elif user_input == '4': # delete product by index
            del products[get_product_index()]
        if user_input != '0': # print products list
            print(f'List of products: {products}')
        
        # Add two seconds delay
        time.sleep(1)
        print('\n  Loading main menu...')
        time.sleep(1)