"""
Define function
    if n == 1:
        print n
    else:
    x = formula
    print x

get user input
while user input is larger or equal to 1:
    call function
    prompt user for another int
exit
"""

def rec(n):
    if n == 1:
        print(n)
        return n
    else:
        #print function also allows us to see the recursion from basecase upwards
        x = rec(n-1) + (2 ** n-1)
        print(x)
        return x


n = int(input("Enter an INT: "))
while n >= 1:
    rec(n)
    n = int(input("Enter an INT: "))
print("Exit!")