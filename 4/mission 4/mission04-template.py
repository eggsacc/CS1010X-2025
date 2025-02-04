#
# CS1010X --- Programming Methodology
#
# Mission 4
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hi_graph import *

##########
# Task 1 #
##########

# (a)
# unit_line_at_y: (Number) -> (Curve)
# Quite confused about this: I assume the 'Curve' type is just any function that generates points
# based on number of unit-intervals?

# (b)
# a_line: (Unit-interval) -> (Point)

# (c)
def vertical_line(point, length):
    "your answer here"
    # Vertical line: x-coord constant, changing y
    # Unit interval is the fraction of the total length, hence y-coord = t*length
    # Offset by point x, y
    return lambda t: make_point(x_of(point), t*length + y_of(point))

#draw_connected(200, vertical_line(make_point(0.1, 0.1), 0.4))

# (d)
# vertical_line: (Point, Number) -> (Curve)

# (e)
# draw_connected(2, vertical_line(make_point(0.5, 0.25), 0.5))

##########
# Task 2 #
##########

# (a)
# Maybe can call the reflect function twice to see if the resulting curve is the same as original.
# Another way if verbose debugging is allowed is probably just to print out the x and y values of
# some/each point generated for each unit interval, of both the original & reflected curve

# (b)
def reflect_through_y_axis(curve):
    # Reflection about y-axis: negate x-coords
    def reflected_curve(t):
        "your answer here"
        point = curve(t)
        return make_point(-x_of(point), y_of(point))

    return reflected_curve
	
draw_connected_scaled(200, arc)
draw_connected_scaled(200, reflect_through_y_axis(arc))
