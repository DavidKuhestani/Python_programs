"""
Define function taking two parameters
    convert both strings to lowercase
    check if string 1 ends with string 2 and opposite
    if string_1 ends with string_2
        return true
    elif string_2 ends with string_1
        return true
"""

def string(x,y):
    string_1 = x.lower()
    string_2 = y.lower()
    result_1 = string_1.endswith(string_2)
    result_2 = string_2.endswith(string_1)
    if result_1 is True:
        return result_1
    elif result_2 is True:
        return result_2


user_input = input("Enter first string: ")
user_input_2 = input("Enter first string: ")

print(string(user_input, user_input_2))

