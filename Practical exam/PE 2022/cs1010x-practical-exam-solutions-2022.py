# Solutions from JAVIER LIM JUN YI

# Q1
def encrypt(message, cipher):
	plain = list(ascii_uppercase)
	res = ''
	for char in message:
		if char == ' ':
			res += ' '
			continue
		i = plain.index(char)
		encrypted = cipher[i]
		popped = plain.pop(i)
		plain.insert(0, popped)
		res += encrypted
	return res

# Q2
def decrypt(message, cipher):
	plain = list(ascii_uppercase)
	res = ''
	for char in message:
		if char == ' ':
			res += ' '
			continue
		i = cipher.index(char)
		el = plain.pop(i)
		res += el
		plain.insert(0, el)
	return res

# Q3
def decrypt_wbw(message, cipher):
	msg_list = message.split()
	res = ''
	plain = list(ascii_uppercase)
	for word in msg_list:
		char_list = []
		for char in word:
			i = cipher.index(char)
			el = plain[i]
			res += el
			char_list.append(el)
		char_list = sorted(list(set(char_list)))
		for char in char_list[::-1]:
			j = plain.index(char)
			el = plain.pop(j)
			plain.insert(0, el)
		res += ' '
	return res.rstrip(' ')

# Q4
def stackn_list(pics):
	n = len(pics)
	if n == 1:
		return pics[0]
	else:
		return stack_frac(1/n, pics[0], stackn_list(pics[1:]))

# Q5
def mxn_matrix(pics, matrix):
	assigned_mat = [[pics[i] for i in row] for row in matrix]
	accumulated = []
	for row in assigned_mat:
		row = [quarter_turn_right(pic) for pic in row]
		merged = stackn_list(row)
		accumulated.append(quarter_turn_left(merged))
	return stackn_list(accumulated)

# Q6
def get_shape(arr):
	cur = arr
	res = []
	while type(cur) == type([]):
		res.append(len(cur))
		cur = cur[0]
	return res

# Q7
def get_value(arr, idx):
	cur = arr
	for i in idx:
		cur = cur[i]
	return cur

# Q8
def set_value(arr, idx, val):
	cur = arr
	while len(idx) != 1:
		cur = cur[idx[0]]
		idx.pop(0)
	cur[idx[0]] = val

# Q9
def create_arr(shape):
	i = shape.pop()
	base = [0 for j in range(i)]
	arr = base
	while shape:
		i = shape.pop()
		arr = [arr.copy() for j in range(i)]
	return arr

# Q10
def next_idx(idx, shape):
	idx[-1] += 1
	while True:
		valid = True
		if idx[0] == shape[0]:
			return 
		for i in range(len(idx) - 1, 0, -1):
			if idx[i] >= shape[i]:
				idx[i] = 0
				idx[i-1] += 1
				valid = False
				break
		if valid:
			return idx

# Q11
def sum_along(axis, arr):
	shape = get_shape(arr)
	if len(shape) == 1:
		return sum(arr)
	idx = [0 for i in range(len(shape))]
	res_shape = shape.copy()
	res_shape.pop(axis)
	res = create_arr(res_shape)
	while idx != None:
		val = get_value(arr, idx)
		_ = idx.copy()
		_.pop(axis)
		i = _[-1]
		if len(_) <= 1:
			cur = res
		else:
			cur = get_value(res, _[:-1])
		cur[i] += val
		idx = next_idx(idx, shape)
	return res

# Q12
class Matrix(object):
    ## Task A ###
	def __init__(self, nrows, ncols):
		# write your code here
		self.rows = nrows
		self.cols = ncols
		self.matrix = {}
		
	def get(self, idx):
		# write your code here
		if idx in self.matrix:
			return self.matrix[idx]
		else:
			return 0
	def insert(self, idx, val):
		self.matrix[idx] = val
		
	def delete(self, idx):
		self.matrix[idx] = 0
		
	def dict2list(self):
		res = [[0 for i in range(self.cols)] for j in range(self.rows)]
		for row, col in self.matrix:
			res[row][col] = self.get((row, col))
		return res
	## Task B ###
	def transpose(self):
		# write your code here
		transposed = Matrix(self.cols, self.rows)
		for row, col in self.matrix:
			transposed.insert((col, row), self.get((row,col)))
		return transposed
	## Task C ###
	def multiply(self, m2):
		# write your code here
		res = Matrix(self.rows, m2.cols)
		for i in range(self.rows):
			for j in range(m2.cols):
				for k in range(self.cols):
					res.insert((i,j), res.get((i,j)) + self.get((i, k)) * m2.get((k, j)))
		return res

