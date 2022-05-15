# Aim: To write a easy-to-follow refactored code

products = ['Coke Zero', 'Fanta', 'Tea', 'Coffee']
product_menu_options = ['Main Menu', 'Print Product List', 'Create New Product',
                        'Update Existing Product', 'Delete Product']

def get_main_menu_option():
    return input('Enter 0 to exit or 1 to open product menu: ')

def get_product_menu_option():
    print('Enter a number for each product:')
    for option in enumerate(product_menu_options):
        print(f'{option}')
    return input()

def get_product_index():
    for product in enumerate(products):
            print(f'{product}')
    return int(input('Enter index of product: '))

user_input = get_main_menu_option()
if user_input == '0':
    exit()
else:
    user_input = get_product_menu_option()
    if user_input == '0':
        user_input = get_main_menu_option()
    elif user_input == '1':
        print(products)
    elif user_input == '2':
        products.append(input('Enter new product: '))
        print(products)
    elif user_input == '3':
        index = get_product_index()
        products[index] = input('Enter update of product: ')
        print(products)
    elif user_input == '4':
        del products[get_product_index()]
        print(products)
        