# Aim: To improve user experience from earlier version of app.py from Week 1

import os       # Helpful to clear terminal
import time     # Helpful to add waiting times
from logo import clear_terminal, display_logo     # Collects my logo from 'logo.py'
from menu import Menu, get_active
from items import ItemsMenu
from orders import PRODUCT_IDS_KEY, COURIER_KEY, STATUS_KEY, OrdersMenu

PRODUCTS_FILE_NAME = 'products.csv'
COURIERS_FILE_NAME = 'couriers.csv'
ORDERS_FILE_NAME = 'orders.csv'

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

product_keys = ["name", "price"]

couriers_menu_options = [
    'Main Menu',
    'Print Couriers List',
    'Create New Courier',
    'Update Existing Courier',
    'Delete Courier'
]

courier_keys = ["name", "phone number"]

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
    PRODUCT_IDS_KEY,
    COURIER_KEY,
    STATUS_KEY
]

statuses = [
    "Preparing...", 
    "On the way...", 
    "Knock, knock...", 
    "Delivered!"
]


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
    order_menu = OrdersMenu('order', order_menu_options, ORDERS_FILE_NAME, order_keys, 
                            product_menu, courier_menu, statuses)
    menus = (main_menu, product_menu, courier_menu) # irreplacable objects 
    menu_index = 0          # Tuple-index of active menu in 'menus'

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

        # After using the menu, determine which menu will be active next and load it
        menu_index = get_active(menus)
        if menu_index != None:
            menus[menu_index].delay_loading_menu(1.5)

    # Once no menu is active, save changes and close the application
    close_app(menus)     