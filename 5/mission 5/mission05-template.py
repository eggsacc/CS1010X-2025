#
# CS1010X --- Programming Methodology
#
# Mission 5
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hi_graph import *

##########
# Task 1 #
##########

def connect_ends(curve1, curve2):
    "your solution here!"
    c1_endpoint = curve1(1)
    c2_startpoint = curve2(0)
    delta_x = x_of(c1_endpoint) - x_of(c2_startpoint)
    delta_y = y_of(c1_endpoint) - y_of(c2_startpoint)
    translater = translate(delta_x, delta_y)
    c2_translated = translater(curve2)
    return connect_rigidly(curve1, c2_translated)


##########
# Task 2 #
##########

#scaling factor: rt(2) / 2
# rotated pi/4 and -pi/4
# translated such that endpoint of c1 matches start of c2
def show_points_gosper(level, num_points, initial_curve):
    "your solution here!"
    def gosper_curve_any(level):
        return repeated(gosperize, level)(initial_curve)
    
    def show_point_gosper(level):
         squeezed_curve = squeeze_curve_to_rect(-0.5,-0.5, 1.5, 1.5)(gosper_curve_any(level))
         draw_points(num_points, squeezed_curve)
         
    show_point_gosper(level)

##########
# Task 3 #
##########

def your_gosper_curve_with_angle(level, angle_at_level):
    if level == 0:
        return unit_line
    else:
        return your_gosperize_with_angle(angle_at_level(level))(your_gosper_curve_with_angle(level-1, angle_at_level))

def your_gosperize_with_angle(theta):
    def inner_gosperize(curve_fn):
        left_curve = rotate(theta)(curve_fn)
        right_curve = rotate(-theta)(curve_fn)
        return put_in_standard_position(connect_ends(left_curve, right_curve))
    return inner_gosperize

# testing
# draw_connected(200, your_gosper_curve_with_angle(10, lambda lvl: pi/(2+lvl)))
# draw_connected(200, your_gosper_curve_with_angle(5, lambda lvl: (pi/(2+lvl))/(pow(1.3, lvl))))
