"""
Define function
Calculate the number
if number is perfect, return

Get user input
Loop through all user input numbers to see if its perfect
    print the perfect numbers


"""

def isPerfect(number):
    divisibles = []
    perfect_numbers = []
    for i in range(1, number):
        if number % i == 0:
            divisibles.append(i)

    if sum(divisibles) == number:
        perfect_numbers.append(sum(divisibles))
        return perfect_numbers


number = int(input("Enter a positive number: "))
for x in range (1, number):
    if isPerfect(x):
        print(x , " is a perfect number")
