#!usr/bin/python
import cmath
from math import *
#objetivo: devolver una lista de puntos en un archivo
#ecuacion: Z = z + i^dz / |z| donde d= floor(7 *rand
def Z(z_before, def_of_d):
    z = z_before
    d = def_of_d
    abs_of_z = abs(z)
    z = z_before + d * z /abs_of_z
    return z

def spring_spiral():
    z_before = 1 + 0j;
    one_half = 0.5
    list_of_points = []
    exp_of_5ij= 0
    for iterator in range(1,1000,1):
        exp_of_5ij = cmath.exp(one_half * 1j*iterator)
        second_term = exp_of_5ij*one_half
        list_of_points.append(z_before)
        z_before = Z(z_before,second_term)

    return list_of_points
list_of_points = spring_spiral()

output = open('pointsOfSpring.txt','w')
for point in list_of_points:
    output.write("%s %s\n" % (point.real, point.imag))
    

