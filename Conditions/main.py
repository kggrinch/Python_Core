age = int(input("Enter age: "))

if age >= 100:
    print("You are to old to sign up.")
elif age >= 18: # can add parenthesis in the condition (age >= 18)
    print("You are now signed up.")
elif age < 0:
    print("You haven't been born yet.")
elif age >= 100:
    print("You are ")
else:
    print("You are under age.")

# booleans in if statements
for_sale = False
if for_sale:
    print("This item is for sale")
else:
    print("This item is not for sale")

# Conditional Expressions = A one-line shortcut for the if-else statement  (ternary operator). Print one or assign one of two values base on a condition.
#                           x if condition else y

# positive or negative
num = 5
string = "Positive" if num > 0 else "Negative"
print(string)

# even or odd
num2 = 6
string = "Even" if num2 % 2 == 0 else "Odd"
print(string)

# largest value
x = 3
y = 5
max_num = x if x >= y else y
print(max_num)

