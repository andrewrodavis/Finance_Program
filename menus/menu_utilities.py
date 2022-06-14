import platform
import os
import time

# ---------------------------------------------------------------------
# Function: confirm_exit
# --------------------------------------------------------------------- 
def confirm_exit():
    confirmFlag = True
    while confirmFlag:
        confirm = input("Are you sure you want to exit the program? (y/n): ")
        if confirm == "y":
            print("Saving your data and exiting.")
            time.sleep(1)
            print("Goodbye!\n\n")
            return True
        elif confirm == "n":
            confirmFlag = False
            return False
        else:
            print("!Input Error! Please try again\n")
            confirmFlag = False
# ---------------------------------------------------------------------
# Function: persistent_menu
# ---------------------------------------------------------------------    
def persistent_menu():
    print("------------Commands at Any Point------------")
    print("| ~    : Go to Main Menu                    |")
    print("| ..   : Go to Previous Menu                |")
    print("| exit : Exit the program                   |")
    print("---------------------------------------------\n\n")
    
# Checks if the user entered a persistent menu option
def check_pers_flag(menuInput):
    if menuInput == "..":
        return True
    elif menuInput == "~":
        return True
    elif menuInput.lower() == "exit":
        return True
    else:
        return False

# Checks the user input to be within a specified range
def check_input(listRange, value):
    try:
        value = int(value)
    except ValueError:
        return False

    if value in listRange:
        return True
    else:
        return False

# Clears the screen based on the operating system
def clear_screen():
    if platform.system() == "Linux":
        os.system('clear')
    else:
        os.system('cls')