#from core.balances import *
from core.budget_processing import *
from core.report import *

print("Hello, this is the Song Financial Planner. I hope you are having a great day!")
print("To start, I will ask you a couple simple questions.")
#while True:
entry_type = input("Are we looking at income or an expense?\n")
if entry_type.lower() == "income":
    while True:
        est_input = input("First, what is your estimated income?\nEstimate: ")
        est_yn = input(f"Wonderful! Your estimated income is {est_input}, is that correct? (Y/N): ")
        if est_yn.lower() == "y":
            break
        else:
            print("Let's try that again.\n")
    print("Perfect! Now for the next question.")
    while True:
        act_input = input("Next, what is your actual income?\nActual: ")
        act_yn = input(f"Amazing! Your actual income is {act_input}, is that correct?\n (Y/N): ")
        if act_yn.lower() == "y":
            break
        else:
            print("Let's try again.\n")
elif entry_type.lower() == "expense":
    while True:
        expense_type = input("Lets start with the type of expense you are adding. Kind of expense is this? (eg. food, medical, utilities, etc...): ")
        type_yn = input(f"The type of expense is {expense_type}, correct? (Y/N): ")
        if type_yn.lower() == "y":
            break
        else:
            print("Let's try that again.\n")
        expense_name = input("Now, let's add where the purchase is from. Please tell me where the purchase is from or to: ")
        name_yn = input(f"The expense is from/to {expense_name}, correct? (Y/N): ")
        if name_yn.lower() == "y":
            break
        else:
            print("Let's try that again.\n")
        est_input = input("First, what is your estimated expense?\nEstimate: ")
        est_yn = input(f"Wonderful! Your estimated expense is {est_input}, is that correct? (Y/N): ")
        if est_yn.lower() == "y":
            break
        else:
            print("Let's try that again.\n")
    print("Perfect! Now for the next question.")
    while True:
        act_input = input("Next, what is your actual expense?\nActual: ")
        act_yn = input(f"Amazing! Your actual expense is {act_input}, is that correct?\n (Y/N): ")
        if act_yn.lower() == "y":
            break
        else:
            print("Let's try again.\n")
else:
    print("I didn't quite get that. Let's try again.")
    


transfer = expense("test", est_input, act_input)
difference = transfer.diff_calc()

act = act_input
est = est_input

report_result = report(difference)

print("\nThank you for using the Song Financial Planner input test!")
print(f"Your estimated balance was {est} and your actual balance was {act}.")
print(f"The following is your balance report.\n{report_result}")
exit()