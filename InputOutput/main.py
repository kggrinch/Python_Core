## Comments

# Input
name = input("Enter name: ")
age = int(input("Enter age: ")) # Type cast string to int

# Output Printing Methods 

# Output printing
print("Hello World!")

# Print function automatically adds a newline after
# If you want to remove the newline do this
print("Hello ", end="")
print("World!")

# Automatically adds a space between first and second parameters
print("Hello:", name, "age: ", age) 

# String concatenation in print
print("Hello: " + name + "age: " + str(age))

# Formatted string literals (preferred)
print(f"Hello: {name} age: {age}")

# str.format() method
print("Hello: {} age: {}".format(name, age))

# Older style print (printf in java printing)
print("Hello: %s age %d" % (name, age))

# Multi-line print
print(F"""Hello: 
    {name}
    {age}""")

# Custom separators and endings
print("Hello:", name, "age:", age, sep=" | ", end="\n")


