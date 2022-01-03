"""
Define a function that takes two parameters
initialize a tuple
loop through the range of the smallest of the two parameters
    if both numbers modulo i equals 0 then
        append to tuple
    return divisors

prompt user for two ints
check if numbers are larger than 0
if they are:
    call function with the inputs as the two parameters for the function
    print tuple of common divisors
"""


def findDivisors(num1, num2):
    divisors = ()
    for i in range(1, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            divisors += (i,)
    return divisors

number1 = int(input('Enter a positive INT: '))
number2 = int(input('Enter another positive INT: '))

if number1 <= 0 or number2 <= 0:
    print("Numbers should be > 0.")
else:
    divisors = findDivisors(number1, number2)
    print('The common divisors of', number1, 'and', number2, 'are', divisors)


