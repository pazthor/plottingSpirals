#!usr/bin/python
import cmath
from math import *

#objetivo: obtener una lista de puntos para graficar una spiral
#ecuacion: z = z + d/|z|
#donde d =  exp( pi * i * w *j^p, w = 0.3299 y p = 1.781237 y j=  "creo" iterador

def Z (z_before, def_of_d):
    z = z_before
    d = def_of_d
    abs_of_z = abs(z)
    z =  z + d/ abs_of_z
    return z
def trigonometric_spiral():
    w = 0.3299
    p = 1.781237
    list_of_points = []
    point_of_z = 1 + 0j
    for iterator in range(1, 1000, 1):
        j_to_p = iterator**p
        pi_i_w_p= cmath.pi * 1j * w * j_to_p
        exp_of_pi = cmath.exp(pi_i_w_p)
        point_of_z  = Z(point_of_z, exp_of_pi)
        list_of_points.append(point_of_z)

    return list_of_points

list_of_points = trigonometric_spiral()
output_file = open ('pointsOfTrigonometric.txt','w')
for point in list_of_points:
    output_file.write("%s %s\n" % (point.real, point.imag))
    
