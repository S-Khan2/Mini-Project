# Mini-Project
Backend for a cafe application, with command line interaction.
# How it Functions?

## app.py
- Hard-codes the menu options and textfile names.
- Creates a menu dictionary storing relevant information for each menu.
- Contains methods to get user's choice from any menu, and user's choice of product / courier after displaying them.
- Depending on user input, the app either exits or goes to product / courier menu from the main menu.
- At the product / courier menu, the user either returns to the main menu, sees the list of products/couriers, or adds / updates / deletes a product / courier.
- After each change, the textfiles are updated.
- Returns to the same menu after using the product / courier menu.

## file_handler.py
- Read / write a list of strings from / into a textfile

## logo.py
- Currently contain's the logo for this terminal-based application, which shall appear at the top of the visible terminal.


# Project Requirements from Generation:
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

