"""
Define a function
    define another function
    convert parameter to lowercase string
    initialize variable
    iterate over string
        add characters to new variable
    return variable

    define another sub function
    check if the length of the string is one
        if it is, then return true
    else
        Compare the first and the last letters and check
        the remainder of the string
    return result

"""


def isPalindrome(s):
    """Checks if string s is a palindrome"""
    def toChars(s):
        """convert string to lowercase and removes non-letters"""
        s = s.lower()
        letterstring = ''
        for c in s:
            if c in 'abcdefghijlkmnopqrstuvwxyz':
                letterstring += c
        return letterstring
    def isPal(s):
        """checks if string s is a palindrom"""
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])
    return isPal(toChars(s))

str = input("Enter a string (empty string to exit): ")

while str != '':
    if isPalindrome(str):
        print(str, 'is a palindrome')
    else:
        print(str, 'is not a palindrome')
    str = input("Enter a string (empty string to exit): ")

print("Finished!")