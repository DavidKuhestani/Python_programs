
"""
prompt user for a number
while number does not equal 0:
    id number is less than 0
        assign a new variable the negative alue of number
    else
    assign the new variable the positive value of number
    cube root = 0
    while cube root ** 3 < new_variable:
        increment cube root by 1
    if cube root ** 3 == new_variable:
        if number is less than 0:
            cube_root equals negative cube_root
        print cube root
    else
        print cube root is not perfect
    prompt user for another integer

"""


number = int(input("Enter an int you wish you calculate the cube root of: "))

while number != 0:
    if number < 0:
        number_2 = -number
    else:
        number_2 = number

        cube_root = 0
    while cube_root ** 3 < number_2:
        cube_root += 1
    if cube_root ** 3 == number_2:
        if number < 0:
            cube_root = -cube_root
        print('Cube root of', number, "is", cube_root)
    else:
        print(number, "is not a perfect cube")
    number = int(input("Enter an int you wish you calculate the cube root of (enter 0 to exit): "))
