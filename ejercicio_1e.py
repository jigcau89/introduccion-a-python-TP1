"""
Escribir un procedimiento numeros_par_impar(entrada) que, dada una lisa de 
números, eleve cada elemento impar en ella al cuadrado y los mueva a otra lista 
e imprima ambas. La lista de números la ingresa el usuario en forma de números 
separados por coma.
Suponiendo que el usuario ingresa la siguiente lista:
1,2,3,4,5,6,7,8,9
Entonces, la salida del programa debería ser:
2,4,6,8
1,9,25,49,81
"""

def numeros_par_impar(entrada):
    # Divide la cadena en una lista de números
    numeros = list(map(int, entrada.split(',')))
    
    numeros_impares = []   # Lista para los números impares
    numeros_pares = []   # Lista para los números pares
    
    # Recorre la lista de números
    for numero in numeros:
        # Si es impar, elevo al cuadrado y añado a la lista de impares
        if numero % 2 != 0:
            numeros_impares.append(numero ** 2)
        # Si es par, añado a la lista de pares
        else:
            numeros_pares.append(numero)
    
    # Imprime las listas de números
    print('--------------------------------------------')
    print('Numero pares e impares ingresados')
    print('Números impares:', numeros_impares)
    print('Números pares:', numeros_pares)
    print('--------------------------------------------')
    print(f'- Números Pares:',','.join(map(str, numeros_pares)))
    print(f'- Números Impares al Cuadrado:',','.join(map(str, numeros_impares)))

entrada_usuario = input("Ingresa una lista de números separados por coma (,): ")
numeros_par_impar(entrada_usuario)

