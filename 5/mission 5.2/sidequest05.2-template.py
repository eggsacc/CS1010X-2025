#
# CS1010X --- Programming Methodology
#
# Mission 5 - Sidequest 2
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hi_graph_connect_ends import *

##########
# Task 1 #
##########

import math

def kochize(level):
    "your answer here"
    if(level == 0):
        return unit_line
    else:
        curve = kochize(level - 1)
        return scale(1/3)(connect_ends(connect_ends(curve, rotate(math.pi/3)(curve)),
                            connect_ends(rotate(-math.pi/3)(curve), curve)))

def show_connected_koch(level, num_points):
    draw_connected(num_points, kochize(level))

#show_connected_koch(0, 4000)
#show_connected_koch(5, 4000)

##########
# Task 2 #
##########

def snowflake():
    "your answer here"
    fractal_portion = kochize(5)
    final = fractal_portion
    
    for i in range(1, 4):
        final = connect_ends(final, rotate(-i * 2 * math.pi / 3)(fractal_portion))

    return final

draw_connected_scaled(10000, snowflake())
