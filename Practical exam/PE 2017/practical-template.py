import csv
import datetime

##############
# Question 1 #
##############

def parse_keylog(log):
    # Your answer here
    ret = ""
    for char in log:
        if(ret and char == "3"):
            ret = ret[:-1]
        else:
            ret += char
        
    return ret

def test1a():
    print('Q1a')
    print(parse_keylog("coolbeans"))
    print(parse_keylog("p@sst3wiq33Ore3d"))
    print(parse_keylog("33do3o3o3o3ont"))

test1a()

###################
# Q1b - Real deal #
###################

def parse_keylog(log):
    # Your answer here
    idx = 0
    ret = []
    for char in log:
        print(ret, "idx: ", idx)
        if(idx > 0 and ret and char == "1"):
            idx -= 1
        elif(idx < len(ret) and char == "2"):
            idx += 1
        elif(ret and char == "3"):
            ret.pop(idx-1)
            idx -= 1
        else:
            ret.insert(idx, char)
            idx += 1

    ret_str = ""
    for char in ret:
        ret_str += char

    return ret_str
            

def test1b():
    print('Q1b')
    print(parse_keylog("ac1b"))
    print(parse_keylog("ac1b2de12f"))
    print(parse_keylog("ac1b2r3de1t32f"))
test1b()

######################
# Q2 - Twitter Mania #
######################
# These functions are provided for you
# Do not make any changes to them

def read_csv(filename):  # provided
    with open(filename, 'r') as f:
        lines = csv.reader(f, delimiter=',')
        return tuple(lines)

def make_datetime(string): # provided
    string = string.split(' ')
    date_str = string[0].split('/')
    time_str = string[1].split(':')
    date_int = [int(x) for x in date_str]
    time_int = [int(x) for x in time_str]
    return datetime.datetime(date_int[2],date_int[1],date_int[0],time_int[0],time_int[1])
    
#######
# Q2A #
#######

def read_csv(filename):  # provided
    with open(filename, 'r') as f:
        lines = csv.reader(f, delimiter=',')
        return tuple(lines)

def make_datetime(string): # provided
    string = string.split(' ')
    date_str = string[0].split('/')
    time_str = string[1].split(':')
    date_int = [int(x) for x in date_str]
    time_int = [int(x) for x in time_str]
    return datetime.datetime(date_int[2],date_int[1],date_int[0],time_int[0],time_int[1])

def parse_data(filename):
    # Your answer here
    data = read_csv(filename)
    ret = []
    for item in data:
        lst = [int(item[0]), item[1], make_datetime(item[2]), list(map(lambda x: int(x), item[3:]))]
        ret.append(lst)
    return ret


## Tests ##
def test2a():
    parsed_data = parse_data('htags.csv')
    print('=== Q2A ===')
    ele0 = [8361, '#Tehran', datetime.datetime(2009, 6, 11, 21, 54),\
        [13, 11, 11, 10, 9, 9, 9, 8, 8, 8, 9, 11, 12, 15, 17, 19,\
        21, 24, 26, 28, 28, 28, 28, 30, 37, 43, 49, 58, 73, 90, 113,\
        129, 133, 137, 145, 153, 161, 171, 174, 180, 195, 207, 211,\
        211, 206, 193, 180, 166, 146, 125, 110, 99, 89, 84, 84, 86,\
        87, 89, 91, 88, 85, 85, 81, 79, 76, 73, 69, 65, 63, 60, 58,\
        54, 49, 45, 40, 36, 32, 29, 26, 23, 22, 21, 22, 24, 25, 26,\
        28, 30, 32, 35, 37, 36, 35, 34, 34, 33, 32, 30, 29, 27, 26,\
        24, 22, 20, 18, 16, 15, 15, 15, 15, 14, 13, 13, 14, 13, 12,\
        10, 9, 8, 7, 7, 6, 6, 7, 8, 10, 11, 14]]
    print(ele0 == parsed_data[0])
    ele1 = [20340, '#fact', datetime.datetime(2009, 6, 12, 7, 25),\
        [4, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 3, 3,\
        3, 3, 3, 3, 3, 3, 2, 3, 11, 20, 31, 51, 94, 164, 254,\
        373, 497, 643, 812, 1001, 1173, 1298, 1399, 1445, 1452,\
        1422, 1394, 1369, 1350, 1332, 1253, 1117, 946, 791, 645,\
        527, 438, 367, 330, 326, 354, 393, 441, 495, 556, 616,\
        662, 698, 712, 715, 719, 722, 722, 717, 711, 691, 662,\
        620, 573, 545, 524, 506, 491, 489, 491, 510, 557, 606,\
        656, 720, 793, 856, 917, 970, 992, 989, 970, 932, 876,\
        813, 744, 664, 607, 570, 549, 552, 559, 586, 615, 666,\
        717, 758, 805, 828, 868, 879, 887, 882, 831, 781, 724,\
        686, 632, 595, 546, 466, 411, 372, 358, 349]]
    print(ele1 == parsed_data[1])

test2a()

#######
# Q2B #
#######

def get_approx_date(filename,event_hashtag):
    # Your answer here
    data = parse_data(filename)
    for item in data:
        if(item[1] == event_hashtag):
            return item[2].date()
    return None

## Tests ##
def test2b():
    print('=== Q2B ===')
    print(get_approx_date('htags.csv','#Haiti')==datetime.date(2009,6,11)) # Haiti earthquake
    print(get_approx_date('htags.csv','#coup')==datetime.date(2009,6,14)) # Hondurus coup d'état
    print(get_approx_date('htags.csv','#Jackson')==datetime.date(2009,6,25)) # Tribute to Michael Jackson

test2b()

#######
# Q2C #
#######
def peak_time(filename,event_hashtag):
    # Your answer here
    data = parse_data(filename)
    for id, tag, date, posts in data:
        if(tag == event_hashtag):
            hrs = 1
            max = 0
            max_hrs = 0
            for post in posts:
                if(post > max):
                    max = post
                    max_hrs = hrs
                hrs += 1
            return date + datetime.timedelta(hours=max_hrs)

    return None

## Tests ##
def test2c():
    print('=== Q2C ===')
    print(peak_time('htags.csv','#GoogleWave'))
    print(peak_time('htags.csv','#IranElections'))

test2c()

#######
# Q2D #
#######
def trending_hashtags(filename,k):
    # Your answer here
    data = parse_data(filename)
    data.sort(key=lambda x: x[1])
    data.sort(reverse=True, key=lambda x: sum(x[3]))
    last = sum(data[k-1][3])
    while k < len(data) and sum(data[k][3]) == last:
        k += 1
    return [x[1] for x in data[:k]]
    

## Tests ##
def test2d():
    print('=== Q2D ===')
    print(trending_hashtags('htags.csv',3))
    print(trending_hashtags('htags.csv',5))

test2d()


###################
# Q3 - Mastermind #
###################

class Mastermind(): 
    # Your answer here
    def __init__(self, colors, answer):
        self.colors = set(colors)
        self.answer = answer
        self.guesses = set()
        self.solved = False
    
    def length(self):
        return len(self.colors)
    
    def guesses(self):
        return len(self.guesses)
    
    def generate_solutions(self,colours, n):
        ans = [()]
        for i in range(n):
            new_list = []
            for a in ans:
                for c in colours:
                    new_list.append(tuple(a) +(c,))
            ans = new_list
        for item in ans:
            self.guesses.add(item)
    
    def pegs(self, guess):

    def try_solution(self, *args):
        if(self.solved):
            return "Already solved!"
        if(len(args) > len(self.answer)):
            return "Wrong number of pegs"
        for color in args:
            if(color not in self.colors):
                return "Invalid colour"
        if(args in self.guesses):
            return "Tried before!"
        if(args == self.answer):
            self.solved = True
            return "Solution found!"


def test3():
    m = Mastermind(("red","blue"), ("red","red","blue"))
    print(m.remaining_possibilities()==8)
    print(m.try_solution("red","blue","green")=="Invalid colour")
    print(m.try_solution("red","blue","blue","red")=="Wrong number of pegs")
    print(m.remaining_possibilities()==8)
    print(m.try_solution("red","blue","blue")==[2,0])
    print(m.remaining_possibilities()==3)
    print(m.try_solution("red","blue","red")==[1,2])
    print(m.remaining_possibilities()==1)
    print(m.try_solution("red","red","blue")=="Solution found!")
    print(m.try_solution("red","red","blue")=="Already solved!")

    m = Mastermind(("red","blue","green"), ("red","red","blue"))
    print(m.remaining_possibilities()==27)
    print(m.try_solution("red","blue","green")==[1,1])
    print(m.remaining_possibilities()==6)
    print(m.try_solution("red","blue","green")=="Tried before!")
    print(m.remaining_possibilities()==6)
    print(m.try_solution("green","red","blue")==[2,0])
    print(m.remaining_possibilities()==3)
    print(m.try_solution("red","blue","red")==[1,2])
    print(m.remaining_possibilities()==1)
    print(m.try_solution("red","red","blue")=="Solution found!")

    m = Mastermind(("red","blue","green","white"), ("red","white","blue"))
    print(m.remaining_possibilities()==64)
    print(m.try_solution("red","blue","green")==[1,1])
    print(m.remaining_possibilities()==12)
    print(m.try_solution("green","red","green")==[0,1])
    print(m.remaining_possibilities()==3)
    print(m.try_solution("white","blue","red")==[0,3])
    print(m.remaining_possibilities()==1)
    print(m.try_solution("red","white","blue")=="Solution found!")
    
#test3()
