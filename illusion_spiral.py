#!usr/bin/python
import cmath
from math import *

#Objetivo: devuelve en un arhivo una lista de puntos para graficar con gnuplot.
#ecuacion: Z = az + bz/ |z|
#donde a= 0.6 + 0.8i y  b = 0.65 + 0.7599i

def Z( z_before, def_of_a, def_of_b):
    a = def_of_a
    b = def_of_b
    z = z_before
    abs_of_z = abs(z_before)
    z = a*z + b*z/abs_of_z
    return z


def illusion_spiral():
    first_term = 0.6 + 0.8j
    second_term = 0.65 + 0.7599j
    point_of_z= 1 + 0j
    list_of_points = []
    for iterator in range(1,1000,1):
        list_of_points.append(point_of_z)
        point_of_z = Z(point_of_z, first_term, second_term)

    return list_of_points

list_of_points = illusion_spiral()

#save to file
output_file = open('pointsOfIllusionSpiral.txt','w')
for point in list_of_points:
    output_file.write("%s %s\n" % (point.real, point.imag))
    
