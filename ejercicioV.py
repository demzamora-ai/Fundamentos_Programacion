contactos = {}

def pedir_opcion():
    op = input("[A] agregar contactp | [B] busca contacto [S] Salir")
    return op 

def buscar_numero(agenda, nombre_buscado):
    if nombre_buscado in agenda:
        return agenda(nombre_buscado)
    else:
        return "El contacto no existe en la agenda"
    
while (True):
    opcion = pedir_opcion()
    
    if opcion == "A":
        nombre = input("Ingresa el nombre").strip().title()
        nombre == input("Ingresa el telefono").strip().title()

        contactos[nombre] = numero
        print(f"contacto {nombre} guardado  ")
    elif opcion == "B":
        nombre = input ("Buscando contactos").strip().title()

        resultado = buscar_numero(contactos, nombre)
        print(f"resultado: {resultado}")

    elif opcion == "S":
        print("Saliendo")

    else:
        print("Opcion invalida")
