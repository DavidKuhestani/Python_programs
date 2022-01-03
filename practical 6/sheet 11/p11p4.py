"""
Calculate the factorial of 2 * n
calculate the factorial of n + 1
calculate the factorial of n

Plot the numbers in the formula  = ((2*n)!)/((n+1)!*n!)
Print the Catalan number

"""

n = int(input("Enter an integer value:" ))

top_fac = 2*n
x = 1
for i in range(1, top_fac + 1):
    x *= i

bottom_fac_one = n + 1
y = 1
for i in range(1, bottom_fac_one + 1):
    y *= i

n_fac = 1
for i in range(1, n + 1):
    n_fac *= i

c = x / (y * n_fac)
print("The Catalan number for", n, "is", c)