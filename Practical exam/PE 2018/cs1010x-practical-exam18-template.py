import csv
from math import sqrt

##############
# Question 1 #
##############


###################
# Q1a - In circle #
###################

def digit_product(n):
    ret = 1
    while n != 0:
        digit = n % 10
        ret *= digit
        n //= 10
    return ret

def test1a():
    print('=== Q1a ===')
    print(digit_product(1111)==1)
    print(digit_product(123)==6)
    print(digit_product(123041)==0)

test1a()



########################
# Q1b - Furthest Apart #
########################

def max_digit_product(n,k):
    digits = str(n)
    ret = 1
    front_idx = 0
    end_idx = 0
    while end_idx < k:
        ret *= int(digits[end_idx])
        end_idx += 1
    
    max = 0
    while end_idx < len(digits):
        ret = ret / int(digits[front_idx]) * int(digits[end_idx])
        if ret > max:
            max = ret
        front_idx += 1
        end_idx += 1
    
    return max



def test1b():
    print('=== Q1b ===')
    print(max_digit_product(11123,1)==3)
    print(max_digit_product(11123,2)==6)
    print(max_digit_product(1111111,5)==1)
    print(max_digit_product(189113451,2)==72)

test1b()


###########################
# Q2 - Show me the Money! #
###########################
# These functions are provided for you
# Do not make any changes to them

def read_csv(filename):  # provided
    with open(filename, 'r') as f:
        lines = csv.reader(f, delimiter=',')
        return tuple(lines)
def count_NA_employment(data):
    return len(list(filter(lambda x: x[4] == "NA", data)))
def count_NA_salary(data):
    return len(list(filter(lambda x: x[5] == "NA", data)))

#######
# Q2A #
#######

def parse_data(filename):
    data = read_csv(filename)
    ret = []
    idx = 1
    while idx < len(data) - 1:
        yr, uni, sch, deg, type, val = data[idx]
        yr1, uni1, sch1, deg1, type1, val1 = data[idx+1]
        if(deg == deg1):
            ret.append([int(yr), uni, sch, deg, float(val), float(val1)])
            idx += 2
        else:
            if(type == "employment_rate_overall"):
                ret.append([int(yr), uni, sch, deg, float(val), "NA"])
            else:
                ret.append([int(yr), uni, sch, deg, "NA", float(val)])
            idx += 1
    
    return ret




def count_NA_employment(data):   # Helper for testing
    return len(list(filter(lambda x: x[4] == "NA", data)))
def count_NA_salary(data):       # Helper for testing
    return len(list(filter(lambda x: x[5] == "NA", data)))

def test2a():
    print('=== Q2a ===')
    print(len(parse_data("employment.csv"))==179)
    print(count_NA_employment(parse_data("employment.csv"))==1)
    print(count_NA_salary(parse_data("employment.csv"))==1)

test2a()

#######
# Q2B #
#######

def compute_employment_rate(filename,university,degree,start,end):
    data = parse_data(filename)
    filtered = filter(lambda l: l[0] >= start and l[0] <= end and l[1] == university and l[3] == degree, data)
    total = 0
    cnt = 0
    for item in filtered:
        if(item[4] != "NA"):
            total += item[4]
            cnt += 1
    if(cnt == 0):
        return "NA"
    return total / cnt

def test2b():
    print('=== Q2b ===')
    print(compute_employment_rate("employment.csv",'National University of Singapore', \
        "Bachelor of Medicine and Bachelor of Surgery",2000,2018)==100.0)
    print(compute_employment_rate("employment.csv",'Nanyang Technological University', \
        "Bachelor of Medicine and Bachelor of Surgery",2000,2018)=="NA")
    print(compute_employment_rate("employment.csv",'National University of Singapore', \
        "Bachelor of Medicine and Bachelor of Surgery",2014,2014)=="NA")
    print(compute_employment_rate("employment.csv",'National University of Singapore', \
        "Bachelor of Computing (Computer Science)",2014,2018)==93.8)

test2b()

#######
# Q2C #
#######

def top_k_degree(filename,start,end,k):
    data = parse_data(filename)
    filtered = list(filter(lambda l: l[0] >= start and l[0] <= end and l[4] != "NA" and l[5] != "NA", data))
    filtered.sort(key=lambda x: x[0])
    filtered.sort(key=lambda x: x[3])
    
    idx = 0
    ret = []
    prev_pay = 0
    while idx < len(filtered):
        yr, uni, sch, course, emp, pay = filtered[idx]
        prev_pay = pay
        valid = True
        total_pay = 0
        cnt = 0
        while idx < len(filtered) - 1 and course == filtered[idx + 1][3]:
            if(filtered[idx + 1][5] <= prev_pay):
                valid = False
            idx += 1
            total_pay += filtered[idx][5]
            cnt += 1
        if(valid and cnt == end - start):
            ret.append([course, uni, total_pay])
        idx += 1
    ret.sort(key=lambda x: x[2], reverse=True)

    return list(map(lambda x: [x[0], x[1]], ret[:k]))




def test2c():
    print('=== Q2c ===')
    print(top_k_degree("employment.csv",2014,2015,3))
    print(top_k_degree("employment.csv",2014,2015,3)==\
          [['Business and Computing', 'Nanyang Technological University'],\
           ['Bachelor of Engineering (Computer Engineering)', 'National University of Singapore'], \
           ['Bachelor of Business Administration (Hons)', 'National University of Singapore']])
    print(top_k_degree("employment.csv",2014,2018,3)==[])
    print(top_k_degree("employment.csv",2014,2018,3))

test2c()

################################
# Q3 - Social Network Security #
################################

privacy_settings = ["private", "friends", "FOF", "public"]
# private = no one can read
# friends = friends can read
# FOF = friends of friends can read
# public = anyone can read

class User:
    def __init__(self, name):
        self.name = name
        self.pending_request = set()
        self.pending_accept = set()
        self.friends = set()
        self.last_setting = "public"
        self.posts = []

    def __repr__(self):
        return self.name
    
    def request(self, user):
        if(user in self.pending_request):
            return False
        else:
            if(self in user.pending_request):
                self.friends.add(user)
                user.friends.add(self)
                user.pending_request.remove(self)
            else:
                user.pending_accept.add(self)
                self.pending_request.add(user)
            return True
    
    def accept(self, user):
        if(user in self.pending_accept):
            self.pending_accept.remove(user)
            user.pending_request.remove(self)
            self.friends.add(user)
            user.friends.add(self)
            return True
        return False
                
    def is_friend(self, user):
        return user in self.friends

    def unfriend(self, user):
        if(user in self.friends):
            self.friends.remove(user)
            user.friends.remove(self)
            return True
        return False

    def post(self, message, privacy=None):
        if(not privacy):
            self.posts.append((self.last_setting, message))
        else:
            self.last_setting = privacy
            self.posts.append((privacy, message))
    
    def read_posts(self, user):
        if(user == self):
            return [item[1] for item in self.posts]
        
        permission = set()
        permission.add("public")
        if(self in user.friends):
            permission.add("friends")
            permission.add("FOF")
        else:
            for friend in self.friends:
                if(user in friend.friends):
                    permission.add("FOF")
                    break
        
        ret = []
        for post in user.posts:
            if(post[0] in permission):
                ret.append(post[1])
        
        return ret


    def update_privacy(self, message, privacy):
        for i in range(len(self.posts)-1, -1, -1):
            if(self.posts[i][1] == message):
                if(self.posts[i][0] != privacy):
                    self.posts[i] = (privacy, self.posts[i][1])
                    return
                else:
                    continue
        return "Message not found"







def test3():
    print('=== Q3 ===')
    ben = User("Ben")
    oana = User("Oana")
    chenhao = User("Chenhao")
    clement = User("Clement")

    print(" ###### BLK 1 ########")
    print(ben.is_friend(oana)==False)
    print(ben.is_friend(chenhao)==False)
    print(ben.accept(oana)==False)

    print(" ###### BLK 2 ########")
    print(oana.request(ben)==True)
    print(oana.request(chenhao)==True)
    print(oana.request(chenhao)==False)
    print(oana.is_friend(ben)==False)
    print(oana.is_friend(chenhao)==False)

    print(" ###### BLK 3 ########")
    print(ben.accept(oana)==True)
    print(chenhao.request(oana)==True)
    print(oana.is_friend(ben)==True)
    print(oana.is_friend(chenhao)==True)
    
    ben.post("CS1010X is fun")
    ben.post("No tutorials next week","FOF")
    ben.post("Did you remember to order pizza?","friends")
    ben.post("Exam grading will be done on Tuesday.")
    ben.post("Finals will be very difficult","private")

    print(" ###### BLK 4 ########")
    print(ben.read_posts(ben) == ['CS1010X is fun', 'No tutorials next week', 'Did you remember to order pizza?', 'Exam grading will be done on Tuesday.', 'Finals will be very difficult'])
    print(oana.read_posts(ben) == ['CS1010X is fun', 'No tutorials next week', 'Did you remember to order pizza?', 'Exam grading will be done on Tuesday.'])
    print(chenhao.read_posts(ben) == ['CS1010X is fun', 'No tutorials next week'])
    print(clement.read_posts(ben) == ['CS1010X is fun'])

    print(" ###### BLK 5 ########")
    ben.post("Finals will be very difficult")
    ben.update_privacy("Finals will be very difficult","public")
    print(ben.read_posts(ben) == ['CS1010X is fun', 'No tutorials next week', 'Did you remember to order pizza?', 'Exam grading will be done on Tuesday.', 'Finals will be very difficult', 'Finals will be very difficult'])
    print(oana.read_posts(ben) == ['CS1010X is fun', 'No tutorials next week', 'Did you remember to order pizza?', 'Exam grading will be done on Tuesday.', 'Finals will be very difficult'])
    print(chenhao.read_posts(ben) == ['CS1010X is fun', 'No tutorials next week', 'Finals will be very difficult'])
    print(clement.read_posts(ben) == ['CS1010X is fun', 'Finals will be very difficult'])

    print(" ###### BLK 6 ########")
    ben.update_privacy("Finals will be very difficult","friends")
    print(ben.read_posts(ben)==['CS1010X is fun', 'No tutorials next week', 'Did you remember to order pizza?', 'Exam grading will be done on Tuesday.', 'Finals will be very difficult', 'Finals will be very difficult'])
    print(oana.read_posts(ben)== ['CS1010X is fun', 'No tutorials next week', 'Did you remember to order pizza?', 'Exam grading will be done on Tuesday.', 'Finals will be very difficult'])
    print(chenhao.read_posts(ben)==['CS1010X is fun', 'No tutorials next week'])
    print(clement.read_posts(ben) == ['CS1010X is fun'])

    print(" ###### BLK 7 ########")
    ben.update_privacy("Finals will be very difficult","friends")
    print(oana.read_posts(ben)==['CS1010X is fun', 'No tutorials next week', 'Did you remember to order pizza?', 'Exam grading will be done on Tuesday.', 'Finals will be very difficult', 'Finals will be very difficult'])
    print(chenhao.read_posts(ben)==['CS1010X is fun', 'No tutorials next week'])
    print(clement.read_posts(ben)==['CS1010X is fun'])

    print(" ###### BLK 8 ########")
    print(oana.unfriend(chenhao)==True)
    print(oana.unfriend(chenhao)==False)
    print(oana.is_friend(chenhao)==False)

    print(" ###### BLK 9 ########")
    print(oana.read_posts(ben)==['CS1010X is fun', 'No tutorials next week', 'Did you remember to order pizza?', 'Exam grading will be done on Tuesday.', 'Finals will be very difficult', 'Finals will be very difficult'])
    print(chenhao.friends)

    print(chenhao.read_posts(ben)==['CS1010X is fun'])
    print(clement.read_posts(ben)==['CS1010X is fun'])

test3()
