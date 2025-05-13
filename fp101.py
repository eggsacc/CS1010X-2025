def deposit(principal, interest, duration):
    for _ in range(duration):
        interest_amt = principal * interest
        principal += interest_amt
    
    return principal

print(deposit(100, 0.05, 2))
print(deposit(100, 0.05, 1))

def balance(principal, interest, payout, duration):
    for _ in range(duration):
        principal *= (1 + interest)
        principal -= payout
    
    return principal

print(balance(100000, 0.01, 5000, 1))
print(balance(100000, 0.01, 5000, 2))

def new_balance(principal, gap, payout, duration):
    def helper(monthly_interest):
        val = principal
        val = deposit(val, monthly_interest, gap-1)
        val = balance(val, monthly_interest, payout, duration)
        return val

    return helper

print(new_balance(1000, 2, 100, 2)(0.1))
print(new_balance(10000, 3, 1000, 3)(0.05))

def find_cpf_rate():
    principal = 166000
    helper = new_balance(principal, 119, 1280, 240)
    i = 0.0026283

    def close(a, b):
        return abs(a-b) <= 0.1
    
    while(i < 0.01):
        amt = helper(i)
        if(amt > 5):
            break
        if(close(amt, 0)):
            return round((1+i) ** 12 - 1, 3)
        i += 0.000000001
        
print(find_cpf_rate())