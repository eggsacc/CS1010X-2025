import time

def fib(n):
    if(n <= 1):
        return 0
    if(n == 2):
        return 1
    
    return fib(n-1) + fib(n-2)

memoized_table = {}

def memoize(f, n):
    if(n in memoized_table):
        return memoized_table[n]
    else:
        result = f(n)
        memoized_table[n] = result
        return result
    
def mem_fib(n):
    if(n <= 1):
        return 0
    if(n == 2):
        return 1
    
    return memoize(mem_fib, n-1) + memoize(mem_fib, n-2)

    
def test(range, *args):
    for func in args:
        now = time.time()
        result = func(range)
        end = time.time()
        print(f"Fn[{func.__name__}]: {end - now} sec, result: {result}")

test(20, fib, mem_fib)