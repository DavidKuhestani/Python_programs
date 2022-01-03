
"""
Define a function
    return count of string('code')

get user input
call function and print number of times the substring appeared in the string
"""

def check_string(string):
    return string.count('code')

string = input("Enter a string: ")
print('"code" appeared', check_string(string), 'times in the string.')

