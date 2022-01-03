"""
If year does not divisible 4 then it is a common year
else
if year is not divisible by 100 then it is a leaper year
else
if year is not divisible by 400 then it is a common year
else it is a leap year.

"""

year = int(input('Enter a year: '))

if year >= 0:
    if year % 4 != 0:
        print('It is a common year')
    elif year % 100 != 0:
        print('It is a leap year.')
    elif year % 400 != 400:
        print('It is a common year.')
    else:
        print('It is a leap year.')


