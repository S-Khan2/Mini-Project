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

menu_dict = {
    '0' : ['Main Menu', main_menu_options],
    '1' : ['Products Menu', product_menu_options],
    '2' : ['Couriers Menu', couriers_menu_options]
}

def display_menu_options(menu_key):
    print(menu_dict(menu_key)[0])
    for i, choice in enumerate(menu_dict(menu_key)[1]):
        print(f'  [{i}]  {choice}')

def get_menu_option(menu_key):
    display_logo()
    display_menu_options(menu_key)
    return input(f'Enter option: ')

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