"""
Define function
Initialise an empty tuple and another tuple including 1 and the number itself
loop through numbers to find common divisor, and append to tuple
add two tuples together and return that

prompt user for a number
if number is less or equal to 0
    print number should be larger than 0.
else
    call function
    print divisors
"""
def findDivisors(number):
    divisors = ()
    """Initialising another tuple for 1 and the number itself
    to add two tuples later on"""
    divisors_1 = (1, number)
    for i in range(2, number):
        if number % i == 0:
            divisors += (i,)
    new_divisors = divisors_1 + divisors
    return new_divisors


number = int(input('Enter a positive INT: '))
if number <= 0:
    print("Numbers should be > 0.")
else:
    divisors = findDivisors(number)
    print('The common divisors of', number, 'are', divisors)



