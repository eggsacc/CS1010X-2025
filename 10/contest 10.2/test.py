from contest import *
from puzzle_AI import *
import cma
from statistics import mean


def evaluate_weights(weights):
    scores = []

    def ai(board):
        return AI(board, weights)

    for _ in range(10):  # Run 10 games per weight set (adjust as needed)
        score, mat, _ = get_AI_score(ai)  # You need to implement this
        scores.append(score)
    return -mean(scores) 

def optimize_weights():
    # Initial guess for weights (e.g., [w1, w2, w3, w4, w5])
    initial_weights = [1.0, 2.0, 1.5, 1.0, 2.0, 0.3]
    
    # Define bounds (optional but helps stability)
    bounds = [0.1, 10.0]
    
    # Run CMA-ES
    es = cma.CMAEvolutionStrategy(
        initial_weights,  # Initial guess
        0.5,             # Initial step size (sigma)
        {'bounds': bounds, 'maxiter': 30}  # Max iterations
    )
    
    # Optimize
    while not es.stop():
        solutions = es.ask()  # Generate new candidate solutions
        fitness = [evaluate_weights(x) for x in solutions]  # Evaluate each
        es.tell(solutions, fitness)  # Update CMA state
    
    # Best found weights
    best_weights = es.result.xbest
    print("Optimized weights:", best_weights)
    return best_weights

print(optimize_weights())

# [0.3297049,  1.78679355, 1.39111996, 0.5508617,  1.5550242]
# [1.747407,  3.22317644, 1.38721803, 2.20519778, 1.04636205]