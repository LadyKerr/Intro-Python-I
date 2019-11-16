"""
Python exposes a terse and intuitive syntax for performing 
slicing on lists and strings. This makes it easy to reference
only a portion of a list or string. 

This Stack Overflow answer provides a brief but thorough
overview: https://stackoverflow.com/a/509295

Use Python's slice syntax to achieve the following:
"""

a = [2, 4, 1, 7, 9, 6]

# Output the second element: 4:
a_slice = a[slice(1,2)] # OR a[1:2] => So will output from first and what us between that and the last index. last index wont be outputed
print()
print(f"This is the second element {a_slice}")

# Output the second-to-last element: 9
nine = a[-2:-1] #starts at -2 and ends before -1 which is also -2 so will output only 9
print()
print(f"This is the second to last element {nine}")


# Output the last three elements in the array: [7, 9, 6]
last_three = a[-3:] #starts at the third to last index and goes to the end
print()
print(f"These are the last three elements {last_three}")


# Output the two middle elements in the array: [1, 7]
print()
print(a[2:4])

# Output every element except the first one: [4, 1, 7, 9, 6]
not_first = a[1:]
print()
print(not_first)

# Output every element except the last one: [2, 4, 1, 7, 9]
print()
print(a[:-1])

# For string s...

s = "Hello, world!"

# Output just the 8th-12th characters: "world"
print(s)
print()
print(s[:]) #printing the entire string using slice()
print()
print(s[7:12]) 
#with strings the last index is included but the first index is not, so opposite of what lists/tuples do