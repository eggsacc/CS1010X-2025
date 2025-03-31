# 1)

import math

def sqrt(x):
    return math.sqrt(x)

def square(x):
    return x * x

def magnitude(p1x, p1y, p2x, p2y):
    return sqrt(square(abs(p1x - p2x)) + square(abs(p1y - p2y)))


# 2a)
def area(base, height):
    return 0.5 * base * height

# 2b)
def area2(a, b, angle_ab):
    return 0.5 * a * b * math.sin(angle_ab)

# 2c)
# No. Each function has difference input parameters and calculates the area based on different properties.
# the area() function is only limited to right-angled triangles while area2() can be any type of triangle.

# 2d)
def area3(x1, y1, x2, y2, x3, y3):
    a = magnitude(x1, y1, x2, y2)
    b = magnitude(x2, y2, x3, y3)
    c = magnitude(x1, y1, x3, y3)
    s = (a + b + c) / 2
    
    return sqrt(s*(s-a)*(s-b)*(s-c))

# 3a)
# 1+2+3 ... +9 = 45

# 3b)
# 1 + 2 -> break since i == 3, hence 3

# 3c)
# Same as 3a), 45

# 3d)
# 2 + 3 + 5 + 6 + 8 + 9 = 33

# 4)

def sum_even_factorials(n):
    # Set n to previous even number if odd
    if n % 2:  
        n -= 1

    total_sum = 0
    factorial = 1

    for i in range(2, n + 1, 2):
        # Multiple factorial by next 2 numbers
        # * i and i-1 since i increments in steps of 2
        factorial *= i * (i - 1)  
        total_sum += factorial  

    # +1 to compensate for skipping 1! in loop
    return total_sum + 1

print(sum_even_factorials(6))

# 5)
def f(g):
    return g(2)
def square(x):
    return x ** 2
# Returns error since f(f) returns f(2) which returns 2(2), and 2 is an int not a function.

def xtra2():
    i = 100
    for i in range(i, i+2):
        i += 100
    return i
print(xtra2())
