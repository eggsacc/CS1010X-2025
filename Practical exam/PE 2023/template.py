#----------------
#    TOPIC 1
#----------------

# Question 1

def record(f):
    """Please do not paste the record function to Coursemology"""
    def helper(*args):
        global count
        count += 1
        return f(*args)
    return helper

def clamp(val, max):
    return max if val > max else val

@record # include this line in your submission
def jump_locate(aList, begin, end, jump, num_to_find):
    if(aList[begin] == num_to_find):
        return begin
    if(begin >= end):
        return "Not Found"
    nxt_idx = clamp(begin + jump, end)
    if(aList[nxt_idx] == num_to_find):
        return nxt_idx
    elif(aList[nxt_idx] < num_to_find):
        return jump_locate(aList, nxt_idx + 1, end, jump * 2, num_to_find)
    else:
        return jump_locate(aList, begin + 1, nxt_idx - 1, 1, num_to_find)

count = 0
print(jump_locate(list(range(1, 10000, 2)), 0, 4999, 1, 1001))
print(count)

count = 0
print(jump_locate(list(range(1, 10000, 2)), 0, 4999, 1, 1000))
print(count)


#----------------
#    TOPIC 2
#----------------

def print_tree(tree):
    """Function to print a binary tree in friendly format. Do not modify and do not submit to Coursemology."""
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

# iTupleList is just a list of public test cases for your convenience
iTupleList = []
iTupleList.append(((8, -1, 6), (7, 4, 9), (5, 1, 2), (1, 7, -1), (2, 3, 8), (3, -1, 0)))
iTupleList.append(((0, 1, 2),))
iTupleList.append(((0, 2, -1), (1, 0, -1)))
iTupleList.append(((2, -1, 0), (0, -1, 1)))
iTupleList.append(((0, 3, 2), (1, 4, 0)))

# Question 2

# Fuck this autistic iTuple name
def find_root(tup):
    seen = set()
    for item in tup:
        for num in item:
            if(num != -1 and num not in seen):
                seen.add(num)
    
    for item in tup:
        for num in item[1:]:
            if(num != -1 and num in seen):
                seen.remove(num)
    
    return seen.pop()

for iTuple in iTupleList:
    print(find_root(iTuple))

# Question 3

def binary_tree(tup):
    def helper(root):
        if(root == -1):
            return ()
        
        left = -1
        right = -1
        for branch in tup:
            if(branch[0] == root):
                left = branch[1]
                right = branch[2]
                break
        left_tup = () if left == -1 else (left,)
        right_tup = () if right == -1 else (right,)
        if(not left_tup and not right_tup):
            return (root, (), ())
        else:
            return (root, helper(left), helper(right))
    
    return helper(find_root(tup))
        
        


for iTuple in iTupleList:
    tree = binary_tree(iTuple) 
    print(tree)
    print_tree(tree)


#----------------
#    TOPIC 3
#----------------

# Question 4

class Tribes():
    def __init__(self, N):
        # Use a dictionary to capture the leader for each of the N tribes
        self.leader = {}
        for i in range(1, N+1):
            self.leader[i] = i
        self.owned = {}

    def tribe_leader(self, A):
        # Find the leader of tribe A, which is A if no one has conquered it before,
        # or ... (this is related to what you do for the next function, conquer)
        return self.leader[A]

    def conquer(self, A, B):
        # Purpose: Tribe A conquers tribe B
        if(A not in self.owned):
            self.owned[A] = [B]
        else:
            self.owned[A].append(B)
        if(B in self.owned):
            self.owned[A].extend(self.owned[B])
        for tribe in self.owned[A]:
            self.leader[tribe] = A


    def is_same_tribe(self, A, B):
        # Return True if tribe A and tribe B have the same leader,
        # otherwise return False
        return self.leader[A] == self.leader[B]

def testTribes():
    N = 100
    T = Tribes(N)
    T.conquer(10, 20)
    print(T.tribe_leader(20))
    print(T.is_same_tribe(20, 11))
    T.conquer(5, 10)
    T.conquer(10, 11)
    print(T.is_same_tribe(20, 11))

testTribes()


#----------------
#    TOPIC 4
#----------------

# Question 5

def subtree_distance(tree):
    def helper(node):
        max = -1
        for i in range(len(tree)):
            if(tree[i] == node):
                result = 1 + helper(i)
                if result > max:
                    max = result
        if(max != -1):
            return max
        else:
            return 0
        
    ret = []
    for i in range(len(tree)):
        ret.append(helper(i))
    return ret


print(subtree_distance([-1, 0, 0, 1, 2, 2, 5]))

# Question 6

def dfs(tree):
    ret = [-1] * len(tree)
    path_length = 0
    def helper(node):
        nonlocal path_length
        for i in range(len(tree)):
            if(tree[i] == node):
                path_length += 1
                helper(i)
                path_length -= 1
            else:
                continue
        ret[node] = path_length
    
    helper(0)
    return ret


def tree_distance(tree):
    root_depth = dfs(tree)
    max_subtree = subtree_distance(tree)
    print("root depth: ", root_depth)
    print("max_subtree: ", max_subtree)
    ret = []
    for i in range(len(tree)):
        if(i == 0):
            ret.append(max_subtree[0])
            continue

        dist_1 = 0
        dist_2 = 0
        # Case 1: max from node
        if(tree[i] != -1):
            dist_1 = max_subtree[i]
        
        # Case 2: traverse to root node then other side
        parent = tree[i]
        max_other_branch = 0


        if(parent == 0):
            if(i == 1):
                max_other_branch = max_subtree[2] + 1
            else:
                max_other_branch = max_subtree[1] + 1
        else:
            while(parent != 1 and parent != 2):
                parent = tree[parent]

            if(parent == 1):
                max_other_branch = max_subtree[2] + 1
            else:
                max_other_branch = max_subtree[1] + 1

        dist_2 = root_depth[i] + max_other_branch

        ret.append(max(dist_1, dist_2))
    
    return ret

         


print(tree_distance([-1, 0, 0, 1, 2, 2, 5]))
print(tree_distance([-1, 0, 0, 1, 2, 3, 4]))


#----------------
#    TOPIC 5
#----------------

# Question 7
def count_bugles(n, m):
    regular = 0
    size = 1
    while size < n and size < m:
        regular += (n - size) * (m - size) * 4
        size += 1

    extended = 0
    size = 2
    while size < n and size < m:
        extended += (n - size) * (m - size) * 4
        size += 2
    
    size = 2
    while size < n and size < m:
        extended += (n - size) * 2 + (m - size) * 2
        size += 2
    
    if(n >= 5):
        for i in range(5, n + 1, 2):
            extended += (m - i // 2) * 2
    if(m >= 5):
        for i in range(5, m + 1, 2):
            extended += (n - i // 2) * 2

    return regular + extended

    

print(count_bugles(3, 3))
print(count_bugles(4, 5))
