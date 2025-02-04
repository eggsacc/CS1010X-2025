#
# CS1010X --- Programming Methodology
#
# Mission 2 - Side Quest 2
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

##########
# Task 1 #
##########

# Simplifed Order notations:

# 4^n * n^2
# Ans: 4^n

# n * 3^n
# Ans: 3^n

# 1000000000n^2
# Ans: n^2

# 2^n/1000000000
# Ans: 2^n

# n^n + n^2 + 1
# Ans: n^n

# 4^n + 2^n
# Ans: 4^n

# 1^n
# Ans: 1

# n^2
# Ans: n^2

# Faster order of growth in each group:

# i. O(4^n * n^2)
# ii. O(2^n / 1000000000)
# iii. O(n^n + n^2 + 1)
# iv. O(n^2)


##########
# Task 2 #
##########

# Time complexity: O(n)
# Space complexity: O(n)

# bar() is recursively called for n+1 times. -> O(n) time
# Each call creates 1 new stack frame -> o(n) space

##########
# Task 3 #
##########

# Time complexity of bar: O(n)
# Time complexity of foo: O(n^2)

# Space complexity of bar: O(n)
# Space complexity of foo: O(n^2)

# Analysis: foo() sums all the numbers from 1-x, for x in range [1, n].
# For improved space complexity, simply use a for loop instead of recursion to make constant space since only 2 variables are required (sum, i)
# For time complexity, use an alternate algorithm for the sum:
#
# Example: n = 5
#
#  5          -> 5 * (n-4) +
#  4 4        -> 4 * (n-3) +
#  3 3 3      -> 3 * (n-2) +
#  2 2 2 2    -> 2 * (n-1) +
#  1 1 1 1 1  -> 1 * n     = sum

def improved_foo(n):
    # Fill in code here
    sum = 0
    for i in range(1, n + 1):
        sum += i * (n - i + 1)
    return sum
    
print(bar(5))
# Improved time complexity: O(n)
# Improved space complexity: O(1)
