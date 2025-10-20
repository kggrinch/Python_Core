# Strings Functions

name  = "john Doe"
phone = "123-456-7890"

# length of a string
name_length = len(name)

# first occurrence of a character
# example: John Doe | find(" ") = 4 | find("o") = 1 | find("6") = -1
first_occurrence = name.find(" ")

# last occurrence of a character
# example: John Doe | find(" ") = 4 | find("o") = 6 | find("6") = -1
# note: empty spaces count as characters
last_occurrence = name.rfind("o")

# Capitalize the first char in a string
name_capitalized = name.capitalize()

# Makes all characters uppercase
name_uppercase = name.upper()

# Makes all characters lowercase
name_lowercase = name.lower()

# Contains only digits
is_digits = name.isdigit()

# Contains only alphabetical characters
# note: empty spaces do not count as alphabetical characters
is_alpha = name.isalpha()

# Count number of occurrences of a character in a string
dashes = phone.count('-')

# replace any characters with another
dashes_replaced = phone.replace('-', ' ')

# Outputs
print(name_length)
print(first_occurrence)
print(last_occurrence)
print(name_capitalized)
print(name_uppercase)
print(is_digits)
print(is_alpha)
print(dashes)
print(dashes_replaced)


# String Indexing - accessing elements of a sequence using [] (indexing operation)
#                   [start : end : step]
#                   start = where you start (inclusive) 
#                   end = where you end (exclusive)
#                   step = access character by a given step
credit_number = "1234-5678-9012-3456"
print(credit_number[0])
print(credit_number[0:4]) # first four digits of the credit number
print(credit_number[:4]) # can omit the starting position and python will assume that the start is the beginning of the strings

print(credit_number[5:9])
print(credit_number[5:]) # can omit the last position with colon and python will assume the rest of the string

# negatives
print(credit_number[-1]) # get last character of the string using negative
print(credit_number[-2]) # get char from reverse

# steps
print(credit_number[::]) # assuming everything from beginning to end
print(credit_number[::2]) # accessing character by 2 steps

# reversing a string (negatives)
print(credit_number[::-1]) # reverses the string (start to end with -1 step)

# A list of a bunch of string methods
# print(help(str))