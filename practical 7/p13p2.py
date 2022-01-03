#program to print out the largest of two numbers from the user
#Uses a function named max
#uses max in a print statement

def max(a, b):
    """Function that returns the largest of its two args"""
    if a > b:
        return a
    else:
        return b

#Prompting user for two INTs
number_1 = float(input('Enter a number: '))
number_2 = float(input('Enter a number: '))

print('The largest of', number_1, 'and', number_2, 'is', max(number_1, number_2))