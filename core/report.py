from core.budget_processing import *

def report():
    difference = diff_calc()
    if difference != 0:
        return (f"balance not accurate. Please review accounting! Difference is {difference}")
    else:
        return "All is well in the world."