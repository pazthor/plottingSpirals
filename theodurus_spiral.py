#!usr/bin/python
import cmath
from math import *
from random import *
#objetivo: devolver una lista de puntos en un archivo
#ecuacion: Z = z + i^dz / |z| donde d= floor(7 *rand
def Z(z_before):
    z = z_before
    d = floor(7 * random() )
    i_to_d = 1j ** d
    abs_of_z = abs(z)
    z = z_before + i_to_d * z /abs_of_z
    return z

def theodorus_spiral():
    z_before = 1 + 0j;
    list_of_points = []
    for iterator in range(1,5000,1):
        list_of_points.append(z_before)
        z_before = Z(z_before)

    return list_of_points
list_of_points = theodorus_spiral()

output = open('pointsOfTheodorus.txt','w')
for point in list_of_points:
    output.write("%s %s\n" % (point.real, point.imag))
    

