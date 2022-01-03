


user_input = int(input("Enter an INT: "))

while user_input >= 0:
    if user_input == 0:
        print("Sorry, the numbered entered is 0.")
    elif user_input == 1:
        print("Fibonacci of", user_input, "is 0")
    elif user_input == 2:
        print("Fibonacci of", user_input, "is 0, 1.")
    else:
        a = 0
        b = 1
        c = a + b
        print('Series is: ', a, ', ', b, sep="", end = "")
        for i in range(2, user_input):
            c = a + b
            print(',', c, end= " ")
            a = b
            b = c

    print()
    user_input = int(input("Enter another INT (negative INT to exit): "))
