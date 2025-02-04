#
# CS1010X --- Programming Methodology
#
# Mission 2 - 2D Contest
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *

########
# Task #
########

# You may submit up to 3 entries. Please update your entry number below.

# Entry 0 of 3
# ============
# Write your function here. It should return a rune.

# @brief Creates a spiral pattern from primitive
# @param[in] size (number of iterations)
# @param[in] primitive
# @retval painter function

def spiral(size, primitive):

    # Generate primitive box
    row = quarter_turn_left(stackn(size, primitive))
    vert_row = quarter_turn_left(stackn(size - 2, primitive))
    column = stack_frac(1/size, vert_row, stack_frac((size - 2)/(size - 1), blank_bb, vert_row))
    prim = stack_frac(1/size, row, stack_frac((size - 2)/(size - 1), quarter_turn_right(column), row))

    canvas = prim

    # Overlay rotated & scaled boxes to form spiral
    for i in range(size):
        canvas = overlay_frac(2/(2+i), prim, scale(0.918, rotate(0.05, canvas)))

    return canvas


hollusion(spiral(50, black_bb))




