#id, nombre, tipo_cuenta, consignación
#validaciones
#mostrar

"""Captura de datos, mostrar información, variables, operaciones lógicas (condicionales)
loops, variables (contadoras, acumuladoras, auxiliares), funciones, lista(introducción)
"""

#Capturando la información desde el teclado
id = input("Digite su documento de identidad: ") #método
nombre = input("Nombre del cliente: ")
tipo_cuenta = input("Tipo de cuenta: ")
consignacion = float(input("Valor a consignar: "))

#Mostrando información por pantalla
print("Identificación: "+id)
print("Nombre        : {}".format(nombre))
print(f"Tipo de cuenta : {tipo_cuenta}")
print("Valor a consignar : {:,.5f}".format(consignacion))