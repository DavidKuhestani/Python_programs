#Program to illustrate scoping in Python

def f(x):
    """Function that adds 1 to its argument and prints it out"""
    print('In function f:')
    x += 1
    y = 1
    a = x + y

    print('x is', x)
    print('y is', y)
    print('z is', z)
    print('a is', a)
    print('b is', b)
    return x



x, y, z, a, b = 5, 10, 15, 20, 2
#Adding two new variables, a and b.
# a and b will have new values in each section.

print('Before function f:')
print('x is', x)
print('y is', y)
print('z is', z)
print('a is', a)
print('b is', b)

#Use Z's new value (from function) in variable a.
z = f(x)
a = b + z

print('After function f:')
print('x is', x)
print('y is', y)
print('z is', z)
print('a is', a)
print('b is', b)
