"""
For number in range(2,20)
    for i in range(2, number)
        if number modulo i equals 0 then
            for x in range(1, number):
                if number modulo x equals 0 then:
                    print number equals x * number // x)
            break
    else
        print prime number
"""
for number in range(2,20):
    for i in range(2, number):
        if number % i == 0:
            for x in range(1, number):
                if number % x == 0:
                    print(number, 'equals', x, '*', number//x)
            break
    else:
        print(number, 'is a prime number')