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

# Arguments are passed by object reference to functions in python.
# The "name" of any variable is just a name-tag attached to the object in memory.
# When we pass, say a list m into a function foo(lst), lst is created as a local variable that points to the
# same object in memory (the list) as m.
# When we index lst in the function and change the value, we are accessing the shared list in memory and directly
# modifying it.
# However, if we try to re-assign the list to another list in the function, the local variable
# "list" simply switches to referencing the other list object. The original "m" outside the function is unchanged.

def sumT(t, term, next):
    pass

def transpose(t):
    return sumT(t, lambda N: [map(lambda row: row[0], N)], 
                lambda N: map(lambda row: row[1:], N) if True else 0) 
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
    for item in m[2]:
        if(item[0] == x and item[1] == y):
            return item[3]

# Also need to add another extry if the requested index does not exist.
# And drop (remove) the entry if it's value is updated to 0.
def set(m, x, y, val):
    if(x >= rows(m) - 1 or y >= cols(m) - 1):
        return m

    for item in m[2]:
        if(item[0] == x and item[1] == y):
            if(val == 0):
                m[2].remove([x, y, item[3]])
            else:
                item[3] = val

    # Yet to implement: insert new entry if does not exist
     
def transpose(m):
    entries = m[2]

    # Don't forget to swap the sizes too!!!
    m[0], m[1] = m[1], m[0]

    for item in entries:
        item[0], item[1] = item[1], item[0]
    
    entries.sort()
    return m

def print_matrix(mat):
    rows, clmns, entries = mat
    idx = 0
    for row in range(rows):
        string = "["
        for clmn in range(clmns):
            if(entries[idx][0] == row and entries[idx][1] == clmn):
                string += str(entries[idx][2]) + ", "
                idx += 1
            else:
                string += "0, "

        print(string + "]")

# Alternative way:
# Create a return array of size n x m of all 0s, then for each entry in the sparse array, set the corresponding value.

another = [[1, 0, 3], [4, 0, 0], [7, 0, 0], [0, 0, 0], [0, 0, 15]]
test = make_matrix(another)
# print(test)
# print(transpose(test))
print_matrix(test)