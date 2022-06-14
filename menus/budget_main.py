import time

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
def budget_main():
    # Ranges used to validate input. Min is always 1
    maxMenuOption = 5   # This is always 1 more than the total number of options

    # Single-use flag for error message printing
    errorOnInput = True

    # Ask for input until the user gets it right
    while True:
        clear_screen()
        persistent_menu()
        
        print("------------Welcome to the BUDGET Menu!------------")
        if not errorOnInput:
            print("| !Invalid Input! Select a value from the menu.|")
        print("| 1: View Current Budget                           |")
        print("| 2: View a Different Budget                       |")
        print("| 3: Add a New Budget                              |")
        print("| 4: Edit a Budget                                 |")
        print("-------------------------------------------------\n")
        menuInput = input("Please Select a Menu Option: ")

        # Check the input is within a valid range
        errorOnInput = check_input(list(range(1, maxMenuOption)), menuInput)
        # If it is true, then we have a regular menu option
        if errorOnInput:
            menuInput = int(menuInput)
            break
        # Otherwise, we check to see if it is a persistent menu option
        if check_pers_flag(menuInput):
            menuInput = menuInput.lower()
            break
        # Catch All
        else:
            continue
    
    # Respond/Direct appropriately
    if menuInput == "~":
        print("Returning to the Main Menu...")
        time.sleep(1)
        return True, "main", True
    elif menuInput == "..":
        print("Returning to the Previous Menu...")
        time.sleep(1)
        return True, "main", True
    elif menuInput == "exit":
        sureExit = confirm_exit()
        if sureExit:
            return True, "", False
        else:
            return True, "main", True
    elif menuInput == 1:   # Return a process to get the current budget
        print("Pulling your current budget...")
        time.sleep(1)
        return False, "budget current", True
    elif menuInput == 2:   # Return a menu to select the budget to pick
        print("Pulling your budget list...")
        time.sleep(1)
        return False, "budget all", True
    elif menuInput == 3:   # Return a process to add a new budget
        print("Preparing to add a new budget...")
        time.sleep(1)
        return False, "budget new", True
    elif menuInput == 4:   # Return a menu to select the budget to pick
        print("Pulling your budget list...")
        time.sleep(1)
        return False, "budget all edit", True
    else:
        print("Error: Should not reach this point")
    # print("In the budget menu")
    # return True, "transaction", True