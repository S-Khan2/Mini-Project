# menu.py
# This menu module sets up the foundations of how the app functions

import time
from logo import display_logo
from list_handler import print_list


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
        display_logo()
        print(f'\nLoading {self.type.title()} Menu ...')
        time.sleep(time_delay / 2)


def get_active(menus: list[Menu]) -> int:
    for index, is_active in enumerate([menu.is_active for menu in menus]):
        if is_active:
            return index
    return None
