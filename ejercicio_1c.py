"""
Escriba un procedimiento procesar_palabras(entrada) que acepte una 
secuencia de palabras separadas por coma, las ordene y las imprima. 
Suponiendo que la entrada provista al programa es la siguiente:
te,felicito,que,bien,actuas
La salida esperada es:
actuas,bien,felicito,que,te
"""

def procesar_palabras(entrada):
    # Divide la cadena en una lista de palabras
    palabras = entrada.split(',')
    print(palabras)
    
    # Ordena la lista de palabras
    palabras.sort()
    
    # Imprime las palabras en orden
    for palabra in palabras:
        print(palabra, end=', ')

entrada = "te,felicito,que,bien,actuas"
procesar_palabras(entrada)
