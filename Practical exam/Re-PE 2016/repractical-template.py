######################################
#   CS1010X AY2015/2016 Semester 2   #
#   Template for Re-Practical Exam   #
######################################

########################
# Q1 - Circular Primes #
########################

from math import *

#################
# Q1a - Warm Up #
#################

def rotations(n):
    # Write your solution here
    str_n = str(n)
    ret = []
    for i in range(len(str_n)):
        if(int(str_n) not in ret):
            ret.append(int(str_n))
        temp = str_n[-1]
        str_n = temp + str_n[:-1]
    return ret

def test1a():
    print('Q1a')
    print(sorted(rotations(1))==sorted([1]))
    print(sorted(rotations(11))==sorted([11]))
    print(sorted(rotations(101))==sorted([101, 11, 110]))
    print(sorted(rotations(123))==sorted([123, 231, 312]))
    print(sorted(rotations(221))==sorted([221, 212, 122]))
    print(sorted(rotations(1231))==sorted([1231, 2311, 3112, 1123]))
    print(sorted(rotations(1212))==sorted([1212, 2121]))

#test1a()


###############################
# Q1b - Count Circular Primes #
###############################

def is_prime(n): # Bonus! :-) 
    if n==1:
        return False
    for i in range(2,int(sqrt(n))+1):
        if n%i == 0:
            return False
    return True

def count_circular_primes(n):
    # Write your solution here
    count = 0
    for i in range(2, n+1):
        nums = rotations(i)
        is_circular = True
        for num in nums:
            if(not is_prime(num)):
                is_circular = False
        if(is_circular):
            count += 1
    return count

def test1b():
    print('Q1b')
    print(count_circular_primes(2)==1)
    print(count_circular_primes(4)==2)
    print(count_circular_primes(13)==6)
    print(count_circular_primes(57)==9)
    print(count_circular_primes(100)==13)

#test1b()

##############################
# Q2 - Tyrion's Flight Mania #
##############################
# DATA Reference : quantquote.com
import csv

def import_csv(filename):
    with open(filename, 'r') as f:
        lines = csv.reader(f, delimiter=',')
        return tuple(lines)

#########################
# Q2a - Get Num Flights #
#########################
def get_num_flights(src, dst, filename):
    # Write your solution here
    data = import_csv(filename)
    flights = 0
    for flight in data:
        if(flight[1] == src and flight[2] == dst):
            flights += 1
    print(flights)
    return flights
        

def test2a():
    print('Q2a')
    print(get_num_flights('VIE','HAM','flight_routes.csv')==1)
    print(get_num_flights('SIN','MNL','flight_routes.csv')==3)
    print(get_num_flights('SIN','HAV','flight_routes.csv')==0)

#test2a()

#####################
# Q2b  - Top K Hubs #
#####################

def get_top_k_hubs(k, filename):
    # Write your solution here
    data = import_csv(filename)
    flights_dic = {}
    for flight in data:
        if(flight[1] not in flights_dic):
            flights_dic[flight[1]] = 1
        else:
            flights_dic[flight[1]] += 1
    
    flights_lst = []
    for key, value in flights_dic.items():
        flights_lst.append((key, value*2))

    flights_lst.sort(key=lambda x: x[0])
    flights_lst.sort(key=lambda x: x[1], reverse=True)
    while(k < len(flights_lst) and flights_lst[k][1] == flights_lst[k-1][1]):
        k += 1
    return flights_lst[:k]

def test2b():
    print('Q2b')
    print(get_top_k_hubs(1,'flight_routes.csv')==[('SIN', 224)])
    print(get_top_k_hubs(2,'flight_routes.csv')==[('SIN', 224), ('MNL', 144)])
    print(get_top_k_hubs(3,'flight_routes.csv')==[('SIN', 224), ('MNL', 144), ('CGN', 134)])
    print(get_top_k_hubs(4,'flight_routes.csv')==[('SIN', 224), ('MNL', 144), ('CGN', 134), ('CTU', 122)])

#test2b()

#######################
# Q2c - Flight Search #
#######################

def search_routes(src, dest, filename, max_hops):
    # Write your solution here
    data = import_csv(filename)
    airports = {}
    related_nodes = []
    idx = 0
    for flight in data:
        if flight[1] not in airports:
            airports[flight[1]] = idx
            related_nodes.append([flight[2]])
            idx += 1
        else:
            related_nodes[airports[flight[1]]].append(flight[2])

    routes = []
    path = [src]
    def helper(now, dst, n):
        if(n < 0):
            return False
        if(now == dst):
            if(path not in routes):
                routes.append(path.copy())
            return True
        else:
            for node in related_nodes[airports[now]]:
                if(node not in path):
                    path.append(node)
                    helper(node, dst, n-1)
                    path.pop()
    
    helper(src, dest, max_hops)
    routes.sort(key=lambda x: len(x))
    print(routes)
    return routes




def test2c():
    print('Q2c')

    def order_not_increasing(lst): # returns True if routes are NOT arranged in increasing order
        curr_size = 0
        for i in lst:
            if curr_size <= len(i):
                curr_size = len(i)
            else:
                return True
        return False

    ans1 = search_routes('LED','NBC','flight_routes.csv',1)
    model_ans1 = [['LED','NBC']]
    ans2 = search_routes('LED','NBC','flight_routes.csv',2)
    model_ans2 = [['LED', 'NBC'], ['LED', 'DME', 'NBC']]
    ans3 = search_routes('LED','NBC','flight_routes.csv',3)
    model_ans3 = [['LED', 'NBC'], ['LED', 'DME', 'NBC'], ['LED', 'KZN', 'DME', 'NBC'], ['LED', 'KZN', 'SVX', 'NBC'], ['LED', 'UUA', 'DME', 'NBC'], ['LED', 'ASF', 'DME', 'NBC'], ['LED', 'SCW', 'SVX', 'NBC'], ['LED', 'OVB', 'SVX', 'NBC'], ['LED', 'DYU', 'DME', 'NBC'], ['LED', 'DYU', 'SVX', 'NBC'], ['LED', 'LBD', 'DME', 'NBC'], ['LED', 'CSY', 'DME', 'NBC'], ['LED', 'MCX', 'DME', 'NBC'], ['LED', 'SKX', 'DME', 'NBC'], ['LED', 'VOZ', 'DME', 'NBC']]

    if order_not_increasing(ans1):
        print(False)
    else:
        print(sorted(ans1)==sorted(model_ans1))
    if order_not_increasing(ans2):
        print(False)
    else:
        print(sorted(ans2)==sorted(model_ans2))
    if order_not_increasing(ans3):
        print(False)
    else:
        print(sorted(ans3)==sorted(model_ans3))

#test2c()


########################
# Q3 - Tech Tree Mania #
########################

class TechTree:
    # Write your solution here
    def __init__(self, name):
        self.name = name
        self.tech = {}
        self.unlocked = {}

    def get_name(self):
        return self.name
    
    def add_tech(self, tech):
        if(tech in self.tech):
            return False
        else:
            self.tech[tech] = []
            self.unlocked[tech] = False
            return True
    
    def add_dependency(self, parent, child):
        if(parent not in self.tech or child not in self.tech):
            return False
        else:
            self.tech[parent].append(child)
            return True
    
    def get_parents(self, tech):
        ret = []
        for parent, child in self.tech.items():
            for item in child:
                if(item == tech):
                    ret.append(parent)
        
        return ret
    
    def get_ancestors(self, tech):
        if(tech not in self.tech):
            return False
        ret = []
        def helper(tech):
            items = self.get_parents(tech)
            if(not items):
                return
            else:
                for item in items:
                    if(item not in ret):
                        ret.append(item)
                    helper(item)
        
        helper(tech)
        return ret
    
    def unlock(self, tech):
        if(self.unlocked[tech]):
            return False
        
        else:
            ancestors = self.get_ancestors(tech)
            for item in ancestors:
                if(not self.unlocked[item]):
                    return False
            
            self.unlocked[tech] = True
            return True
    
    def is_unlocked(self, tech):
        return self.unlocked[tech]

    def has_loop(self):
        seen = []
        has_loop = False
        def dfs(node):
            if(not self.tech[node]):
                return
            for tech in self.tech[node]:
                if(tech in seen):
                    nonlocal has_loop 
                    has_loop = True
                    return
                else:
                    seen.append(tech)
                    dfs(tech)
                    seen.pop()

        
        for key in self.tech.keys():
            dfs(key)
        
        return has_loop


def test3():
    print("Q3")
    tt = TechTree("civilization")
    tt.add_tech("metal working")
    tt.add_tech("stone working")
    tt.add_tech("bronze working")
    tt.add_tech("iron working")
    tt.add_tech("construction")
    tt.add_tech("mining")
    tt.add_tech("craftsmanship")
    tt.add_dependency("metal working","bronze working")
    tt.add_dependency("bronze working","iron working")
    tt.add_dependency("iron working","construction")
    tt.add_dependency("stone working","mining")
    tt.add_dependency("stone working","craftsmanship")
    tt.add_dependency("craftsmanship","construction")
    tt.add_dependency("stone working","construction")


    print("1", sorted(tt.get_parents("mining"))==sorted(['stone working']))
    print("2", sorted(tt.get_ancestors("mining"))==sorted(['stone working']))
    print("3", sorted(tt.get_parents("construction"))==sorted(['iron working', 'craftsmanship', 'stone working']))
    print("4", sorted(tt.get_ancestors("construction"))==sorted(['stone working', 'craftsmanship', 'iron working', 'bronze working', 'metal working']))
    print(tt.get_ancestors("construction"))
    print("5", tt.is_unlocked("stone working")==False)
    print("6", tt.unlock("stone working")==True)
    print("7", tt.is_unlocked("stone working")==True)
    print("8", tt.is_unlocked("construction")==False)
    print("9", tt.unlock("construction")==False)
    print("10", tt.is_unlocked("construction")==False)
    print("11", tt.has_loop()==False)
    tt.add_dependency("construction","stone working")
    print("12", tt.has_loop()==True)

test3()

# tt = TechTree("civilization")
# tt.add_tech("metal working")
# tt.add_tech("stone working")
# tt.add_tech("bronze working")
# tt.add_tech("iron working")
# tt.add_tech("construction")
# tt.add_tech("mining")
# tt.add_tech("craftsmanship")
# tt.add_dependency("metal working","bronze working")
# tt.add_dependency("bronze working","iron working")
# tt.add_dependency("iron working","construction")
# tt.add_dependency("stone working","mining")
# tt.add_dependency("stone working","craftsmanship")
# tt.add_dependency("craftsmanship","construction")
# tt.add_dependency("stone working","construction")
