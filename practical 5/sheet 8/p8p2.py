"""
Get a number from the user
while i <= number
    j = 0
    while j <= number do
        print i * j
        increment j
    print new line
    increment i
"""

number = int(input("Enter an integer: "))

i = 1
while i <= number:
    j = 1
    while j <= number:
        print(i * j, " ", end = "")
        j += 1
    print()
    i +=1

