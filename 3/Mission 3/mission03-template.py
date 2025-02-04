#
# CS1010X --- Programming Methodology
#
# Mission 3
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

###########
# Task 1a #
###########

def compose(f, g):
    return lambda x:f(g(x))

def thrice(f):
    return compose(f, compose(f, f))

def identity(x):
    return x
def repeated(f, n):
    if n == 0:
        return identity
    else:
        return compose(f, repeated(f, n - 1))
    
def add1(x):
    return x + 1

# Your answer here:
# n = 9

###########
# Task 1b #
###########

identity = lambda x: x
add1 = lambda x: x + 1
sq = lambda x: x**2

# (i) print(thrice(thrice)(add1)(6))
# Explanation:

# (ii) print(thrice(thrice)(identity)(compose))
# Explanation:

print(thrice(thrice)(sq)(1.1))
# Explanation:

# (iv) print(thrice(thrice)(sq)(2))
# Explanation:


###########
# Task 2a #
###########

def combine(f, op ,n):
    result = f(0)
    for i in range(n):
        result = op(result, f(i))
    return result

def smiley_sum(t):
    def f(x):
        # your answer here
        return (x+1) * (x+1)
    
    def op(x, y):
        # your answer here
        return (x) if y == 1 else (x + 2*y)
        
    n = t # replace your answer here
    
    # Do not modify this return statement
    return combine(f, op, n)
#print(smiley_sum(1))

###########
# Task 2b #
###########

def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

def new_fib(n):
    def f(x, last_2 = [0, 1]):
        # answer here
        if(x == 0):
            return [0, 1]
        else:
            return -1
        
        
    def op(x, y):
        # answer here
        if(y != -1):
            new_fib = x[0] + x[1]
            return [x[1], new_fib]
        
    # do not modify this return statement
    return combine(f, op, n+1)

# Your answer here:
print(new_fib(10))
