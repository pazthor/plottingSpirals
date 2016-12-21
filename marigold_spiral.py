#!usr/bin/python
import cmath
from math import *

#Objetivo: devuelve en un arhivo una lista de puntos para graficar con gnuplot.
#ecuacion: Z = az + bz/ |z|
#donde a= exp(pi*i/4) = (1/sqr(2)(1 + i) y b = Conjugado(a)

def Z( z_before, def_of_a, def_of_b):
    a = def_of_a
    b = def_of_b
    z = z_before
    abs_of_z = abs(z_before)
    z = a*z + b*z/abs_of_z
    return z


def marigold_spiral():
    exp_of_pi = cmath.exp(cmath.pi * 1j)
    #another form: (1/sqr(2) ) ( 1 + 1*j)
    first_term = (1.0/ sqrt(2) ) * (1 + 1j)
   # first_term = exp_of_pi / 4.0
    conjugate_of_first =  first_term.conjugate()
    second_term = conjugate_of_first
    point_of_z= 1 + 0j
    list_of_points = []
    for iterator in range(1,1000,1):
        list_of_points.append(point_of_z)
        point_of_z = Z(point_of_z, first_term, second_term)

    return list_of_points

list_of_points = marigold_spiral()
print list_of_points

#save to file
output_file = open('pointsOfMarigoldSpiral.txt','w')
for point in list_of_points:
    output_file.write("%s %s\n" % (point.real, point.imag))
    
