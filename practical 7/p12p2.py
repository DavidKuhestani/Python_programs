"""
define a function
    loop thorugh and calculate the fibonacci series

prompt user for a non negative INT
check if user input is positive
    if it is positive then pass the user input to the function and print the fib
else
    print error message
"""
#Program 2A
def fib(x):
    a = 0
    b = 1
    print(a, b, end=" ")
    for i in range(x - 2):
        c = a + b
        print(c, end=" ")
        a = b
        b = c
    exit()

#Program 2B
number = int(input("Enter a non-negative INT: "))
if number >= 0:
    print(fib(number))
else:
    print("Sorry, you entered a negative integer.")

