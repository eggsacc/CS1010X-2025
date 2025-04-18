# 1a)
def make_matrix(seq):
    return seq

def make_matrix_2(seq):
    mat = []
    for row in seq:
        mat.append(list(row))
    return mat

m = [[ 1, 2, 3], [4, 5, 6], [7, 8, 9]]


# Yes, the sequence is already a matrix representation. The other version 
# also handles cases where the sequence is not a list by converting
# each row to a list.

# 1b)
def rows(m):
    return len(m)

def cols(m):
    return len(m[0])

def get(m, i, j):
    return m[i][j]

def set(m, i, j, val):
    m[i][j] = val
    return m

def transpose(m):
    rows = len(m)
    clmns = len(m[0])
    
    new_mat = [[0 for i in range(rows)] for j in range(clmns)]
    
    for i in range(rows):
        for j in range(clmns):
            new_mat[j][i] = m[i][j]
    return new_mat

def print_matrix(mat):
    for row in mat:
        print(row)

# 2a)
def make_matrix(seq):
    data = []
    for i in range(len(seq)):
        for j in range(len(seq[0])):
            if seq[i][j] != 0:
                data.append([i,j,seq[i][j]])
    return [len(seq),len(seq[0]),data]

def rows(m):
    return m[0]

def cols(m):
    return m[1]

def get(m, x, y):
    return m[2][x*rows(m) + y][2]

def set(mat, x, y, val):
    mat[2][x*rows(mat) + y] = [x, y, val]
    return mat

def transpose(m):
    pass

test = make_matrix(m)
print(test)
print(get(test, 1, 2))
print(set(test, 1, 2, 7))
