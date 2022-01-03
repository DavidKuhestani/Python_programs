"""
initialize a counter = 0
Prompt user for a positive integer
while counter < input
    counter += 1
    total = counter + total
    counter increment
print(total)

"""
total = 0
counter = 0

number = int(input("Enter a number: "))
while counter <= number:
    total = total + counter
    counter += 1
print(total)