# logo.py
# This module handles the refreshing of the screen and the logo design

import os

logo = '''____________________________________________________

                           (       
                _           ) )      Sahl's Mini
             _,(_)._       ( (         Project
        ___,(_______).        )
    ,' __.   /      \     /\_             )
   / ,' /  |""|       \  /  /            (
   | | |   |__|        |;  /               )
   \ '.|                  /           _.-~(~-.
    `. :            :    /           (@\`---'/.   
      `.             :.,'           ('  `._.'  `)
        `-.________,-'               `-..___..-'  
____________________________________________________
'''

def clear_terminal():
    '''Clear terminal, independant of operation system'''
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def display_logo(): 
    '''Clear terminal and print logo'''
    clear_terminal()
    # return None # Temporarily do not print logo
    print(logo)