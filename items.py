# items.py
# Module to handle items (product/courier) and partially handle orders
# Some functionality is inherited from the parent class Menu

import time
from menu import Menu
from file_handler import read_csvfile, write_csvfile


class Item:
    def __init__(self, item_type: str, item_keys, item_values=None):
        self.type = item_type
        self.keys = item_keys
        self.content = dict()
        if item_values == None:
            for key in self.keys:
                self.content[key] = (
                    input(f"For this {item_type}, enter the {key}: ").strip().title()
                )
        else:
            self.content = dict(zip(item_keys, item_values))

    def update(self):
        for key in self.keys:
            updated_input = (
                input(f"For this {self.type}, enter the updated {key} or leave blank: ")
                .strip()
                .title()
            )
            if updated_input:
                self.content[key] = updated_input

    def print(self, time_gap):
        for key, value in self.content.items():
            print(f"  {key}: {value}")
        print()
        time.sleep(time_gap)

    def exists_in(self, items: list["Item"]) -> bool:
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


class ItemsMenu(Menu):
    def __init__(
        self, menu_type: str, menu_options: list[str], file_name: str, item_keys: list[str]
    ):
        super().__init__(menu_type, menu_options)
        self.file_name = file_name
        self.file_type = file_name.split(".")[-1]
        contents = read_csvfile(file_name)
        self.items = []
        self.items = [Item(self.type, list(item.keys()), item.values()) for item in contents]
        self.item_keys = item_keys

    def save(self):
        contents = [item.content for item in self.items]
        write_csvfile(self.file_name, contents, self.item_keys)

    def print_items(self, is_indexed: bool, time_gap: float, final_delay: float):
        for i, item in enumerate(self.items):
            if is_indexed:
                print(f"  [{i}]")
            item.print(time_gap)
        time.sleep(final_delay)

    def get_item_index(self) -> int:
        self.print_items(True, 0, 0.5)
        try:
            index = int(input(f"Enter the {self.type} number: "))
            if index in range(len(self.items)):
                return index
            else:
                print(f"InputError: Not a valid {self.type} number")
                return None
        except:
            print(f"InputError: Not a valid {self.type} number")
            return None

    def add_item(self):
        item = Item(self.type, self.item_keys)
        if not (item.exists_in(self.items)):
            self.items.append(item)
        else:
            print(f"{item} is already in our {self.type} list")

    def update_item(self):
        index = self.get_item_index()
        if isinstance(index, int):
            self.items[index].update()

    def delete_item(self):
        index = self.get_item_index()
        if isinstance(index, int):
            del self.items[index]
