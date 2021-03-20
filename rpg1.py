import random, cmd, os, textwrap, time, sys
from attacks import *

##### Title Screen #####
def title_screen_selections():
    option = input("> ")
    if option.lower() == ("play"):
        start_game()
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print ("Please enter a valid command.")
        option = input(">")
        if option.lower() == ("play"):
            start_game()
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("quit"):
            sys.exit()

def title_screen():
    os.system('cls')
    print('Welcome to the Text RPG!')
    print('       | play |       ')
    print('       | help |       ')
    print('       | quit |       ')
    title_screen_selections()

def help_menu():
    os.system('cls')
    print('Welcome to the Text RPG!')
    print('type commands to trigger them!')
    print('action packed battles and more!')
    title_screen_selections()

#Actual Game functionality#

def start_game():
    os.system ('cls')
    print ("you explore the dungeon")
    forw = input("keep going?")
    if forw == ("yes"):
        enemybattle()
    else:
        start_game()

title_screen()
