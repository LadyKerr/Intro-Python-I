"""
List comprehensions are one cool and unique feature of Python.
They essentially act as a terse and concise way of initializing
and populating a list given some expression that specifies how
the list should be populated. 

Take a look at https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
for more info regarding list comprehensions.
"""

# 1. Write a list comprehension to produce the array [1, 2, 3, 4, 5]

y = []

for i in range(6): #range of 6 because python wont read the last value 6
    y.append(i)

print (y[1:]) #this will print from the second index 1, leaving out the first index 0
print()

# 2. Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

y = []

for x in range(10):
    y.append(x * x * x) #cube - the number multiplied by itself 3 times

print(y)
print()

# 3. Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".

a = ["foo", "bar", "baz"]

y = []

for i, v in enumerate(a): #enumerate returns the index & the value. by accessing the value I can copy the list
    y.append(v.upper())

print(y)
print()

# 4. Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

x = input("Enter comma-separated numbers: ").split(',')

y = []

for i in x:
    if int(i) % 2 == 0:
        y.append(int(i))

print(y)