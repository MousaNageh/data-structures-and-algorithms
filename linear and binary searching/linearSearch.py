

#######################problem###########################################
# QUESTION 1: Alice has some cards with numbers written on them. She arranges the cards in decreasing order, and lays them out face down in a sequence on a table. She challenges Bob to pick out the card containing a given number by turning over as few cards as possible. Write a function to help Bob locate the card.#

# O(N)
###############################data#####################################
# test = {
#     'input': {
#         'cards': [13, 11, 10, 7, 4, 3, 1, 0],
#         'query': 7
#     },
#     'output': 3
# }

# tests={
#     'input': {
#         'cards': [9, 7, 5, 2, -9],
#         'query': 4
#     },
#     'output': -1
# }

# test =  {
#   'input':{
#           'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
#           'query': 6
#         },
#         'output': 2}

#################cases################################################

# query is the first element in cards.
# query is the last element in cards.
# The list cards contains just one element, which is query.
# The list cards does not contain number query.
# The list cards is empty.
# The list cards contains repeating numbers.
# The number query occurs at more than one position in cards.


#########################solution##################################
import time


def find_element_in_cards(cards, query):
    array_length = len(cards)
    if not array_length:
        return -1
    elif array_length > 0:
        i = 0
        while i < array_length:
            if cards[i] == query:
                return i
            i += 1
    return -1


tests = [
    {'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 7}, 'output': 3},
    {'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 1}, 'output': 6},
    {'input': {'cards': list(range(100000000, 0, -1)),
               'query': 2}, 'output': 9999998},
    {'input': {'cards': [4, 2, 1, -1], 'query': 4}, 'output': 0},
    {'input': {'cards': [3, -1, -9, -127], 'query': -127}, 'output': 3},
    {'input': {'cards': [6], 'query': 6}, 'output': 0},
    {'input': {'cards': [9, 7, 5, 2, -9], 'query': 4}, 'output': -1},
    {'input': {'cards': [], 'query': 7}, 'output': -1},
    {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'query': 3},
     'output': 7},
    {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
               'query': 6},
     'output': 2}

]
test_number = 0
time_before = time.time() * 1000
for test in tests:
    test_number += 1
    result = find_element_in_cards(**test["input"])
    if result == test['output']:
        print(
            f"(test number {test_number}:passed , matched index : {result} )")
    else:
        print(
            f"(test number {test_number}:passed , matched index : {result}) ")
time_after = time.time() * 1000
print("execution time :", time_after-time_before)
