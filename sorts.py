def bubble_sort(lst):
    lst_length = len(lst)
    for i in range(lst_length):
        for j in range(lst_length - i - 1):
            if(lst[j] > lst[j + 1]):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

lst = [523, 12, 845, 34, 91, 237, 678, 453, 98, 105, 782, 999, 431, 220, 334, 670, 19, 23, 564, 711, 42, 8, 92, 374, 651, 222, 814, 746, 100, 333, 567, 876, 290, 111, 54, 671, 892, 755, 267, 125, 308, 666, 503, 78, 420, 589, 600, 101, 20, 931]

print(bubble_sort(lst))

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

print(merge_sort(lst))
