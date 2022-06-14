import time
from datetime import date

from menu_utilities import *
from budget_menu_funcs import *
# ---------------------------------------------------------------------

# Function: budget_menu



# ---------------------------------------------------------------------    
def budget_main_menu():
    # Ranges for user validation
    minMenuOption = 1
    maxMenuOption = 5   # Max value is 1 less than assigned, for list generation

    # Single-use flag for error message printing
    flag = True

    # Ask for user input until valid input received
    while True:
        clear_screen()
        persistent_menu()
        print("Welcome to the Budget Menu!\n")
        if not flag:
            print("Invalid input. Select value within menu range.\n")
        print("1: View Current Budget")
        print("2: View a Different Budget")
        print("3: Add a New Budget")
        print("4: Edit a Budget")
        menuInput = input("Please select an option: ")
        flag = check_input(list(range(minMenuOption, maxMenuOption)), menuInput)
        # if this is true, then we have a regular menu item
        if flag:
            menuInput = int(menuInput)
            break
        # Otherwise, we should check if it is a persistent menu option
        if check_pers_flag(menuInput):
            menuInput = menuInput.lower()
            break
        else:
            continue
    
    # Select next menu item based on input
    if menuInput == "~":
        print("Returning to the main menu")
        time.sleep(1)
        main_menu()
    elif menuInput == "..":
        print("Returning to the previous menu")
        time.sleep(1)
        pass
    elif menuInput == "exit":
        print("Saving your data and exiting")
        print("Goodbye!")
        quit()
    elif menuInput == 1:
        print("Displaying your current budget...")
        display_current_budget()
        time.sleep(1)
    elif menuInput == 2:
        print("Select a budget...")
        time.sleep(1)
    elif menuInput == 3:
        print("Add a new budget...")
        time.sleep(1)
    elif menuInput == 4:
        print("Edit a budget...")
        time.sleep(1)

# ---------------------------------------------------------------------

# Function: main_menu



# ---------------------------------------------------------------------    
def main_menu():
    # Ranges for user validation
    minMenuOption = 1
    maxMenuOption = 5   # Max value is 1 less than assigned, for list generation

    # Single-use flag for error message printing
    flag = True

    # Ask for user input until valid input received
    while True:
        clear_screen()
        persistent_menu()
        print("Welcome to the Main Menu!\n")
        if not flag:
            print("Invalid input. Select value within menu range.\n")
        print("1: Budget")
        print("2: Transactions")
        print("3: Accounts")
        print("4: Financial Reports")
        menuInput = input("Please select an option: ")
        flag = check_input(list(range(minMenuOption, maxMenuOption)), menuInput)
        # if this is true, then we have a regular menu item
        if flag:
            menuInput = int(menuInput)
            break
        # Otherwise, we should check if it is a persistent menu option
        if check_pers_flag(menuInput):
            menuInput = menuInput.lower()
            break
        else:
            continue
    
    # Select next menu item based on input
    if menuInput == "~":
        print("Returning to the main menu")
        time.sleep(1)
        main_menu()
    elif menuInput == "..":
        print("Returning to the previous menu")
        time.sleep(1)
        pass
    elif menuInput == "exit":
        print("Saving your data and exiting")
        print("Goodbye!")
        return False
    elif menuInput == 1:
        print("Budget menu selected...")
        budget_main_menu()
        time.sleep(1)
    elif menuInput == 2:
        print("Transaction menu selected...")
        time.sleep(1)
    elif menuInput == 3:
        print("Account menu selected...")
        time.sleep(1)
    elif menuInput == 4:
        print("Reports menu selected...")
        time.sleep(1)
    
    
    


main_menu()