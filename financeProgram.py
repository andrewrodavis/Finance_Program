# Program: financeProgram.py
# Author: Andrew Davis
# Description: This file is the engine for the simple-to-use finance being designed
# Key Tasks:
# - Set all filepaths

import sys
import os

# Get the current path: good
current = os.path.dirname(os.path.realpath(__file__))

# Get all required paths: good
menusDir = current + "/menus"
dataDir = current + "/dataManagement"
# Get all process file paths
processesDir = current + "/processes"
budgetProcessDir = processesDir + "/budget_processes"
transProcessDir = processesDir + "/transaction_processes"

# Add all paths to the system path list: good
sys.path.append(menusDir)
sys.path.append(dataDir)

# Process path appends
sys.path.append(processesDir)
sys.path.append(budgetProcessDir)
sys.path.append(transProcessDir)

# Import all relevant modules
import time

from main_menu import main_menu
from budget_main import budget_main
from trans_main import trans_main
from account_main import account_main
from report_main import report_main

# ---------------------------------------
# 
# Function: begin_process
# Input: The string to match, to determine which process to trigger
#   Sub-tags: corresdponding processes will start with an appropriate tag
#       budget <process>, transaction <process>, financials <process>, account <process>
# Output: Sends to a process manager to complete said process
# Return: Returns, to the engine
#   isMenu: The next step depends on whether there is another menu, info, or a prompt
#   nextStep: Return the next process/menu to display
#   keepRunnin: Always return True, unless the the user confirmed an exit
# Description: This simply displays the menu for the user to pick, then returns their input value
# 
# ---------------------------------------
def begin_process(theProcess):
    if "budget" in theProcess:
        print("This is a budget process")
    elif "transaction" in theProcess:
        print("This is a transaction process")
    elif "financials" in theProcess:
        print("This is a financials process")
    elif "account" in theProcess:
        print("This is a account process")
    else:
        print("Error: Should not reach this point")

# ---------------------------------------
# 
# Function: display_menu
# Input: The string to match, to determine which menu to display
#   Menu Options to Display: main, budget, transaction, financials, account
# Output: To screen, present the menu
# Return: Returns some flags, and the next thing to do
#   isMenu: If the next step is a menu item, return True
#   nextStep: Return the next process/menu to display
#   keepRunnin: Always return True, unless the the user confirmed an exit
# Description: This simply displays the menu for the user to pick, then returns their input value
# 
# ---------------------------------------
def display_menu(selectedMenu):
    if selectedMenu == "main":
        print("Going to the Main Menu...")
        time.sleep(1)
        # isMenu, nextStep, keepRunning = main_menu()
        return main_menu()
    elif selectedMenu == "budget":
        print("Going to the Budget Menu...")
        time.sleep(1)
        return budget_main()
    elif selectedMenu == "transaction":
        print("Going to the Transaction Menu...")
        time.sleep(1)
        return trans_main()
    elif selectedMenu == "reports":
        print("Going to the View Reports Menu...")
        time.sleep(1)
        return report_main()
    elif selectedMenu == "account":
        print("Going to the Accounts Menu...")
        time.sleep(1)
        return account_main()
    else:
        print("Error: Should not reach this point")
# ---------------------------------------
# Function: main 
# ---------------------------------------
def main():
    nextStep = "main"
    currentProcess = ""
    keepRunnin = True   # Flag to ensure we keep running or not
    isMenu = True   # If this is true, the next step is to display another menu. If not, then begin a process
    
    while keepRunnin:
        lastStep = nextStep   # Store the "current" menu
        # If true, determine which menu to display
        if isMenu:
            isMenu, nextStep, keepRunnin = display_menu(nextStep)
        # If false, determine which process to begin
        elif not isMenu:
            isMenu, nextStep, keepRunning = begin_process(nextStep)

main()