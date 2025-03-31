#
# CS1010X --- Programming Methodology
#
# Mission 6
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from diagnostic import *
from hi_graph_connect_ends import *
import math

# Mission 6 requires certain functions from Mission 5 to work.
# Do copy any relevant functions that you require in the space below:







# Do not copy any other functions beyond this line #
##########
# Task 1 #
##########

# Example from the mission description on the usage of time function:
# profile_fn(lambda: gosper_curve(1000)(0.1), 500)

# Choose a significant level for testing for all three sets of functions.

# -------------
# gosper_curve:
# -------------
# write down and invoke the function that you are using for this testing
# in the space below

"""
for i in range(5): 
    print(profile_fn(lambda: gosper_curve(1000)(0.1), 3000))
"""

# ***
# Level: 1000
# Iterations: 3000
# ***
# Time 1: 10773.91660000012
# Time 2: 10764.056999999411
# Time 3: 10674.732200000108
# Time 4: 10790.843300000233
# Time 5: 10958.064299999933
# Average: 10792ms (truncating decimals)

# ------------------------
# gosper_curve_with_angle:
# ------------------------
# write down and invoke the function that you are using for this testing
# in the space below

"""
for i in range(5):
    print(profile_fn(lambda: gosper_curve_with_angle(1000, lambda x: math.pi/4)(0.1), 3000))
"""
# ***
# Level: 1000
# Iterations: 3000
# ***
# Time 1: 10400.608800000555
# Time 2: 10372.414100000242
# Time 3: 10321.020399999725
# Time 4: 10304.685499999323
# Time 5: 10614.349699999366
# Average: 10402ms (truncating decimals)

#
# -----------------------------
# your_gosper_curve_with_angle:
# -----------------------------
# write down and invoke the function that you are using for this testing
# in the space below
"""
def your_gosper_curve_with_angle(level, angle_at_level):
    if level == 0:
        return unit_line
    else:
        return your_gosperize_with_angle(angle_at_level(level))(your_gosper_curve_with_angle(level-1, angle_at_level))

def your_gosperize_with_angle(theta):
    def inner_gosperize(curve_fn):
        left_curve = rotate(theta)(curve_fn)
        right_curve = rotate(-theta)(curve_fn)
        return put_in_standard_position(connect_ends(left_curve, right_curve))
    return inner_gosperize

for i in range(5):
    print(profile_fn(lambda: your_gosper_curve_with_angle(1000, lambda x: math.pi/4)(0.1), 2))
"""
# ***
# Level: 1000
# Iterations: 2
# ***
# Time 1: 9849.27289999905
# Time 2: 9736.75379999986
# Time 3: 9802.611199998864
# Time 4: 9825.408799999423
# Time 5: 9830.632700000933
# Average: 9808ms (truncating decimals)

# Conclusion:
# Comparing gosper_curve with gosper_curve_with_angle, we see that the less customizable function gosper_curve actually
# runs slightly slower (~3.7%) since it took an average of 390ms longer to run 3000 tests for a point at level 1000.
#
# Comparing gosper_curve_with_angle to your_gosper_curve_with_angle, however, produces a rather surprising result: The
# time taken to run your_gosper_curve_with_angle for only 2 iterations is almost the same as that used by gosper_curve_with_angle
# for 3000 iterations for the same level.
#
# While the results slightly contradicts one another, I would say that more customizable functions take longer to run
# given how significant the difference is in the second comparison. But how is the difference even that large??

##########
# Task 2 #
##########

#  1) Yes, he simply replaced "pt" with it's original definition


#  2) In rotate(), curve(t) is only called once and the point is saved in the variable "pt" in each iteration.
#     However, in joe_rotate(), curve(t) is called twice each iteration. Each level of recursion hence doubles the number of
#     curve() function calls. This results in a time complexity of O(2**n), which is exponential compared to the original O(n).


print(profile_fn(lambda: gosper_curve(10)(0.1), 1000))

##########
# Task 3 #
##########

#
# Fill in this table:
#
#                    level      rotate       joe_rotate 
#                      1          3              4
#                      2          5              10
#                      3          7              22
#                      4          9              46
#                      5          11             94
#
#  Difference between number of calls in each iteration for rotate: constant at 2
#  Difference between number of calls in each iteration for joe_rotate:
#  6, 12, 24, 48
#  Since the difference doubles in every iteration, the complexity of joe_rotate is exponential.
#  Complexity: O(a * 2**n + b)
#  Subbing in data points, we get the final equation O(3 * 2**n - 2), which simplifies to O(2**n).
#  Hence, joe_rotate() is indeed much less desirable since it has a time complecity of O(2**n) as compared to
#  rotate(), whose complexity is only O(n).
