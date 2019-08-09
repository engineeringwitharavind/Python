# STRINGS IN PYTHON

# Program to find the length of the string:

str = "Aravind"
# manual input ===>  str = input("Enter a String: ")
counter = 0

for s in str:
    counter += 1
print("The length of the string is ", counter)
######################################################################################################

'''
Program to find number of characters (character frequency) in a string:
'''


def char_frequency(string):
    dict = {}
    for n in string:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict


print(char_frequency('Avengers'))
#######################################################################################################

'''
Program to get a string made of first 2 and last 2 chars from a given string. If length is less than 2 then 
return it instead of an empty string:
'''

string = "Aravind"
# for manual input ===>  string = input("Enter a string: ")

if len(string) > 2:
    string = string[0:2] + string[-2:]
    print(string)
else:
    print(string)
########################################################################################################

'''
Program to get a string where all the occurrences of the first char is replaced with '$' except the first char
itself: 
'''

str = "aravind"
# for manual input ===>  string = input("Enter a string: ")
char = str[0]
for i in str:
    str = char + str[1:].replace(char, '$')

print("The String is", str)
##########################################################################################################

'''
Program to get a single string from two given strings, separated by a space and swap first two characters of
a each string:
'''

str1 = "Washing"
str2 = "Machine"
# for manual input ===>  str1 = input("Enter a string: ") "\n" str2 = input("Enter a String: ")
for i in str1 and str2:
    str = str2[0] + str1[1:] + ' ' + str1[0] + str2[1:]

print(str)
############################################################################################################

'''
Program to add 'ing' at the end of the given string(length should be at least 3) if the given string already ends 
with 'ing' add 'ly' instead. If the length of the word is less than 3 then leave the word unchanged
'''

str = "Carry"
# for manual input ==> str = input("Enter a String: ")
if (len(str)) > 3 and ('ing' not in str):
    print("The String is ", str + 'ing')
elif (len(str)) > 3 and ('ing' in str):
    print("The String is ", str + 'ly')
else:
    print("The String is", str)
#################################################################################################################

'''
Program to find the first appearance of the substring 'not' and 'poor' from a given string. If 'bad' follows the 'poor'
replace the whole 'not'..'poor' substring with 'good'. Return the resulting string.
'''

str = "book not poor bad"
# for manual input ==> str = input("Enter a string: ")
a = str.find('not')
b = str.find('poor')
c = str.find('bad')
if [b > a, c > b and a > 0, b > 0]:
    str = str.replace(str[a:b + 4], 'good', 1)
    print(str)
else:
    print(str)
######################################################################################################################

'''
Write a python function that takes a list of words and returns the length of longest one
'''


def longest(my_list):
    count = 0
    for i in my_list:
        if len(i) > count:
            count = len(i)
            word = i
    return word


my_list = ['bala', 'aravind', 'ram']
print(longest(my_list))
#####################################################################################################################

'''
Program to remove the nth index character from a nonempty string:
'''

str = "aravind"
# for manual input ==>  str = input("Enter the string: ")
n = 3
# for manual input ==>  n = int(input("Enter the index of character to be removed: "))

i = str[n]

if len(str) > 1:
    str = str.replace(i, '', 1)
else:
    str = str
print(str)
###################################################################################################################

'''
Program to change a given string to new string where the first and last chars have been exchanged:
'''

str = "aravind"
# str = input("Enter a String: ")

if len(str) > 1:
    str = str[-1] + str[1:-1] + str[0]
    print(str)
##################################################################################################################

'''
Program to remove characters which have odd values in a given string
'''

str = "aravind"
# str = input("Enter a String: ")
s = ""
for i in range(len(str)):
    if i % 2 == 0:
        s = s + str[i]
print(s)
##################################################################################################################

'''
Program to count occurrences of each word in a given sentence:
'''

str = "This is the best game in the world"
# str = input("Enter a String: ")
s = "the"
# s = input("Enter a word to find its occurrence: ")
count = 0
str = str.split()
for i in str:
    if i == s:
        count += 1
print("Word Occurrence Count is", count)
##################################################################################################################

'''
Write a Python script to take input from user and display it in both Upper and lower cases
'''

str = "aravind"
# str = input("Enter a String: ")

if len(str) > 1:
    print(str.upper())
    print(str.lower())
##################################################################################################################

'''
Program to accept comma separated values as input and return distinct values in sorted form (alphanumerically):
'''

str = " blue, red, black, green"
# for manual input ==> str = input("Enter comma separated values: ")
words = [word for word in str.split(',')]
print(",".join(sorted(set(words))))

#################################################################################################################

'''
Program to create HTML string with tags <> around the words
'''


def add_htmltags(tag, word):
    return "<%s>%s</%s>" % (tag, word, tag)


# sample outputs
print(add_htmltags('i', 'Python'))
print(add_htmltags('t', 'text'))
#################################################################################################################

'''
Python function to insert a new string in the middle of the string
'''

a = "aravindgmail.com"


def insert_char(mystring, position, chartoinsert):
    long = len(mystring)
    mystring = mystring[:position] + chartoinsert + mystring[position:]
    return mystring


print(insert_char(a, 7, '@'))
# sample output
# ==> aravind@gmail.com
#################################################################################################################

'''
Python Function to get a string made of 4 copies of last two characters of a specified string(length must be at least 2)
'''


def str_copy(mystring):
    if len(mystring) > 2:
        mystring = mystring + 4 * mystring[-2:]
    return mystring


print(str_copy('sruthi'))
####################################################################################################################

'''
Python function to reverse a string if its length is a multiple of 4
'''


def rev_str(mystring):
    if len(mystring) % 4 == 0:
        return mystring[::-1]
    else:
        return mystring


print(rev_str('guru'))
#####################################################################################################################

'''
Python Function to convert a given string to all Uppercase if it contains at least 2 uppercase characters in the first
4 characters:
'''


def to_upper(mystring):
    num_upper = 0
    for i in mystring[:4]:
        if i.upper() == i:
            num_upper += 1
    if num_upper >= 2:
        return mystring.upper()
    return mystring


print(to_upper("PyThon"))
####################################################################################################################

'''
Program to check whether a given string starts with specific characters:
'''

str = "aravind"
# for manual input ==> str = input("Enter a String to Check: ")
s = 'a'
# for manual input ==> s = input("Enter a Specific character: ")
if s == str[0]:
    print("Yes, the given Sting starts with Specific Characters.")
else:
    print("No, the given string does'nt starts with that specific characters.")
#####################################################################################################################