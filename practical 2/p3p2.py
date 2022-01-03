#program that calculates the area of a square
length_square = 202048.83
area_square = length_square ** 2
print('Area of square:', round(area_square,2))

#program that calculates the volume of a cube
length_cube = 202048.83
volume_cube = length_cube ** 3
print('Volume of cube:', round(volume_cube,2))

#program that calculates the area of a circle
import math
radius_circle = 202048.83 / 2
pi = math.pi
area_circle = pi * (radius_circle ** 2)
print('Area of circle: ', round(area_circle,2))

#program that calculates the volume of a sphere
radius_sphere = 202048.83 / 2
pi = math.pi
volume_sphere = ((4 / 3) * pi * (radius_sphere ** 3))
print('Volume of sphere:', round(volume_sphere,2))

#program that calculates the volume of a cylinder
diameter_cylinder = 202048.83
height_cylinder = diameter_cylinder
radius_cylinder = diameter_cylinder / 2
pi = math.pi
volume_cylinder = pi * (radius_cylinder ** 2) * height_cylinder
print('Volume of cylinder:', volume_cylinder)
