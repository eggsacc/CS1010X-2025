#
# CS1010X --- Programming Methodology
#
# Mission 2
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *


###########
# Task 1a #
###########

# @brief Recursively generates fractal based on primitive.
#
#        Uses a helper function recursive_func to preserve original primitive
#        through iterations.

def fractal(primitive, iterations):
    # Fill in code here
    # Helper function
    def recursive_func(current_fractal, remaining_iterations):
        
        if(remaining_iterations == 1):
            return current_fractal
        else:
            # Stack previous fractal & place beside original primitive
            stacked_prim = stack(current_fractal, current_fractal)
            new_fractal = beside(primitive, stacked_prim)
            return recursive_func(new_fractal, remaining_iterations - 1)
        
    return recursive_func(primitive, iterations)
    

# Test
# show(fractal(make_cross(rcross_bb), 3))
# show(fractal(make_cross(rcross_bb), 7))
# Write your additional test cases here

###########
# Task 1b #
###########

def fractal_iter(primitive, iterations):
    # Fill in code here
    if(iterations == 1):
        return primitive

    new_fractal = primitive

    for _ in range(iterations - 1):
        stacked_prim = stack(new_fractal, new_fractal)
        new_fractal = beside(primitive, stacked_prim)
        
    return new_fractal

# Test
# show(fractal_iter(make_cross(rcross_bb), 3))
# show(fractal_iter(make_cross(rcross_bb), 7))
# Write your additional test cases here


###########
# Task 1c #
###########

def dual_fractal(prim_a, prim_b, iterations):
    # Helper function
    def recursive_func(current_fractal, remaining_iterations):
        
        if(remaining_iterations == 1):
            return current_fractal
        else:
            # Stack previous fractal & place beside either prim_a or prim_b, depending on iteration count
            stacked_prim = stack(current_fractal, current_fractal)
            
            new_fractal = beside(prim_a if remaining_iterations % 2 == 0 else prim_b, stacked_prim)
            
            return recursive_func(new_fractal, remaining_iterations - 1)

    # Start with prim_a or prim_b depending on if number of iterations is odd or even
    return recursive_func(prim_b if iterations % 2 == 0 else prim_a, iterations)

# Test
# show(dual_fractal(make_cross(rcross_bb), make_cross(nova_bb), 1))
# show(dual_fractal(make_cross(rcross_bb), make_cross(nova_bb), 4))
# show(dual_fractal(make_cross(rcross_bb), make_cross(nova_bb), 7))
# Write your additional test cases here

# Note that when n is even, the first (biggest) rune should still be rune1

###########
# Task 1d #
###########

def dual_fractal_iter(prim_a, prim_b, iterations):
    # Fill in code here
    if(iterations == 1):
        return prim_a

    # Decide which primitive to start with 
    new_fractal = prim_b if iterations % 2 == 0 else prim_a
    prim_to_place = 0 if iterations % 2 == 0 else 1
    
    for i in range(iterations - 1):
        stacked_prim = stack(new_fractal, new_fractal)
        new_fractal = beside(prim_a if prim_to_place == 0 else prim_b, stacked_prim)
        
        # Toggle fractal
        prim_to_place ^= 1
        
    return new_fractal

# Test
# show(dual_fractal_iter(make_cross(rcross_bb), make_cross(nova_bb), 3))
# show(dual_fractal_iter(make_cross(rcross_bb), make_cross(nova_bb), 4))
# show(dual_fractal_iter(make_cross(rcross_bb), make_cross(nova_bb), 7))
# Write your additional test cases here

# Note that when n is even, the first (biggest) rune should still be rune1

##########
# Task 2 #
##########

def steps(prim_a, prim_b, prim_c, prim_d):
    # Fill in code here
    # Generate 4 layers
    layer_1 = beside(stack(prim_d, blank_bb), stack(blank_bb, blank_bb))
    layer_2 = beside(stack(blank_bb, prim_c), stack(blank_bb, blank_bb))
    layer_3 = beside(stack(blank_bb, blank_bb), stack(blank_bb, prim_b))
    layer_4 = beside(stack(blank_bb, blank_bb), stack(prim_a, blank_bb))

    # Stack the 4 layers
    return overlay(overlay(layer_1, layer_2), overlay(layer_3, layer_4))
                    

# Test
# show(steps(rcross_bb, sail_bb, corner_bb, nova_bb))
