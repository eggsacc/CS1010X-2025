from math import *


###############
# Question 1a #
###############
def smallest(*lst):
    lst = sorted(lst)
    idx = 0
    ret = ""
    
    if(idx == 0 and lst[idx] == 0):
        while(lst[idx] == 0):
            idx += 1
        ret += str(lst[idx])
        for i in range(idx):
            ret += "0"
        for i in range(idx+1, len(lst)):
            ret += str(lst[i])
    else:
        for item in lst:
            ret += str(item)
    return int(ret)


def test1a():
    print('=== Q1a ===')
    print(smallest(9,1,3)==139)
    print(smallest(1,3,9,0,0)==10039)
    print(smallest(2,1,1,3,9,0)==101239)
 
test1a() 

###############
# Question 1b #
###############
def second_smallest(*lst):
    lst = sorted(lst)
    idx = len(lst)-1
    prev = lst[-1]
    while idx >= 0 and prev == lst[idx]:
        idx -= 1
    if(lst[idx] == lst[-1]):
        return None

    lst[-1], lst[idx] = lst[idx], lst[-1]
    ret = ""
    idx = 0
    if(idx == 0 and lst[idx] == 0):
        while(lst[idx] == 0):
            idx += 1
        ret += str(lst[idx])
        for i in range(idx):
            ret += "0"
        for i in range(idx+1, len(lst)):
            ret += str(lst[i])
    else:
        for item in lst:
            ret += str(item)
    return int(ret)



def test1b():
    print('=== Q1b ===')
    print(second_smallest(9,1,3))
    print(second_smallest(1,3,9,0,0))
    print(second_smallest(2,1,1,3,9,0))
    print(second_smallest(1,1,1)==None)
    print(second_smallest(0,0,0,1, 1,1, 1, 2, 2, 2,2 ,2))
     
test1b() 

##############
# Question 2 #
##############

import csv
def read_csv(csvfilename):
    """
    Reads a csv file and returns a list of list
    containing rows in the csv file and its entries.
    """
    rows = []

    with open(csvfilename) as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            rows.append(row)
    return rows

###############
# Question 2a #
###############

def most_common_major(filename, year):
    filtered = list(filter(lambda x: int(x[0]) == year and x[3] != "na", read_csv(filename)[1:]))
    common_course = None
    max = 0
    for year, gender, course, grad in filtered:
        if(int(grad) > max):
            max = int(grad)
            common_course = course
    return common_course


def test2a():
    print('=== Q2a ===')
    print(most_common_major("graduates-by-first-degree.csv", 1993))
    print(most_common_major("graduates-by-first-degree.csv", 2000))
    print(most_common_major("graduates-by-first-degree.csv", 2010))

test2a()

###############
# Question 2b #
###############

def new_courses(filename,start_year,end_year):
    data = read_csv(filename)[1:]
    seen = set(map(lambda x: x[2], list(filter(lambda x: x[3] != "na" and int(x[0]) <= start_year, data))))
    filtered = map(lambda x: (x[2], int(x[0])), list(filter(lambda x: x[3] != "na" and int(x[0]) > start_year and int(x[0]) <= end_year, data)))
    filtered = list(filter(lambda x: x[0] not in seen, filtered))
    seen.clear()
    ret = []
    for item in filtered:
        if(item[0] not in seen):
            seen.add(item[0])
            ret.append(item)
    return ret




def test2b():
    print('=== Q2b ===')
    print(new_courses("graduates-by-first-degree.csv",1993,2000)
)
    print(new_courses("graduates-by-first-degree.csv",2001,2010)
)
    print(new_courses("graduates-by-first-degree.csv",1993,2020))

test2b()

###############
# Question 2c #
###############

def topk_growing_major(filename,k,start_year,end_year):
    data = read_csv(filename)[1:]
    start = set(map(lambda x: x[2], filter(lambda x: int(x[0]) == start_year and x[3] != "na", data)))
    end = set(map(lambda x: x[2], filter(lambda x: int(x[0]) == end_year and x[3] != "na", data)))
    valid_courses = start.intersection(end)
    filtered_start = list(map(lambda x: (x[2], int(x[3])), filter(lambda x: x[3] != "na" and x[2] in valid_courses and int(x[0]) == start_year, data)))
    filtered_end = list(map(lambda x: (x[2], int(x[3])), filter(lambda x: x[3] != "na" and x[2] in valid_courses and int(x[0]) == end_year, data)))
    ret = []
    seen = set()
    for i in range(len(filtered_start)):
        ret.append([filtered_start[i][0], filtered_end[i][1] - filtered_start[i][1]])
    ret.sort(key=lambda x: x[1], reverse=True)
    return list(map(lambda x: x[0], ret[:k]))

def test2c():
    print('=== Q2c ===')
    print(topk_growing_major("graduates-by-first-degree.csv",3,1993,2000)
)
    print(topk_growing_major("graduates-by-first-degree.csv",2,2000,2010))
    print(topk_growing_major("graduates-by-first-degree.csv",3,2000,2014))

test2c()
    
##############
# Question 3 #
##############

class Timeline:
    def __init__(self):
        self.years = {}
    
    def born(self, name, year, lifespan):
        person = Person(name, year, lifespan)
        if(year not in self.years):
            self.years[year] = [person]
        else:
            self.years[year].append(person)
    
    def get_people(self, year):
        ret = []
        for item in self.years[year]:
            ret.append((item.name, item.id))
        return ret

        


        

class Person:
    def __init__(self, timeline, name, year, lifespan):
        self.timeline = timeline
        self.name = name
        self.lifespan = lifespan
        self.id = year
    
    def jump(self, from_year, to_year, identity):
            if(from_year > self.id + self.lifespan):
                return False
            self.timeline.years[]


def test3():
    print('=== Q3 ===')
    t = Timeline()
    thor = t.born("Thor",518,5000)
    thanos = t.born("Thanos",1950,1000000)

    print(t.get_people(2017)==[('Thor', 518), ('Thanos', 1950)])
    print(thor.kill(2018,thanos,1950)) # whoops. Violence. :'(
    print(not thor.kill(2018,thanos,1950)) # Can't kill him twice!
    print(t.get_people(2018)==[('Thor', 518)]) # Thanos dead.
    
    thor.jump(2023,2013,518)
    thor.jump(2014,2024,2023)

    print(set(t.get_people(2013))==set([('Thor', 2023), ('Thor', 518), ('Thanos', 1950)]))
    print(set(t.get_people(2014))==set([('Thor', 518), ('Thanos', 1950)]))

    print(t.get_people(2022)==[('Thor', 518)])
    print(t.get_people(2023)==[])
    print(t.get_people(2024)==[('Thor', 2014)])

    thanos.jump(2014,2024,1950)
    print(set(t.get_people(2024))==set([('Thor', 2014), ('Thanos', 2014)]))

    # New Thor and old Thanos jumped so only old Thor left
    print(t.get_people(2014)==[('Thor', 518)]) 
    print(t.get_people(2017)==[('Thor', 518)])

    #Thanos is no longer around to die. 
    print(not thor.kill(2018,thanos,1950))


#test3()


             
