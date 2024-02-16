import json


def guardar_datos(datos):
    with open("usuarios.json", "w") as archivo:
        json.dump(datos, archivo, indent=2)

##--------------------------------------------------------- Creacion de funciones --------------------------------------------------------------------------
def crear_usuario():
    with open("usuarios.json", "r") as archivo:
        datos = json.load(archivo)

        ti = input ("Ingrese documento de identificacion del usuario: ")
        nombre = input("Ingrese el nombre del usuario: ")
        direccion = input("Ingrese la direccion del usuario: ")
        telefono = input("Ingrese el telefono del usuario: ")
        categoria = input("Ingrese la categoria del usuario: ")

    datos["usuarios"]["ti"] = ti
    datos["usuarios"]["nombre"] = nombre
    datos["usuarios"]["direccion"] = direccion
    datos["usuarios"]["telefono"] = telefono
    datos["usuarios"]["categoria"] = categoria
    guardar_datos(datos)
    print("El usuario se guardo con exito.")

def editar_usuario():
    with open("usuarios.json", "r") as archivo:
        datos = json.load(archivo)

        ti = input ("Ingrese el nuevo documento de identificacion del usuario: ")
        nombre = input("Ingrese el nuevo nombre del usuario: ")
        direccion = input("Ingrese la nueva direccion del usuario: ")
        telefono = input("Ingrese el nuevo telefono del usuario: ")
        categoria = input("Ingrese la nueva categoria del usuario: ")

    datos["usuarios"]["ti"] = ti
    datos["usuarios"]["nombre"] = nombre
    datos["usuarios"]["direccion"] = direccion
    datos["usuarios"]["telefono"] = telefono
    datos["usuarios"]["categoria"] = categoria
    guardar_datos(datos)
    print("El usuario se actualizo con exito.")

def eliminar_usuario():
    with open("usuarios.json", "r") as archivo:
        datos = json.load(archivo)

        ti = ""
        nombre = ""
        direccion = ""
        telefono = ""
        categoria = ""

    datos["usuarios"]["ti"] = ti
    datos["usuarios"]["nombre"] = nombre
    datos["usuarios"]["direccion"] = direccion
    datos["usuarios"]["telefono"] = telefono
    datos["usuarios"]["categoria"] = categoria

    guardar_datos(datos)
    print("El usuario se elimino con exito.")

def asignar_categoria():
    with open("usuarios.json", "r") as archivo:
        datos = json.load(archivo)
        if datos["usuarios"]["ti"]=="":
            print("No hay un usuario registrado actualmente.")
        else:
            categoria = input("ingrese la nueva categoria del usuario (Nuevo, Regular o Leal): ")

            datos["usuarios"]["categoria"] = categoria
            print("La categoria se guardo con exito.")

    guardar_datos(datos)
   

##---------------------------------------------------------- Creacion de menus ------------------------------------------------------------------------------

def menu_principal():
    print("MENU PRINCIPAL")
    print("1. Administracion")
    print("2. Gestion de servicios")
    print("3. Reportes")
    print("4. Bonificacion de clientes leales")
    print("5. Salir del programa")

def menu_administracion_general():
    print("MENU ADMINISTRACION")
    print("1. Gestion usuarios")
    print("2. Historial de usuarios")
    print("3. Servicios")
    print("4. Fidelizacion de clientes")
    print("5. Salir")

def menu_administracion_gestion():
    print("GESTION USUARIOS")
    print("1. Crear usuario")
    print("2. Editar usuario")
    print("3. Eliminar usuario")
    print("4. Asignar categoria")
    print("5. Salir")

def menu_administracion_historial():
    print("HISTORIAL USUARIOS")
    print("1. Servicios utilizados")
    print("2.")
    print("3. Salir")

def menu_administracion_servicios():
    print("SERVICIOS")

def menu_administracion_fidelizacion():
    print("FIDELIZACION CLIENTES")    


    ##----------------------------------------------------------------- Uso de menus---------------------------------------------------------------------
def principal():
    menu_principal()
    while True:
        opcion = input("Ingrese una opcion (1-5): ")

        if opcion == "1":
            menu_administracion_general()
        elif opcion == "2":
            pass
        elif opcion == "3":
            pass
        elif opcion == "4":
            pass
        elif opcion == "5":
            break
        
def iniciar_administracion():
    menu_administracion_general()
    while True:
        opcion = input("Ingrese una opcion (1-5): ")
        
        if opcion == "1":
            crear_usuario()
        elif opcion == "2":
            editar_usuario()
        elif opcion == "3":
            eliminar_usuario()
        elif opcion == "4":
            asignar_categoria()
        elif opcion == "5":
            break



        


principal()

