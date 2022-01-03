"""
Define function
if n equals 1 then return 2
else
    return alghoritm

prompt user for input
while user input is larger or equal to 1:
    if user input is larger or equal to 1
        then do a for loop
            print(function call of each number of loop)
        prompt user for another int
"""

def rec(n):
    if n == 1:
        return 2
    else:
        return 2 * rec(n-1)


n = int(input("Enter an INT: "))
while n >= 1:
    if n >= 1:
        for i in range(1, n + 1):
            print(rec(i))
    else:
        print("You entered an INT <= 0.")
    n = int(input("Enter an INT: "))