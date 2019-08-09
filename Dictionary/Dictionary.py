# DICTIONARY IN PYTHON

# Program to create a dictionary:

# Empty Dictionary:
Dict = {}
print("Empty Dictionary: ")
print(Dict)

# Dictionary with Integer Keys:
Dict = {1: 'Aravind', 2: 'Subramanian'}
print("\nDictionary with the use of Integer Keys: ")
print(Dict)

# Dictionary with Mixed Keys:
Dict = {'Name': 'Aravind', 1: [1, 2, 3, 4, 5]}
print("\nDictionary with the use of Mixed Keys: ")
print(Dict)

# Creating Dictionary with the use of dict() Method:
Dict = dict({1: 'One', 2: 'Two', 3: 'Three'})
print("\nDictionary with the use of dict() method: ")
print(Dict)
##################################################################################################################

'''
Program to the access the values in the dictionary:
'''

# accessing the element using key:
Dict = {'Name': 'Aravind', 'Age': 24}
print(Dict['Age'])

# accessing the element using get() :
Dict = {1: 'One', 2: 'Two', 3: 'Three'}
print("\nAccessing the element using get: ")
print(Dict.get(3))
###################################################################################################################

'''
Program to update the above created Dictionary:
'''
Dict = {'Name': 'Aravind', 'Age': 24}
Dict.update({'City': 'Chennai'})
print("\nUpdated Dictionary: ")
print(Dict)
###################################################################################################################

'''
Program to delete the above created Dictionary:
'''

Dict = {'Name': 'Aravind', 'Age': 24, 'City': 'Chennai'}

# Deleting by using key value:
del Dict['City']
print("\nDeleting a Specific Key: ")
print(Dict)

# Deleting a key using pop:
Dict.pop('Age')
print("\nDeleting using pop: ")
print(Dict)

# Deleting the entire Dictionary:
Dict.clear()
print("\nDeleting Entire Dictionary: ")
print(Dict)
#################################################################################################################

'''
Python Code to Copy the Entire Dictionary into a new Dictionary:
'''

Dict1 = {1: 'One', 2: 'Two', 3: 'Three'}
Dict2 = Dict1.copy()

# Updating copied Dictionary:
Dict2.update({4: 'Four'})

print("\nInitial Dictionary: ", Dict1)
print("\nUpdated Dictionary: ", Dict2)
##################################################################################################################

'''
Program to sort the elements of the Dictionary:
'''

# Sorting Dictionary by Keys:
Dict = {'a': 2, 'b': 56, 'c': 32, 'd': 24}

for key in sorted(Dict.keys()):
    print("Sorted by Keys: %s %s" % (key, Dict[key]))

# Sorting Dictionary by Values:
Dict = {'a': 2, 'b': 56, 'c': 32, 'd': 24}

for key, value in sorted(Dict.items(), key=lambda item: item[1]):
    print("Sorted by Values: %s %s" % (key, value))
###############################################################################

# Function to Sort Elements of the Dictionary:


def dictionary():
    key_value = {}

    # Initialize value
    key_value[2] = 56
    key_value[1] = 2
    key_value[4] = 24
    key_value[3] = 32

    print("\nKeys and Values sorted in",
          "alphabetical order by the key:")

    # sorted(key_value) returns an iterator over the  Dictionary’s value sorted in keys.
    for i in sorted(key_value):
        print((i, key_value[i]), end=" ")


def main():
    # function calling
    dictionary()


# main function calling
if __name__ == "__main__":
    main()
####################################################################################################################
