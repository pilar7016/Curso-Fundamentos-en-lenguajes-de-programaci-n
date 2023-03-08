#Funciones de texto title(), capitalize(), upper(), lower(), strip()
#Operadores relacionales < > <= != >= == (True, False)
#Operadores lógicos and or not (True, False) 
#Operadores matemáticos (+-*/)

#Capturando la información desde el teclado
id = input("Digite su documento de identidad: ") #método
nombre = input("Nombre del cliente: ").title()
tipo_cuenta = input("Tipo de cuenta: ").upper()
if tipo_cuenta == "CORRIENTE" :
    print("¡Tipo de cuenta sí existe - Continuar con consignación!")
    consignacion = float(input("Valor a consignar: "))
    if consignacion <= 30000:
        print("¡No es posible realizar la consignación - Tope mínimo 3.000!")
    elif consignacion >= 3000000:
        print("¡No es posible realizar la consignación - Tope máximo 3.000.000!")
    else:
        print("¡Consignación realizada con éxito!")
        #Mostrando información por pantalla
        print("Valor consignado        : {:,.2f}".format(consignacion))
        print("Identificación          : "+id)
        print("Nombre                  : {}".format(nombre))
        print(f"Tipo de cuenta         : {tipo_cuenta}")     
elif tipo_cuenta == "AHORROS" :
    print("¡Tipo de cuenta sí existe - Continuar con consignación!")
    consignacion = float(input("Valor a consignar: "))
    if consignacion <= 30000:
        print("¡No es posible realizar la consignación - Tope mínimo 3.000!")
    elif consignacion >= 3000000:
        print("¡No es posible realizar la consignación - Tope máximo 3.000.000!")
    else:
        print("¡Consignación realizada con éxito!")  
        #Mostrando información por pantalla
        print("Valor consignado       : {:,.2f}".format(consignacion))
        print("Identificación          : "+id)
        print("Nombre                  : {}".format(nombre))
        print(f"Tipo de cuenta         : {tipo_cuenta}")       
else:
    print("¡Tipo de cuenta no existe - Consignación cancelada!")
    
        

        


