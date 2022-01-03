"""
Program to print out the largest of two numbers inputted from the user
"""
def max (a, b):
    """Function that returns the largest of its two arguments"""
    if a > b:
        return a
    else:
        return b

#Acquiring two inputs from the user
number_1 = float(input('Enter a number: '))
number_2 = float(input('Enter a number: '))

biggest = max(number_1, number_2)
print('The largest of', number_1, 'and', number_2, 'is', biggest)