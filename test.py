def bar(n):
    if n == 0:
        return 0
    else:
        return n + bar(n- 1)
def foo(n):
    if n == 0:
        return 0
    else:
        return bar(n) + foo(n- 1)
    
def improved_foo(n):
    # Fill in code here
    sum = 0
    for i in range(1, n + 1):
        sum += i * (n - i + 1)
    return sum

x = 11
print(foo(x))
print(improved_foo(x))