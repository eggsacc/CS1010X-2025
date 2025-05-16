# A stack class which you can use when you implement your functions.
# If you use this class in your solutions, please copy and paste the code to Coursemology as well.
class stack(object):
    def __init__(self):
        self.lst = []
    def push(self, x): # push an element to the stack
        self.lst.append(x)
    def pop(self): # pop the top element in the stack
        return self.lst.pop(-1)
    def top(self): # get the top element in the stack
        return self.lst[-1]
    def size(self): # get the size of the stack
        return len(self.lst)
    def empty(self): # return True if the stack is empty, otherwise False
        return self.size() == 0


# Q1
def generate_key(s):
    dic = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0,
           'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0,
           'w':0, 'x':0, 'y':0, 'z':0,}
    lst = []
    for i in range(len(s)):
        if(s[i] != " "):
            if(dic[s[i]] == 0):
                lst.append(s[i])
            dic[s[i]] += 1
    
    for key, value in dic.items():
        if(value == 0):
            lst.append(key)
    lst.sort()
    lst.sort(key=lambda x: dic[x], reverse=True)
    ret = ""
    for char in lst:
        ret += char
    return ret
        
    


print('=' * 9, 'Question 1', '=' * 9)
print(generate_key("the lazy fox jumps over a brown dog"))


# Q2
def encrypt(msg, s):
    encryption_key = generate_key(s)
    ret = ""
    for char in msg:
        if(ord(char) < 97 or ord(char) > 122):
            ret += char
        else:
            idx = ord(char) - 97
            ret += encryption_key[idx]
    return ret


print('=' * 9, 'Question 2', '=' * 9)
print(encrypt("##Hello World!!", "the lazy fox jumps over a brown dog"))


# Q3
def decrypt(msg, s):
    encryption_key = generate_key(s)
    dic = {}
    for i in range(len(encryption_key)):
        dic[encryption_key[i]] = i

    ret = ""
    for char in msg:
        if(ord(char) < 97 or ord(char) > 122):
            ret += char
        else:
            ret += chr(dic[char] + 97)
    
    return ret

print('=' * 9, 'Question 3', '=' * 9)
print(decrypt("##Hbmms Wsvmr!!", "the lazy fox jumps over a brown dog"))


# Q4
def leader(A):
    stack = []
    idx = len(A) - 1
    ret = [-1] * len(A)

    while idx >= 0:
        while(stack and A[idx] > stack[-1]):
            stack.pop()
        if(stack):
            ret[idx] = stack[-1]
        else:
            ret[idx] = A[idx]
        stack.append(A[idx])
        idx -= 1
    
    return ret


print('=' * 9, 'Question 4', '=' * 9)
print(leader([1, 2, 1, 3, 2, 4, 5, 7, 6]))


# Q5
def k_leader(A, k):
    stack = []
    idx = len(A) - 1
    ret = [-1] * len(A)
    while idx >= 0:
        print(stack)
        while(stack and stack[-1] > k + idx):
            stack.pop()
        if(stack):
            ret[idx] = A[stack[-1]]
        else:
            ret[idx] = A[idx]
        stack.append(idx)
        idx -= 1
    
    return ret

print('=' * 9, 'Question 5', '=' * 9)
print(k_leader([1, 2, 1, 3, 2, 4, 5, 7, 6], 2))


# Q6
def minimum(A):
    num = A[-1] - A[0] // 2
    prev = 0

    def sum(A, n):
        sum = 0
        for item in A:
            sum += abs(item - n)
        return sum
    
    first = sum(A, num)
    if(first < sum(A, num+1)):
        prev = first
        num -= 1
        now = sum(A, num)
        while now < prev:
            prev = now
            num -= 1
            now = sum(A, num)
    else:
        prev = first
        num += 1
        now = sum(A, num)
        while now < prev:
            prev = now
            num -= 1
            now = sum(A, num)
        
    return prev

print('=' * 9, 'Question 6', '=' * 9)
print(minimum([1, 3, 7, 8, 11, 17, 25, 31]))


# Q7
def constrained_minimum(A, k):
    pass

print('=' * 9, 'Question 7', '=' * 9)
print(constrained_minimum([[1, 2, 3, 5, 6, 7], [2, 2, 3, 3, 6, 7], [1, 1, 3, 5, 5]], 2))
print(constrained_minimum([[4], [5], [6]], 10))


# Q8
def constrained_minimum_adv(A, k):
    pass

print('=' * 9, 'Question 8', '=' * 9)
print(constrained_minimum_adv([[1, 2, 3, 5, 6, 7], [2, 2, 3, 3, 6, 7], [1, 1, 3, 5, 5], [1, 2, 5, 8, 9]], 2))
print(constrained_minimum_adv([[4], [5], [6], [7]], 10))
