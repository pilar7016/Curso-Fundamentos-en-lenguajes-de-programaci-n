#Funciones de texto title(), capitalize(), upper(), lower(), strip()
#Operadores relacionales < > <= != >= == (True, False)
#Operadores lógicos and or not (True, False) 
#Operadores matemáticos (+-*/)

#Capturando la información desde el teclado
id = input("Digite su documento de identidad: ") #método
nombre = input("Nombre del cliente: ").title()
tipo_cuenta = input("Tipo de cuenta: ").upper().strip()
consignacion = float(input("Valor a consignar: "))

#Mostrando información por pantalla
print("Identificación          : "+id)
print("Nombre                  : {}".format(nombre))
print(f"Tipo de cuenta         : {tipo_cuenta}")
print("Valor a consignar       : {:,.2f}".format(consignacion))

