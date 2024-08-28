"""
Escribir un programa que resuelva la secuencia de Fibonacci a pedido del 
usuario. Deberá codificar una función fibonacci(numero), cuyo parámetro 
numero debe ser ingresado por el usuario y su tipo, al igual que en el ejercicio 
anterior, validado. La función debe encargarse de calcular la secuencia para 
dicho número. A continuación, una descripción matemática de la famosa 
secuencia
"""
def fibonacci(numero):

    secuencia = [0, 1]  # Los dos primeros números de la secuencia
    while len(secuencia) < numero:
        secuencia.append(secuencia[-1] + secuencia[-2]) 
    return secuencia[:numero]  

    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    
    secuencia = [0, 1]  
    for i in range(2, n):
        secuencia.append(secuencia[-1] + secuencia[-2]) 
    return secuencia

def validar_numero():
    while True:
        entrada = input(("Ingrese un numero entero: "))
        if entrada.isdigit():
            return int(entrada)
        else:
            print(("Por favor, ingrese un valor numerico válido. "))

numero = validar_numero()
resultado = fibonacci(numero)

print(f"La secuencia de Fibonacci hasta el número {numero} es: {resultado}")

#de manera recursiva
"""    total = 0
    if numero == 0:
        return 0
    elif numero == 1:
        return 1
    else:
        return fibonacci(numero-1) + fibonacci(numero- 2)
    """