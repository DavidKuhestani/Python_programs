"""
For number in range(2,20)
    for i in range(2, number)
        if number modulo i equals 0 then
            print number
            break
        else
            print prime number
"""

for number in range(2,20):
    for i in range(2, number):
        #In the nested loop when we encounter a even number,
        # it will print accordingly and stop the loop, then increment itself again.
        if number % i == 0:
            print(number, 'equals', i, '*', number//i)
            break
    else:
        print(number, 'is a prime number')