

#program A and C)

def fact_recursive(n):
    if n < 0:
        return 'Error, INT is < 0.'
    elif n < 2:
        """Print is also to illustrate the recursion progress from basecase"""
        print(1)
        return 1
    else:
        """To illustrate the operation of the recursion and its progress 
        I add variable x and print it, comment it out and add the comment underneath
        to get the factorial through recursion for program a and b"""
        x = n * fact_recursive(n-1)
        print(x)
        return x
#return n * fact_recursive(n-1) This is for program a)


#Program B)

user_input = int(input("Enter a non-negative INT: "))
if user_input < 0:
    print("You entered an INT < 0.")
else:
    n = user_input
    print('The recursive factorial of', n, 'is', fact_recursive(n))
