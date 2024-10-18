import math
#Ejemplo de hallar el x de una ecuación lineal, donde a y b son números ingresados por el usuario y r es el resultado de que debe dar y x el el valor que el programa debe mostrar.
#ax+b=r
print("EJEMPLO 1 - Ecuación Lineal")
print("ax+b=r")
a=int(input("Ingresa un numero para a: "))
b=int(input("Ingresa otro numero para b: "))
r=a+b

#Encontrando x
if a != 0:
    x = (r-b)/a
    print(f"El valor de x es: ", x)
else:
    print("a no puede ser 0")

#Ejemplo de hallar el x en una ecuación cuadrática usando factorización, donde a es 1,b es 5 ,c es 6 que son números ingresados por el usuario y se debe encontrar el valor de x.
#ax^2+bx+c=0
print()
print("EJEMPLO 2 - Ecuación Cuadratica")
print("ax^2+bx+c=0")
print("Se recomienda que a=1 b=5 c=6")
print()
a=int(input("Ingresa un numero para a: "))
b=int(input("Ingresa un numero para b: "))
c=int(input("Ingresa un numero para c: "))

#Encontrando x
for i in range(-abs(c), abs(c) + 1):
    if i != 0 and c % i == 0:
        j = c // i
    if i + j == b:
        x = -i
        print(f"x es ",x)
        break
else:
    print("No hay resultado")

#Ejemplo de hallar el x en una ecuación cuadrática usando formula cuadrática donde a=2,b=3,c=-2 y debe hallar el valor de x
#x=(-b±√(b^2 - 4ac))/2a
print()
print("EJEMPLO 3 - Ecuación Cuadratica")
print("x=(-b±√(b^2 - 4ac))/2a")
a=2
b=3
c=-2
print("Los valores son a=",a, "b=",b ,"y c=",c)

# Encontrar X
discriminante = b**2 - 4*a*c
if discriminante >= 0:
    x = (-b + math.sqrt(discriminante)) / (2 * a)
    print("La solución es: x =",x)
else:
    print("No hay resultado")
