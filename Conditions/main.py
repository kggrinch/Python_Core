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
