#
# CS1010X --- Programming Methodology
#
# Contest 7.2 Template

from more_lazy_susan import *
import random

lcg_seed = 1

# @brief Pseudo-random number generator
#        (Linear congruential generator)
#
# @param[in] max value
# @retval Random int -> [0, max]
def lcg(max):
    global lcg_seed
    result = (1664525 * lcg_seed + 1013904223) & 0xFF
    lcg_seed = result
    return int(result / 255 * max)

def create_solver(coins):
    # insert your code here

    def random_solver(move_id):
        k = lcg(coins - 1)
        return [True] * k + [False] * (coins - k)
    
    def random_solver_2(move_id):
        idx = lcg(coins // 2)
        k = lcg(coins - idx - 1)
        return [False] * idx + [True] * k + [False] * (coins - idx - k)
    
    def random_solver_3(move_id):
        k = random.randint(1, coins-1)
        move = [True]* k + [False] * (coins - k)
        random.shuffle(move)
        return move

    return random_solver_3

def tester(solver, level, iterations, verbouse=False):
    sizes = [10, 13, 15]
    size = sizes[level]
    scores = [0 for i in range(size-1)]

    for iter in range(iterations):
        if(verbouse):
            print(f"##### Iteration #{iter+1} #####")
        for i in range(1, size):
            result = get_contest_score_2(solver, level, i)
            if(verbouse):
                print(f"k:{i}, result: {result}")
            scores[i-1] += result
    
    print(f"### Size: {size}, iterations: {iterations}###")
    for i in range(len(scores)):
        print(f"{i+1}, {scores[i] / iterations}")

# UNCOMMENT THE FOLLOWING LINE AND RUN TO GRADE YOUR SOLVER
#get_contest_score_2(create_solver, 0)
tester(create_solver, 0, 5, True)
tester(create_solver, 1, 5)
tester(create_solver, 2, 5)