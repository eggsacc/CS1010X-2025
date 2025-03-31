#
# CS1010X --- Programming Methodology
#
# Mission 7 - Sidequest 1
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from lazy_susan import *

##########
# Task 1 #
##########

def solve_trivial_2(table):
    """ Write your code here """
    flip_coins(table, get_table_state(table))
    

# test:
# t2_1 = create_table(2)
# solve_trivial_2(t2_1)
# print(check_solved(t2_1))


########################################################
## VISUALIZATION ALTERNATIVE
## Run the following two lines below to see how the
## coins on the table are flipped and rotated.

# t2_1_run = create_table(2)
# run(t2_1_run, solve_trivial_2)

########################################################
## GUI ALTERNATIVE
## Run the following two lines below to use the
## interactive GUI to solve the table instead.

# t2_1_susan = create_table(4)
# Susan(t2_1_susan)

########################################################





##########
# Task 2 #
##########

def solve_trivial_4(table):
    """ Write your code here """
    flip_coins(table, get_table_state(table))


# test:
# t4_2 = create_table(4)
# solve_trivial_4(t4_2)
# print(check_solved(t4_2))


########################################################
## VISUALIZATION ALTERNATIVE
## Run the following two lines below to see how the
## coins on the table are flipped and rotated.

# t4_2_run = create_table(4)
# run(t4_2_run, solve_trivial_4)

########################################################
## GUI ALTERNATIVE
## Run the following two lines below to use the
## interactive GUI to solve the table instead.

# t4_2_susan = create_table(4)
# Susan(t4_2_susan)

########################################################





##########
# Task 3 #
##########

def solve_2(table):
    """ Write your code here """
    if(check_solved(table)):
        return

    flip_coins(table, (1, 0))
   

# test:
# t2_3 = create_table(2)
# solve_2(t2_3)
# print(check_solved(t2_3))


########################################################
## VISUALIZATION ALTERNATIVE
## Run the following two lines below to see how the
## coins on the table are flipped and rotated.

# t2_3_run = create_table(2)
# run(t2_3_run, solve_2)

########################################################
## GUI ALTERNATIVE
## Run the following two lines below to use the
## interactive GUI to solve the table instead.

# t2_3_susan = create_table(2)
# Susan(t2_3_susan)

########################################################





##########
# Task 4 #
##########

def solve_4(table):
    """ Write your code here """
    seq_a = (1, 0, 1, 0)
    seq_b = (1, 1, 0, 0)
    seq_c = (1, 0, 0, 0)

    flip_seq = (seq_a, seq_b, seq_a, seq_c, seq_a, seq_b, seq_a)

    for seq in flip_seq:
        if(check_solved(table)):
            return
        
        flip_coins(table, seq)

# test:
# t4_4 = create_table(4)
# solve_4(t4_4)
# print(check_solved(t4_4))


########################################################
## VISUALIZATION ALTERNATIVE
## Run the following two lines below to see how the
## coins on the table are flipped and rotated.

# t4_4_run = create_table(4)
# run(t4_4_run, solve_4)

########################################################
## GUI ALTERNATIVE
## Run the following two lines below to use the
## interactive GUI to solve the table instead.

# t4_4_susan = create_table(4)
# Susan(t4_4_susan)

########################################################





##########
# Task 5 #
##########

# @brief Solver
# @param table
# @note - I figured that for each additional power of 2 starting from the base case of N = 4,
#         the flipping sequences table is modified according to the pattern:
#
#            table1 -> table1 | table1
#                     ----------------
#                      table1 | all 0s
#
#            For eg:
#                
#                1 1 1 1      1 1 1 1 | 1 1 1 1
#                1 0 1 0  ->  1 0 1 0 | 1 0 1 0
#                1 1 0 0      1 1 0 0 | 1 1 0 0
#                1 0 0 0      1 0 0 0 | 1 0 0 0
#                             -----------------
#                             1 1 1 1 | 0 0 0 0
#                             1 0 1 0 | 0 0 0 0
#                             1 1 0 0 | 0 0 0 0
#                             1 0 0 0 | 0 0 0 0
#
#       Hence, the solver generates this sequence using N=4 as the base case, then generates the sequence to apply
#       the flipping sequence using a Tower of Hanoi method.

def solve(table):
    """ Write your code here """
    n = get_table_size(table)

    if(n == 2):
        flip_coins(table, [1, 0])
        return
        
    # @brief Generates sequence using Tower of Hanoi concept
    # @param[in] number of coins
    # @retval sequence list
    def rot(n):
        if n == 0:
            return []
        a = rot(n-1) + [n-1]
        return a + rot(n-1)

    # @brief Generates individual flipping sequences (A, B, C, D etc)
    # @param[in] number of coins
    # @retval flipping sequence list
    def block(n):
        seqs = []
        a = [1, 1, 1, 1]
        b = [1, 0, 1, 0]
        c = [1, 1, 0, 0]
        d = [1, 0, 0, 0]
        prev_mat = [a, b, c, d]
        new_mat = []
        i = 4
        while i < n:
            new_mat = []
            for item in prev_mat:
                new_mat.append(item *2)
            for item in prev_mat:
                new_mat.append(item + [0 for k in range(len(item))])
            prev_mat = new_mat
            i *= 2
        return prev_mat[1:]
    
    seq = rot(n)
   
    block_seq = block(n)

    # Try flipping sequence 2^n-1 times.
    # If still not solved, return False
    for i in range(2**n - 1):
        if(check_solved(table)):
            return
        else:
            flip_coins(table, block_seq[seq[i]])

    return False
        

def block(n):
    seqs = []
    a = [1, 1, 1, 1]
    b = [1, 0, 1, 0]
    c = [1, 1, 0, 0]
    d = [1, 0, 0, 0]
    prev_mat = [a, b, c, d]
    new_mat = []
    i = 4
    while i < n:
        new_mat = []
        for item in prev_mat:
            new_mat.append(item *2)
        for item in prev_mat:
            new_mat.append(item + [0 for k in range(len(item))])
        prev_mat = new_mat
        i *= 2
    return new_mat[1:]

def rot(n):
    if n == 0:
        return []
    a = rot(n-1) + [n-1]
    return a + rot(n-1)

                    

# test:
t4_5 = create_table(4)
solve(t4_5)
print(check_solved(t4_5))

t8_5 = create_table(8)
solve(t8_5)
print(check_solved(t8_5))

t16_5 = create_table(16)
solve(t16_5)
print(check_solved(t16_5))

# Note: It is not advisable to execute run() if the table is large.
