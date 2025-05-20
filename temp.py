def triangle(n):
    ret = "*\n"
    prev = "*\n"
    for i in range(1,n):
        if(i % 2):
            prev = " " + prev
            ret = ret + prev
        else:
            prev = "*" + prev
            ret = ret + prev

    return ret

print(triangle(5))

def triangle_iterative(n):
    ret = ""
    for i in range(n):
        ret += "$" * (i + 1)
        if(True or i != n-1):
            ret += "\n"
    
    return ret

print(triangle_iterative(1))

def triangle_recursive(n):
    if(n == 1):
        return "$\n"
    else:
        return triangle_recursive(n-1) + "$" * n + "\n"
    
print(triangle_recursive(5))

def makeTriangle(sign):
    def helper(n):
        ret = ""
        for i in range(n):
            ret += sign * (i + 1) + "\n"
        return ret
    
    return helper

print(makeTriangle('*')(5))
print(makeTriangle('@')(8))