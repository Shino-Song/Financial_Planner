def actual(act):
    act_balance = act
    return act_balance

def estimate(est):
    est_balance = est
    return est_balance

def act_est_compare(actual_bal, estimate_bal):
    difference = actual_bal - estimate_bal
    return difference
    
def report(actual_bal, estimate_bal):
    difference = act_est_compare(actual_bal, estimate_bal)
    if difference != 0:
        return (f"balance not accurate. Please review accounting! Difference is {difference}")
    else:
        return "All is well in the world."

act_input = actual(10)
est_input = estimate(100)

report_result = report(act_input, est_input)
print(report_result)
