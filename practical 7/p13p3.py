#program to print out the largest of two numbers entered by user
#Uses two functions: max and print_max

def print_max():
    """Function that prints out the largest of two numbers
    Uses the function max to find the largest """
    def max(a, b):
        if a > b:
            return a
        else:
            return b
    #prompt user for two numbers
    number_1 = float(input('Enter a number: '))
    number_2 = float(input('Enter a number: '))
    print('The largest of', number_1, 'and', number_2, 'is', max(number_1, number_2))
    return

print_max()

