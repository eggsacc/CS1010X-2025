import csv

##############
# Question 1 #
##############

#################
# Q1a - Warm Up #
#################

def contains(a, b):
    # Write your solution here
    a_str = str(a)
    b_str = str(b)
    return b_str in a_str


def test1a():
    print('Q1a')
    print(contains(123, 123) == True)
    print(contains(1234, 123) == True)
    print(contains(4123, 123) == True)
    print(contains(123555, 123) == True)
    print(contains(123555, 23) == True)
    print(contains(1243555, 123) == False)

test1a()



########################
# Q1b - Longest Streak #
########################

def count_longest_streak(a):
    # Write your solution here
    a_str = str(a)
    prev = a_str[0]
    count = 0
    max_count = 0
    for i in range(len(a_str)):
        curr = a_str[i]
        if(curr != prev):
            if(count > max_count):
                max_count = count
            count = 1
        else:
            count += 1
        prev = curr

    return max_count if max_count > count else count

def test1b():
    print('Q1b')
    print(count_longest_streak(123456789) == 1)
    print(count_longest_streak(111123456789) == 4)
    print(count_longest_streak(123444456789) == 4)
    print(count_longest_streak(11112211111) == 5)

test1b()



##############################
# Q2 - Stock Market Analysis #
##############################
# These functions are provided for you
# Do not make any changes to them

def import_csv(filename):
    with open(filename, 'r') as f:
        lines = csv.reader(f, delimiter=',')
        return tuple(lines)


#######################
# Q2a - Minimum Price #
#######################

def min_stock(datafile, start, end):
    # Write your solution here
    table = import_csv(datafile)
    if(start > int(table[len(table) - 1][0]) or start > end):
        return None
    
    start = start if start >= int(table[0][0]) else int(table[0][0])
    end = end if end <= int(table[len(table) - 1][0]) else int(table[len(table) - 1][0])
    
    min = 9999
    date = start
    idx = 0
    while(date <= end and idx < len(table)):
        if(int(table[idx][0]) >= start):
            if(float(table[idx][4]) < min):
                min = float(table[idx][4])
        date = int(table[idx][0])
        idx += 1
    
    return min



EPS = 1e-10 # For approximation of floating point answers
def close(a, b):
    return b-EPS <= a <= b+EPS

def test2a():
    print('Q2a')
    print(close(min_stock("table_tap.csv", 19980218, 19980309), 11.6277))
    print(close(min_stock("table_tap.csv", 19980102, 20130809), 11.0139))
    print(close(min_stock("table_apa.csv", 19980102, 20130809), 6.91758))

test2a()


##################
# Q2b - Volatity #
##################

def average_daily_variation(datafile, start, end):
    # Write your solution here
    table = import_csv(datafile)
    if(start > int(table[len(table) - 1][0]) or end < start):
        return None
    
    start = start if start >= int(table[0][0]) else int(table[0][0])
    end = end if end <= int(table[len(table) - 1][0]) else int(table[len(table) - 1][0])
    
    idx = 0
    count = 0
    total = 0
    while(idx < len(table) and int(table[idx][0]) <= end):
        if(int(table[idx][0]) >= start):
            total += (float(table[idx][3]) - float(table[idx][4]))
            count += 1
        idx += 1
    
    return total / count if count > 0 else None




def test2b():
    print('Q2b')
    print(close(average_daily_variation("table_tap.csv", 19980218, 19980309), 0.47104285714285715))
    print(close(average_daily_variation("table_tap.csv", 19980102, 20130809), 0.668375878757002))
    print(close(average_daily_variation("table_apa.csv", 19980102, 20130809), 1.6702794752929195))

test2b()

#######################
# Q2c - Optimal Trade #
#######################

def trade_stock(datafile, start, end):
    table = import_csv(datafile)

    # Clamp start and end to data bounds
    if start > int(table[-1][0]) or end < start:
        return None

    start = max(start, int(table[0][0]))
    end = min(end, int(table[-1][0]))

    # Filter relevant rows in date range
    filtered = [row for row in table if start <= int(row[0]) <= end]

    if not filtered:
        return None

    max_profit = -1
    min_price = float(filtered[0][2])
    max_profit = 0
    for row in filtered:
        low = float(row[4])
        high = float(row[3])
        if low < min_price:
            min_price = low
        profit = high - min_price
        if(profit > max_profit):
            max_profit = profit
    
    return max_profit


def test2c():
    print('Q2c')
    print(close(trade_stock("table_tap.csv", 19980218, 19980309), 1.3630999999999993))
    print(close(trade_stock("table_tap.csv", 19980102, 20130809), 42.7361))
    print(close(trade_stock("table_apa.csv", 19980102, 20130809), 136.89742))

    # Test null set

test2c()
#print(trade_stock("table_tap.csv", 19980102, 20130809))

#####################
# Q3 - Going Places #
#####################

# @brief Map class
# @note Stores nodes in a dictionary. Stored links in a list.
#       Dictionary returns the index to look for links related to a node in the list.
class Map():
    # Write your solution here
    def __init__(self):
        self.nodes = {}
        self.hash = 0
        self.links = []
    
    def add_node(self, node):
        if(node not in self.nodes):
            self.nodes[node] = self.hash
            self.hash += 1
            self.links.append([])
            return True
        else:
            return False
    
    def add_link(self, node1, node2, distance):
        if(node1 not in self.nodes or node2 not in self.nodes):
            return False
        else:
            self.links[self.nodes[node1]].append((node2, distance))
            self.links[self.nodes[node2]].append((node1, distance))
            return True

    def get_distance(self, node1, node2):
        if(node1 not in self.nodes or node2 not in self.nodes):
            return False
        else:
            for link in self.links[self.nodes[node1]]:
                if(link[0] == node2):
                    return link[1]
            return False
        
    def get_paths(self, node1, node2):
        if node1 not in self.nodes or node2 not in self.nodes:
            return []

        all_paths = []

        def dfs(current, destination, path, visited):
            if current == destination:
                all_paths.append(path[:])  # append a copy of the current path
                return
            visited.add(current)
            for neighbor, _ in self.links[self.nodes[current]]:
                if neighbor not in visited:
                    path.append(neighbor)
                    dfs(neighbor, destination, path, visited)
                    path.pop()
            visited.remove(current)

        dfs(node1, node2, [node1], set())
        return all_paths

    def shortest_path(self, node1, node2):
        paths = self.get_paths(node1, node2)

        if(not paths):
            return False
        
        min = 99999
        for path in paths:
            total = 0
            for i in range(len(path) - 1):
                node = path[i]
                next = path[i + 1]
                total += self.get_distance(node, next)
            
            if(total < min):
                    min = total
        
        return min






def test3():
    m = Map()
    m.add_node("Singapore")
    m.add_node("Seoul")
    m.add_node("San Francisco")
    m.add_node("Tokyo")
    m.add_link("Tokyo","Seoul",1152)
    m.add_link("Singapore","Seoul",4669)
    m.add_link("Singapore","Tokyo",5312)
    m.add_link("Tokyo","San Francisco",5136)

    def sortall(lst):
        return sorted(list(map(sortall, lst))) if type(lst) is list else lst

    print("Q3")
    print(sortall(m.get_paths("Singapore","Seoul")) ==\
            sortall([['Singapore', 'Seoul'], ['Singapore', 'Tokyo', 'Seoul']]))

    print(sortall(m.get_paths("San Francisco","Seoul")) ==\
            sortall([['San Francisco', 'Tokyo', 'Seoul'],\
            ['San Francisco', 'Tokyo', 'Singapore', 'Seoul']]))

    print(sortall(m.get_paths("Seoul","San Francisco")) ==\
            sortall([['Seoul', 'Tokyo', 'San Francisco'],\
            ['Seoul', 'Singapore', 'Tokyo', 'San Francisco']]))

    print(m.shortest_path("Singapore","Seoul") == 4669)
    print(m.shortest_path("San Francisco","Seoul") == 6288)
    print(m.shortest_path("Seoul","San Francisco") == 6288)

test3()
