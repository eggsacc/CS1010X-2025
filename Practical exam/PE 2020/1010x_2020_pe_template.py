##########################################
# Question 1a: Alien numbers [ 5 Marks ] #
##########################################

def ET_number(num, mapping):
    ret = ""
    base = len(mapping)
    while num != 0:
        digit = mapping[num % base]
        ret = digit + ret
        num //= base
    return ret

def test1a():
    print("=====Test 1a=====")
    # checking if simple decimal numbers can be produced
    print(ET_number(5, ('0','1','2','3','4','5','6','7','8','9')) == '5')
    # checking for switching some digits
    print(ET_number(20, ('9','8','7','6','5','4','3','2','1','0')) == '79')
    # checking for different bases
    print(ET_number(10, ('0','1','2','3','4','5')) == '14')
    print(ET_number(6, ('0','4')) == '440')
    print(ET_number(5, ('1', '0')) == '010')
    print(ET_number(10, ('a', 'b', 'c')) == 'bab')

test1a()

#################################################
# Question 1b: Largest alien number [ 5 Marks ] #
#################################################

def max_ET_number(ET_numbers, mapping):
    def get_et_val(num):
        base = len(mapping)
        val = 0
        reversed_num = num[::-1]
        for i in range(len(num)):
            val += int(mapping.index(reversed_num[i])) * base ** i
        return val

    max = -9999
    max_et = None
    for num in ET_numbers:
        val = get_et_val(num)
        if(val > max):
            max = val
            max_et = num
    return max_et





def test1b():
    print("=====Test 1b=====")
    # checking for normal decimal
    print(max_ET_number(('1','2','3','4','5'), ('0','1','2','3','4','5','6','7','8','9')) == '5')
    # checking for swapped digits
    print(max_ET_number(('12','34','42','58'), ('0','1','8','3','5','4','6','7','2','9')) == '42')
    print(max_ET_number(('19','20','21','22','23'), ('0','2','1','3','4','5','6','7','8','9')) == '19')
    # different bases
    print(max_ET_number(('14','15'),('0','1','2','3','5','4'))=='14')
    print(max_ET_number(('707','700','770'),('0','7'))=='770')
    print(max_ET_number(('0', '4', '40', '44', '400', '404', '440', '444', '4000', '4004', '4040'),('0','4'))=='4040')
    print(max_ET_number(('317','311','713','413'),('7','1','3','4'))=='413')
    print(max_ET_number(('aba', 'abc', 'ca', 'cb'), ('a', 'b', 'c')) == 'cb')

test1b()

############################
# Question 2: Tesla stocks #
############################

import csv
import datetime

def read_csv(csvfilename):
    """
    Reads a csv file and returns a list of list
    containing rows in the csv file and its entries.
    """
    rows = []

    with open(csvfilename, 'r') as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            rows.append(row)
    return rows

######################################################
# Question 2a: Retrieving tweets by date [ 3 Marks ] #
######################################################
def get_tweet_by_date(date):
    data = read_csv("tweets.csv")[1:]
    date = datetime.datetime.strptime(date, "%m/%d/%Y")
    filtered = tuple(map(lambda x: x[2], filter(lambda x: datetime.datetime.strptime(x[6], "%m/%d/%Y") == date, data)))
    return filtered

def test2a():
    print("=====Test 2a=====")
    print(get_tweet_by_date('12/21/2019') == ('Great show  https://t.co/12rguHHpgz', 'Holiday gift ideas https://t.co/uBBofvkYAI'))
    print(get_tweet_by_date('5/1/2020') == ('Now give people back their FREEDOM', 'I am selling almost all physical possessions. Will own no house.', 'Tesla stock price is too high imo', "And the rocket's red glare, the bombs bursting in air", 'Rage, rage against the dying of the light of consciousness'))
    print(get_tweet_by_date('12/12/2001') == ())
    print(get_tweet_by_date('5/21/2021') == ()) 

test2a()

#############################################################
# Question 2b: Effect of tweets on stock prices [ 3 Marks ] #
#############################################################
def tweet_effect(date):
    date = datetime.datetime.strptime(date, "%m/%d/%Y")
    tweet_data = read_csv("tweets.csv")[1:]
    stock_data = read_csv("TSLA.csv")[1:]
    tweets_on_day = tuple(map(lambda x: x[2], filter(lambda x: datetime.datetime.strptime(x[6], "%m/%d/%Y") == date, tweet_data)))
    date_limit = date + datetime.timedelta(days=5)
    stock_reformatted = map(lambda x: [datetime.datetime.strptime(x[0], "%m/%d/%Y"), float(x[1])], stock_data)
    stock_filtered = list(map(lambda x: x[1], filter(lambda x: x[0] >= date and x[0] <= date_limit, stock_reformatted)))
    
    return (tweets_on_day + (stock_filtered,)) if tweets_on_day and stock_filtered else None

def test2b():
    print("=====Test 2b=====")
    print(tweet_effect('5/8/2013'))
    print(tweet_effect('3/23/2017') == None)
    print(tweet_effect('7/14/2019') == ('To Infinity and Beyond! https://t.co/dgysTBqWfV', [253.5, 252.380005, 254.860001, 253.539993, 258.179993]))

test2b()

##########################################
# Question 2c: Money tweets [ 4 Marks ]  #
##########################################

def money_tweets(start_date, end_date):
    start_date = datetime.datetime.strptime(start_date, "%m/%d/%Y")
    end_date = datetime.datetime.strptime(end_date, "%m/%d/%Y")
    date = start_date
    max_diff = 0
    max_day = None

    while date < end_date:
        
        data = tweet_effect(date.strftime("%m/%d/%Y"))
        if(data == None):
            date += datetime.timedelta(days=1)
            continue
        else:
            stocks = data[-1]
            min_stock = 9999
            max_stock = -9999
            for stock in stocks:
                if(stock < min_stock):
                    min_stock = stock
                if(stock > max_stock):
                    max_stock = stock
            diff = max_stock - min_stock
            if(diff > max_diff):
                max_diff = diff
                max_day = date
            date += datetime.timedelta(days=1)
        
    tweets = get_tweet_by_date(max_day.strftime("%m/%d/%Y"))

    if(tweets):
        return (tweets, max_diff)
    else:
        return None




def test2c():
    print("=====Test 2c=====")
    print(money_tweets('5/12/2020', '5/21/2020'))
    print(money_tweets('4/29/2020', '5/1/2020'))

test2c()

############################################
# Question 3: TOY TRAIN                    #
############################################

class carriage:
    def __init__(self, x, y):
        self.x = x
        self.y= y
        self.attached = None

    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def get_pos(self):
        return (self.x, self.y)
    
    def attach(self, car):
        if(abs(car.x - self.x) <= 1 and abs(car.y - self.y) <= 1):
            self.attached = car
            return "Attached."
        else:
            return "Can't attach."
    

class engine (carriage):
    def __init__(self, x, y):
        super().__init__(x, y)

    def move (self, track):
        moves =  {"u": (0, 1), "d": (0, -1), "r": (1, 0), "l": (-1, 0)}
        def move_car(car, move):
            car.x += move[0]
            car.y += move[1]
            return car.get_pos()
        
        def move_to(car, location):
            car.x = location[0]
            car.y = location[1]

        def get_state(engine):
            state = set()
            car = engine
            while car.attached != None:
                state.add(car.get_pos())
                car = car.attached
            return state
        
        def check_collision(engine, move):
            state = get_state(engine)
            cache = engine.get_pos()
            if(move_car(engine, move) in state):
                move_to(engine, cache)
                return False
            else:
                move_to(engine, cache)
                return True
        
        def move_carriages(engine, move):
            car = engine.attached
            location_cache = engine.get_pos()
            move_car(engine, move)

            while car != None:
                temp = car.get_pos()
                move_to(car, location_cache)
                location_cache = temp
                car = car.attached
        
        for cmd in track:
            valid_move = check_collision(self, moves[cmd])
            if(valid_move):
                move_carriages(self, moves[cmd])
            else:
                return "Collision!"

        return None



        

def test3():
    print("=====Test 3=====")
    c0 = carriage(1,0)
    c1 = carriage(1,1)
    c2 = carriage(1,2)
    c3 = carriage(2,2)
    c4 = carriage(3,4)
    e  = engine(2,3)

    # Checking for get_x and get_y functions
    print("########## 1 #############")
    print(c1.get_x() == 1)
    print(c3.get_y() == 2)
    # Checking for get_pos function
    print("########## 2 #############")
    print(c0.get_pos() == (1,0))

    # Attaching carraiges together to build the train
    print("########## 3 #############")
    print(e.attach(c3) == "Attached.")
    print(c3.attach(c2) == "Attached.")
    print(c2.attach(c1) == "Attached.")

    # c1 and c4 are not adjacent
    print("########## 4 #############")
    print(c1.attach(c4) == "Can't attach.")
    
    print(c1.attach(c0) == "Attached.")

    # Checking for movement
    print("########## 5 #############")
    print((e.get_pos(), c3.get_pos(), c2.get_pos(), c1.get_pos(), c0.get_pos()))
    print(e.move('uuu') == None)
    print((e.get_pos(), c3.get_pos(), c2.get_pos(), c1.get_pos(), c0.get_pos()) )
    print(e.move('r') == None)
    print((e.get_pos(), c3.get_pos(), c2.get_pos(), c1.get_pos(), c0.get_pos()) )
    print(e.move('uuuuuu') == None)
    print((e.get_pos(), c3.get_pos(), c2.get_pos(), c1.get_pos(), c0.get_pos()) )
    print(e.move('rdll'))
    print((e.get_pos(), c3.get_pos(), c2.get_pos(), c1.get_pos(), c0.get_pos()) )
    print(e.move('ldrr'))
    print((e.get_pos(), c3.get_pos(), c2.get_pos(), c1.get_pos(), c0.get_pos()) )
    print(e.move('d') == None)
    print((e.get_pos(), c3.get_pos(), c2.get_pos(), c1.get_pos(), c0.get_pos()) )

test3()