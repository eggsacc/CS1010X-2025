#
# CS1010X --- Programming Methodology
#
# Mission 5 - Sidequest 1
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hi_graph import *

##########
# Task 1 #
##########

# Visual difference: The points on unit_circle are evenly spaced out, while the points on alternative_unit_circle
# are more concentrated at the top and becomes more spread out going clockwise.
# Code difference: The angle between points scale linearly with t in unit_circle, while the angle scales quadratically in alternative_unit_circle.
# The quadratic scaling of the angle with respect to t leads to the non-uniform & increasing spacing between points.

##########
# Task 2 #
##########

# (a)
def spiral(t):
    "your answer here"
    # Spiral is a circle with increasing radius
    r = t
    return make_point(r* sin(2*pi*t), r * cos(2*pi*t))
# draw_connected_scaled(1000, spiral)

# (b)
def heart(t):
    "your answer here"
    def mirror(curve):
        def mirrored(t):
            pt = curve(t)
            return make_point(-x_of(pt), y_of(pt))
        return mirrored
    
    return connect_rigidly(spiral, mirror(spiral))(t)






draw_connected_scaled(1000, heart)
