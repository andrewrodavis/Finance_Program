from datetime import date
import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)

from budget_processes import *


# ---------------------------------------------------------------------
# Function: display_current_budget
# ---------------------------------------------------------------------
def display_current_budget():
    month = date.today().month
    year = date.today().year
    print("today's date: ", month)
    print("today's date: ", year)
    testprinting()

# ---------------------------------------------------------------------
# Function: display_different_budget
# ---------------------------------------------------------------------
def display_different_budget():
    pass

# ---------------------------------------------------------------------
# Function: add_new_budget
# ---------------------------------------------------------------------
def add_new_budget():
    pass

# ---------------------------------------------------------------------
# Function: edit_budget
# ---------------------------------------------------------------------
def edit_budget():
    pass