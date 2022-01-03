"""
Define a function
    convert string to lowercase
    find the index matching "xyz"
    create new variable and deduct 1 from the index above
    check if the new variable index does not equal "."
        return True
    else
        return False
"""

def match(s):
    string = s.lower()
    result = string.find("xyz")
    new_variable = int(result) - 1
    if string[new_variable] != ".":
        return True
    else:
        return False

user_input = input("Enter a string: ")
print(match(user_input))