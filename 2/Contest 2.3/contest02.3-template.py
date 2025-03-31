#
# CS1010X --- Programming Methodology
#
# Mission 2 - 3D Contest
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *

########
# Task #
########

# You may submit up to three entries. Please update your entry number below.

# Entry 1 of 3
# ============
# Write your function here. It should return a rune.

# Found an artist called Kazuki Takamatsu, his artworks looks exactly like a depth map.
# The sample image is a color inverted version of his artpiece "Impression of Death"

# @brief Generates a spiral frame using a primitive
def frame(size, pim):

    # Some constants to tweak while experimenting
    primitive = black_bb
    scale_fac = 1
    
    # Generate primitive box
    row = quarter_turn_left(stackn(size, scale(scale_fac, primitive)))
    vert_row = quarter_turn_left(stackn(size - 2, scale(scale_fac, primitive)))
    column = stack_frac(1/size, vert_row, stack_frac((size - 2)/(size - 1), blank_bb, vert_row))
    prim = stack_frac(1/size, row, stack_frac((size - 2)/(size - 1), quarter_turn_right(column), row))

    canvas = prim

    # Generate spiral frame
    for i in range(5):
        canvas = overlay_frac(2/(2+i), prim, scale(0.97, rotate(0.02, canvas)))

    # Layering: frame - image - frame
    return overlay_frac(0.6, overlay_frac(0.4, canvas, pim), rotate(0.1, scale(0.85, canvas)))
    
pim = image_to_painter("7.jpg")

hollusion(frame(25, pim))
