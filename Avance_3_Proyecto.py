#Funciones de texto title(), capitalize(), upper(), lower(), strip()
#Operadores relacionales < > <= != >= == (True, False)
#Operadores lógicos and or not (True, False) 
#Operadores matemáticos (+-*/)

#BLOQUE DE FUNCIONES

def validar_documento_identidad():
    while True: 
        try:
            id = int(input("Digite su documento de identidad: "))
            if id < 0:
                print("¡Digite un documento de identidad correcto!")
                continue
            else:
                break
        except:
            print("¡El valor debe de ser numérico!")
            continue
    return id

def validar_tipo_cuenta():
    while True:
        tipo_cuenta = input("Tipo de cuenta (CORRIENTE - AHORROS - CDT): ").upper() 
        if tipo_cuenta != "CORRIENTE" and tipo_cuenta != "AHORROS" and tipo_cuenta != "CDT" :
            print("¡Tipo de cuenta {} no existe - Digite un tipo de cuenta correcto!".format(tipo_cuenta))
            continue
        else:
            print ("Tipo de cuenta {} sí existe - Continuar con consignación".format(tipo_cuenta))
            break
    return tipo_cuenta

def validar_valor_consignacion():
    while True: 
        try:
            consignacion = float(input("Valor a consignar: "))
            if consignacion < 3000 or consignacion > 3000000:
                print("¡No es posible realizar la consignación - Tope mínimo 3.000 y Tope máximo 3.000.000!")
                print("¡Volver a ingresar valor a consignar!")
                continue
            else:
                print("¡Consignación realizada con éxito!")
                break
        except:
            print("¡El valor debe de ser numérico!")
            continue
    return consignacion

#BLOQUE PRINCIPAL

id = validar_documento_identidad()
nombre = input("Nombre del cliente: ").title()
tipo_cuenta = validar_tipo_cuenta()
consignacion = validar_valor_consignacion()

#Mostrando información por pantalla
print("")
print("INFORNACIÓN DE CONSIGNACIÓN")
print("Valor consignado               : {:,.2f}".format(consignacion))
print("Identificación                 : {}".format(id))
print("Nombre                         : {}".format(nombre))
print(f"Tipo de cuenta                 : {tipo_cuenta}")     

