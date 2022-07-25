# orders.py
# Module to handle an order


from menu import Menu
from items import Item, ItemsMenu
from file_handler import read_csvfile, write_csvfile
from list_handler import print_list, get_indices, get_index

PRODUCT_IDS_KEY = 'product indices'
COURIER_KEY = 'courier\'s index'
STATUS_KEY = 'status'

# TODO: Initialise and update an order. - DONE!
# TODO: Breakdown add_or_update back into two methods
# Will need to pass in the list of products and couriers
class Order(Item):
    def __init__(self, item_type: str, item_keys: list[str], 
                product_menu: ItemsMenu, courier_menu: ItemsMenu, 
                statuses: list[str], item_values=None):
        self.type = item_type
        self.keys = item_keys
        self.product_menu = product_menu
        self.courier_menu = courier_menu
        self.statuses = statuses
        self.content = {}
        if item_values == None:
            # TODO: For order, ask for value for keys {name, address, phone}
            for key in self.keys:
                if key == PRODUCT_IDS_KEY:
                    self.add_or_update_products(True)
                elif key == COURIER_KEY:
                    self.add_or_update_courier(True)
                elif key == STATUS_KEY:
                    self.add_or_update_status(True)
                else:
                    self.content[key] = (input(f"For this order, enter the {key}: ").strip().title())
        else:
            self.content = dict(zip(item_keys, item_values))

    def add_or_update_products(self, to_add: bool):
        # to_add is True if we are adding, or False if we are updating
        # TODO: print product list, ask for comma-separated indices
        #       get_indices(list_items).
        if to_add:
            print(f"For this order, select the products you\'d like")
            self.product_menu.print_items(True, 0.3, 0.8)
            self.content[PRODUCT_IDS_KEY] = get_indices(len(self.product_menu.items))
        else:
            print(f"For this order, select the products you\'d like and leave blank to keep current {PRODUCT_IDS_KEY}")
            self.product_menu.print_items(True, 0.3, 0.8)
            print(f"Current {PRODUCT_IDS_KEY} of this order:  {self.content[PRODUCT_IDS_KEY]}")
            updated_indices = get_indices(len(self.product_menu.items))
            print(f"updated_indices = {updated_indices}") # REMOVE LATER
            if updated_indices:
                self.content[PRODUCT_IDS_KEY] = updated_indices
            print(f"product indices = {self.content[PRODUCT_IDS_KEY]}") # REMOVE LATER

    def add_or_update_courier(self, to_add: bool):
        # to_add is True if we are adding, or False if we are updating
        # TODO: Print courier list, ask for courier index
        if to_add:
            print(f"For this order, select the courier you\'d like")
            self.courier_menu.print_items(True, 0.3, 0.8)
            self.content[COURIER_KEY] = get_index(len(self.courier_menu.items), False)
        else:
            print(f"For this order, select the preferred courier number and leave blank to keep current courier")
            self.courier_menu.print_items(True, 0.3, 0.8)
            print(f"Current {COURIER_KEY} of this order:  {self.content[COURIER_KEY]}")
            updated_index = get_index(len(self.courier_menu.items), True)
            if updated_index:
                self.content[COURIER_KEY] = updated_index
            
    def add_or_update_status(self, to_add: bool):
        # to_add is True if we are adding, or False if we are updating
        # TODO: Print statuses, ask for status index, store status.
        if to_add:
            self.content[STATUS_KEY] = self.statuses[0]
        else:
            print(f"For this order, select the updated status and leave blank to keep current status")
            print_list(self.statuses, True, 0.5)
            print(f"Current {STATUS_KEY} of this order:  {self.content[STATUS_KEY]}")
            updated_index = get_index(len(self.statuses), True)
            if isinstance(updated_index, int):
                self.content[STATUS_KEY] = self.statuses[updated_index]

    def update(self):
        # TODO: Ask for keys that need to be updated
        # Need a method which takes in a list, gets indices
        print('Which entries of this order, do you want to update?')
        print_list([key.title() for key in self.keys], True, 0.3)
        update_indices = get_indices(len(self.keys))
        update_keys = [self.keys[index] for index in update_indices]
        for key in update_keys:
            if key == PRODUCT_IDS_KEY:
                self.add_or_update_products(False)
            elif key == COURIER_KEY:
                self.add_or_update_courier(False)
            elif key == STATUS_KEY:
                self.add_or_update_status(False)

            else:
                print(f"Current {key} of this order: {self.content[key]}")
                updated_input = (
                    input(f"For this {self.type}, enter the updated {key} or leave blank: ")
                    .strip().title()
                )
                if updated_input:
                    self.content[key] = updated_input