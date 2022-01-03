"""
Define a function that takes two arguments as number and epsilon
define variables: step, root
calculate the square root of the number
    increment root += step
if abs(numb-root ** 2) is less than epsilon
    return root
else return failed message

prompt user for number
define epsilon
check if number is non-negative:
    print the returned value from the function (Squareroot)
else
    error message
"""


def squareroot(number, epsilon):
    step = epsilon ** 2
    root = 0
    while abs(number - root ** 2) >= epsilon and root <= number:
        root += step
    if abs(number - root ** 2) < epsilon:
        return root
    else:
        """If program fails to calculate squareroot of number
        then the value -1 will be returned
        """
        return -1

number = float(input("Enter the float number you wish to find the square root of: "))
epsilon = 0.01
if number > 0:
    print('The square root of ', number, 'is', squareroot(number, epsilon))
else:
    print('Sorry, you entered a negative number.')

