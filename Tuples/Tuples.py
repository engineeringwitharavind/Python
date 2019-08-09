# TUPLES IN PYTHON

# Program to create a Tuple:

empty_tup = ()
print(empty_tup)
################################################################################################################

'''
Program to create tuple with different data types:
'''

tup = ("aravind", True, 2.3, 5)
print(tup)
###############################################################################################################

'''
Program to add an item in a tuple:
'''

tup = (4, 6, 2, 8, 3, 1)
print(tup)
# tuples are immutable, so you can not add new elements
# using merge of tuples with the + operator you can add an element and it will create a new tuple
tup = tup + (9,)
print(tup)
# adding items in a specific index
tup = tup[:5] + (15, 20, 25) + tup[:5]
print(tup)
# converting the tuple to list
l = list(tup)
# use different ways to add items in list
l.append(30)
tup = tuple(l)
print(tup)
################################################################################################################

'''
Program to convert a tuple to a string:
'''

tup = ('h', 'e', 'l', 'l', 'o')
s = ''.join(tup)
print(s)
################################################################################################################

'''
Program to check if an element exists in a tuple:
'''


def check(tup, n):
    if n in tup:
        return True
    else:
        return False


# check:
tup = (1, 2, 3, 4, 5)
n = 2
if check(tup, n):
    print("Element Exists")
else:
    print("Element Not exists")
################################################################################################################

'''
Program to convert a list to tuple:
'''


def convert(list):
    return tuple(list)


# check
list = [1, 2, 3, 4, 5]
print(convert(list))
################################################################################################################

'''
Program to remove an item from a tuple:
'''

tup = ('a', 'r', 'a', 'v', 'i', 'n', 'd')
print(tup)
# tuples are immutable, so you can not remove elements
# using merge of tuples with the + operator you can remove an item and it will create a new tuple
tup = tup[:2] + tup[3:]
print(tup)
################################################################################################################

'''
Program to find length of the tuple:
'''


def length(tup):
    return len(tup)


# check
tup = ('h', 'e', 'l', 'l', 'o')
print(length(tup))
#################################################################################################################

'''
Program to convert a tuple to dictionary:
'''

tup = ((2, 'a'), (3, 'b'))
print(dict((y, x) for x, y in tup))
#################################################################################################################

'''
Program to reverse a tuple:
'''


def rev(tup):
    new_tup = tup[::-1]
    return (new_tup)


# check
tup = (1, 2, 3)
print(rev(tup))
#################################################################################################################
