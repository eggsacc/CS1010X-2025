def is_odd(x):
    # Fill in code here
    return True if x % 2 else False
    
def is_negative(x):
    # Fill in code here
    return x < 0
    
def is_even_and_positive(x):
    # Fill in code here
    if not is_odd(x):
        if not is_negative(x):
            return True
        return False
    return False

print(is_even_and_positive(-8))