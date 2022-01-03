"""
Prompt user for an INT
If user_input is less or equal to zero
    print related message
else if user input equals 1
    print series is 0
else if series is 2
    print series is 0, 1
otherwise
    a, b, c = 0, 1, a + b
    print a and b
    while c <= user_input:
        print c
        a = b
        b = c
        c = a + b
"""
a = 0
b = 1

user_input = int(input("Enter INT: "))
if user_input <= 0:
    print('Number you entered is less or equal to 0.')
elif user_input == 1:
    print('Series is:', a)
elif user_input == 2:
    print('Series is: ', a, ', ', b, sep = "")
else:
    a = 0
    b = 1
    c = a + b
    print('Series is: ', a, ', ', b, sep="", end = "")
    while c <= user_input:
        print(",", c, end=" ")
        a = b
        b = c
        c = a + b