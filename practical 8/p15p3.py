"""
Define function
    if n equals 0 return 13
    elif n equals 1 return 8
    else
        return f(n-2) + 13 x f(n-1)

get user input
if user input is larger or equals to 0:
    for i in range(user input):
    print(function(i)
    reprompt user
exit
"""
def rec(n):
    if n == 0:
        return 13
    if n == 1:
        return 8
    else:
        return rec(n-2) + 13 * rec(n-1)


n = int(input("Enter an INT: "))
while n >= 0:
    for i in range(n + 1):
        print(rec(i))
    n = int(input("Enter an INT: "))
print("Exit!")
