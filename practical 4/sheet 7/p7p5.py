7"""
Assign two variables, total and count
Loop through the numbers up to 10000
    if the numbers are divisible by 3 or 5
        then number for counter should be added with the total
print total
"""
total = 0
count = 0

for count in range(10001):
    if count % 3 == 0 or count % 5 == 0:
        total = total + count
print(total)
