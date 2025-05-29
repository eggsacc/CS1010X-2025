############################################################
#
# Question 1
#
#############################################################
def day_of_date( dd, mm, yyyy ):
    non_leapyear_code = [0, 0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5]
    leapyear_code = [0, 6, 2, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5]
    century_code = {16:0, 17:6, 18:4, 19:2, 20:0, 21:6}
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    def is_leapyear(year):
        if(year % 400 == 0):
            return True
        else:
            if(year % 4 == 0 and year % 100 != 0):
                return True
            return False
        
    box1 = dd
    box2 = 0
    box3 = 0
    box4 = 0
    box5 = 0

    if(is_leapyear(yyyy)):
        box2 = leapyear_code[mm]
    else:
        box2 = non_leapyear_code[mm]
    
    box3 = century_code[yyyy // 100 + 1]
    box4 = yyyy % 100
    box5 = box4 // 4

    return days[(box1 + box2 + box3 + box4 + box5) % 7]

print ("")
print (" * * * Question 1 * * *")
print (day_of_date(25, 12, 2000) == "Monday")
print (day_of_date(25, 12, 1900) == "Tuesday")
print (day_of_date(1, 1, 1997) == "Wednesday")
print (day_of_date(11, 11, 1999) == "Thursday")
print (day_of_date(1, 1, 1897) == "Friday")
print (day_of_date(5, 6, 2021) == "Saturday")
print (day_of_date(5, 6, 1898) == "Sunday")

############################################################
#
# Question 2
#
#############################################################
from runes import *

def stackn(n,pic):
    if n == 1: 
        return pic
    else: 
        return stack_frac(1/n, pic, stackn(n-1, pic))

def nxn(n,pic):
    return stackn(n, quarter_turn_right(stackn(n, quarter_turn_left(pic) ) ) )

print ("")
print (" * * * Question 2 * * *")
#########
#
# Question 2: Question 2 A.
#
#########
def stackn_alt(n, pic1, pic2, flag=1):
    if n == 1: 
        return pic1 if flag else pic2
    else: 
        return stack_frac(1/n, pic1 if flag else pic2, stackn_alt(n-1, pic1, pic2, flag ^ 1))
    
#show(stackn_alt(5, make_cross(nova_bb), make_cross(rcross_bb)))
#show(stackn_alt(6, make_cross(nova_bb), make_cross(rcross_bb)))
#show(stackn_alt(5, make_cross(circle_bb), make_cross(heart_bb)))

#########
#
# Question 3: Question 2 B. 
# Recursive
#
#########
def nxn_alt(n, pic1, pic2):
    return stackn_alt(n, quarter_turn_right(stackn_alt(n, quarter_turn_left(pic2), quarter_turn_left(pic1))), quarter_turn_right(stackn_alt(n, quarter_turn_left(pic1), quarter_turn_left(pic2))))

#show(nxn_alt(5, make_cross(nova_bb), make_cross(rcross_bb)))
#show(nxn_alt(4, make_cross(nova_bb), make_cross(rcross_bb)))
#show(nxn_alt(6, make_cross(nova_bb), make_cross(rcross_bb)))
show(nxn(5, heart_bb))
#show(nxn_alt(5, make_cross(circle_bb), heart_bb))

#########
#
# Question 4: Question 2 C. 
# Use for or while loop
#
#########
def nxn_alt(n,pic1, pic2):
    pat1 = quarter_turn_right(stackn_alt(n, quarter_turn_left(pic2), quarter_turn_left(pic1)))
    pat2 = quarter_turn_right(stackn_alt(n, quarter_turn_left(pic1), quarter_turn_left(pic2)))

    flag = n%2
    base = pic1 if flag else pic2
    for i in range(n):
        base = stack_frac(1/(i+1), pat1 if flag else pat2, base)
        flag ^= 1
    return base

#show(nxn_alt(5, make_cross(nova_bb), make_cross(rcross_bb)))
#show(nxn_alt(4, make_cross(nova_bb), make_cross(rcross_bb)))
#show(nxn_alt(6, make_cross(nova_bb), make_cross(rcross_bb)))
#show(nxn_alt(5, make_cross(circle_bb), make_cross(heart_bb)))


############################################################
#
# Question 3
#
#############################################################
lst = [ [1, 2, 3, 4, 5, 6, 7, 8],
        [9, 0, 1, 2, 3, 4, 5, 6],
        [7, 8, 9, 0, 1, 2, 3, 4],
        [5, 6, 7, 8, 9, 0, 1, 2],
        [3, 4, 5, 6, 7, 8, 9, 0] ]

lst2 = [[-2, 94, 7, -90, -34],
        [30, 24, 3, 100, -23],
        [22, -9, 49, -45, 29], 
        [-65, -28, -65, 93, -76], 
        [58, -36, 36, 80, 54]]

lst3 = [[-66, 45, 95, -84, -35, -70, 26, 94, 15, 20],
        [66, -3, -47, -76, 24, -93, -1, 10, 55, 95], 
        [96, -100, 78, 14, -32, 84, -42, 51, -74, -19], 
        [-93, -95, -94, 66, 38, -98, -3, 75, -45, 8], 
        [85, -93, 35, -44, 95, 12, 26, 41, -41, -12]]

lst4 = [[-86, -77, -79, -8, -57],
        [88, 71, -22, -36, 55],
        [-46, 55, -91, 48, 74],
        [-60, 10, 63, 0, 85],
        [30, -5, 39, 13, 28],
        [-32, -91, -93, -7, 19],
        [-19, -3, 8, 34, -58],
        [43, -55, -40, -41, -94],
        [-55, -17, -56, -66, 30],
        [30, -8, 31, 72, 43]]


def rect_sum(lst, i, j):
    sum = 0
    for ii in range(0, i+1):
        for jj in range(0, j+1):
            sum += lst[ii][jj]
    return sum

def naive_sum(lst):
    result_lst = []
    for i in range(0, len(lst)):
        result_lst.append([0]*len(lst[0]))
        for j in range(0, len(lst[0])):
            result_lst[i][j] = rect_sum(lst, i, j)
    return result_lst

sample_result = naive_sum(lst)
sample_result2 = naive_sum(lst2)
sample_result3 = naive_sum(lst3)
sample_result4 = naive_sum(lst4)

#########
#
# Question 5: Question 3 A.
#
#########
# State the time complexity in coursemology: (nxm)^2

#########
#
# Question 6: Question 3 B.
#
#########
def better_sum(lst):
    n = len(lst)
    m = len(lst[0])
    ret = [[0 for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            ret[i][j] = lst[i][j]

    for i in range(n):
        for j in range(m):
            if(j == 0):
                continue
            ret[i][j] = ret[i][j] + ret[i][j-1]
            
    for j in range(m):
        for i in range(n):
            if(i == 0):
                continue
            ret[i][j] = ret[i][j] + ret[i-1][j]
    return ret

print ("")
print (" * * * Question 3B * * *")
print( sample_result == better_sum(lst) )
print( sample_result2 == better_sum(lst2) )
print( sample_result3 == better_sum(lst3) )
print( sample_result4 == better_sum(lst4) )

#########
#
# Question 7: Question 3 C.
#
#########
def dp_sum(lst):
    n = len(lst)
    m = len(lst[0])
    dp_table = [[0 for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            up = 0
            left = 0
            overcount = 0
            if(i > 0):
                up = dp_table[i-1][j]
            if(j > 0):
                left = dp_table[i][j-1]
            if(i > 0 and j > 0):
                overcount = dp_table[i-1][j-1]
            dp_table[i][j] = up + left - overcount + lst[i][j]
    
    return dp_table


print ("")
print (" * * * Question 3C * * *")
print(dp_sum(lst))
print( sample_result2 == dp_sum(lst2) )
print( sample_result3 == dp_sum(lst3) )
print( sample_result4 == dp_sum(lst4) )

#########
#
# Question 8: Question 3 D.
#
#########
# State the time complexity in coursemology

#########
#
# Question 9: Question 3 E.
#
#########
def search_rect_sum(result_lst, ii, jj, i, j):
    top = 0
    left = 0
    overcount = 0
    if(min(j, jj) > 0):
        left = result_lst[max(ii, i)][min(jj, j)-1]
    if(min(i, ii) > 0):
        top = result_lst[min(i, ii)-1][max(j, jj)]
    if(min(i, ii) > 0 and min(j, jj) > 0):
        overcount = result_lst[min(i, ii)-1][min(j, jj)-1]
    return result_lst[max(i, ii)][max(j, jj)] - left - top + overcount
    

print ("")
print (" * * * Question 3E * * *")
x = sample_result
print( search_rect_sum(x, 0, 0, 4,7) == 180 )
print( search_rect_sum(x, 3, 6, 4,7) == 12 )
print( search_rect_sum(x, 3, 7, 4,7) == 2)
print( search_rect_sum(x, 4, 6, 4,7) == 9)
print( search_rect_sum(x, 1, 0, 4, 7) == 144)
print( search_rect_sum(x, 1, 0, 3, 6) == 90)
print( search_rect_sum(x, 0, 1, 3, 6) == 96)
print( search_rect_sum(x, 1, 1, 3, 6) == 69)
print( search_rect_sum(x, 2, 3, 3, 6) == 24)

print( search_rect_sum(sample_result2, 0, 0, 4, 4) == 206 )
print( search_rect_sum(sample_result3, 2, 3, 4, 9) == 100 )
print( search_rect_sum(sample_result4, 3, 2, 9, 4) == 10 )
