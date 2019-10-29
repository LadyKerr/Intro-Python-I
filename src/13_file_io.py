"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# YOUR CODE HERE

with open("foo.txt") as file:
    read = file.read()
    print(read)
    file.close()


# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

# YOUR CODE HERE

#write a new file
with open("bar.txt", "w") as new_file:
    one = new_file.write("I just created a new file.")
    two = new_file.write("I like learning python.")
    three = new_file.write("I need to go to sleep.")

    print(f"Here is the new file: {one} {two} {three}")

#open & read the new file
with open("bar.txt") as bar:
    read = bar.read()
    print(read)