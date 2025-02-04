#
# CS1010X --- Programming Methodology
#
# Mission 5 - Sidequest 3
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hi_graph_connect_ends import *

##########
# Task 1 #
##########

def dragonize(order, curve):
    "your answer here"
    if(order == 0):
        return curve
    else:
        new_curve = dragonize(order - 1, curve)
        return put_in_standard_position(connect_ends(revert(rotate(-pi/2)(new_curve)), new_curve))

# test:
draw_connected_scaled(100, dragonize(3, unit_line))

# draw_connected_scaled(200, connect_ends(revert(unit_line), unit_circle))
