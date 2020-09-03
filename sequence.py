n = int(input("Enter the length of the sequence: ")) # Do not change this line

# Design an algorith that generates the first n numbers
# in the following sequence: 1,2,3,6,11,20,37

# the next sequence number is the number
# of the previous 3 numbers

# n gives me the sequence of the n sums in the sequence
# commen

for i in range(1, n + 1):
    if i == 1:
        current = first = i
    elif i == 2:
        current = second = i
    elif i == 3:
        current = third = i
    else:
        current = first + second + third
        first, second, third = second, third, current
    print(current)

# i = 1
# first = 1, current = 1

# i = 2
# second = 2, current = 2

# i = 3
# third = 3, current = 3

# current = first + second + third  >> 1 + 2 + 3 = 6
# current = 6

# Endurskilgreini ég first, second og third
# first = second, first = 2
# second = third, second = 3
# third = current, third = 6

# Fer aftur í gegnum loop-una með 

# i = 4
# first = 2
# second = 3
# third = 6
# current = 2 + 3 + 6 = 11
# ENDURSKILGREINI first, second, third
# first = second = 3, second = third = 6, third = current = 11 




