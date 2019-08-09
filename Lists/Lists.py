# LISTS IN PYTHON

# Program to sum all elements in the list:

mylist = [1, 2, 3, 5, 7]
total = 0
for i in range(0, len(mylist)):
    total += mylist[i]

print("Sum of all elements in the list is", total)
#################################################################################################################

'''
Program to multiply all the elements in the list:
'''

mylist = [1, 3, 4, 5, 6, 7]
product = 1
for i in range(0,len(mylist)):
    product *= mylist[i]

print("The product of all elements in the list is", product)
#################################################################################################################

'''
Program to get the largest number from the list:
'''

mylist = [1, 4, 5, 7, 9]
largest_num = 0
for i in mylist:
    if i > largest_num:
        largest_num = i
print("The largest number in the list is", largest_num)
###################################################################################################################

'''
Program to get the smallest number from the list:
'''

mylist1 = [33, 54, 55, 22, 15]
mylist1.sort()
print("Smallest number is the list is", mylist1[0])
###################################################################################################################

'''
Program to remove duplicates from the list:
'''


def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list


# Driver Code
duplicate = [2, 4, 10, 20, 5, 2, 20, 4]
print(Remove(duplicate))
####################################################################################################################

'''
Program to check if a list is empty or not:
'''


def Enquiry(lst):
    if len(lst) == 0:
        return 0
    else:
        return 1


lst = []
if Enquiry(lst):
    print("It is not a Empty list")
else:
    print("Empty list")
#################################################################################################################

'''
Program to clone or copy a list:
'''


def cloning(mylst1):
    mylst_copy = mylst1[:]
    return mylst_copy


mylst1 = [1, 3, 4, 5, 6]
mylst2 = cloning(mylst1)
print("Orginal list:", mylst1)
print("After Cloning:", mylst2)
##################################################################################################################

'''
Program to print a specified list after removing 0th, 4th and 5th elements:
Sample list = ['red', 'green', 'blue', 'black', 'yellow', 'orange', 'white']
Expected Output = ['green', 'blue', 'black', 'white']
'''

mylis1 = [0, 1, 2, 3, 4, 5, 6, 7]
mylis1 = [x for (i, x) in enumerate(mylis1) if i not in (0, 4, 5)]
print(mylis1)
###################################################################################################################

'''
Program to get the difference between two list:
'''


def diff(l1, l2):
    return list(set(l1) - set(l2))


l1 = [1, 2, 3, 4, 5, 6, 7, 8]
l2 = [1, 3, 5, 7, 9]

print(diff(l1, l2))
###################################################################################################################

'''
Program to find whether all the numbers in the list are greater than the specified number:
'''


def check(lis1, val):
    for x in lis1:
        if val >= x:
            return False
    return True


# check
lis1 = [33, 23, 22, 11, 15, 14]
val = 10
if check(lis1, val):
    print("yes")
else:
    print("no")
####################################################################################################################

'''
Program  to find a tuple, the smallest second index value from the list of tuples:
'''

a = [(1, 3), (2, 4), (2, 5), (3, 6)]
print(min(a, key=lambda n: (n[1], -n[0])))
####################################################################################################################

'''
Program to find whether an element exists in the given list or not:
'''


def check_element(n, a):
    if n in a:
        return True
    else:
        return False


# Check:
a = [1, 2, 4, 5, 6, 7]
n = 3
if check_element(n, a):
    print("Exists")
else:
    print("Not Exists")
###################################################################################################################

'''
Program to replace the last element with another list:
'''

n1 = [1, 3, 5, 6, 10]
n2 = [2, 3, 4, 1]
n1[-1:] = n2
print(n1)
##################################################################################################################

'''
Program to check if all the elements of given list is equal to a given string:
'''

a1 = ["ram", "siva", "guna", "bala"]
a2 = {"aravind", "aravind", "aravind"}
print(all(i =="guru" for i in a1))
print(all(i == "aravind" for i in a2))
##################################################################################################################

'''
Program to convert a String to a list:
'''
a = "aravind"
a.split(',')
l = list(a)
print(l)

b = "Good Noon"
l2 = list(b.split(" "))
print(l2)
#################################################################################################################

'''
Program to concatenate elements of a list:
'''
a3 = ['h', 'e', 'l', 'l', 'o']
c = ''
for i in a3:
    c += i
print(c)
#################################################################################################################

'''
Program to create multiple lists:
'''

obj = {}
for i in range(1, 6):
    obj[str(i)] = []
print(obj)
##################################################################################################################

'''
Program to find common elements from two lists:
'''


def common_element(a,b):
    a_set = set(a)
    b_set = set(b)
    if a_set & b_set:
        print(a_set & b_set)
    else:
        print("No Common Elements")


# Check
a = [1, 2, 3, 4, 5, 6, 7]
b = [1, 3, 5, 7, 9]

common_element(a,b)
##################################################################################################################

'''
Program to generate all sublist of a list
'''


def sub_lists(l1):
    sublist = [[]]
    for i in range(len(l1) + 1):
        for j in range(i+1, len(l1) +1):
            sub = l1[i:j]
            sublist.append(sub)
    return sublist


# Check:
l1 = [1, 2, 3, 4]
print(sub_lists(l1))
##################################################################################################################

'''
Program to get unique values from a list:
'''


def unique_values(l2):
    unique_list = []
    for i in l2:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list


# check:
l2 = [1, 3, 3, 4, 4, 5]
print(unique_values(l2))
###################################################################################################################
