#
# CS1010S --- Programming Methodology
#
# Mission 8 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from ippt import *
import csv

##########
# Task 1 #
##########

# Function read_csv has been given to help you read the csv file.
# The function returns a tuple of tuples containing rows in the csv
# file and its entries.

# Alternatively, you may use your own method.

def read_csv(csvfilename):
    rows = ()
    with open(csvfilename) as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            rows += (tuple(row), )
    return rows

def read_data(filename):
    rows = read_csv(filename)
    "Your Solution Here"
    # row, column = age, reps
    
    # Process reps
    reps = rows[0][1:]
    reps = tuple([int(x) for x in reps])

    # Process age & data
    age = ()
    data = ()
    for row in rows[1:]:
        age += (int(row[0]),)
        data += (tuple([int(x) for x in row[1:]]),)
        
    return create_table(data, age, reps)

pushup_table = read_data("pushup.csv")
situp_table = read_data("situp.csv")
run_table = read_data("run.csv")

ippt_table = make_ippt_table(pushup_table, situp_table, run_table)

print("## Q1 ##")
# Sit-up score of a 24-year-old who did 10 sit-ups.
print(access_cell(situp_table, 24, 10))    # 0

# Push-up score of a 18-year-old who did 30 push-ups.
print(access_cell(pushup_table, 18, 30))   # 16

# Run score of a 30-year old-who ran 12 minutes (720 seconds)
print(access_cell(run_table, 30, 720))     # 36

# Since our run.csv file does not have data for 725 seconds, we should
# get None if we try to access that cell.
print(access_cell(run_table, 30, 725))     # None


##########
# Task 2 #
##########

def pushup_score(pushup_table, age, pushup):
    "Your Solution Here"
    if(pushup >= 60):
        return 25
    if(pushup < 1):
        return 0
    return access_cell(pushup_table, age, pushup)

def situp_score(situp_table, age, situp):
    "Your Solution Here"
    if(situp >= 60):
        return 25
    if(situp < 1):
        return 0
    return access_cell(situp_table, age, situp)

def run_score(run_table, age, run):
    "Your Solution Here"
    if(run >= 1050):
        return 0

    if(run <= 510):
        return 50

    last_digit = run % 10
    rounding_diff = 0 if not last_digit else (10 - last_digit)
    
    return access_cell(run_table, age, run + rounding_diff)
    

print("## Q2 ##")
print(pushup_score(pushup_table, 18, 61))   # 25
print(pushup_score(pushup_table, 18, 70))   # 25
print(situp_score(situp_table, 24, 0))      # 0

print(run_score(run_table, 30, 720))        # 36
print(run_score(run_table, 30, 725))        # 35
print(run_score(run_table, 30, 735))        # 35
print(run_score(run_table, 30, 500))        # 50
print(run_score(run_table, 30, 1300))       # 0


##########
# Task 3 #
##########

def ippt_award(score):
    "Your Solution Here"
    if(score >= 85):
        return "G"
    elif(score >= 75):
        return "S"
    elif(score >= 61):
        return "P$"
    elif(score >= 51):
        return "P"
    else:
        return "F"

print("## Q3 ##")
print(ippt_award(50))     # F
print(ippt_award(51))     # P
print(ippt_award(61))     # P$
print(ippt_award(75))     # S
print(ippt_award(85))     # G


##########
# Task 4 #
##########

def ippt_results(ippt_table, age, pushup, situp, run):
    "Your solution here"
    total_score = run_score(ippt_table[2], age, run) + situp_score(ippt_table[1], age, situp) + pushup_score(ippt_table[0], age, pushup)
    award = ippt_award(total_score)

    return (total_score, award)

print("## Q4 ##")
print(ippt_results(ippt_table, 25, 30, 25, 820))      # (53, 'P')
print(ippt_results(ippt_table, 28, 56, 60, 530))      # (99, 'G')
print(ippt_results(ippt_table, 38, 18, 16, 950))      # (36, 'F')
print(ippt_results(ippt_table, 25, 34, 35, 817))      # (61, 'P$')
print(ippt_results(ippt_table, 60, 70, 65, 450))      # (100, 'G')


##########
# Task 5 #
##########
def make_training_program(rate_pushup, rate_situp, rate_run):
    def training_program(ippt_table, age, pushup, situp, run, days):
        "Your solution here"
        # Calculate improved reps / time
        imp_pushup = days // rate_pushup + pushup
        imp_situp = days // rate_situp + situp
        imp_run = run - days // rate_run

        # Calculate new score
        new_score = ippt_results(ippt_table, age, imp_pushup, imp_situp, imp_run)

        return (imp_pushup, imp_situp, imp_run, new_score)

    return training_program

# print("## Q5 ##")
tp = make_training_program(7, 3, 10)
print(tp(ippt_table, 25, 30, 25, 820, 30))        # (34, 35, 817, (61, 'P$'))


##########
# Bonus  #
##########

def make_tp_bonus(rate_pushup, rate_situp, rate_run):
    def tp_bonus(ippt_table, age, pushup, situp, run, days):
        "Your solution here"
        # Get a list of excercise and rate
        ex_and_rates = [[rate_pushup, 'p'], [rate_situp, 's'], [rate_run, 'r']]
        # Sort the list so to pick out excercise with fasetst growth
        ex_and_rates.sort()

        scores = [pushup, situp, run]
        
        fastest_rate = 0
        days_elapsed = 0
        reps_imp = 0

        # @brief Update the score based on current excercise
        # @retval None
        def update_score(fastest_rate, scores):
            if(ex_and_rates[fastest_rate][1] == 'p'):
                scores[0] += 1
            elif(ex_and_rates[fastest_rate][1] == 's'):
                scores[1] += 1
            else:
                scores[2] += 1

        # @brief Check if the current excercise has already improved to it's limit
        # @retval bool 
        def check_score_limit(fastest_rate, age, scores):
            if(ex_and_rates[fastest_rate][1] == 'p'):
                if(pushup_score(ippt_table[0], age, scores[0]) >= 25):
                    return True
            elif(ex_and_rates[fastest_rate][1] == 's'):
                if(situp_score(ippt_table[1], age, scores[1]) >= 25):
                    return True
            else:
                if(run_score(ippt_table[2], age, scores[2]) >= 50):
                    return True
                
        # While loop: simulate training        
        while(days_elapsed <= days):

            # If current excercise has already attained highest possible score,
            # start training next fastest-growth excercise
            if(check_score_limit(fastest_rate, age, scores)):
                fastest_rate += 1
                
            days_elapsed += ex_and_rates[fastest_rate][0]

            # Only increase score if training rate falls within number of days
            if(days_elapsed <= days):
                update_score(fastest_rate, scores)
            
        new_score = ippt_results(ippt_table, age, scores[0], scores[1], scores[2])

        return (scores[0], scores[1], scores[2], new_score)
        

    return tp_bonus

tp_bonus = make_tp_bonus(7, 3, 10)
tp_bonus(ippt_table, 25, 20, 30, 800, 30)

# Note: Depending on your implementation, you might get a different number of
# sit-up, push-up, and 2.4km run timing. However, the IPPT score and grade
# should be the same as the sample output.

print(tp_bonus(ippt_table, 25, 20, 30, 800, 30))      # (20, 40, 800, (58, 'P'))
print(tp_bonus(ippt_table, 25, 20, 30, 800, 2))       # (20, 30, 800, (52, 'P'))
