"""
Define function with 2 parameters:
Assign empty tuple
for i in range (1, min(num1, num2) + 1)
    if num 1 and num 2 modulo i equals zero then
        add i to the tuple
    return tuple

prompt user for two ints
check if user input is larger than 0
    print error message if not
else
    call function
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


