#Programs that prints whether the number you typed is postitive, negative or == 0
number = float(input('Type a floating-point number: '))

if number > 0:
    print('You typed a positive number.')
elif number < 0:
    print('You typed a negative number.')
else:
    print('You typed 0.')