#
# CS1010X --- Programming Methodology
#
# Sidequest 9.1 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

import json
import time

#####################
# Reading json file #
#####################

def read_json(filename):
    """
    Reads a json file and returns a list of modules
    To find out more about json, please google it :P

    For example, file.txt contains:
    [["CS3216", "SOFTWARE DEVELOPMENT ON EVOLVING PLATFORMS", "TAN KENG YAN, COLIN"], ["CS2010", "DATA STRUCTURES & ALGORITHMS II", "STEVEN HALIM"], ["CS1010S", "PROGRAMMING METHODOLOGY", "LEONG WING LUP, BEN"]]

    Calling read_json('file.txt') will return the following array
    [
        ["CS3216", "SOFTWARE DEVELOPMENT ON EVOLVING PLATFORMS", "TAN KENG YAN, COLIN"],
        ["CS2010", "DATA STRUCTURES & ALGORITHMS II", "STEVEN HALIM"],
        ["CS1010S", "PROGRAMMING METHODOLOGY", "LEONG WING LUP, BEN"]
    ]
    """
    datafile = open(filename, 'r', encoding='utf-8')
    return json.loads(datafile.read())

#############
# Accessors #
#############

def module_code(module):
    return module[0]

def module_name(module):
    return module[1]

def module_prof(module):
    return module[2]


###########
# Task 1a #
###########

def merge_lists(all_lst):
    # Your code here
    output = []
    
    # Filter input lists first to remove any empty sub-lists
    all_lst = [lst for lst in all_lst if lst]
    
    while all_lst != []:
        
        # Init smallest value to first list first value,
        # and smallest list index to 0
        smallest = all_lst[0][0]
        idx = 0

        # Loop through sub-lists & pick out list with smallest first element
        for i in range(len(all_lst)):
            if(all_lst[i][0] < smallest):
                idx = i
                smallest = all_lst[i][0]

        # Append smallest value to output list,
        # and pop first element from relevant sub-list
        output.append(all_lst[idx][0])
        all_lst[idx].pop(0)

        # Manage remaining lists to remove any empty ones
        all_lst = [lst for lst in all_lst if lst]
        
    return output

all_lst = [[2, 7, 10], [0, 4, 6], [3, 11]]
al_lst = []
print("## Q1a ##")
print(merge_lists(all_lst)) # [0, 2, 3, 4, 6, 7, 10, 11]
print(merge_lists(al_lst))

###########
# Task 1b #
###########

def merge(all_lst, field):
    # Your code here
    output = []
    
    # Filter input lists first to remove any empty sub-lists
    all_lst = [lst for lst in all_lst if lst]
    
    while all_lst != []:
        
        # Init smallest value to first list first value,
        # and smallest list index to 0
        smallest = field(all_lst[0][0])
        idx = 0

        # Loop through sub-lists & pick out list with smallest first element
        for i in range(len(all_lst)):
            if(field(all_lst[i][0]) < smallest):
                idx = i
                smallest = field(all_lst[i][0])

        # Append smallest value to output list,
        # and pop first element from relevant sub-list
        output.append(all_lst[idx][0])
        all_lst[idx].pop(0)

        # Manage remaining lists to remove any empty ones
        all_lst = [lst for lst in all_lst if lst]
        
    return output
    


list_of_lists = [[["CS1010S", "PROGRAMMING METHODOLOGY", "LEONG WING LUP, BEN"],
                  ["CS3235", "COMPUTER SECURITY", "NORMAN HUGH ANDERSON"]],
                 [["CS4221", "DATABASE DESIGN", "LING TOK WANG"],
                  ["CS2010", "DATA STRUCTURES & ALGORITHMS II", "STEVEN HALIM"]]]
print("## Q1b ##")
print(merge(list_of_lists, module_prof))
# [[’CS1010S’, ’PROGRAMMING METHODOLOGY’, ’LEONG WING LUP, BEN’],
#  [’CS4221’, ’DATABASE DESIGN’, ’LING TOK WANG’],
#  [’CS3235’, ’COMPUTER SECURITY’, ’NORMAN HUGH ANDERSON’],
#  [’CS2010’, ’DATA STRUCTURES & ALGORITHMS II’, ’STEVEN HALIM’]

##########
# Task 2 #
##########

# @brief Splits a list into k portions evenly
# @param[in] list
# @param[in] portions
# @retval distributed list
def distribute(lst, k):
    subarr = []
    start_idx = 0
    end_idx = 0
    segment_size = len(lst) // k
    extras = len(lst) % k

    for i in range(k):
        # Distribute the extra elements evenly
        end_idx = start_idx + segment_size + (1 if extras else 0)
        subarr.append(lst[start_idx : end_idx])
        # Update number of extra elements to distribute
        extras -= 1 if ((end_idx - start_idx) != segment_size) else 0
        start_idx = end_idx
        
    return subarr

def merge_sort(lst, k, field):
    # Your code here
    size = len(lst)

    if(size <= 1):
        return lst
    
    split_lst = distribute(lst, k)

    sorted_sub = [merge_sort(sub, k, field) for sub in split_lst]
    return merge(sorted_sub, field)


# For your own debugging
# modules = read_json('modules_small.txt')
# for module in merge_sort(modules, 2, module_code):
     # print(module)


########### DO NOT REMOVE THE TEST BELOW ###########
########### DO NOT REMOVE THE TEST BELOW ###########
########### DO NOT REMOVE THE TEST BELOW ###########
########### DO NOT REMOVE THE TEST BELOW ###########
########### DO NOT REMOVE THE TEST BELOW ###########

def print_list_to_str(list):
    return '\n'.join(str(x) for x in list)

def test(testfile_prefix):
    print("\n*** Testing with ",testfile_prefix,".txt ***")
    modules = read_json(testfile_prefix+'.txt')
    total_time = 0

    # Open correct answers
    modules_sorted_code = open(testfile_prefix+'_sorted_code.txt', 'r', encoding='utf-8').read()
    modules_sorted_name = open(testfile_prefix+'_sorted_name.txt', 'r', encoding='utf-8').read()
    modules_sorted_prof = open(testfile_prefix+'_sorted_prof.txt', 'r', encoding='utf-8').read()

    ks = [2,3,5,8,13,21,34,55,89,144]
    pass_k = 0

    for k in ks:
        start_time = time.time()
        # Execute
        modules_answer_code = merge_sort(modules, k, module_code)
        modules_answer_name = merge_sort(modules, k, module_name)
        modules_answer_prof = merge_sort(modules, k, module_prof)
        end_time = time.time()
        total_time += (end_time - start_time)

        # Check
        code_same = print_list_to_str(modules_answer_code) == modules_sorted_code
        name_same = print_list_to_str(modules_answer_name) == modules_sorted_name
        prof_same = print_list_to_str(modules_answer_prof) == modules_sorted_prof
        if (code_same and name_same and prof_same):
            pass_k += 1
        print("k = ", k, ", code: ",code_same,", name: ", name_same,", prof: ",prof_same)

    print(pass_k,"/", len(ks), " correct! Total time taken: ", total_time, " seconds.")

print("## Q2 ##")
test('modules_small')
test('modules')
test('modules_empty')
