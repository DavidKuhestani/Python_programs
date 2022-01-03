"""
If year is equal or larger than 0 then
    if (uear modulo 4 equals 0 and year modulo 100 does not equal 0) or year modulo 400 equals 0 then
        print year is a leaper year
    else
    print year is not a leap year
else
tell user that year must be equal or larger to 0.
"""

year = int(input('Enter a year: '))

if year >= 0:
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print(year, 'is a leap year.')
    else:
        print(year, 'is not a leap year.')
else:
    print('Year must be greater than 0')
