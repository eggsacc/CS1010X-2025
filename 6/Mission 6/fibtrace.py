from diagnostic import *
from hi_graph_connect_ends import *

def fib(n):
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


calls = 5
original_rotate = rotate
trace(x_of)
gosper_curve(calls)(0.5)
untrace(x_of)
print("###############")

replace_fn(rotate, joe_rotate)
trace(x_of)
gosper_curve(calls)(0.5)
untrace(x_of)

replace_fn(rotate, original_rotate)

