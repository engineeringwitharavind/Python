import random
import os
import sys

# Python Variables,Keywords and Identifiers

''' 
#1 Write a Python program using 
  (if, else, elif, for, range, while, pass, break, continue, class, def, global, local, nonlocal, lambda, 
   filter(), map(), None, try, except, finally, del, return)
 '''

# if elif else:
num = 3

if num > 0:
    print("This number is positive")
elif num == 0:
    print("This is Zero")
else:
    print("This number is negative")
################################################################################
# for loop:

#list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#variable to store the sum
sum_value = 0

for val in numbers:
    sum_value = sum_value + val

print("The total sum is ", sum_value)

# for loop with else:

digits = [1, 2, 5]
for i in digits:
    print(i)
else:
    print("No items left in the list")
#######################################################################################

# range function:
print(range(10))
#O/P : range(0, 10)

print(list(range(10)))
#O/P : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list(range(2, 20, 3)))  # 3 is the step size
#O/P : [2, 5, 8, 11, 14, 17]

# Program to iterate through a list using indexing with range function:

genre = ['pop', 'jazz', 'melody']
# iterate over list using index
for i in range(len(genre)):
    print("I like", genre[i])

####################################################################################################

# While Loop:

# Program to find sum of natural numbers upto sum = 1+2+3+....+n
# To get input from the user use         n = int(input("Enter a number: "))

n = 10
# initializing sum_value and counter
sum_val = 0
i = 1

while i <= n:
    sum_val += i  # it is equivalent to sum_val = sum_val + i
    i += 1   # updating the counter

print("The sum is", sum_val)

# While loop with else:

# Program to understand While loop with else:
counter = 0

while counter < 3:
    print("Inside Loop")
    counter = counter + 1
else:
    print("Inside Else")

###########################################################################################################

# Break, Continue, Pass function:

# Break:
for val in "string":
    if val == 'i':
        break
    print(val)

print("The End")

# Continue:
for val in "string":
    if val == 'i':
        continue
    print(val)

print("The End")

# Pass:  It is a null statement. It results into no operation
# Difference between pass and comment is 'comment' is ignored by python interpreter but 'pass' is not ignored
sequence = ['p', 'a', 's', 's']
for val in sequence:
    pass
print(sequence)

# Looping:
# Infinite Loop using 'while' # press Ctrl + C to exit from the Loop

'''
while True:
    n = int(input("enter an integer: "))
    print("The Double of", num, "is", 2 * num)
'''

# Using Loop in middle:

# Program to Check if user enters a 'VOWEL' or not:
vowels = "aeiouAEIOU"

# infinite loop
while True:
    v = 'a'
    #v = input("Enter a vowel: ")
# Condition in the middle
    if v in vowels:
        break
    print("That's not a vowel. TRY AGAIN!!")

print("THANK YOU")

################################################################################################

# class and def:
class mynewclass:
    """ This is a docstring.I have created a new class """
    pass

class myclass:
    """ This is my second class """
    a = 10
    def func(self):
        print('Hello Aravind')


# Output for class
print(myclass.a)

print(myclass.func)

print(myclass.__doc__)

############################################################################################

# Global , Local and Nonlocal Variables:

# Global Variable: Variable assigned outside a function or in global scope and can be accessed inside or outside a loop
x = "global"

def foo():
    print("x inside:", x)


foo()
print("x outside:", x)

# Local Variable: Variable created inside a function or within local scope. cannot be called outside a function.
def foo():
    y = "local"
    print(y)


foo()

# Using Global and Local variables in same code for better Understanding
x = "global"

def foo():
    global x
    y = "local"
    x = x * 2
    print(x)
    print(y)


foo()

# Non local Variables: Used in Nested Functions whose local scope is not defined. its neither local nor global.
def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)


outer()

##################################################################################################

# Lambda, filter(), map()

# Anonymous / Lambda Functions: Functions defined without a name. Uses "lambda" keyword for anonymous function

#Program to show the use of Lambda Function:
double = lambda x: x * 2

print(double(4))
##################################################################

# Lambda functions can be used with built-in functions like filter() , map()

'''
filter(): A function is called with all items in the list and new list is returned which  
contains items for which the function evaluates to True.
'''
# Program to filter even items from the list
my_list = [2, 3, 4, 5, 6, 7, 8, 9]

new_list = list(filter(lambda x: (x%2 == 0), my_list))

print(new_list)

'''
map(): The function is called with all the items in the list and a new list is returned which 
contains items returned by that function for each item.
'''
# Program to Double each item in the list
my_list = [2, 3, 4, 5, 6]

new_list = list(map(lambda x: x * 2, my_list))

print(new_list)
########################################################################################################

# None: 'None' is a python keyword Equivalent to 'NULL'

########################################################################################################

# try, except , finally:

# try: The try keyword is used in try...except blocks. It defines a block of code test if it contains any errors.
try:
  x > 3
except:
  Exception("Something went wrong")
##########################################

#except: It is used in try...except blocks. It defines a block of code to run if the try block raises an error.
x = "hello"

try:
  x > 3
except NameError:
  print("You have a variable that is not defined.")
except TypeError:
  print("You are comparing values of different type")
############################################

'''
finally: 
The finally keyword is used in try...except blocks. 
It defines a block of code to run when the try...except...else block is final.
The finally block will be executed no matter if the try block raises an error or not.
This can be useful to close objects and clean up resources.
'''
try:
  x > 3
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
finally:
  print("The try...except block is finished")
##################################################################################################################

# del: used for deleting objects. It can be variables,user-defined objects, lists, items within lists, dictionaries etc.

# deleting user defined object:
class myclass:
    a = 10
    def func(self):
        print("Hello")


del myclass

# deleting variable, list, tuple and dictionary
my_var = 5
my_list = [2, 3, 4, 5]
my_tuple = (2, 3, 4)
my_dict = {'name': 'Aravind', 'age': 23}


del my_var
del my_list[3]
del my_tuple
del my_dict
#########################################################################################################

# return keyword: The return keyword is to exit a function and return a value.

def myfunction():
  return 3+3


print(myfunction())
#########################################################################################################

#2 Write the rules for writing Identifiers

'''
 1.Identifiers can be a combination of letters in lowercase (a to z) or uppercase (A to Z) or digits (0 to 9)
 or an underscore _.
 2.An identifier cannot start with a digit. 1variable is invalid, but variable1 is perfectly fine.
 3.Keywords cannot be used as identifiers.
 4.We cannot use special symbols like !, @, #, $, % etc. in our identifier.
 5.Identifier can be of any length.
'''

# Understanding Recursion in Python:

'''
Recursion is the process of defining something in terms of itself.

A physical world example would be to place two parallel mirrors facing each other. 
Any object in between them would be reflected recursively.
'''

# Example of recursive function to find factorial of a number:
def cal_factorial(x):
    """ This is a recursive function
    to find factorial of a number """

    if x == 1:
        return 1
    else:
        return x * cal_factorial(x - 1)


num = 4
print("The Factorial of", num, "is", cal_factorial(num))

##################################################################################################################