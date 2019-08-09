import random
import sys
import os

# Python Operators

# Arithmetic Operations

num1 = float(input(" Please Enter the First Value Number 1: "))
num2 = float(input(" Please Enter the Second Value Number 2: "))

# Add Two Numbers
add = num1 + num2

# Subtracting num2 from num1
sub = num1 - num2

# Multiply num1 with num2
multi = num1 * num2

# Divide num1 by num2
div = num1 / num2

# Modulus of num1 and num2
mod = num1 % num2

# Exponent of num1 and num2
expo = num1 ** num2

print("The Sum of {0} and {1} = {2}".format(num1, num2, add))
print("The Subtraction of {0} from {1} = {2}".format(num2, num1, sub))
print("The Multiplication of {0} and {1} = {2}".format(num1, num2, multi))
print("The Division of {0} and {1} = {2}".format(num1, num2, div))
print("The Modulus of {0} and {1} = {2}".format(num1, num2, mod))
print("The Exponent Value of {0} and {1} = {2}".format(num1, num2, expo))

#################################################################################################################

# Assignment Operators

a = 21
b = 10
c = 0

c = a + b
print("Value of c is ", c)

c += a
print("Value of c is ", c)

c *= a
print("Value of c is ", c)

c /= a
print("Value of c is ", c)

c = 2

c %= a
print("Value of c is ", c)

c **= a
print("Value of c is ", c)

c //= a
print("Value of c is ", c)

##################################################################################################################

# Comparison Operators

a = 9
b = 4

print(" The Output of 9 > 4 is : ", a > b )
print(" The Output of 9 < 4 is : ", a < b )
print(" The Output of 9 <= 4 is : ", a <= b )
print(" The Output of 9 >= 4 is : ", a >= b )
print(" The Output of 9 Equal to 4 is : ", a == b )
print(" The Output of 9 Not Equal To is : ", a != b )

##################################################################################################################

# Logical Operators

age = 29

# Logical AND Example
if 33 > age > 20:
    print ("Young Man")
else:
    print(" Not Eligible ")

# Logical OR Example
if age < 18 or age > 60:
    print(" Not Eligible to Work ")
else:
    print(" Please forward Your Resume ")

###################################################################################################################

# Identity Operators:

a = 20
b = 20

if a is b:
    print("a and b have same identity")
else:
    print("a and b do not have same identity")

if id(a) == id(b):
    print("a and b have same identity")
else:
    print("Line 2 - a and b do not have same identity")

b = 30

if a is b:
    print("a and b have same identity")
else:
    print("Line 3 - a and b do not have same identity")

if a is not b:
    print("a and b do not have same identity")
else:
    print("a and b have same identity")

#################################################################################################################

# Bitwise Operators:

a = 9
b = 65

print("Bitwise AND Operator On 9 and 65 is = ", a & b)
print("Bitwise OR Operator On 9 and 65 is = ", a | b)
print("Bitwise EXCLUSIVE OR Operator On 9 and 65 is = ", a ^ b)
print("Bitwise NOT Operator On 9 is = ", ~a)

print("Bitwise LEFT SHIFT Operator On 9 is = ", a << 1)
print("Bitwise RIGHT SHIFT Operator On 65 is = ", b >> 1)

###################################################################################################################

