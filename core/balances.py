def actual():
    act_balance = 100
    return act_balance

def estimate():
    est_balance = 10
    return est_balance

def act_est_compare():
    actual_bal = actual()
    estimate_bal = estimate()
    difference = actual_bal - estimate_bal
    return difference
    
def report():
    difference = act_est_compare()
    if difference != 0:
        return print(f"balance not accurate. Please review accounting! Difference is {difference}")
    else:
        return print("All is well in the world.")


report = report()
print(f"{report}")
