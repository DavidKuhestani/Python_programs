"""
Prompt user for input
while user input >= 0
    total = 0
    for x in range 0 up to including the userinput
        total += x
    print the total
    prompt user for another integer
"""

user_input = int(input("Enter INT: "))

while user_input >= 0:
    total = 0
    for i in range(0, user_input + 1):
        total += i
    print(total)
    user_input = int(input("Enter another INT (Enter negative int to exit): "))








