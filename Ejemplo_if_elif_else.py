#if elif else
estado = input("¿Como te sientes hoy?").title().strip()
if estado == "Feliz" or estado == "Contento" or estado == "Alegre":
    print("Me alegra mucho")
    ciudad = input("¿En qué ciudad vives?").title()
    if ciudad == "Cali":
        print("Con razón estás {}".format(estado))
    else:
        print("Pero {} también es muy chevere".format(ciudad))
elif estado == "Triste" or estado == "Despechado":
    print("Lo siento mucho")
elif estado == "Aburrido":
    print("Relajese")
else:
    print("Oh de veras")