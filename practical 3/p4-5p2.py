import math
#the area of a square program
length_square = float(input('Insert length of square: '))
area_of_square = ((length_square) ** 2)

if length_square < 0:
    print('Length must be >= 0. Please try again.')
else:
    print('The area of the square is ' + str(area_of_square))


#volume of a cube program
length_cube = float(input('Insert length of cube: '))
volume_of_cube = ((length_cube) ** 3 )

if length_cube < 0:
    print('Length must be >= 0. Please try again.')
else:
    print('The volume of the cube is ' + str(volume_of_cube))

#area of a circle program
radius_of_circle = float(input('Insert radius of circle: '))
pi = math.pi
area_circle = (pi * (float(radius_of_circle) ** 2))
if radius_of_circle < 0:
    print('Radius must be >= 0. Please try again.')
else:
    print('The area of the circle is:', round(area_circle))

#volume of sphere program
radius_sphere = float(input('Insert radius of sphere: '))
pi = math.pi
volume_sphere = (4.0 / 3.0) * pi * (float(radius_sphere) ** 3)

if radius_sphere < 0:
    print('Radius must be >= 0. Please try again')
else:
    print('The volume of the sphere is:', round(volume_sphere, 2))

#program volume of a cylinder
radius_cylinder = float(input('Insert height OR radius of cylinder: '))
height_cylinder = radius_cylinder
pi = math.pi
volume_cylinder = pi * float(radius_cylinder) ** 2 * float(height_cylinder)

if radius_cylinder < 0:
    print('Radius or height must be >= 0. Please try again.')
else:
    print('The volume of the cylinder is:', round(volume_cylinder, 2))

