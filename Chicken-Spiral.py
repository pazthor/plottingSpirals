#!usr/bin/python
import cmath 
from math import *

#objetivo sacar una lista de puntos (x,yi) donde la variable i se
#refiere a numeros complejos de la siguiente ecuacion
# z  = az + bz/|z|
#Donde: a = exp(pi * i) y b =  sin(j) + sin j/5


#tema de recursion

def f():
    #lo directo: a = exp(pi *1j)
    a = cmath.exp(pi *1j/4)
    #haciendo cambios porque limitaciones del lenguaje
    #
    #exponencial = exp(1)
    #a = exponencial**(pi*1j)
    z = 1 + 0j
    lis = []
    op = 0.0001

    for iterator in range(0,1000000,1):
        b = sin(iterator) + sin(iterator)/5.0
        z = a*b + (b*z)/abs(z+1) 
        lis.append(z)
        
    return lis

def Z (z_before , exp_pi, addsins):
    a = exp_pi
    #sin(ite ) + sin(ite )/5.0
    b = addsins
    abs_of_z= abs(z_before)
    z = z_before
    z = a*z + b*z/abs_of_z    
    return z
    
def m_inf():
    exp_pi = cmath.exp(pi *1j / 4.0)
    # en el codigo usan como primer iteracion numeros complejo
    # de este estilo, creo que debo seguir como lo hacen en
    # su implementacion, asi que lo cambio....
    addsins = 1+0j 
    z = 1 + 0j
    mi_list_inf = []
    for iterator in range(1,1000,1):
        mi_list_inf.append(z)
        z = Z( z,exp_pi, addsins )
        addsins = sin(iterator) + sin(iterator)/5.0
        
    return mi_list_inf

#guardar en lista
lis = m_inf()

print lis

#guarda en un archivo.
thefile = open('test.txt','w')
for item in lis:
    thefile.write("%s %s\n" %  (item.real, item.imag ) )
