'''
1)Question 1: Given an array of integers nums sorted in ascending order, find the starting and ending position of a given number.

'''
##############################binary search ##############################
test = {
    "input": {
        "array": [1, 2, 3, 4, 5, 6, 6, 6, 6, 6, 6, 6, 7, 8, 9, 10, 11],
        "input": 6
    },
    "output": [5, 11]
}


def find_last_location(array, element, middle_index):
    if (array[middle_index] == element):
        if (middle_index+1) <= (len(array)-1) and array[middle_index+1] == element:
            return 'go-right'
        else:
            return 'found'
    elif array[middle_index] < element:
        return 'go-right'
    elif array[middle_index] > element:
        return 'go-left'


def find_first_location(array, element, middle_index):
    if (array[middle_index] == element):
        if (middle_index-1) >= 0 and array[middle_index-1] == element:
            return 'go-left'
        else:
            return 'found'
    elif array[middle_index] < element:
        return 'go-right'
    elif array[middle_index] > element:
        return 'go-left'


def get_first_and_last_indexes(array, element):
    founded_indexes = []
    if not len(array):
        return founded_indexes
    low_index, high_index = 0, len(array)-1
    while low_index <= high_index:
        midde_index = (low_index+high_index)//2
        result = find_first_location(array, element, midde_index)
        if result == 'found':
            founded_indexes.append(midde_index)
            break
        elif result == 'go-right':
            low_index = midde_index+1
        elif result == 'go-left':
            high_index = midde_index - 1
    low_index, high_index = 0, len(array)-1
    while low_index <= high_index:
        midde_index = (low_index+high_index)//2
        result = find_last_location(array, element, midde_index)
        if result == 'found':
            founded_indexes.append(midde_index)
            break
        elif result == 'go-right':
            low_index = midde_index+1
        elif result == 'go-left':
            high_index = midde_index - 1
    if not founded_indexes:
        return founded_indexes
    else:
        if founded_indexes[0] == founded_indexes[1]:
            return [founded_indexes[0]]
        else:
            return founded_indexes


print(get_first_and_last_indexes(
    test["input"]["array"], test["input"]["input"]))


"""
2)Question 2:
Problem - Rotated Lists:


You are given list of numbers, obtained by rotating a sorted list an unknown number of times. Write a function to determine the minimum number of times the original sorted list was rotated to obtain the given list. Your function should have the worst-case complexity of O(log N), where N is the length of the list. You can assume that all the numbers in the list are unique.

Example: The list [5, 6, 9, 0, 2, 3, 4] was obtained by rotating the sorted list [0, 2, 3, 4, 5, 6, 9] 3 times.

We define "rotating a list" as removing the last element of the list and adding it before the first element. E.g. rotating the list [3, 2, 4, 1] produces [1, 3, 2, 4].

"Sorted list" refers to a list where the elements are arranged in the increasing order e.g. [1, 3, 5, 7].


"""

###########################solution by linear search ########################


def get_number_of_rotations_linear(array):
    array_length = len(array)
    if not array or array_length == 1:
        return 0
    else:
        i = 0

        while i < array_length-1:
            if array[i] > array[i+1]:
                return i+1
            i += 1
        return 0


tests = [
    {
        'input': [19, 25, 29, 3, 5, 6, 7, 9, 11, 14],
        'output': 3
    },
    {
        'input': [],
        'output': 0
    },
    {
        'input': [19],
        'output': 0
    },
    {
        'input': [2, 3, 4, 5, 6, 7, 8, 9, 1],
        'output': 8
    },
    {
        'input': [2, 1],
        'output': 1
    },
    {
        'input': [1, 2],
        'output': 0
    },
    {
        'input': [1, 2, 3, 4, 5, 6, 7, 8, 9],
        'output': 0
    },

]
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
for test in tests:
    print(get_number_of_rotations_linear(test["input"]))

################solution by binary search ######################

# If the middle element is smaller than its predecessor(element before it), then it is the answer. However, if it isn't, this check is not sufficient to determine whether the answer lies to the left or the right of it. Consider the following examples.

# [7, 8, 1, 3, 4, 5, 6] (answer lies to the left of the middle element)

# [1, 2, 3, 4, 5, -1, 0] (answer lies to the right of the middle element)

# Here's a check that will help us determine if the answer lies to the left or the right: If the middle element of the list is smaller than the last element of the range, then the answer lies to the left of it. Otherwise, the answer lies to the right.


def get_number_of_rotations_binary(array):
    array_length = len(array)
    if not array or array_length == 1:
        return 0
    else:
        low_index, high_index = 0, array_length-1
        while low_index <= high_index:
            middle_index = (low_index+high_index)//2
            if array[middle_index] < array[middle_index-1]:
                return middle_index
            if array[middle_index] < array[high_index]:
                high_index = middle_index-1
            else:
                low_index = middle_index+1
    return 0


print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
for test in tests:
    print(get_number_of_rotations_binary(test["input"]))
