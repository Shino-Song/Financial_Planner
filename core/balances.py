def actual(act):
    return float(act)

def estimate(est):
    return float(est)

def act_est_compare(actual_bal, estimate_bal):
    difference = actual_bal - estimate_bal
    return difference
    
def report(actual_bal, estimate_bal):
    difference = act_est_compare(actual_bal, estimate_bal)
    if difference != 0:
        return (f"balance not accurate. Please review accounting! Difference is {difference}")
    else:
        return "All is well in the world."