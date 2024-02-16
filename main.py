import json

def cargar_datos():
    with open("usuarios.json", "r") as archivo:
        datos = json.load(archivo)
        return datos
print(cargar_datos)

def guardar_datos(datos):
    with open("usuarios.json", "w") as archivo:
        json.dump(datos, archivo, indent=2)


def menu_principal():
    print("Menu principal.")