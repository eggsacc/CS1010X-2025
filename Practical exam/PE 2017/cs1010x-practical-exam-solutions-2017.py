import csv
import datetime

##############
# Question 1 #
##############

#################
# Q1a - Warm Up #
#################

def parse_keylog(log):
    ans = ""
    for c in log:
        if c != "3":
            ans += c
        else:
            ans = ans[:-1]
    return ans

def test1a():
    print('=== Q1a ===')
    print(parse_keylog("coolbeans")=="coolbeans")
    print(parse_keylog("p@sst3wiq33Ore3d")=="p@sswOrd")
    print(parse_keylog("33do3o3o3o3ont")=="dont")

def test1a_e():
    print('=== Q1a ===')
    print(parse_keylog("3t33ta3r@n5f3o335f0r3rme3ers5335") == "tr@n5f0rmer5")
    print(parse_keylog("@3ag03033039o0d330dd434@3y") == "a9o0dd4y")
    print(parse_keylog("35335umar33e3me3er") == "5ummer")
    print(parse_keylog("") == "")
    print(parse_keylog("3") == "")
    print(parse_keylog("3333") == "")
    print(parse_keylog("a3b3c3d3") == "")
    print(parse_keylog("aa3b3c3d3") == "a")
    
#test1a()
#test1a_e()

###################
# Q1b - Read deal #
###################

def parse_keylog(log):
    left = ""
    right = ""
    for c in log:
        if c == "1":
            if left != "":
                right = left[-1]+right
                left = left[:-1]
        elif c == "2":
            if right != "":
                left += right[0]
                right = right[1:]
        elif c == "3":
            left = left[:-1]
        else:
            left += c
    return left+right

def test1b():
    print('=== Q1b ===')
    print(parse_keylog("ac1b")=="abc")
    print(parse_keylog("ac1b2de12f")=="abcdef")
    print(parse_keylog("ac1b2r3de1t32f")=="abcdef")

def test1b_e():
    print('=== Q1b ===')
    print(parse_keylog("3a12bc132eg") == "aceg")
    print(parse_keylog("e3a1b3c1e223azy13x1z232x")== "ecazyx")
    print(parse_keylog("3b231ac1b1d322gf13de") == "abcdef")
    print(parse_keylog("") == "")
    print(parse_keylog("1") == "")
    print(parse_keylog("2") == "")
    print(parse_keylog("3") == "")
    print(parse_keylog("1111") == "")
    print(parse_keylog("2222") == "")
    print(parse_keylog("3333") == "")
    print(parse_keylog("1231233321") == "")
    
#test1b()
#test1b_e()


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

def parse_data(filename):
    data = read_csv(filename)
    ans = []
    for line in data:
        ans.append([int(line[0]), line[1], make_datetime(line[2]), list(map(lambda x: int(x),line[3:]))])
    return ans
    
## Tests ##
def test2a():
    print('=== Q2a ===')
    parsed_data = parse_data('htags.csv')
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

def test2a_e():
    print('=== Q2a ===')
    parsed_data = parse_data('htags.csv')
    full_data = parse_data('htags_full.csv')
    empty_data = parse_data('empty.csv')

    ans1 = [9797, '#tehran', datetime.datetime(2009, 6, 11, 22, 49),\
            [22, 22, 21, 20, 18, 16, 15, 15, 16, 19, 21, 23, 26, 31,\
            36, 41, 42, 41, 41, 39, 37, 35, 34, 34, 37, 41, 46, 52,\
            62, 73, 85, 92, 101, 110, 118, 131, 139, 146, 154, 166,\
            172, 172, 173, 165, 153, 141, 133, 124, 116, 114, 114,\
            115, 118, 125, 125, 125, 124, 120, 114, 107, 102, 96,\
            92, 87, 83, 79, 75, 73, 70, 66, 62, 58, 53, 48, 44,\
            42, 40, 39, 37, 35, 35, 37, 40, 43, 45, 49, 52, 58,\
            63, 69, 70, 67, 64, 59, 56, 51, 48, 44, 40, 38, 36,\
            36, 32, 29, 28, 27, 26, 26, 26, 23, 23, 25, 24, 23,\
            22, 19, 17, 16, 16, 12, 11, 13, 14, 17, 22, 28, 35, 44]] 
    print(ans1 == parsed_data[17])
    ans2 = [76547, '#MJ', datetime.datetime(2009, 6, 15, 4, 39),\
            [14, 14, 14, 14, 13, 13, 13, 13, 14, 15, 15, 16, 18,\
            19, 20, 21, 21, 21, 22, 22, 21, 21, 21, 21, 22, 23,\
            23, 24, 25, 25, 26, 27, 27, 27, 29, 35, 41, 50, 62,\
            72, 83, 95, 105, 105, 100, 93, 80, 70, 63, 57, 47,\
            39, 34, 30, 31, 33, 35, 36, 35, 34, 31, 29, 27, 24,\
            20, 17, 14, 13, 12, 11, 11, 10, 11, 11, 11, 11, 11,\
            12, 13, 15, 14, 14, 14, 13, 13, 11, 11, 9, 8, 8, 7,\
            7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6, 5, 4, 4, 3, 2, 2,\
            2, 2, 2, 2, 2, 2, 2, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4,\
            4, 5, 4]]
    print(ans2 == parsed_data[121])
    ans3 = [75789, '#marvel', datetime.datetime(2009, 6, 15, 3, 21),\
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0,\
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 4, 5, 7,\
            10, 13, 17, 19, 20, 19, 17, 16, 14, 13, 12, 11, 10, 10,\
            9, 9, 9, 9, 9, 9, 8, 8, 8, 8, 8, 8, 8, 7, 6, 5, 5, 4,\
            3, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3,\
            3, 3, 3, 3, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1,\
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0,\
            1, 1, 1, 1, 1, 1, 1]]
    print(ans3 == parsed_data[361])
    ans4 = [162801, '#Rajavi', datetime.datetime(2009, 6, 21, 11, 45),\
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,\
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2,\
            2, 3, 4, 5, 5, 4, 4, 3, 3, 3, 2, 2, 1, 1, 1, 1, 2, 2, 2,\
            3, 3, 3, 3, 3, 2, 2, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1,\
            1, 1, 1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,\
            0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,\
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    print(ans4 == full_data[936])
    ans5 = [22960, '#Liverpool', datetime.datetime(2009, 6, 12, 9, 53),\
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,\
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 2, 3, 5, 7, 10, 12,\
            16, 19, 24, 27, 28, 26, 22, 19, 15, 12, 9, 6, 4, 2, 1, 1,\
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,\
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0,\
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,\
            0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    print(ans5 == full_data[941])
    ans6 = [22249, '#Madonna', datetime.datetime(2009, 6, 12, 9, 14),\
            [0, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1,\
            0, 1, 1, 1, 1, 1, 1, 1, 2, 5, 7, 11, 14, 19, 26, 33, 44,\
            49, 50, 51, 52, 53, 52, 55, 52, 46, 38, 31, 24, 19, 16,\
            13, 9, 7, 5, 4, 4, 4, 4, 5, 5, 6, 7, 8, 9, 10, 12, 10,\
            10, 9, 9, 8, 7, 6, 4, 3, 3, 3, 2, 2, 2, 3, 3, 2, 2, 2,\
            3, 3, 3, 3, 4, 4, 5, 5, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1,\
            1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 4, 5, 6, 7, 9, 11, 9, 8, 7,\
            5, 4, 3, 3, 1]]
    print(ans6 == full_data[976])
    ans7 = []
    print(ans7 == empty_data)
    

#test2a()
#test2a_e()

#######
# Q2B #
#######

def get_approx_date(filename,event_hashtag):
    data = parse_data(filename)
    for id, tag, date, time_series in data:
        if event_hashtag == tag:
            return date.date()
    return None

## Tests ##
def test2b():
    print('=== Q2b ===')
    print(get_approx_date('htags.csv','#Haiti')==datetime.date(2009,6,11)) # Haiti earthquake
    print(get_approx_date('htags.csv','#coup')==datetime.date(2009,6,14)) # Hondurus coup d'état
    print(get_approx_date('htags.csv','#Jackson')==datetime.date(2009,6,25)) # Tribute to Michael Jackson

def test2b_e():
    print('=== Q2b ===')
    print(get_approx_date('htags.csv', '#iranelection') == datetime.date(2009,6,12))
    print(get_approx_date('htags.csv', '#ComicCon') == datetime.date(2009,6,12))
    print(get_approx_date('htags.csv', '#newmoon') == datetime.date(2009,6,11))
    print(get_approx_date('htags_full.csv', '') == None)
    print(get_approx_date('htags_full.csv', '#TomTom') == datetime.date(2009,6,12))
    print(get_approx_date('htags_full.csv', '#SMS') == datetime.date(2009,6,11))
    print(get_approx_date('htags_full.csv', '#Eminem') == None)
    print(get_approx_date('empty.csv', '#Rihanna') == None)

#test2b()
#test2b_e()

#######
# Q2C #
#######
def peak_time(filename,event_hashtag):
    data = parse_data(filename)
    for id, tag, date, time_series in data:
        if event_hashtag == tag:
            maximum = max(time_series) 
            for i in range(1,len(time_series)):
                if time_series[i] == maximum:
                    return date + datetime.timedelta(hours = i+1)
    return None

## Tests ##
def test2c():
    print('=== Q2c ===')
    print(peak_time('htags.csv','#GoogleWave')==datetime.datetime(2009,6,13,17,58))
    print(peak_time('htags.csv','#IranElections')==datetime.datetime(2009,6,14,2,8))

def test2c_e():
    print('=== Q2c ===')
    print(peak_time('htags.csv','#Venezuela') == datetime.datetime(2009,6,14,23,38))
    print(peak_time('htags.csv','#USA') == datetime.datetime(2009,6,13,19,13))
    print(peak_time('htags.csv','#americanidol') == datetime.datetime(2009,6,13,20,13))
    print(peak_time('htags_full.csv','') == None)
    print(peak_time('htags_full.csv','#worldcup') == datetime.datetime(2009,6,13,14,0))
    print(peak_time('htags_full.csv','#usmc') == datetime.datetime(2009,6,14,14,56))
    print(peak_time('htags_full.csv','#Lawson') == None)
    print(peak_time('empty.csv','') == None)


#test2c()
#test2c_e()

#######
# Q2D #
#######
def trending_hashtags(filename,k):
    data = parse_data(filename)
    tag_count = {}
    for id, tag, date, time_series in data:
        if tag not in tag_count:
            tag_count[tag] = 0
        tag_count[tag] += sum(time_series)
    a = list(tag_count.items())
    a.sort(key = lambda x: x[0])
    a.sort(key = lambda x: x[1],reverse=True)
    if len(a) <= k:
        return list(map(lambda x: x[0], a))
    else:
        if k == 0:
            return []
        k_threshold = a[k-1][1]
        return [x[0] for x in a if x[1] >= k_threshold] # map and filter in one go! \m/

## Tests ##
def test2d():
    print('=== Q2d ===')
    print(trending_hashtags('htags.csv',3)==['#fact', '#rememberwhen', '#shoutout'])
    print(trending_hashtags('htags.csv',5)==['#fact', '#rememberwhen', '#shoutout', '#Haiti', '#red'])

def test2d_e():
    print('=== Q2d ===')
    print(trending_hashtags('htags.csv',9) == ['#fact', '#rememberwhen', '#shoutout', '#Haiti', '#red', '#IranElection', '#moonfruit', '#lolquiz', '#JonasOnUstream'])
    print(trending_hashtags('htags.csv',10) == ['#fact', '#rememberwhen', '#shoutout', '#Haiti', '#red', '#IranElection', '#moonfruit', '#lolquiz', '#JonasOnUstream', '#gr88'])
    print(trending_hashtags('htags.csv',15) == ['#fact', '#rememberwhen', '#shoutout', '#Haiti', '#red', '#IranElection', '#moonfruit', '#lolquiz', '#JonasOnUstream', '#gr88', '#bestsex', '#whateverhappenedto', '#iwish', '#iloveitwhen', '#googlewave'])
    print(trending_hashtags('htags_full.csv',0) == [])  
    print(trending_hashtags('htags_full.csv',33) == ['#fact', '#rememberwhen', '#shoutout', '#Haiti', '#red', '#IranElection', '#moonfruit', '#lolquiz', '#JonasOnUstream', '#gr88', '#bestsex', '#whateverhappenedto', '#iwish', '#iloveitwhen', '#googlewave', '#Iranelection', '#haveuever', '#why', '#dontyouhate', '#jtv', '#forasarney', '#davidarchuleta', '#iadmit', '#wave', '#GiladShalit', '#youtubefail', '#iremember', '#DMV', '#bb11', '#thoughtsduringsex', '#petpeeve', '#ihatewhen', '#bbcqt'])
    print(trending_hashtags('htags_full.csv',100) == ['#fact', '#rememberwhen', '#shoutout', '#Haiti', '#red', '#IranElection', '#moonfruit', '#lolquiz', '#JonasOnUstream', '#gr88', '#bestsex', '#whateverhappenedto', '#iwish', '#iloveitwhen', '#googlewave', '#Iranelection', '#haveuever', '#why', '#dontyouhate', '#jtv', '#forasarney', '#davidarchuleta', '#iadmit', '#wave', '#GiladShalit', '#youtubefail', '#iremember', '#DMV', '#bb11', '#thoughtsduringsex', '#petpeeve', '#ihatewhen', '#bbcqt', '#90s', '#goodtimes', '#squarespace', '#turnon', '#neda', '#imtiredof', '#2010', '#backintheday', '#Pakistan', '#DavidArchuleta', '#Neda', '#thingsilove', '#tehran', '#michaeljackson', '#sdcc', '#redsox', '#helpiranelection', '#paramore', '#lies', '#whatif', '#Tehran', '#btw09', '#bestadvice', '#ashes', '#apple', '#LIVESTRONG', '#marsiscoming', '#olympics', '#uksnow', '#nothingpersonal', '#NOH8', '#turnoff', '#Bones', '#mileycyrus', '#Supernatural', '#truth', '#craigferguson', '#pawpawty', '#Fact', '#911', '#watch', '#duringsex', '#imsinglebecause', '#india', '#Honduras', '#haveyouever', '#Venezuela', '#Gaza', '#newmoon', '#140tc', '#translation', '#nn09', '#warriors', '#supernatural', '#niley', '#Apple', '#Amazon', '#inaperfectworld', '#Olympics', '#912', '#nocleanfeed', '#cop15', '#cool', '#zensursula', '#GoogleWave', '#moo', '#defcon'])
    print(trending_hashtags('empty.csv',66) == [])
    print(trending_hashtags('htags_equal.csv',2)  == ['#fact', '#America', '#Tehran', '#Thailand'])

#test2d()
#test2d_e()

###################
# Q3 - Mastermind #
###################

class Mastermind():

    def __init__(self, colours, solution):
        self.colours = tuple(colours)
        self.solution = tuple(solution)
        self.tries = []
        self.solved = False
        self.combinations_left = self.generate_solutions(colours,len(solution))

    def length(self):
        return len(self.solution)

    def guesses(self):
        return len(self.tries)

    def generate_solutions(self,colours, n): #Helper to generate solutions
        ans = [()]
        for i in range(n):
            new_list = []
            for a in ans:
                for c in colours:
                    new_list.append(tuple(a) +(c,))
            ans = new_list
        return ans
                                                         
    def try_solution(self,*answer):

        for c in answer: # Check colours are correct.
            if c not in self.colours:
                return "Invalid colour"
        
        if self.solved:
            return "Already solved!"
        elif len(answer) != len(self.solution):
            return "Wrong number of pegs"
        elif answer in self.tries:
            return "Tried before!"
        elif answer == self.solution:
            self.tries.append(answer)
            self.solved = True
            return "Solution found!"
        else:
            self.tries.append(answer)
            ans = self.check_solution(self.solution,answer)
                            
            #update possible solutions
            self.combinations_left = list(filter(lambda possible: self.check_solution(possible, answer)== ans,self.combinations_left))
            return ans

    def remaining_possibilities(self):
        return len(self.combinations_left) 

    def check_solution(self, solution, attempt):   # Helper function
        found = [False]*len(attempt)
        used = [False]*len(attempt)

        blacks = 0
        for i in range(len(attempt)): # Check for blacks
            if attempt[i] == solution[i]:
                blacks +=1
                found[i] = True
                used[i] = True
            
        whites = 0
        for i in range(len(attempt)):  #Check for whites
            for j in range(len(attempt)):
                if i != j and not found[i] and not used[j] and attempt[i] == solution[j]:
                    whites +=1
                    found[i] = True
                    used[j] = True
                if blacks + whites == len(attempt):
                    break
        return [blacks, whites]

##################
# Marking scheme #
##################
# 1 mark  - getting length() right
# 1 mark  - getting guesses() right
# 5 marks - getting try solutions() right
#    o 1/2 mark  - "Invalid colour"
#    o 1/2 mark  - "Already solved!"
#    o 1/2 mark  - "Wrong number of pegs"
#    o 1/2 mark  - "Tried before!"
#    o 1/2 mark  - "Solution found!"
#    o 5/2 marks - Correct [black,white] => check solution implemented correctly
# 3 marks - getting remaining possibilities() right => Basically filtering using check solutions correctly. 

def test3():
    print('=== Q3 ===')
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


def test3_e():
    print('=== Q3 ===')
    m = Mastermind(("yellow","green","blue","pink"), ("green","pink","yellow"))
    print(m.length() == 3)
    print(m.guesses() == 0)
    print(m.remaining_possibilities() == 64)
    print(m.try_solution("blue","green","green") == [0, 1])
    print(m.guesses() == 1)
    print(m.remaining_possibilities() == 14)
    print(m.try_solution("yellow","pink") == "Wrong number of pegs")
    print(m.remaining_possibilities() == 14)
    print(m.try_solution("blue","green","green") == "Tried before!")
    print(m.remaining_possibilities() == 14)
    print(m.try_solution("white","blue","green") == "Invalid colour")
    print(m.guesses() == 1)
    print(m.remaining_possibilities() == 14)
    print(m.try_solution("green","yellow","pink") == [1, 2])
    print(m.guesses() == 2)
    print(m.remaining_possibilities() == 1)
    print(m.try_solution("green","pink","yellow") == "Solution found!")
    print(m.try_solution("green","pink","yellow") == "Already solved!")

    m = Mastermind(("green","blue","yellow"), ("green","green","blue","yellow"))
    print(m.length() == 4)
    print(m.remaining_possibilities() == 81)
    print(m.try_solution("pink","pink") == "Invalid colour")
    print(m.remaining_possibilities() == 81)
    print(m.try_solution("green","green","yellow") == "Wrong number of pegs")
    print(m.remaining_possibilities() == 81)
    print(m.try_solution("green","green","yellow","blue") == [2, 2])
    print(m.guesses() == 1)
    print(m.remaining_possibilities() == 5)
    print(m.try_solution("green","yellow","blue","green") == [2, 2])
    print(m.remaining_possibilities() == 3)
    print(m.try_solution("green","green","blue","yellow") == "Solution found!")

    m = Mastermind((""), (""))
    print(m.length() == 0)
    print(m.remaining_possibilities() == 1)
    print(m.try_solution("pink","pink") == "Invalid colour")
    print(m.guesses() == 0)

    m = Mastermind((),())
    print(m.length() == 0)
    print(m.remaining_possibilities() == 1)
    print(m.try_solution("pink","blue") == "Invalid colour")
    print(m.guesses() == 0)

    m = Mastermind(("yellow"), ("yellow","green"))
    print(m.remaining_possibilities() == 36)
    print(m.try_solution("pink","blue") == "Invalid colour")
    print(m.remaining_possibilities() == 36)
    print(m.try_solution("green","green") == "Invalid colour")
    print(m.remaining_possibilities() == 36)
    print(m.try_solution("yellow","green","green") == "Invalid colour")
    print(m.remaining_possibilities() == 36)
    print(m.try_solution("yellow","green") == "Invalid colour")
    
#test3()
#test3_e()
