#
# CS1010X --- Programming Methodology
#
# Mission 2 - Side Quest 1
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *
from math import sin, cos, pi

##########
# Task 1 #
##########

def tree(n, primitive):
    # Fill in code here
    canvas = primitive
    
    for i in range(0, n-1):
        prim_scaled = scale((n - i - 1)/n, primitive)
        canvas = overlay_frac(1/(2 + i), prim_scaled, canvas)
    print(canvas)  
    return canvas

# Test
#show(tree(4, circle_bb))


##########
# Task 2 #
##########

# use help(math) to see functions in math module
# e.g to find out value of sin(pi/2), call math.sin(math.pi/2)

# @brief Creates a circle of primitives of decreasing depth
#
# Notes:
# Individual runes scaled -> 2/n
# Circular pattern radius -> 1/2 - 1/n
# Darkest (highest) rune -> bottom center
# Depth increases in anti-clockwise manner
#
# Approach: Start from lowest depth (first rune to the left of bottom center) and go clockwise.
#           For each rune, calculate new translation based on iteration * discrete step angle (2pi / n)
#
# Equations used (delta x, y after rotating a rune from bottom center clockwise by angle θ):
# delta_x = -radius * sin(θ)
# delta_y = radius * cos(θ)

def helix(primitive, n):
    # Fill in code here
    # Sclaing of primitive, radius & discrete step angle calculation
    scaled_prim = scale(2/n, primitive)
    radius = 0.5 - 1/n
    angle_step = (2*math.pi) / n
    print(f"radius: {radius}, step_angle: {angle_step}")
    # Generate initial canvas (lowest depth rune)
    delta_x = -radius * math.sin(angle_step)
    delta_y = radius * math.cos(angle_step)
    canvas = translate(delta_x, delta_y, scaled_prim)
    
    for i in range(n - 1):
        # +2 offset in tranlation angle iterations since the base canvas
        # is already the first rune in clockwise direction.
        delta_x = -radius * math.sin((i + 2)*angle_step)
        delta_y = radius * math.cos((i + 2)*angle_step)

        print(f"{delta_x}, {delta_y}")
        translated_prim = translate(delta_x, delta_y, scaled_prim)
        
        # Overlay translated primitive with even spacing
        canvas = overlay_frac(1/(2 + i), translated_prim, canvas)
        print(1/(2 + i))
        
    return canvas

# Test
show(helix(make_cross(rcross_bb),12))
