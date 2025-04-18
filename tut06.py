# 1a) not correct, he is modifying the list while iterating, which causes unexpected behaviour

#1b) Do not modify the list when iterating by index

# 1c)
def at_least_n(lst, n):
    items = lst.copy()
    for item in items:
        if(item < n):
            lst.remove(item)
    return lst

# 1d)
def at_least_n_2(lst, n):
    new = []
    for item in lst:
        if(item >= n):
            new.append(item)
    
    return new

# 2a)
def col_sum(mat):
    rows = len(mat)
    clmns = len(mat[0])
    sums = []
    for clmn in range(clmns):
        sum = 0
        for row in range(rows):
            sum += mat[row][clmn]
        sums.append(sum)
    
    return sums

# 2b)
def row_sum(mat):
    rows = len(mat)
    clmns = len(mat[0])
    sums = []
    for row in range(rows):
        sum = 0
        for clmn in range(clmns):
            sum += mat[row][clmn]
        sums.append(sum)
    
    return sums

# 2c)
def transpose(matrix):
    rows = len(matrix)
    clmns = len(matrix[0])
    
    for i in range(clmns):
        buffer = []
        for j in range(rows):
            buffer += [matrix[j][i]]
        matrix.append(buffer)

    for i in range(rows):
        matrix.pop(0)
        
    return matrix

m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(col_sum(m))
print(row_sum(m))
print(transpose(m))

# 3a) Insertion sort: go index by index, swap item if smaller than previous until at correct pos
# 3b) Iterate through and find the largest/smallest item each time, and swap with head or tail
# 3c) Start at idx 0 every pass, and swap if item larger than next. Track stop idx
# 3d) Split list into half each time, processing the LHS first, recombine in sorted order

# 4a)
def mode_score(students):
    dicc = {}
    out = []
    for student in students:
        if(student[2] not in dicc):
            dicc[student[2]] = 1
        else:
            dicc[student[2]] += 1
    max_freq = 0
    for val in dicc.values():
        if val > max_freq:
            max_freq = val
    for key, value in dicc.items():
        if(value == max_freq):
            out.append(key)
    return out

# 4b)
def sort_name(students):
    for i in range(len(students)):
        min_idx = i  # Start with current index as minimum
        for j in range(i+1, len(students)):
            if students[j][0] < students[min_idx][0]:  # Compare full names
                min_idx = j
        students[i], students[min_idx] = students[min_idx], students[i]  # Swap
    return students

def sort_grade(students):
    for i in range(len(students)):
        max_idx = i  
        for j in range(i+1, len(students)):
            if students[j][2] > students[max_idx][2]: 
                max_idx = j
        students[i], students[max_idx] = students[max_idx], students[i]  # Swap
    return students

def top_k(students, k):
    sorted_st = sort_grade(sort_name(students))
    last_score = sorted_st[k-1][2]
    while(sorted_st[k][2] == last_score):
        k += 1
    return sorted_st[:k]

def top_k_2(students, k):
    students.sort(key=lambda x: x[0])
    students.sort(key=lambda x: x[2], reverse=True)
    print(students)
    last_score = students[k-1][2]
    while(students[k][2] == last_score):
        k += 1
    return students[:k]

students = [
 ('tiffany', 'A', 15),
 ('jane', 'B', 10),
 ('ben', 'C', 8),
 ('simon', 'A', 21),
 ('eugene', 'A', 21),
 ('john', 'A', 15),
 ('jimmy', 'F', 1),
 ('charles', 'C', 9),
 ('freddy', 'D', 4),
 ('dave', 'B', 12)]

print(top_k_2(students, 5))