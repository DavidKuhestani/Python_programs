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
        print("About to return True from isPal from the base case")
        if true then return true
    else
        assign variable =  s[0] == s[-1] and isPal(s[1:-1])
        print ’About to return result’, result, ’from isPal with argument’, s
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
            print("About to return True from isPal from the base case")
            return True
        else:
            result = s[0] == s[-1] and isPal(s[1:-1])
            print('About to return result', result, 'from isPal with argument', s)
            return result
    return isPal(toChars(s))

str = input("Enter a string (empty string to exit): ")

while str != '':
    if isPalindrome(str):
        print(str, 'is a palindrome')
    else:
        print(str, 'is not a palindrome')
    str = input("Enter a string (empty string to exit): ")

print("Finished!")