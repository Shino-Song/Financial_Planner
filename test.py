#from core.balances import *
from core.budget_processing import *
from core.report import *

print("Hello, this is the Song Financial Planner. I hope you are having a great day!")
print("To start, I will ask you a couple simple questions.")
while True:
    est_input = input("First, what is your estimated balance?\nEstimate: ")
    est_yn = input(f"Wonderful! Your estimated balance is {est_input}, is that correct? (Y/N): ")
    if est_yn.lower() == "y":
        break
    else:
        print("Let's try that again.\n")
print("Perfect! Now for the next question.")
while True:
    act_input = input("Next, what is your actual balance?\nActual: ")
    act_yn = input(f"Amazing! Your actual balance is {act_input}, is that correct?\n (Y/N): ")
    if act_yn.lower() == "y":
        break
    else:
        print("Let's try again.\n")

#budget_transfer = budget("test1", )
transfer = expense("test", est_input, act_input)

act = act_input
est = est_input

#report_result = report(act_transfer, est_transfer)
report_result = report(transfer)

print("\nThank you for using the Song Financial Planner input test!")
print(f"Your estimated balance was {est:.2f} and your actual balance was {act:.2f}.")
print(f"The following is your balance report.\n{report_result}")
exit()