# Canciòn: la vaca lola la vaca lola tiene cabeza y tiene cola

#1 ejercicio Propiedad Conmutativa para suma
def point_conmutativo(a, b):
    return a + b == b + a

#1 ejercicio Propiedad Conmutativa para multiplicación
def point_multiplicacion(a, b):
    return a * b == a * b

#1 ejercicio Propiedad asociativa para suma
def asociado_suma(a, b, c):
    return (a + b) + c == a + (b + c)

#1 ejercicio Propiedad asociativa para multiplicación
def asociados_de_multiplicacion(a, b, c):
    return (a * b) * c == a * (b * c)

#1 ejercicio Propiedad distributiva para multiplicación
def distribucion_disc(a, b, c):
    return a * (b + c) == (a * b) + (a * c)

#1 ejercicio Propiedad identidad para suma
def sumas_identidad(a):
    return a + 0 == a

#1 ejercicio Propiedad identidad para multiplicación
def multi_identidad(a):
    return a * 1 == a

#1 ejercicio Propiedad inverso para suma
def inversiones_suma(a):
    return a + (-a) == 0

#1 ejercicio Propiedad inverso para multiplicación
def inverso_multiplicacion(a):
    if a != 0:
        return a * (1/a) == 1
    return "Indeterminado"

#1 ejercicio Propiedad Cierre para suma
def cierre(a, b):
    return isinstance(a +b, (int, float))

#1 ejercicio Propiedad Cierre para multiplicacion
def cierre2_multiplicacion(a, b):
    return isinstance(a * b, (int, float))

# Mira los resultados!!
if __name__ == "__main__":
    print("Conmutativa Suma (4,6):", point_conmutativo(4,6))
    print("Conmutativa Multiplicación (6, 4):", point_multiplicacion(6,4))
    print("Asociativa Suma (2, 5, 3):", asociado_suma(2,5,3))
    print("Asociativa Multiplicación (7, 9, 8):", asociados_de_multiplicacion(7,9,8))
    print("Distributiva (5, 4, 2):", distribucion_disc(5,4,2))
    print("Identidad Suma (9):", sumas_identidad(9))
    print("Identidad Multiplicación (6):", multi_identidad(6))
    print("Inverso Suma (7):", inversiones_suma(7))
    print("Inverso Multiplicación (5):", inverso_multiplicacion(5))
    print("Cierre Suma (9, 1):", cierre(9,1))
    print("Cierre Multiplicación (3, 6):", cierre2_multiplicacion(3,6))
