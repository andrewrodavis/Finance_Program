from time import sleep

def budget_process_switch(nextProcess):
    if nextProcess == "budget current":
        print("Pulling you current budget")
        time.sleep(1)
    elif nextProcess == "budget all":
        print("Pulling all available budgets")
        time.sleep(1)