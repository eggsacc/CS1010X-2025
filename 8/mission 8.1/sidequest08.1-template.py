#
# CS1010S --- Programming Methodology
#
# Sidequest 8.1 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from planets import *
from math import sin, cos, pi, sqrt
# Set up the environment of the simulation
planets = (Earth, Mars, Moon)

plot_planets(planets, Mars)

##########
# Task 1 #
##########
# a)
# Follows trigonometry angle.
# E.g. 0 degree -> East
# E.g. 90 degree -> North
def get_velocity_component(angle, velocity):
    v_x = velocity * cos(angle / 180 * pi)
    v_y = velocity * sin(angle / 180 * pi)

    return (v_x, v_y)

# print(get_velocity_component(30, 50)) #(43.30127018922194, 24.999999999999996)
# note that the exact values of each component may differ slightly due to differences in precision

# b)
def calculate_total_acceleration(planets, current_x, current_y):
    total_accel_x = 0
    total_accel_y = 0
    
    for planet in planets:
        planet_x = get_x_coordinate(planet)
        planet_y = get_y_coordinate(planet)
        planet_mass = get_mass(planet)
        
        distance = sqrt((abs(planet_x - current_x))**2 + (abs(planet_y - current_y))**2)
        
        r_x = planet_x - current_x
        r_y = planet_y - current_y
        
        accel_x = G * planet_mass * r_x / ((distance) ** 3)
        accel_y = G * planet_mass * r_y / ((distance) ** 3)
        
        total_accel_x += accel_x
        total_accel_y += accel_y
        
    return (total_accel_x, total_accel_y)

print(calculate_total_acceleration(planets, 0.1, 0.1)) #(-1511.54410020574, -1409.327982470404)

# c)
# Do not change the return statement
def f(t, Y):
    vx = Y[2] 
    vy = Y[3] 
    ax, ay = calculate_total_acceleration(planets, Y[0], Y[1])
    #your code here
    return np.array([vx, vy, ax, ay])

np.set_printoptions(precision=3)
print(f(0.5, [0.1, 0.1, 15.123, 20.211])) #[ 15.123 20.211 -1511.544 -1409.328]

##########
# Task 2 #
##########

# Uncomment and change the input parameters to alter the path of the spacecraft
vx, vy = get_velocity_component(79, 27.2)


##############################################################################################
# Uncomment the following line to start the plot
start_spacecraft_animation(vx, vy, f)
