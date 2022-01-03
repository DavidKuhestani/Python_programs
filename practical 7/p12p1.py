"""
define a function
    intialize factorial
    calculate factorial in a for loop
    return factorial

prompt user for input
if input is larger or equal to zero:
    pass the input to the function to calculate the factorial, and print it
else
    print error message

"""

#Program 1A
def fact(x):
    factorial = 1
    for i in range(1, x+1):
        factorial *= i
    return factorial

#Program 1B
user_input = int(input("Enter a non-negative INT: "))

if user_input >= 0:
    print("The factorial of", user_input, "is", fact(user_input))
else:
    print("The INT you entered is negative.")