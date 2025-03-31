def sort_by_gender_then_age(lst):
    # Fill in your code here
    def gender_sort(lst):
        male = []
        female = []
        for item in lst:
            if(item[0] == 'M'):
                male.append(item)
            else:
                female.append(item)
        return male + female

    def age_sort(lst):
        n = len(lst)

        for i in range(n):
            largest = i
            for j in range(i+1, n):
                if(lst[j][1] > lst[largest][1]):
                    largest = j
            lst[i], lst[largest] = lst[largest], lst[i]
        return lst
    
    return gender_sort(age_sort(lst))
    

def merge_lists(list1, list2):
    # Fill in your code here
    merged_list = []
    while(list1 != [] or list2 != []):
        
        if(list1 == []):
            for item in list2:
                merged_list.append(item)
            list2 = []
        elif(list2 == []):
            for item in list1:
                merged_list.append(item)
            list1 = []
        elif(list1[0] > list2[0]):
            merged_list.append(list1[0])
            list1.pop(0)
        else:
            merged_list.append(list2[0])
            list2.pop(0)
            
    return merged_list


def top_k(lst, k):
    # Fill in your code here
    n = len(lst)
    for i in range(n-1):
        max_idx = -1
        for j in range(i, n):
            if(lst[j] > lst[max_idx]):
                max_idx = j
        lst[i], lst[max_idx] = lst[max_idx], lst[i]
    return lst[:k]

def f(n):
    # Your code here
    if(n < 3):
        return n
    
    f0, f1, f2 = 0, 1, 2
    
    for i in range(3, n+1):
        fn = f2 + 2 * f1 + 3 * f0
        f0, f1, f2 = f1, f2, fn
        
    return fn

def is_fib(n):
    # Your code here
    # Apparently all fibonacci numbers follow the rule:
    # 5N^2 + 4 or 5N^2 - 4 are perfect squres
    def is_perfsq(x):
        sqrt = int(x**0.5)
        return (sqrt * sqrt == x)
    
    return (is_perfsq(5*n*n + 4) or is_perfsq(5*n*n - 4))

def calc_integral(f, a, b, n):
    # Put your code here #
    h = (b - a) / n
    sum = f(a)
    pdt = 1
    
    for i in range(1, n):
        if(pdt):
            sum += 4 * f(a + i*h)
        else:
            sum += 2 * f(a + i*h)
        pdt ^= 1
    
    return h / 3 * (sum + f(a + n * h))

def fold(op, f, n):
    if n == 0:
        return f(0)
    return op(f(n), fold(op, f, n-1))

def g(k):
    return  fold(lambda x, y: x * y, lambda x: x-(x+1)**2, k)

def accumulate(combiner, base, term, a, next, b):
    if(a > b):
        return base
    else:
        return combiner(term(a), accumulate(combiner, base, next(a), next, b))

def accumulate_iter(combiner, null_value, term, a, next, b):
    
    stack = []
    
    while(a <= b):
        val = term(a)
        stack.append(val)
        a = next(a)
    
    result = null_value
    print(stack)
    
    for i in range(len(stack)):
        last = stack.pop()
        print(last)
        result = combiner(last, result)
    
    return result

def make_segment(p1, p2):
    #Your code here
    def foo(x):
        if x == 0:
            return p1(0)
        elif x == 1:
            return p1(1)
        elif x == 2:
            return p2(0)
        else:
            return p2(1)
            
    return foo

def make_point(x, y):
    #Your code here
    return lambda w: y if w else x

def x_point(p):
    #Your code here
    return p(0)
    
def y_point(p):
    #Your code here
    return p(1)

def start_segment(s):
    #Your code here
    return lambda x: s(1) if x else s(0)

def end_segment(s):
    #Your code here
    return lambda x: s(3) if x else s(2)

def midpoint_segment(segment):
    #Your code here
    mid_x = (x_point(start_segment(segment)) + x_point(end_segment(segment))) / 2
    mid_y = (y_point(start_segment(segment)) + y_point(end_segment(segment))) / 2
    return make_point(mid_x, mid_y)


def odd_even_sums(val):
    #Write your code here
    flag = 1
    even_sum = 0
    odd_sum = 0
    
    for item in val:
        if(flag):
            odd_sum += item
        else:
            even_sum += item
        flag ^= 1
        
    return (odd_sum, even_sum)  

def hanoi(n, src, dsc, aux):
    #Write your code here
    ans = []
    def helper(n, src, dsc, aux, tup):
        if n == 0:
            tup.append((src, dsc),)
            return
        else:
            print(tup)
            helper(n-1, src, aux, dsc, tup)
            tup.append((src, dsc),)
            helper(n-1, aux, dsc, src, tup)
    helper(n, src, dsc, aux, ans)    
    return ans

def make_stack(seq):
    return [x for x in seq]

def make_empty_stack():
    return make_stack([])

def is_empty_stack(stack):
    return (stack == [])

def push_stack(stack, item):
    # pushes an item onto the stack, returns the stack
    stack.append(item)
    return stack

def pop_stack(stack):
    # removes the top item of the stack, returns that item. If the stack is empty, it should return None.
    if(stack == []):
        return None
    stack.pop()
    return stack

def calculate(inputs):
    # you may assume that the input is always valid, i.e. you do not need to
    # check that the stack has at least 2 elements if you encounter an operator
    stack = []
    ops = ['+', '-', '*', '/']
    for item in inputs:
        if(item not in ops):
            stack.append(int(item))
        else:
            a = stack.pop()
            b = stack.pop()
            
            if(item == '+'):
                stack.append(a + b)
            elif(item == '-'):
                stack.append(b - a)
            elif(item == '*'):
                stack.append(a * b)
            elif(item == '/'):
                stack.append(b / a)
    return stack[0]

def col_sum(matrix):
    rows = len(matrix)
    clmns = len(matrix[0])
    lst = [0] * clmns
    
    for i in range(rows):
        for j in range(clmns):
            lst[j] += matrix[i][j]
    return lst

def transpose(matrix):

    def cpy(lst):
        return [cpy(item) if isinstance(item, list) else item for item in lst]

    rows = len(matrix)
    clmns = len(matrix[0])
    diff = rows - clmns
    mat_cpy = cpy(matrix)
    print(mat_cpy)
    # Diff positive: more rows than columns
    if(diff > 0):
        for row in matrix:
            # Increase number of columns in each row
            row.append([0 for j in range(diff)])
        # Decrease number of rows
        for i in range(diff):
            matrix.pop()
    # Diff negative: more columns than rows
    elif(diff < 0):
        for row in matrix:
            # Decrease num of columns in each row
            for i in range(-diff):
                row.pop()
        # Increase number of rows
        for i in range(-diff):
            matrix.append([0 for j in range(rows)])
            
    # Else: Square matrix, nothing required to be done
    new_r = len(matrix)
    new_c = len(matrix[0])
    new_rc = len(mat_cpy)
    new_cc = len(mat_cpy[0])
    print(f"{new_r}, {new_c}")
    print(f"{new_rc}, {new_cc}")
    print(mat_cpy)
    for i in range(rows):
        for j in range(clmns):
            print(f"{i}, {j}")
            matrix[j][i] = mat_cpy[i][j]
    return matrix

def transpose_new(matrix):
    def cpy(lst):
        return [cpy(item) if isinstance(item, list) else item for item in lst]

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

def mode_score(students):
    dicc = {}
    out = []
    for student in students:
        if(student[2] not in dicc):
            dicc[student[2]] = 1
        else:
            dicc[student[2]] += 1
    print(dicc)
    max_freq = 0
    for val in dicc.values():
        if val > max_freq:
            max_freq = val
    print(max_freq)
    for key, value in dicc.items():
        if(value == max_freq):
            out.append(key)
    return out

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
