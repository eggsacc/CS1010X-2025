#----------------
#    TOPIC 1
#----------------

# Question 1

count = 0
def record(f):
    def helper(*args):
        global count
        count += 1
        return f(*args)
    return helper

@record # include this line in your submission
def jump_locate(aList, begin, end, jump, num_to_find):
    if begin + jump > end:
        return 'Not Found'
    if aList[begin] == num_to_find:
        return begin
    if aList[begin + jump] == num_to_find:
        return begin + jump
    elif aList[begin + jump] < num_to_find:
        begin = begin + jump + 1
        if begin + jump * 2  <= end:
            return jump_locate(aList, begin, end, jump * 2, num_to_find)
        else:
            return jump_locate(aList, begin, end, 1, num_to_find)
    else:
        begin = begin + 1
        end = begin + jump - 1
        return jump_locate(aList, begin, end, 1, num_to_find)

# count = 0
# print(jump_locate(list(range(1, 10000, 2)), 0, 4999, 1, 1001))
# print(count)
# count = 0
# print(jump_locate(list(range(1, 10000, 2)), 0, 4999, 1, 1000))
# print(count)


#----------------
#    TOPIC 2
#----------------

def print_tree(tree):
    """Function to print a binary tree in friendly format. Do not modify."""
    def to_str(tree):
        if tree == ():
            return [], 0, 0
        if tree[1] == () and tree[2] == ():
            _lst = [f'({tree[0]:03d})']
            return _lst, 5, 2
        ltree, lwidth, lpos = to_str(tree[1])
        rtree, rwidth, rpos = to_str(tree[2])
        _lst = [' ' * lwidth + f'({tree[0]:03d})' + ' ' * rwidth]
        line = (' ' * lpos + '+' + '-' * (lwidth - lpos + 1) + '+' if lwidth else '  +') \
            + ('-' * (rpos + 2) + '+' + ' ' * (rwidth - rpos - 1) if rwidth else '  ')
        _lst.append(line)
        for i in range(max(len(ltree), len(rtree))):
            line = (ltree[i] if i < len(ltree) else ' ' * lwidth) + ' ' * 5 \
                + (rtree[i] if i < len(rtree) else ' ' * rwidth)
            _lst.append(line)
        return _lst, len(_lst[0]), lwidth + 2
    try:
        lst = to_str(tree)[0]
        for s in lst:
            print(s)
    except:
        print('Something went wrong. Your input might be invalid.')

TreeTuples = []
TreeTuples.append(((8, -1, 6), (7, 4, 9), (5, 1, 2), (1, 7, -1), (2, 3, 8), (3, -1, 0)))
TreeTuples.append(((0, 1, 2),))
TreeTuples.append(((0, 2, -1),(1, 0, -1)))
TreeTuples.append(((2, -1, 0),(0, -1, 1)))
TreeTuples.append(((0, 3, 2),(1, 4, 0)))

# Question 2

def find_root(iTuple):
    parent = set()
    children = set()
    for a, b, c in iTuple:
        parent.add(a)
        children.add(b)
        children.add(c)
    for x in parent:
        if x not in children:
            return x

# for iTuple in TreeTuples:
#     print(find_root(iTuple))

# Question 3

def binary_tree(iTuple):
    children = {}
    for a, b, c in iTuple:
        children[a] = (b, c)
    def helper(node):
        if children.get(node, (-1, -1)) == (-1, -1):
            return (node, (), ())
        else:
            left, right = (), ()
            if children[node][0] != -1:
                left = helper(children[node][0])
            if children[node][1] != -1:
                right = helper(children[node][1])
            return (node, left, right)
    root = find_root(iTuple)
    return helper(root)

# for iTuple in TreeTuples:
#     tree = binary_tree(iTuple) 
#     print(tree)
#     print_tree(tree)


#----------------
#    TOPIC 3
#----------------

# Question 4

class Tribes():
    def __init__(self, N):
        self.parent = {}
        for i in range(1, N+1):
            self.parent[i] = i

    def tribe_leader(self, A):
        if self.parent[A] == A:
            return A
        else:
            return self.tribe_leader(self.parent[A])

    def conquer(self, A, B):
        self.parent[B] = A 

    def is_same_tribe(self, A, B):
        return self.tribe_leader(A) == self.tribe_leader(B)

# def testTribes():
#     N = 100
#     T = Tribes(N)
#     T.conquer(10, 20)
#     print(T.tribe_leader(20))
#     print(T.is_same_tribe(20, 11))
#     T.conquer(5, 10)
#     T.conquer(10, 11)
#     print(T.is_same_tribe(20, 11))

# testTribes()


#----------------
#    TOPIC 4
#----------------

# Question 5

def subtree_distance(tree):
    n = len(tree)
    children = [[] for i in range(n)]
    res = [0] * n

    def helper(i):
        for child in children[i]:
            res[i] = max(res[i], 1 + helper(child))
        return res[i]

    for i in range(1, n):
        children[tree[i]].append(i)
    helper(0)
    return res

# print(subtree_distance([-1, 0, 0, 1, 2, 2, 5]))

# Question 6

def tree_distance(tree):
    n = len(tree)
    children = [[] for i in range(n)]
    subtree_distances = [[0, 0] for i in range(n)]
    outside_distances = [0] * n
    res = [0] * n

    def subtree(i):
        for j in range(len(children[i])):
            subtree_distances[i][j] = 1 + max(subtree(children[i][j]))
        return subtree_distances[i]

    def helper(i):
        res[i] = max(subtree_distances[i])
        if i != 0:
            parent = tree[i]
            outside_distances[i] = 1 + outside_distances[parent]
            res[i] = max(res[i], outside_distances[i])
            if i == children[parent][0]:
                res[i] = max(res[i], 1 + subtree_distances[parent][1])
                outside_distances[i] = max(outside_distances[i], 1 + subtree_distances[parent][1])
            else:
                res[i] = max(res[i], 1 + subtree_distances[parent][0])
                outside_distances[i] = max(outside_distances[i], 1 + subtree_distances[parent][0])
        for child in children[i]:
            helper(child)

    for i in range(1, n):
        children[tree[i]].append(i)
    subtree(0)
    helper(0)
    return res

# print(tree_distance([-1, 0, 0, 1, 2, 2, 5]))
# print(tree_distance([-1, 0, 0, 1, 2, 3, 4]))


#----------------
#    TOPIC 5
#----------------

# Question 7
def count_bugles(n, m):
    res = 0
    for i in range(n):
        for j in range(m):
            res += 4 * min(i, j) + 2 * min(i, j, m - j - 1) + 2 * min(j, i, n - i - 1)
    return res

# print(count_bugles(3, 3))
# print(count_bugles(4, 5))
