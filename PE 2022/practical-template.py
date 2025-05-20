################################################################
#                           TOPIC 1                            #
################################################################

## Question 1 ##
from string import ascii_uppercase

def encrypt(message, cipher):
        plain = list(ascii_uppercase)
        pass

# print("*** Question 1 ***")
# print(encrypt('HELLO', 'DEFGHIJKLMNOPQRSTUVWXYZABC') == 'KIODR', encrypt('HELLO', 'DEFGHIJKLMNOPQRSTUVWXYZABC'))
# print(encrypt('I LOVE PYTHON', 'DQOLVJSGYCREUTBKXIWNHAMZPF') == 'Y EBAY XPABSW', encrypt('I LOVE PYTHON', 'DQOLVJSGYCREUTBKXIWNHAMZPF'))


## Question 2 ##

def decrypt(message, cipher):
	pass

# print("\n*** Question 2 ***")
# print(decrypt('KIODR', 'DEFGHIJKLMNOPQRSTUVWXYZABC') == 'HELLO', decrypt('KIODR', 'DEFGHIJKLMNOPQRSTUVWXYZABC'))
# print(decrypt('Y EBAY XPABSW', 'DQOLVJSGYCREUTBKXIWNHAMZPF') == 'I LOVE PYTHON', decrypt('Y EBAY XPABSW', 'DQOLVJSGYCREUTBKXIWNHAMZPF'))


## Question 3 ##

def decrypt_wbw(message, cipher):
	pass

# print("\n*** Question 3 ***")
# print(decrypt_wbw('KHOOR QHOGU PQKLIHW', 'DEFGHIJKLMNOPQRSTUVWXYZABC') == 'HELLO MAJOR GILBERT', decrypt_wbw('KHOOR QHOGU PQKLIHW', 'DEFGHIJKLMNOPQRSTUVWXYZABC'))
# print(decrypt_wbw('Y EBAJ XPHEOK', 'DQOLVJSGYCREUTBKXIWNHAMZPF') == 'I LOVE PYTHON', decrypt_wbw('Y EBAJ XPHEOK', 'DQOLVJSGYCREUTBKXIWNHAMZPF'))


################################################################
#                           TOPIC 2                            #
################################################################

from runes import *

## Question 4 ##

def stackn_list(pics):
	pass

# print("\n*** Question 4 ***")
# print(" --- need to visually check whether the rune is correct or not ---")
# show(stackn_list([make_cross(nova_bb), make_cross(rcross_bb), circle_bb, heart_bb]))
# show(stackn_list([make_cross(rcross_bb), make_cross(nova_bb), pentagram_bb, make_cross(nova_bb), make_cross(rcross_bb)]))


## Question 5 ##

def mxn_matrix(pics, matrix):
	pass

# print("\n*** Question 5 ***")
# print(" --- need to visually check whether the rune is correct or not ---")
# show(mxn_matrix([make_cross(nova_bb), make_cross(rcross_bb), circle_bb, heart_bb], [[0, 1, 2, 3], [1, 0, 1, 2], [2, 1, 0, 1], [3, 2, 1, 0]]))
# show(mxn_matrix([make_cross(rcross_bb), make_cross(nova_bb), pentagram_bb], [[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 1, 2, 2, 1, 0], [0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0]]))


################################################################
#                           TOPIC 3                            #
################################################################

## Question 6 ##

def get_shape(arr):
	pass

# print("\n*** Question 6 ***")
# print(get_shape([1]) == [1], get_shape([1]))
# print(get_shape([1, 2]) == [2], get_shape([1, 2]))
# print(get_shape([[1, 2, 3], [4, 5, 6]]) == [2, 3], get_shape([[1, 2, 3], [4, 5, 6]]))
# print(get_shape([[[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10], [11, 12]]]) == [2, 3, 2], get_shape([[[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10], [11, 12]]]))
# print(get_shape([[[[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10], [11, 12]]]]) == [1, 2, 3, 2], get_shape([[[[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10], [11, 12]]]]))


## Question 7 ##

def get_value(arr, idx):
	pass

# print("\n*** Question 7 ***")
# print(get_value([1], [0]) == 1, get_value([1], [0]))
# print(get_value([1, 2], [1]) == 2, get_value([1, 2], [1]))
# print(get_value([[1, 2, 3], [4, 5, 6]], [0, 2]) == 3, get_value([[1, 2, 3], [4, 5, 6]], [0, 2]))
# print(get_value([[1, 2, 3], [4, 5, 6]], [1, 1]) == 5, get_value([[1, 2, 3], [4, 5, 6]], [1, 1]))
# print(get_value([[[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10], [11, 12]]], [1, 0, 1]) == 8, get_value([[[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10], [11, 12]]], [1, 0, 1]))
# print(get_value([[[[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10], [11, 12]]]], [0, 1, 0, 1]) == 8, get_value([[[[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10], [11, 12]]]], [0, 1, 0, 1]))


## Question 8 ##

def set_value(arr, idx, val):
	pass

# print("\n*** Question 8 ***")

# arr1 = [1]
# arr2 = [1, 2]
# arr3 = [[1, 2, 3], [4, 5, 6]]

# set_value(arr1, [0], 8)
# print(arr1 == [8], arr1)

# set_value(arr2, [1], 18)
# print(arr2 == [1, 18], arr2)

# set_value(arr3, [0, 2], 28)
# print(arr3 == [[1, 2, 28], [4, 5, 6]], arr3)


## Question 9 ##

def create_arr(shape):
	pass

# print("\n*** Question 9 ***")
# print(create_arr([2, 3]) == [[0, 0, 0], [0, 0, 0]], create_arr([2, 3]))
# print(create_arr([2, 3, 2]) == [[[0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0]]], create_arr([2, 3, 2]))


## Question 10 ##

def next_idx(idx, shape):
	pass

def listing_of_indices_given_a_shape(shape):
	idx = [0] * len(shape)
	print(idx)
	while idx != None:
		idx = next_idx(idx, shape) # you are to implement this function
		print(idx)

# print("\n*** Question 10 ***")
# listing_of_indices_given_a_shape([5])           # output should be: [0] [1] [2] [3] [4] None
# listing_of_indices_given_a_shape([2, 3])        # [0, 0] [0, 1] [0, 2] [1, 0] [1, 1] [1, 2] None
# listing_of_indices_given_a_shape([4, 2, 2])     # [0, 0, 0] [0, 0, 1] [0, 1, 0] [0, 1, 1]
#                                                 # [1, 0, 0] [1, 0, 1] [1, 1, 0] [1, 1, 1]
#                                                 # [2, 0, 0] [2, 0, 1] [2, 1, 0] [2, 1, 1]
#                                                 # [3, 0, 0] [3, 0, 1] [3, 1, 0] [3, 1, 1] None
# listing_of_indices_given_a_shape([1, 2, 3, 2])  # output is as shown in the question paper


## Question 11 ##

def sum_along(axis, arr):
	pass

# print("\n*** Question 11 ***")
# print(sum_along(0, [1, 2]) == 3, sum_along(0, [1, 2]))
# print(sum_along(0, [[1, 2, 3], [4, 5, 6]]) == [5, 7, 9], sum_along(0, [[1, 2, 3], [4, 5, 6]]))
# print(sum_along(1, [[1, 2, 3], [4, 5, 6]]) == [6, 15], sum_along(1, [[1, 2, 3], [4, 5, 6]]))
# print(sum_along(0, [[[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10], [11, 12]]]) == [[8, 10], [12, 14], [16, 18]], sum_along(0, [[[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10], [11, 12]]]))
# print(sum_along(2, [[[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10], [11, 12]]]) == [[3, 7, 11], [15, 19, 23]], sum_along(2, [[[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10], [11, 12]]]))
# print(sum_along(3, [[[[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10], [11, 12]]]]) == [[[3, 7, 11], [15, 19, 23]]], sum_along(3, [[[[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10], [11, 12]]]]))


################################################################
#                           TOPIC 4                            #
################################################################

## Question 12 ##

class Matrix(object):
    ## Task A ###
    def __init__(self, nrows, ncols):
    	# write your code here
    	pass

    def get(self, idx):
    	# write your code here
    	pass

    def insert(self, idx, val):
    	# write your code here
    	pass
        
    def delete(self, idx):
    	# write your code here
    	pass
        
    def dict2list(self):
    	# write your code here
    	pass
    
    ## Task B ###
    def transpose(self):
    	# write your code here
    	pass
    
    ## Task C ###
    def multiply(self, m2):
    	# write your code here
    	pass

# print("\n*** Question 12 ***")

# print("\n** Task A **")
# print("* Public Test 1 *")
# m1 = Matrix(1, 3)
# m1.insert((0,0), 1)
# m1.insert((0,1), 2)
# m1.insert((0,2), 3)
# print(m1.dict2list() == [[1, 2, 3]], m1.dict2list())

# print("* Public Test 2 *")
# m1.delete((0,1))
# print(m1.dict2list() == [[1, 0, 3]], m1.dict2list())

# print("* Public Test 3 *")
# print([m1.get((0,1)), m1.get((0,2)), m1.get((0,0))] == [0, 3, 1], [m1.get((0,1)), m1.get((0,2)), m1.get((0,0))])

# print("\n** Task B **")
# print("* Public Test 4 *")
# m2 = m1.transpose()
# print(m2.dict2list() == [[1], [0], [3]], m2.dict2list())

# print("\n** Task C **")
# print("* Public Test 5 *")
# m3 = Matrix(1, 4)
# m3.insert((0,0), 3)
# m3.insert((0,1), 4)
# m3.insert((0,3), 5)
# m4 = m2.multiply(m3)
# print(m4.dict2list() == [[3, 4, 0, 5], [0, 0, 0, 0], [9, 12, 0, 15]], m4.dict2list())

