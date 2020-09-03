num_int = int(input("Input a number: "))    # Do not change this line
# Fill in the missing code

# Design an algorithm that finds the maximum positive
# integer input by a user.

# input repeatedly numbers into the num_int
# break when you put in a negative value

# find the maximum value of all the numbers
max_int = 0

while num_int >= 0:
    if num_int > max_int:
        max_int = num_int
    num_int = int(input("Input a number: "))

print("The maximum is", max_int)    # Do not change this line
