# While Loops - execute code while condition is true

valid = True
count = 0
while(valid):
    if(count > 5): valid = False
    print(f"count: {count}")
    count += 1

answer = input("Enter a: ")
while(answer != 'a' and answer != 'A'):
    print("You did not enter a")
    answer = input("Enter a: ")
print("You entered a good job!")


# For loops
