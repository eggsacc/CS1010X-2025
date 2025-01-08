#
# CS1010X --- Programming Methodology
#
# Mission 1
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *


##########
# Task 1 #
##########

def mosaic(prim_a, prim_b, prim_c, prim_d):
    # Fill in code here
    top_half = beside(prim_d, prim_a)
    bottom_half = beside(prim_c, prim_b)
    return stack(top_half, bottom_half)

# Test
# show(mosaic(rcross_bb, sail_bb, corner_bb, nova_bb))


##########
# Task 2 #
##########

def simple_fractal(primitive):
    # Fill in code here
    right_stack = stack(primitive, primitive)
    
    return beside(primitive, right_stack)

# Test
# show(simple_fractal(make_cross(rcross_bb)))

