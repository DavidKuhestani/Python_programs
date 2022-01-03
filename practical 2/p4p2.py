import math
#the area of a square program
length_square = input('Insert length of square: ')
area_of_square = (int(length_square) ** 2)

print('The area of the square is ' + str(area_of_square))


#volume of a cube program
length_cube = input('Insert length of cube: ')
volume_of_cube = (int(length_cube) ** 3 )
print('The volume of the cube is ' + str(volume_of_cube))

#area of a circle program
radius_of_circle = input('Insert radius of circle: ')
pi = math.pi
area_circle = (pi * (int(radius_of_circle) ** 2))
print('The area of the circle is:', round(area_circle))

#volume of sphere program
radius_sphere = input('Insert radius of sphere: ')
pi = math.pi
volume_sphere = (4.0 / 3.0) * pi * (int(radius_sphere) ** 3)

print('The volume of the sphere is:', round(volume_sphere, 2))

#program volume of a cylinder
radius_cylinder = input('Insert height OR radius of cylinder ')
height_cylinder = radius_cylinder
pi = math.pi
volume_cylinder = pi * int(radius_cylinder) ** 2 * int(height_cylinder)
print('The volume of the cylinder is:', round(volume_cylinder, 2))

