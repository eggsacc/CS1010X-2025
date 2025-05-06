#####
# 1)
#####
a = (("apple", 2), ("orange", 4), (5, 7))
b = dict(a)
c = [[1, 2], [3, 4], [5, 7]]
d = dict(c)

print(b["orange"]) # 4
print(b[5])        # 7
#print(b[1])        # KeyError

b["bad"] = "better"
b[1] = "good"

for key in b.keys():
    print(key)

# apple
# orange
# 5
# bad
# 1

for val in b.values():
    print(val)

# 2
# 4
# 7
# better
# good

del b["bad"]
del b["apple"]

print(tuple(b.keys()))  # ('orange', 5, 1)
print(list(b.values())) # [4, 7, 'good']\

#####
# 2)
#####
def make_stack():
    stk = []
    def stack(cmd):
        if(cmd == "push"):
            return lambda x: stk.append(x) or "pushed"
        elif(cmd == "pop"):
            return stk.pop() if len(stk) >= 1 else "empty_stack"
        elif(cmd == "peek"):
            return stk[len(stk) - 1] if len(stk) >= 1 else "empty_stack"
        elif(cmd == "is_empty"):
            return len(stk) == 0
        elif(cmd == "clear"):
            return stk.clear() or "cleared"
        
    return stack
            
s = make_stack()
print(s("is_empty")) # True
s("push")(1)
s("push")(2)
print(s("peek"))
# 2
print(str(s("pop"))) # 2
print(str(s("pop"))) # 1
print(str(s("pop"))) # None

#####
# 3)
#####
def push_all(stk, seq):
    for item in seq:
        stk("push")(item)
    
    return stk

#####
# 4)
#####
def pop_all(stk):
    output = []
    while(not stk("is_empty")):
        output.append(stk("pop"))
    
    return output

#####
# 5)
#####
def make_calculator():
    stack = make_stack()

    def op_input(cmd):
        a = stack("pop")
        b = stack("pop")
        stack("push")(ops[cmd](b, a))
        return "pushed"
    
    ops = {'+':lambda x, y: x + y,
           '-':lambda x, y: x - y,
           '*':lambda x, y: x * y,
           '/':lambda x, y: x / y,
           'ANSWER':lambda:stack("peek"),
           'CLEAR':lambda:stack("clear"),
           'NUMBER_INPUT':stack("push"),
           'OPERATION_INPUT':op_input}
    
    def oplookup(msg, *args):
        try:
            if(args):
                return ops[msg](args[0])
            else:
                return ops[msg]()
        except KeyError:
            raise Exception("calculator dosn't" + msg)

    return oplookup

c = make_calculator()
print(c('ANSWER'))
print(c('NUMBER_INPUT',4))
print(c('ANSWER'))
print(c('NUMBER_INPUT',5))
print(c('ANSWER'))
print(c('OPERATION_INPUT','+')) 
print(c('ANSWER'))
print(c('NUMBER_INPUT',7))
print(c('OPERATION_INPUT','-')) 
print(c('ANSWER'))
print(c('CLEAR'))
print(c('ANSWER'))
