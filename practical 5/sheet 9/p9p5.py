"""
Get combinations and possibilities from user
Calculate the factorial of n, k and (n-k)
solve the equation
print the factorial

"""
# Getting input from user for combinations.
combinations = int(input("Enter combinations: "))
# Getting input from user for possibilities e.g. a list of topings
possibilities = int(input("Enter possibilities: "))

# c = possibilities! * combinations!(possibilities-combinations)!

# Calculating n!
n = 1
for i in range(1, combinations + 1):
    n *= i
    # print(n)


# Calculating k!
k = 1
for i in range(1, possibilities + 1):
    k *= i
    # print(k)

# Calculating value (n-k) from formula and putting it in a variable z
z = combinations - possibilities


# Calculating value for y which is (n-k)! from formula
y = 1
for i in range(1, z+1):
    # print(i)
    y *= i

# Calculating final value of c which is the total number of the different combinations of toppings.
c = n/(k*y)

print("The total number of different combinations of toppings is {}: ".format(c))
