# Mini-Project
Backend for a cafe application, with command line interaction.

# How it Functions?
## app.py
- Hard-codes the menu options, order keys and file names.
- Item class - Handles creation and updating of a single item (product/courier/order).
- Menu class has basic functionality - print menu options, get user's option, and track whether or not it is active.
- ItemsMenu class inherits attributes and methods from parent Menu class.
- In addition, it can select/add/update/delete an item from the list.
- After each change, the TXT and JSON files are updated.
- Returns to the same menu after using the product/courier menu.

## file_handler.py
- Read/write a list of strings from/into a textfile
- Read/write a list of dicts from/into a JSON file

## list_handler.py
- Print a list of strings with time gaps

## logo.py
- Currently contain's the logo for this terminal-based application, which shall appear at the top of the visible terminal.


# Project Requirements from Generation:
## Week 3:
In addition to week 2 requirements:
- Create, read, update or delete orders into/from a list
- When creating/updating an order, display products and couriers before selection
- Read/write list of orders into/from CSV or JSON file
## Week 2:
In addition to week 1 requirements:
- Create, read, update or delete couriers in/from a list
- Read to and write from .txt files
- Persist list of products and couriers in corresponding .txt files

## Week 1:
- Create a list of products and view all products.
- Be able to add/update/delete a product.
- This updated list will initially not be persisted into storage.

# Requirements to Run Application
## Python
- Only standard libraries are imported: os, time

# Collaboration
- Currently I am not accepting any pull requests (this may change in due course)

I am willing to receive constructive feedback regarding:
- Readability of the project
- Efficiency of the code 
- Additional features to add to this application
- How to write a README.md document

# License
- To be decided . . .

