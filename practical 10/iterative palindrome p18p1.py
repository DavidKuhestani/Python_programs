
"""
Define a function
loop through half of the characters in a string(not incl. the most mid char)
    check if the i-th index does not equal the oppsite character
        return false
return True

get user input
while user input is not empty
    if function call returns true
        then print is palindrome
    else
        is not palindrome
"""

def isPal(s):
    """checks if string s is a palindrom"""
    for i in range(0, int(len(s)/2)):
        if s[i] != s[len(s)-i-1]:
            return False
    return True


s = input("Enter a string (empty string to exit): ")

while s != '':
    if isPal(s):
        print(s, 'is a palindrome')
    else:
        print(s, 'is not a palindrome')
    s = input("Enter a string (empty string to exit): ")

print("Finished!")
