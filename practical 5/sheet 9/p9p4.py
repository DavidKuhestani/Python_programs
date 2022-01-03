"""
prompt user for input

while user_input is larger or equal to zero:
    number equals user input
    factorial equals 1
    while number larger or equal to 1:
        calculate the factorial
        decrement number
    print the factorial
    prompt user for another integer

"""

user_input = int(input("Enter a positive integer: "))

while user_input >= 0:
    number = user_input
    factorial = 1
    while number >= 1:
        factorial *= number
        number -= 1
    print("The factorial of the number", user_input, "is", factorial)
    user_input = int(input("Enter a positive integer (negative to exit): "))


