"""
Prompt user for number
if number is less than 0
    print number was less than 0.
else
    factorial = 1
    for variable in range 1 up to and including number
        factorial =* variable
    print factorial.
"""

number = int(input("Enter number for which you you wish to calculate the factorial: "))
if number < 0:
    print("Error: Number entered was less than 0.")
else:
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    print("Factorial of", number, "is", factorial)
