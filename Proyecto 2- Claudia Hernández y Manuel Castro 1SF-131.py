from calendar import c
from math import *
import matplotlib.pyplot as plt
import numpy as np

def ecu(x):
    y= x**3-2*x-5
    
    return(y)

def ecu2(x):
    y= -0.5*x**2 + 2.5*x + 4.5

    return (y)
    
def Secante():
    x1= float(input('Inserta el x1: '))
    x0= float(input("Inserta el x0: "))
    humanError=float(input("Inserta el error: ")) 
    max_iter= int(input("Inserta el maximo de iteraciones posibles: "))
    raiz=[]
    raiz.insert(0,0)
    i=0
    error=10
    


    while abs(error) > humanError and i<max_iter:
        x2= x1 - (ecu(x1)*(x1-x0))/(ecu(x1)-ecu(x0)) 
        raiz.append(x2)
        x0 = x1
        x1 = x2
        i = i + 1
        error = (raiz[i]-raiz[i-1]/raiz[i])
        print(x2)
    

def regulaFalsi():
    a= float(input('Inserta el valor para a: '))
    b= float(input("Inserta el valor para b: "))
    max_iter= int(input("Inserta el maximo de iteraciones posibles: "))

    if ecu2(a)*ecu2(b)>=0:
        print("ok... vamos a ver\n")
    
    c = a
    for i in range(max_iter):
        try:
            c =(a * ecu2(b)-(b*ecu2(a)))/(ecu2(b)-ecu2(a)) #try exeption
        except:
            print("\t\tNo funciona así, Introduzca otros valores para a y b la proxima vez\n")
            return(None)
        
        if ecu2(c) == 0:
            break
        elif ecu2(a)*ecu2(c)<0:
            b = c
        else:
            a = c
        print(c)
    
    

def main():
    seleccion_de_programa= int(input("Desea resolver el metodo por regula falsi o secante?\n 1= Regula Falsi, 2= Secante\n :"))

    while seleccion_de_programa >= 3 or seleccion_de_programa <=0:
        print("Solo aceptamos los numeros 1 y 2")
        seleccion_de_programa = int(input("Desea resolver el metodo por regula falsi o secante?\n 1= Regula Falsi, 2= Secante\n :"))

    if seleccion_de_programa ==1:
        regulaFalsi()
    elif seleccion_de_programa ==2:
        Secante()
    
    

def repetirPrograma():
    repetir_programa= int(input("¿Deseas hacer otra conversión? si= 1, no =2\n Tu respuesta:"))
    while repetir_programa !=2 and repetir_programa !=1:
        repetir_programa= int(input("Solo aceptamos el 1 y el 2\n ¿Deseas hacer otra conversión? si= 1 no= 2. \nTu respuesta: "))
    if repetir_programa == 1:
        main()
        repetirPrograma()
    else: print("\n\n\t\tGracias por participar de nuestro proyecto\n\n\n")



print("\n\t\t\tBienvenido a nuestro Parcial #2\n\n\t\t\tIntegrantes:\n\t\t\tClaudia Hernández\n\t\t\tManuel Castro\n\t\t\t1SF-131\n\n")
main()
repetirPrograma()


