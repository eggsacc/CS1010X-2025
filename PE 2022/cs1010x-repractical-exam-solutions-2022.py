# Q1
def encrypt(message, plain, c1, c2): #'012345', 'ABCDEF'):
    result=""
    for m in message:
        if m==" ":
            result+=" "
        else:
            row=None
            column=None
            for i in range(len(plain)):
                for j in range(len(plain[0])):
                    if plain[i][j]==m:
                        row=i
                        column=j
            result+=(c1[row]+c2[column])
    return result

# Q2
def decrypt(secret, plain, c1, c2):
    current=0
    result=""
    while current<len(secret):
        if secret[current]==" ":
            result+=" "
            current+=1
        else:
            result+=plain[c1.index(secret[current])][c2.index(secret[current+1])]
            current+=2
    return result

# Q3
def index(lst, char):
    flag = False
    idx = []
    def helper(curlst):
        nonlocal flag
        if not isinstance(curlst, list):
            if curlst == char:
                flag = True
            return
        for i in range(len(curlst)):
            idx.append(i)
            helper(curlst[i])
            if flag:
                return
            idx.pop(-1)
    helper(lst)
    if not idx:
        return None
    result = ''
    for x in idx:
        result += str(x) + '-'
    return result[:-1]

# Q4
def make_rotation_matrix(m, n):
    result=[]
    first=[i for i in range(n)]
    for i in range(m):
        result.append(first)
        first=first[1:]+[first[0]]
    return result

# Q5
def make_symmetrical_matrix(n):
    result = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            result[i][j] = abs(i - j)
    return result

# Q6
def make_concentric_matrix(m,n):
    result = [[0]*n for i in range(m)]
    for i in range(m):
        for j in range(n):
            result[i][j] = min(min(i, m - i - 1), min(j, n - j - 1))
    return result

# Q7
def make_diamond_matrix(m,n):
    result = [[0]*n for i in range(m)]
    for i in range(m):
        for j in range(n):
            result[i][j] = min(i, m - i - 1) + min(j, n - j - 1)
    return result

# Q8
def all_keys(node):
    result = ''
    current = node
    while current != None:
        result += str(current.num) + '-'
        current = current.after
    return result[:-1]

# Q9
def search_layer(node, num):
    result = ''
    current = node
    while current != None:
        result += str(current.num) + '-'
        if current.num >= num:
            break
        current = current.after
    return result[:-1]

# Q10
def search(topMostLst, num):
    current = topMostLst
    result = ''
    while current != None:
        if current.num < num:
            if current.after != None:
                if current.after.num <= num:
                    result += str(current.num) + '-'
                    current = current.after
                else:
                    if current.bottom != None:
                        current = current.bottom
                    else:
                        result += str(current.num) + '-'
                        current = current.after
            else:
                if current.bottom == None: # this is the last layer
                    result += str(current.num) + '-'
                current = current.bottom
        else:
            result += str(current.num) + '-'
            break
    return result[:-1]
