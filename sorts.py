import random
import time

test_size = 1000

test_list = [i for i in range(1, test_size + 1)]
random.shuffle(test_list)

def bubble_sort(lst):
    lst_length = len(lst)
    for i in range(lst_length):
        for j in range(lst_length - i - 1):
            if(lst[j] > lst[j + 1]):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


def merge_sort(lst):
    lst_length = len(lst)

    if(lst_length < 2):
        return lst

    left = merge_sort(lst[:lst_length // 2])
    right = merge_sort(lst[lst_length // 2:])
    return merge(left, right)

def merge(left, right):
    merged = []

    while(len(left) != 0 and len(right) != 0):
        if(left[0] < right[0]):
            merged.append(left[0])
            left.pop(0)
        else:
            merged.append(right[0])
            right.pop(0)

    if(len(left) == 0):
        merged.extend(right)
    else:
        merged.extend(left)

    return merged

def test(*args):
    for func in args:
        start = time.time()
        func(test_list)
        end = time.time()
        print(f"{func.__name__} | [{test_size} samples]: {end - start} seconds")

test(bubble_sort, merge_sort)