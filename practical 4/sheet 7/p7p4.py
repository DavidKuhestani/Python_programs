"""
Assign two variables, total and count
while the counter is less than 5000
    increment the counter and sum the counter with the total
print the total

"""
total = 0
count = 0

for count in range(10001):
    if count % 3 == 0 or count % 5 == 0:
        count += 1
        total = total + count
print(total)

