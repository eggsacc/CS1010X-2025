# Question 1
def dec_to_base(dec, base):
    new = ""
    while dec != 0:
        new = str(dec % base) + new
        dec //= base
    
    return int(new)

print('=' * 9, 'Question 1', '=' * 9)
print(dec_to_base(123, 5))
print(dec_to_base(443, 9))


# Question 2
def encode(S, base_lst):
    base_idx = 0
    ret = ""
    for i in range(len(S)):
        if(base_idx >= len(base_lst)):
            base_idx = 0
        encoded_char = "#" + str(base_lst[base_idx]) + "#" \
        + str(dec_to_base(ord(S[i]), base_lst[base_idx]))
        ret += encoded_char
        base_idx += 1
    
    return ret 


print('=' * 9, 'Question 2', '=' * 9)
print(encode('hello', [5, 3, 7]))


# Question 3
def base_to_dec(num, base):
    new = 0
    pwr = 0
    while num != 0:
        new += (num % 10) * base ** pwr
        num //= 10
        pwr += 1
    
    return new

print('=' * 9, 'Question 3', '=' * 9)
print(base_to_dec(11010, 3))


# Question 4
def decode(S):
    ret = ""
    while len(S) != 1:
        idx = 0
        cnt = 0
        while cnt < 3 and idx < len(S) - 1:
            if(S[idx] == "#"):
                cnt += 1
            if(cnt <= 2):
                idx += 1
        if(idx == len(S)-1):
            char = S
        else:
            char = S[:idx]
        S = S[idx:]
        print(char)
        base = char[1]
        ret += chr(base_to_dec(int(char[3:]), int(base)))
    
    return ret


print('=' * 9, 'Question 4', '=' * 9)
print(decode('#5#404#3#10202#7#213#5#413#3#11010'))


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


# Question 5
def arrange(car_lst, commands):
    stack = []
    queue = []
    for cmd in commands:
        if(cmd == "P"):
            if(car_lst):
                car = car_lst.pop(0)
                stack.append(car)
            else:
                raise Exception("unable to push: car list empty")
        if(cmd == "Q"):
            if(car_lst):
                car = car_lst.pop(0)
                queue.insert(0, car)
            else:
                raise Exception("unable to queue: car list empty")
        if(cmd == "PQ"):
            if(stack):
                car = stack.pop()
                queue.insert(0, car)
            else:
                raise Exception("unable to pop-queue: stack empty")
    
    return queue

print('=' * 9, 'Question 5', '=' * 9)
print(arrange([1, 4, 7, 9, 11, 15], ['P', 'Q', 'PQ', 'Q', 'P', 'P', 'Q', 'PQ', 'PQ']))


# Question 6
def check(car_lst_in, car_lst_out):
    filtered_lst = []
    prev = 0
    for item in car_lst_out[-1::-1]:
        if(item < prev):
            filtered_lst.append(item)
        else:
            prev = item
    
    if(not filtered_lst):
        return "possible"
    
    possible = False
    prev = filtered_lst[0]
    for item in filtered_lst:
        if(item > prev):
            return "impossible"
        prev = item
    
    return "possible"


print('=' * 9, 'Question 6', '=' * 9)
print(check([1, 4, 7, 23, 45, 67], [67, 45, 23, 7, 4, 1]))
print(check([1, 2, 4, 6, 7, 9, 11, 15, 16], [4, 6, 16, 7, 15, 9, 11, 2, 1]))
print(check([1, 2, 4, 6, 7, 9, 11, 15, 16], [4, 7, 16, 6, 15, 9, 11, 2, 1]))


# Question 7
def ACB(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] < nums[k] < nums[j]:
                    return True
    return False

print('=' * 9, 'Question 7', '=' * 9)
print(ACB([1, 2, 3, 4, 5, 6, 7, 8]))
print(ACB([1, 2, 3, 4, 7, 8, 9 ,5]))


# Question 8
def ACB(lst):
    stack = []
    min = -1
    while lst:
        num = lst.pop()
        if(num < min):
            return True
        else:
            while(stack and num > stack[-1]):
                min = stack.pop()
            stack.append(num)
    return False

print('=' * 9, 'Question 8', '=' * 9)
print(ACB([1, 2, 3, 4, 5, 6, 7, 8]))
print(ACB([1, 2, 3, 4, 7, 8, 9 ,5]))
