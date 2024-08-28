'''
Dadas dos listas, lista1 y lista2, escribir un método listas_diferencia(lista1, lista2) que tome ambas como parámetros e imprima 
dos listas, cada una con:
    i. Los elementos en común, en orden inverso.
    ii. Los elementos no comunes, en orden alfabético.
El programa debería arrojar el siguiente resultado:
    listas(['b', 'a', 'c'], ['e', 'b', 'd', 'c'])
    ['c', 'b']
    ['a', 'd', 'e']

'''
# Método
def listas_diferencia(lista1, lista2):
    # Crea lista de elementos comunes
    elementos_comunes = []
    # Busca y encuenra elementos comunes
    for elemento in lista1:
        if elemento in lista2 and elemento not in elementos_comunes:
            elementos_comunes.append(elemento)
    # Ordena a los elementos en común de forma inversa
    elementos_comunes.sort(reverse = True)
    
    # Crea lista de elementos no comunes
    elementos_no_comunes = []
    # Busca  y encuentra elementos no comunes 
    for elemento in lista1:
        if elemento not in lista2 and elemento not in elementos_no_comunes:
            elementos_no_comunes.append(elemento)
    for elemento in lista2:
        if elemento not in lista1 and elemento not in elementos_no_comunes:
           elementos_no_comunes.append(elemento)
    # Ordena elementos no comunes por orden alfabético
    elementos_no_comunes.sort()

    # Imprime las listas dadas, de elementos comunes y no comunes
    print("----------------------------------------------------------")
    print('LISTAS DADAS')
    print("----------------------------------------------------------")
    print(f'- listas = [{lista1} , {lista2}]')
    print("----------------------------------------------------------")
    print(f'- Elementos Comunes (Orden Inverso):', elementos_comunes)
    print("----------------------------------------------------------")
    print(f'- Elementos No Comunes (Orden Alfabético):', elementos_no_comunes)
    print("----------------------------------------------------------")

# Ejemplo   
lista1 = ['b', 'a', 'c']
lista2 = ['e', 'b', 'd', 'c']

# Llama al método
listas_diferencia(lista1, lista2)