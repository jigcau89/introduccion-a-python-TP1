"""
Escribir una función de nombre palabra_no_tiene_letras(palabra, 
letras_prohibidas), la cual retorne True si es que los caracteres que componen 
una palabra no se encuentran en una lista de caracteres prohibidos.
"""

def palabra_no_tiene_letras(palabra, letras_prohibidas):
    for letra in palabra:
        if letra in letras_prohibidas:
            return False
    return True

letras_prohibidas = ['a','b','c']
palabra = str(input("Ingrese una palabra para verificarla: "))

resultado = palabra_no_tiene_letras(palabra, letras_prohibidas)
print(resultado)
