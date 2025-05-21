################################################################
#                           TOPIC 1                            #
################################################################

## Question 1 ##
from string import ascii_uppercase

def encrypt(message, cipher):
		plain = list(ascii_uppercase)
		ret = ""
		for char in message:
			if(char == " "):
				ret += " "
				continue
			idx = 0
			while(plain[idx] != char):
				idx += 1
			ret += cipher[idx]
			plain.remove(char)
			plain.insert(0, char)
		return ret
		

print("*** Question 1 ***")
print(encrypt('HELLO', 'DEFGHIJKLMNOPQRSTUVWXYZABC') == 'KIODR', encrypt('HELLO', 'DEFGHIJKLMNOPQRSTUVWXYZABC'))
print(encrypt('I LOVE PYTHON', 'DQOLVJSGYCREUTBKXIWNHAMZPF') == 'Y EBAY XPABSW', encrypt('I LOVE PYTHON', 'DQOLVJSGYCREUTBKXIWNHAMZPF'))


## Question 2 ##

def decrypt(message, cipher):
	plain = list(ascii_uppercase)
	ret = ""
	for i in range(len(message)):
		if(message[i] == " "):
			ret += " "
		else:
			idx = 0
			while message[i] != cipher[idx]:
				idx += 1
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
	initial = pics[0]
	for i in range(1, len(pics)):
		initial = stack_frac(1-(1/(i+1)), initial, pics[i])
	return initial

print("\n*** Question 4 ***")
print(" --- need to visually check whether the rune is correct or not ---")
#show(stackn_list([circle_bb, circle_bb, circle_bb, circle_bb]))
#show(stackn_list([make_cross(nova_bb), make_cross(rcross_bb), circle_bb, heart_bb]))
#show(stackn_list([make_cross(rcross_bb), make_cross(nova_bb), pentagram_bb, make_cross(nova_bb), make_cross(rcross_bb)]))

## Question 5 ##

def mxn_matrix(pics, matrix):
        rows = []
        for item in matrix:
            row = []
            for obj  in item:
                row.append(quarter_turn_left(pics[obj]))
            rows.append(quarter_turn_right(stackn_list(row)))
        return stackn_list(rows[-1::-1])
    
# print("\n*** Question 5 ***")
# print(" --- need to visually check whether the rune is correct or not ---")
# show(mxn_matrix([make_cross(nova_bb), make_cross(rcross_bb), circle_bb, heart_bb],
                # [[0, 1, 2, 3], [1, 0, 1, 2], [2, 1, 0, 1], [3, 2, 1, 0]]))
# show(mxn_matrix([make_cross(rcross_bb), make_cross(nova_bb), pentagram_bb], [[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 1, 2, 2, 1, 0], [0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0]]))


################################################################
#                           TOPIC 3                            #
################################################################

## Question 6 ##

def get_shape(arr):
	if(type(arr) != list):
		return []
	else:
		return [len(arr)] + get_shape(arr[0])

print("\n*** Question 6 ***")
print(get_shape([1]) == [1], get_shape([1]))
print(get_shape([1, 2]) == [2], get_shape([1, 2]))
print(get_shape([[1, 2, 3], [4, 5, 6]]) == [2, 3], get_shape([[1, 2, 3], [4, 5, 6]]))
print(get_shape([[[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10], [11, 12]]]) == [2, 3, 2], get_shape([[[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10], [11, 12]]]))
print(get_shape([[[[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10], [11, 12]]]]) == [1, 2, 3, 2], get_shape([[[[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10], [11, 12]]]]))


## Question 7 ##

def get_value(arr, idx):
	if(len(idx) == 1):
		return arr[idx[0]]
	else:
		return get_value(arr[idx[0]], idx[1:])

print("\n*** Question 7 ***")
print(get_value([1], [0]) == 1, get_value([1], [0]))
print(get_value([1, 2], [1]) == 2, get_value([1, 2], [1]))
print(get_value([[1, 2, 3], [4, 5, 6]], [0, 2]) == 3, get_value([[1, 2, 3], [4, 5, 6]], [0, 2]))
print(get_value([[1, 2, 3], [4, 5, 6]], [1, 1]) == 5, get_value([[1, 2, 3], [4, 5, 6]], [1, 1]))
print(get_value([[[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10], [11, 12]]], [1, 0, 1]) == 8, get_value([[[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10], [11, 12]]], [1, 0, 1]))
print(get_value([[[[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10], [11, 12]]]], [0, 1, 0, 1]) == 8, get_value([[[[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10], [11, 12]]]], [0, 1, 0, 1]))


## Question 8 ##

def set_value(arr, idx, val):
	if(len(idx) == 1):
		arr[idx[0]] = val
		return
	else:
		return set_value(arr[idx[0]], idx[1:], val)

print("\n*** Question 8 ***")

arr1 = [1]
arr2 = [1, 2]
arr3 = [[1, 2, 3], [4, 5, 6]]

set_value(arr1, [0], 8)
print(arr1 == [8], arr1)

set_value(arr2, [1], 18)
print(arr2 == [1, 18], arr2)

set_value(arr3, [0, 2], 28)
print(arr3 == [[1, 2, 28], [4, 5, 6]], arr3)


## Question 9 ##

def create_arr(shape):
	if(len(shape) == 1):
		return [0] * shape[0]
	else:
		return [create_arr(shape[1:])] * shape[0]

print("\n*** Question 9 ***")
print(create_arr([2, 3]) == [[0, 0, 0], [0, 0, 0]], create_arr([2, 3]))
print(create_arr([2, 3, 2]) == [[[0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0]]], create_arr([2, 3, 2]))


## Question 10 ##

def next_idx(idx, shape):
	for i in range(len(idx)-1, -1, -1):
		if(idx[i] < shape[i] - 1):
			idx[i] += 1
			if(i !=len(shape) - 1):
				for j in range(i + 1, len(shape)):
					idx[j] = 0
			return idx
		
	return None
	

def listing_of_indices_given_a_shape(shape):
	idx = [0] * len(shape)
	print(idx)
	while idx != None:
		idx = next_idx(idx, shape) # you are to implement this function
		print(idx)

print("\n*** Question 10 ***")
listing_of_indices_given_a_shape([5])           # output should be: [0] [1] [2] [3] [4] None
listing_of_indices_given_a_shape([2, 3])        # [0, 0] [0, 1] [0, 2] [1, 0] [1, 1] [1, 2] None
listing_of_indices_given_a_shape([4, 2, 2])     # [0, 0, 0] [0, 0, 1] [0, 1, 0] [0, 1, 1]
#                                                 # [1, 0, 0] [1, 0, 1] [1, 1, 0] [1, 1, 1]
#                                                 # [2, 0, 0] [2, 0, 1] [2, 1, 0] [2, 1, 1]
#                                                 # [3, 0, 0] [3, 0, 1] [3, 1, 0] [3, 1, 1] None
# listing_of_indices_given_a_shape([1, 2, 3, 2])  # output is as shown in the question paper


## Question 11 ##

def sum_along(axis, arr):
	shape= get_shape(arr)

	if(not shape):
		return sum(arr)
	
	output_shape = shape.copy()
	output_shape.pop(axis)
	output = create_arr(output_shape)
	idx = [0 for i in range(len(shape))]
	while idx != None:
		val = get_value(arr, idx)
		temp = idx.copy()
		temp.pop(axis)
		i = temp[-1]
		if(len(temp) <= 1):
			cur = output
		else:
			cur = get_value(output, temp[:-1])
		cur[i] += val
		idx = next_idx(idx, shape)
	return output


print("\n*** Question 11 ***")
print(sum_along(0, [1, 2]) == 3, sum_along(0, [1, 2]))
print(sum_along(0, [[1, 2, 3], [4, 5, 6]]) == [5, 7, 9], sum_along(0, [[1, 2, 3], [4, 5, 6]]))
print(sum_along(1, [[1, 2, 3], [4, 5, 6]]) == [6, 15], sum_along(1, [[1, 2, 3], [4, 5, 6]]))
print(sum_along(0, [[[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10], [11, 12]]]) == [[8, 10], [12, 14], [16, 18]], sum_along(0, [[[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10], [11, 12]]]))
print(sum_along(2, [[[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10], [11, 12]]]) == [[3, 7, 11], [15, 19, 23]], sum_along(2, [[[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10], [11, 12]]]))
print(sum_along(3, [[[[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10], [11, 12]]]]) == [[[3, 7, 11], [15, 19, 23]]], sum_along(3, [[[[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10], [11, 12]]]]))


################################################################
#                           TOPIC 4                            #
################################################################

## Question 12 ##

class Matrix(object):
    ## Task A ###
	def __init__(self, nrows, ncols):
		# write your code here
		self.rows = nrows
		self.clmns = ncols
		self.mat = {}

	def get(self, idx):
		# write your code here
		if(idx in self.mat):
			return self.mat[idx]
		else:
			return 0
		
	def insert(self, idx, val):
    	# write your code here
		self.mat[idx] = val
        
	def delete(self, idx):
    	# write your code here
		if(idx in self.mat):
			self.mat.pop(idx)

        
	def dict2list(self):
    	# write your code 
		mat = [[0] * self.clmns for _ in range(self.rows)]
		for key, value in self.mat.items():
			mat[key[0]][key[1]] = value
		return mat
    
    ## Task B ###
	def transpose(self):
    	# write your code here
		new = {}
		print(self.mat)
		ret = Matrix(self.clmns, self.rows)
		for key, value in self.mat.items():
			new[(key[1], key[0])] = value
		print(new)
		ret.mat = new
		return ret
    
    ## Task C ###
	def multiply(self, m2):
    	# write your code here
		ret = Matrix(self.rows, m2.clmns)
		translated = m2.transpose()
		m1_lst = self.dict2list()
		m2_lst = m2.transpose().dict2list()
		out_mat = [[0] * m2.clmns for _ in range(self.rows)]
		for i in range(len(m1_lst)):
			for j in range(len(m2_lst)):
				sum = 0
				for item in range(len(m2_lst[j])):
					sum += m1_lst[i][item] * m2_lst[j][item]
				out_mat[i][j] = sum
		dic = {}
		for i in range(len(out_mat)):
			for j in range(len(out_mat[0])):
				if(out_mat[i][j] != 0):
					dic[(i, j)] = out_mat[i][j]
		ret.mat = dic
		return ret
				


print("\n*** Question 12 ***")

print("\n** Task A **")
print("* Public Test 1 *")
m1 = Matrix(1, 3)
m1.insert((0,0), 1)
m1.insert((0,1), 2)
m1.insert((0,2), 3)
print(m1.dict2list() == [[1, 2, 3]], m1.dict2list())

print("* Public Test 2 *")
m1.delete((0,1))
print(m1.dict2list() == [[1, 0, 3]], m1.dict2list())

print("* Public Test 3 *")
print([m1.get((0,1)), m1.get((0,2)), m1.get((0,0))] == [0, 3, 1], [m1.get((0,1)), m1.get((0,2)), m1.get((0,0))])

print("\n** Task B **")
print("* Public Test 4 *")
m2 = m1.transpose()
print(m2.dict2list() == [[1], [0], [3]], m2.dict2list())

print("\n** Task C **")
print("* Public Test 5 *")
m3 = Matrix(1, 4)
m3.insert((0,0), 3)
m3.insert((0,1), 4)
m3.insert((0,3), 5)
m4 = m2.multiply(m3)
print(m4.dict2list() == [[3, 4, 0, 5], [0, 0, 0, 0], [9, 12, 0, 15]], m4.dict2list())

