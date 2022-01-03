"""
Get three integers from user
Examine the numbers, if they are even numbers quit the program.
    else compare if x or y or z are the largest odd numbers
        print the largest odd number

"""

x = int(input('Enter an integer: '))
y = int(input('Enter an integer: '))
z = int(input('Enter an integer: '))

if x % 2 == 0:
    if y % 2 == 0:
        if z % 2 == 0:
            print("None of the integers provided are odd.")
        else:
            print(z)
    elif y > z or z % 2 == 0:
        print(y)
    else:
        print(z)
elif y % 2 == 0:
    if z % 2 == 0 or x > z:
        print(x)
    else:
        print(z)
elif z % 2 == 0:
    if x > y:
        print(x)
    else:
        print(y)
else:
    if x > y and x > z:
        print(x)
    elif y > z:
        print(y)
    else:
        print(z)

