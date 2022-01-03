"""
Prompt user for an integer
squareroot = 0
while squareoot ** 2 is less than integer
    increment squareroot

if squareroot equals integer
    print squareroot
else
    print not perfect square
"""
user_input = int(input("Enter an integer: "))

if user_input > 0:
    square_root = 0
    while square_root ** 2 < user_input:
        square_root += 1

    if square_root ** 2 == user_input:
        print('square root of', user_input, "is", square_root)
    else:
        print(user_input, 'is not a perfect square')





