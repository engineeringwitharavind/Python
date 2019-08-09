# ARGUMENTS, PARAMETERS, ANONYMOUS FUNCTIONS AND SCOPE OF VARIABLES.

# List the Scope of Variables in Python:
# ===>  Global Variable and Local Variable

# Write a Program using Lambda Function:

# Lambda Function: An Anonymous Function which can have any number of arguments with only one expression.
a = lambda x: x*x*x
print(a(5))

# Use of lambda with filter():
list1 = [1, 2, 3, 4, 5]
final_list = list(filter(lambda x: (x % 2 != 0), list1))
print(final_list)

# Use of lambda with map():
li1 = [1, 2, 3, 4]
final_list = list(map(lambda x: x * 2, li1))
print(final_list)

# Use of lambda with reduce:
from functools import reduce
mylist = [2, 3, 4, 5, 6]
sum1 = reduce(lambda x, y: x + y, mylist)
print(sum1)
####################################################################################################################

'''
Program using Positional parameters or Keyword arguments:
'''


def greet(name, msg="Good Morning!!"):
    print("Hello", name + ',' + msg)


greet("Aravind")

# 2 Keyword Arguments:
greet(name="Arun", msg="How do you do?")

# 2 keyword Arguments: (Out of Order)
greet(msg="Good Night!!", name="Bala")

# 1 Positional Argument and 1 keyword Argument:
greet("Aravind", msg="This Works fine.")
######################################################################################################################

'''
Program using Arbitrary Arguments:
'''
# In Some cases we know the we will use some no. of arguments before creating a function.
# So, we can use arbitrary Arguments


def greet(*names):
    for name in names:
        print("Hello", name)



greet("Aravind", "Guru", "Bala", "Arun")
#####################################################################################################################
