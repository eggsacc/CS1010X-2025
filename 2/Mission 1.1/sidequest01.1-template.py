#
# CS1010X --- Programming Methodology
#
# Mission 1 - Side Quest
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *

##########
# Task 1 #
##########

# @brief Generates a nxn square with primitive in the center.
#
# Achieved by dividing the pattern into 3 sections: top/bottom row, and a center block
# consisting of the center primitive sandwiched between 2 vertical columns of length n-2.
#
# *|*|*|*|*  -> top row
# ---------
# *|     |*
# *|prim |*  -> center block (2 vertical columns + large center primitive)
# *|     |*
# ---------
# *|*|*|*|* -> bottom row
#
# 1) Top/bottom rows are formed by stacking primitives vertically then rotating by 90deg to form horizontal rows
# 2) Center block is formed by stacking column->primitive->column vertically then rotating 90deg
#
# * * *     *      *
# prim  ->  * prim *
# * * *     *      *
#
# 3) Finally stack all together with proportional heights

def egyptian(primitive, n):
    # Fill in code here
    # Left & right columns
    left_right_column = stackn(n - 2, primitive)

    # Top & bottom rows
    top_bottom_row = quarter_turn_left(stackn(n, quarter_turn_right(primitive)))
    
    # Center chunk
    # @note Account for rotation of center primitive
    center_row = stack_frac(1 - 1/(n-1), quarter_turn_right(primitive), quarter_turn_right(left_right_column))

    # Combine layers
    center_row = stack_frac(1/n, quarter_turn_right(left_right_column), center_row)
    final = stack_frac(1 - 1/(n-1), quarter_turn_left(center_row), top_bottom_row)
    final = stack_frac(1/n, top_bottom_row, final)
    
    return final

# Test
show(egyptian(nova_bb, 9))
