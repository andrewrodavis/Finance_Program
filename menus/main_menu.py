import time
from datetime import date

from menu_utilities import *
from budget_menu_funcs import *
# ---------------------------------------------------------------------
#
# Function: main_menu
# Input: None
# Return: Returns some flags, and the next thing to do
#   isMenu: If the next step is a menu item, return True
#   nextStep: Return the next process/menu to display
#   keepRunnin: Always return True, unless the the user confirmed an exit
# Description: 
#
# ---------------------------------------------------------------------
def main_menu():
    # Ranges used to input validation
    minMenuOption = 1
    maxMenuOption = 5   # This is always 1 more than the total number menu options

    # Single-use flag for error message printing
    errorOnInput = True

    # Ask for user input until the user gets it right
    while True:
        clear_screen()
        persistent_menu()

        print("------------Welcome to the MAIN Menu!------------")
        if not errorOnInput:
            print("| !Invalid Input! Select a value from the menu.|")
        print("| 1: Budget                                     |")
        print("| 2: Transactions                               |")
        print("| 3: Accounts                                   |")
        print("| 4: Financial Reports                          |")
        print("-------------------------------------------------\n")
        menuInput = input("Please Select a Menu Option: ")

        # Check the input is within range of the allowed number options
        errorOnInput = check_input(list(range(minMenuOption, maxMenuOption)), menuInput)
        # If it is true, then we have a regular menu option
        if errorOnInput:
            menuInput = int(menuInput)
            break
        # Otherwise, we check if it is a persistent menu option
        if check_pers_flag(menuInput):
            menuInput = menuInput.lower()
            break
        # Catch all
        else:
            continue

    # Respond/direct appropriately
    if menuInput == "~":
        print("Returning to the Main Menu")
        time.sleep(1)
        return True, "main", True
    elif menuInput == "..":
        print("Returning to the Previous Menu")
        time.sleep(1)
        return True, "", True
    elif menuInput == "exit":
        confirmFlag = True
        while confirmFlag:
            confirm = input("Are you sure you want to exit the program? (y/n): ")
            if confirm == "y":
                print("Saving your data and exiting.")
                time.sleep(1)
                print("Goodbye!\n\n")
                return True, "", False
            elif confirm == "n":
                confirmFlag = False
                return True, "main", True
            else:
                print("!Input Error! Please try again\n")
                confirmFlag = True, "main", True
    elif menuInput == 1:
        print("Budget Menu Selected.")
        time.sleep(1)
        return True, "budget", True
    elif menuInput == 2:
        print("Transaction Menu Selected")
        time.sleep(1)
        return True, "transaction", True
    elif menuInput == 3:
        print("Account Menu Selected")
        time.sleep(1)
        return True, "account", True
    elif menuInput == 4:
        print("Report Menu Selected")
        time.sleep(1)
        return True, "reports", True    