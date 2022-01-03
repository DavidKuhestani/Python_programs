"""
Make different variables to represent a,e,i,o,u
Prompt user for string
while user input is not empty:
    for character in user input:
        if the character equals a:
            increment a count
        else if the character equals a:
            increment e count
        else if the character equals a:
            increment i count
        else if the character equals a:
            increment o count
        else if the character equals a:
            increment u count
    print letter counts
    prompt user for another string
"""


a = 0
e = 0
i = 0
o = 0
u = 0

user_input = input("Enter string: ")
while user_input != "":
    for char in user_input:
        if char == 'a':
            a += 1
        elif char == 'e':
            e += 1
        elif char == 'i':
            i += 1
        elif char == 'o':
            o += 1
        elif char == 'u':
            u += 1
    print("Letter a count:", a)
    print("Letter e count:", e)
    print("Letter i count:", i)
    print("Letter o count:", o)
    print("Letter u count:", u)
    user_input = input("Enter string (empty string to exit): ")




