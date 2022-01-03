"""
Prompt user for positive integer
factorial = 1
if the user input is larger than 0:
    for i in the range from 1 up to and including user_input)
        factorial * i
    print the factorial
"""

user_input = int(input("Enter a positive integer: "))
factorial = 1
if user_input > 0:
    for i in range(1, user_input + 1):
        factorial *= i
    print("The factorial of the number", user_input, "is", factorial)
