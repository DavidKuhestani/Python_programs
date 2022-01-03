"""
Define function
    if n equals 0
        print 2
    else
    f(n) = n + f(n-1)

get input from user
while input is larger or equal to 1:
    call fucntion
    reprompt input from user
exit

"""

def rec(n):
    if n == 1:
        print(2)
        return 2
    else:
        x = n + rec(n-1)
        print(x)
        return x

n = int(input("Enter an INT: "))
while n >= 1:
    rec(n)
    n = int(input("Enter an INT: "))
print("Exit!")