
# Variables = variables in python do not need to specify types. Note python does not assign default values automatically, you must use None keyword or
#             manually assign default values to variables


# Strings
first_name = "John"

# Integer
age = 25

# Floats - a float in python is basically a double in C++
# Precision 15–17 digits
price = 1.234567890123456789 

# Boolean
student = True

# null in python (can also be used as a default value)
null = None


if student:
    print(f"Name: {first_name} age: {age} tuition cost: {price}")
else:
    print(f"Name: {first_name} age: {age} tuition cost: {0}")



# type casting = the process of converting a value of one data type to another (string, integer, float, bool)

name = "bob"
age = 48
gpa = 3.9
student = True

# Data types
print("Data Types:")
print(type(name))
print(type(age))
print(type(gpa))
print(type(student))

# Explicit type casting - manually converting a data type into a different data type

# Integer to float
print(f"Before age: {age}")
age = float(age)
print(f"After age: {age}")

# float to integer
print(f"Before gpa: {gpa}")
gpa = int(gpa)
print(f"After gpa: {gpa}")

# boolean to string
print(f"Before student: {student}")
student = str(student)
print(f"After student: {student}")

# integer to bool
# if a value is != 0 then bool conversion will always be true
print(f"Before gpa: {gpa}")
gpa = bool(gpa)
print(f"After gpa: {gpa}")


# Implicit type casting - a data type is converted to a different data type automatically

# when an integer does mathematics on a float it will convert the value into a float
x = 2 
y = 2.0
x = x / y
print(x)