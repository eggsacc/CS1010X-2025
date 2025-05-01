#
# CS1010X --- Programming Methodology
#
# Contest 10.2 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from random import *
from puzzle_AI import *
import math

##########################################################################################
#                            BIT BOARD UTILITY FUNCTIONS 
##########################################################################################

# @brief Converts a standard game board to bit board representation
# @note MSB = board[0][0]
# @retval bit board
def convert_to_bitboard(board):
    size = len(board)
    bitboard = 0
    for i in range(size):
        for j in range(size):
            if(board[i][j] == 0):
                bitboard <<= 4
            else:
                bitboard = (bitboard << 4) | (int(math.log2(board[i][j])) & 0x0F)
    return bitboard

# @brief Count number of zeores in bit board without iteration
# @warning Fails if input bit board is all 0; result will overflow
# @retval bit board
def count_zero_bitboard(bitboard):
    bitboard |= (bitboard >> 2) & 0x3333333333333333
    bitboard |= (bitboard >> 1)
    bitboard = ~bitboard & 0x1111111111111111
    bitboard += bitboard >> 32
    bitboard += bitboard >> 16
    bitboard += bitboard >> 8
    bitboard += bitboard >> 4
    return bitboard & 0xF

# @brief Locate positions with a 0 in bit board
# @retval list of positions
def find_zero_bitboard(bitboard):
    empty = []
    for i in range(16):
        tile = (bitboard >> (i * 4)) & 0xF
        if(tile == 0):
            empty.append(15 - i)
    return empty

# @brief Returns if win, lose or on-going for a bit board state
# @retval 0 : ongoing, 1 : win -1 : lose
def bitboard_status(bitboard):
    has_empty = False
    combinable_adjacent = False
    temp = 0xF000000000000000
    prev = 0
    tiles = []
    for i in range(16):
        tile = (bitboard & temp) >> (60 - i * 4)
        tiles.append(tile)
        if(tile == 0xB):
            return 1
        if(tile == 0):
            has_empty = True
        if(prev == tile and tile != 0):
            combinable_adjacent = True
        if((i + 1) % 4 == 0):
            prev_tile = 0
        else:
            prev_tile = tile
        temp >>= 4
    
    if(has_empty):
        return 0

    for col in range(4):
        for row in range(3):
            i = row * 4 + col
            if tiles[i] != 0 and tiles[i] == tiles[i + 4]:
                combinable_adjacent = True
                break
    
    if(combinable_adjacent):
        return 0

# @brief Reverses each row of bit board
# @retval bit board
def reverse_bitboard(bitboard):
    r0 = (bitboard >> 48) & 0xFFFF
    r1 = (bitboard >> 32) & 0xFFFF
    r2 = (bitboard >> 16) & 0xFFFF
    r3 = bitboard & 0xFFFF
    r0_n = r1_n = r2_n = r3_n = 0
    mask = 0xF
    for i in range(4):
        r0_n = (r0_n << 4) | ((r0 >> i*4) & mask)
        r1_n = (r1_n << 4) | ((r1 >> i*4) & mask)
        r2_n = (r2_n << 4) | ((r2 >> i*4) & mask)
        r3_n = (r3_n << 4) | ((r3 >> i*4) & mask)
 
    return r0_n << 48 | r1_n << 32 | r2_n << 16 | r3_n

# @brief Transposes bit board
# @retval bit board
def transpose_bitboard(bitboard):
    a1 = bitboard & 0xF0F00F0FF0F00F0F
    a2 = bitboard & 0x0000F0F00000F0F0
    a3 = bitboard & 0x0F0F00000F0F0000
    a = a1 | (a2 << 12) | (a3 >> 12)
    b1 = a & 0xFF00FF0000FF00FF
    b2 = a & 0x00FF00FF00000000
    b3 = a & 0x00000000FF00FF00
    return b1 | (b2 >> 24) | (b3 << 24)

# @brief Merges a bit row towards the right
# @retval bit row
def merge_row_right(bitrow):
    ret = 0
    idx = 0
    mask = 0xF
    prev_tile = -1
    for i in range(4):
        tile = (bitrow >> (i * 4)) & mask
        if(tile != 0):
            if(tile == prev_tile):
                ret = ret & ~(mask << (idx - 4))
                ret |= (tile + 1) << (idx - 4)
            else:
                ret |= tile << idx 
                idx += 4
            prev_tile = tile
    return ret, ret != bitrow
    
# @brief Merges bit board towards the right
# @retval bit board
def merge_bitboard_right(bitboard):
    ret = 0 
    row_mask = 0xFFFF
    modified = False
    for i in range(4):
        row = (bitboard >> (i * 16)) & row_mask
        row, status = merge_row_right(row)
        if(status):
            modified = True
        ret |= row << (i * 16)
    return ret, modified

# @brief Merges bit board towards the left
# @retval bit board
def merge_bitboard_left(bitboard):
    ret, modified = merge_bitboard_right(reverse_bitboard(bitboard))
    return reverse_bitboard(ret), modified

# @brief Merges bit board down
# @retval bit board
def merge_bitboard_down(bitboard):
    ret, modified = merge_bitboard_right(transpose_bitboard(bitboard))
    return transpose_bitboard(ret), modified

# @brief Merges bit board up
# @retval bit board
def merge_bitboard_up(bitboard):
    ret, modified = merge_bitboard_right(reverse_bitboard(transpose_bitboard(bitboard)))
    return transpose_bitboard(reverse_bitboard(ret)), modified

##########################################################################################

##########################################################################################
#                                  SOLVER FUNCTIONS
##########################################################################################

# @brief Evaluate bit board by assigning a score to how favourable the state is
# @retval score
def evaluate_bitboard(bitboard, weights):
    w1, w2, w3, w4, w5, w6 = weights
    status = bitboard_status(bitboard)
    if(status == 1):
        return 99999
    if(status == -1):
        return -99999
    
    empty_cells = count_zero_bitboard(bitboard)
    
    # Gradient weights - prefer high values in upper corners
    gradient_weights = [15, 12, 13, 12, 
                        10,  9,  10, 10, 
                        7,  6,  5,  4, 
                        0,  1,  2,  3]
    
    smoothness = 0
    monotonicity = 0
    gradient_score = 0
    corner_bonus = 0
    max_tile = 0
    max_tile_pos = 0
    
    # Gradient & max tile - prefer boards with tile values that vary smoothly
    for i in range(16):
        tile = (bitboard >> (60 - i * 4)) & 0xF
        if(tile > max_tile):
            max_tile = tile
            max_tile_pos = i
        gradient_score += (1 << tile) * gradient_weights[i]

        if(tile != 0):
            next_tile_right_idx = 0
            next_tile_down_idx = i + 4
            if((i + 1) % 4 != 0):
                next_tile_right_idx = i + 1
            
            if(0 < next_tile_right_idx < 16 and (bitboard >> (next_tile_right_idx * 4)) & 0xF != 0):
                smoothness -= abs(tile - ((bitboard >> (next_tile_right_idx * 4)) & 0xF))
            
            if(0 < next_tile_down_idx < 16 and (bitboard >> (next_tile_down_idx * 4)) & 0xF != 0):
                smoothness -= abs(tile - ((bitboard >> (next_tile_down_idx * 4)) & 0xF))

    # Encourage max tile to be placed in corner
    if max_tile_pos in [0, 3, 12, 15]:
        corner_bonus = 1 << max_tile

    # Monotonicity - prefer increasing/decreasing sequences
    for i in range(4):
        monotonic = True
        reverse_monotonic = True
        prev = 0
        for j in range(4):
            tile = bitboard >> (60 - (i * 16 + j * 4)) & 0xF
            if(tile < prev):
                monotonic = False
            if(tile > prev):
                reverse_monotonic = False
            prev = tile
        if(monotonic or reverse_monotonic):
            monotonicity += 1
        
    # Weighted sum
    return (
        w1 * empty_cells +
        w2 * gradient_score +
        w3 * smoothness +
        w4 * monotonicity +
        w5 * max_tile + 
        w6 * corner_bonus
    )

    
def AI(board):
    moves = ['w', 'a', 's', 'd']
    depths = [3, 4, 5, 6]  

    # Weights are tuned using covariance matrix adaptation evolution strategy (CMA-ES)
    weights=[1.59606712, 1.93039872, 2.72886157, 0.10211406, 0.14038919, 1.42701307]

    # Memoization cache
    cache = {}
    
    bitboard = convert_to_bitboard(board)

    # Count zeroes to determine how occupied the board it.
    zeroes = count_zero_bitboard(bitboard)

    # Variable depth search: more populated boards have greater search depth
    # This is to expedite the filling of loosely populated boards at the starting stages
    depth = depths[int(zeroes/16 * 2)]

    def move(bitboard, key):
        if(key == 'w'):
            return merge_bitboard_up(bitboard)
        elif(key == 'a'):
            return merge_bitboard_left(bitboard)
        elif(key == 's'):
            return merge_bitboard_down(bitboard)
        else:
            return merge_bitboard_right(bitboard)
    
    # @brief Expectimax function to recursively simulate furthur gameplay
    # @note Uses basic alpha-beta pruning
    def expectimax(bitboard, depth, turn, alpha=float('-inf'), beta=float('inf')):
        board_hash = str(bitboard)
        if board_hash in cache and cache[board_hash]['depth'] >= depth:
            return cache[board_hash]['score']
        
        if depth == 0:
            return evaluate_bitboard(bitboard, weights)
        
        if(turn == 1):  
            max_score = -99999
            for key in moves:
                new_bitboard, valid = move(bitboard, key)
                if not valid:
                    continue
                score = expectimax(new_bitboard, depth-1, 0, alpha, beta)
                if score > max_score:
                    max_score = score
                alpha = max(alpha, score)
                if beta <= alpha:
                    break
            cache[board_hash] = {'score': max_score, 'depth': depth}
            return max_score

        else:  
            empty_idx = find_zero_bitboard(bitboard)
            if not empty_idx:
                return evaluate_bitboard(bitboard, weights)
            
            total = 0
            for idx in empty_idx:
                new_bitboard = bitboard | (1 << (60 - idx * 4))
                total += expectimax(new_bitboard, depth-1, 1, alpha, beta)

            avg_score = total / len(empty_idx)
            cache[board_hash] = {'score': avg_score, 'depth': depth}
            return avg_score
    
    best_move = None
    best_score = -999999
    
    # Find best move
    for key in moves:
        new_bitboard, valid = move(bitboard, key)
        if not valid:
            continue
        score = expectimax(new_bitboard, depth-1, 0)
        if score > best_score:
            best_score = score
            best_move = key
    
    return best_move


# UNCOMMENT THE FOLLOWING LINES AND RUN TO WATCH YOUR SOLVER AT WORK
#game_logic['AI'] = AI
#gamegrid = GameGrid(game_logic)

# UNCOMMENT THE FOLLOWING LINE AND RUN TO GRADE YOUR SOLVER
# Note: Your solver is expected to produce only valid moves.
if(__name__ == '__main__'):
    get_average_AI_score(AI, True)
