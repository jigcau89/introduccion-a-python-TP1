import time
from calendar import isleap

#calcular si es un año bisiesto
def anio_bisiesto(anio):
    return isleap(anio)

#calcular el numero de dias de cada mes
def calcular_dias_mes(mes, anio_bisiesto):
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif mes in [4, 6, 9, 11]:
        return 30
    elif mes == 2:
        return 29 if anio_bisiesto else 28
    
# Función para validar que la edad ingresada sea numérica
def validar_edad():
    while True:
        edad = input("Ingrese su edad: ")
        if edad.isdigit():
            return int(edad)
        else:
            print("Por favor, ingrese una edad válida (número).")


def calcular_edad_en_dias(hora_local, anio_comienzo, anio_fin):
    dias = 0
    
    # calcular los dias transcurridos en los años bisiestos y no bisiestos
    for a in range(int(anio_comienzo), int(anio_fin)):
        if (anio_bisiesto(a)):
            dias = dias + 366
        else:
            dias = dias + 365
    
    # agregar los días transcurridos en este año
    for m in range(1, int(hora_local.tm_mon)):
        dias = dias + calcular_dias_mes(m, anio_bisiesto(hora_local.tm_year))
    
    # agregar los días transcurridos en este mes
    dias = dias + int(hora_local.tm_mday)
    
    return dias