# logical operators = used on conditional statements

#   and = check two or more conditions if true
#          0 0 | 0
#          1 0 | 0
#          0 1 | 0
#          1 1 | 1

#   Or = check if at least one condition is true
#          0 0 | 0
#          1 0 | 1
#          0 1 | 1
#          1 1 | 1

#   Not = True if condition if false, and vice versa
#          0 | 1
#          1 | 0

#  == - True if two values are equal to each other
#          0 0 | 1
#          1 0 | 0
#          0 1 | 0
#          1 1 | 1

#  != - True if two values are not equal to each other
#          0 0 | 0
#          1 0 | 1
#          0 1 | 1
#          1 1 | 0




temp = 25

# AND example
if temp > 0 and temp < 30:
    print("The temperature is good")
else:
    print("The temperature is bad")

# OR example
if temp <= 0 or temp >= 30:
    print("The temperature is bad")
else:
    print("The temperature is good")

# Not example
sunny = True
if not sunny:
    print("It is sunny outside.")
else:
    print("It is cloudy outside.") 
