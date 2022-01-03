"""
While the user prompts a positive number
check if number is divisible by 2, 3, 5 or 7.
if number is divisible by above mentioned numbers
print which numbers are divisible
"""

user_input = int(input("Type another an integer (negative number to exit): "))
while user_input >= 0:
        if user_input == 0:
            print("0 cannot be divided.")
            break
        if user_input % 2 == 0:
            print(user_input, "is divisible by 2.")
        if user_input % 3 == 0:
            print(user_input, "is divisible by 3.")
        if user_input % 5 == 0:
            print(user_input, "is divisible by 5.")
        if user_input % 7 == 0:
            print(user_input, "is divisible by 7.")

        user_input = int(input("Type another an integer (negative number to exit): "))