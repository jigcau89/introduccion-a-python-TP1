"""
3_a. Escribir una función suma(numero) que resuelva la siguiente suma, asumiendo 
que numero = 10:
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
En el programa que invoque dicha función:
i. El usuario debe poder ingresar el valor del parámetro numero.
ii. Debe validarse que el dato ingresado por el usuario corresponda a 
un dígito, y no a otro tipo de dato como un carácter.
iii. El cálculo debe realizarse utilizando algún tipo de bucle (ej: for, 
while).
BONUS: Luego, codificar una función equivalente que utilice recursividad.
"""

def suma(numero):
    total = 0
    for i in range(1, numero + 1):
        total += i
    return total

def validar_numero():
    while True:
        entrada = input(("Ingrese un numero entero: "))
        if entrada.isdigit():
            return int(entrada)
        else:
            print(("Por favor, ingrese un valor numerico válido. "))

numero = validar_numero()
resultado = suma(numero)
print(f"La suma recursiva de los numeros del 1 al {numero} es: {resultado}")

#bonus
def suma_recursiva(numero):
    if numero == 1:  
        return 1
    else:
        return numero + suma_recursiva(numero - 1) 