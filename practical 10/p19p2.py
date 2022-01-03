"""
Make a list representing numbers 0-15

define a function with 2 parameters
    convert string to upper case
    loop through chars in string(reversed):
        calculate the numbers (index of list) with base
    return number

prompt user for two arguments
print(call function)
"""

values = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A',
        'B', 'C', 'D', 'E', 'F']

def calculate(string, base):
    new_string = string.upper()
    i = 1
    new_number = 0
    for char in new_string[::-1]:
        new_number += int(values.index(char)) * i
        i *= base
    return new_number


user_string = input("Enter a string or INT you would like to convert to base 10: ")
user_base = int(input("Enter the base of the string/INT you provided: "))
print('The number', user_string, "in base", user_base, "is", calculate(user_string, user_base),"in base 10")


