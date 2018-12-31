
from peewee import *
from collections import OrderedDict
import csv

db = SqliteDatabase('Agenda.db')


class Contactos(Model):
    nombre = TextField()
    apellido = TextField()
    telefono = IntegerField()

    class Meta:
        database = db


def crear_conectar():
    db.connect()
    db.create_tables([Contactos],safe=True)


def tabla_menu():
    """ Tabla de Menu """
    opcion = None
    while opcion != 'q':
        tablaMenu = "\n     Tabla de Menu     "
        print(tablaMenu)
        print('*' *len(tablaMenu))
        for llave, valor in memu.items():
            print("{}) {}".format(llave, valor.__doc__))

        print("presione 'q' para salir")
        opcion = input("Opcion: ").lower().strip()

        if opcion in memu:
            memu[opcion]()
        elif opcion != 'q' :
            mensaje = "Opcion no valida."
            print('*' * len(mensaje))
            print(mensaje)
            print('*' * len(mensaje))

    mensaje = "Hasta pronto."
    print('*' * len(mensaje))
    print(mensaje)
    print('*' * len(mensaje))


def agregar_contacto():
    """ Agregar Contacto """
    print("Ingrese los siguientes datos: ")
    Nombre = input("Nombre: ").lower().strip()
    Apellido = input("Apellido: ").lower().strip()
    Telefono = input("Telefonico: ")
    if Nombre and Apellido and Telefono and input("Desea guardar [Yn]").lower().strip() != 'n':
        Contactos.create(nombre=Nombre, apellido=Apellido, telefono=Telefono)
        print("Has gurdado correctamente. ")
    else:
        print("No ha sido guardado.")


def buscar_contacto():
    """ Buscar Contacto """
    try:
        nombre = input("Ingrese nombre: ").lower().strip()
        contacto = Contactos.get( Contactos.nombre == nombre )
        titulo = "\n  Nombre    Apellido    Telefono  "
        print(titulo)
        print('*' * len(titulo))
        print("{}    {}    {}\n".format(contacto.nombre,
                                      contacto.apellido,
                                      contacto.telefono))
    except:

        mensaje="El contacto no existe."
        print('*'*len(mensaje))
        print(mensaje)
        print('*'*len(mensaje))


def ver_contactos():
    """ Ver todos los contactos """
    titulo = "\n  Nombre    Apellido    Telefono  "
    print(titulo)
    print('*' * len(titulo))
    for contacto in Contactos.select():
        print("{}    {}    {}".format(contacto.nombre,
                                      contacto.apellido,
                                      contacto.telefono))

    print()


def actualizar_contacto():
    """ Actualizar Contacto """
    print("\nEscriba el nombre del contacto que desea actualizar: ")
    nuevo_nombre = ""

    try:
        nombre = input("nombre: ").lower().strip()
        contacto = Contactos.get(Contactos.nombre == nombre)
        titulo = "\n  Nombre    Apellido    Telefono  "
        print(titulo)
        print('*' * len(titulo))
        print("{}    {}    {}\n".format(contacto.nombre,
                                        contacto.apellido,
                                        contacto.telefono))
        opcion = input("Desea actulizar [Yn]:  ").lower().strip()
        if opcion == 'y':
            opcion = input("Desea actualizar el nombre [Yn]: ")
            if opcion == 'y':
                nuevo_nombre = input("Nuevo nombre: ").lower().strip()
                Contactos.update(nombre=nuevo_nombre).where(Contactos.nombre == nombre).execute()
                print("El nombre ha sido actualizado.")
            opcion = input("Dease actuallizar apellido [Yn]: ")
            if opcion == 'y':
                nuevo_apellido = input("Nuevo apellido: ").lower().strip()
                Contactos.update(apellido=nuevo_apellido).where(Contactos.nombre == nombre).execute()
                print("El apellido ha sido actualizado.")
            opcion = input("Desea actualizar numero de telefono [Yn]: ")
            if opcion == 'y':
                nuevo_telefono = input("Nuevo numero de telefono: ")
                Contactos.update(telefono=nuevo_telefono).where(Contactos.nombre == nombre).execute()
                print("El numero telefonico ha sido actualizado.")
        print()
    except:
        mensaje = "El contacto no existe."
        print('*' * len(mensaje))
        print(mensaje)
        print('*' * len(mensaje))


def borrar_contacto():
    """ Borrar Contacto """
    try:
        print("\nEscriba el nombre del contacto que desea borrar: ")
        nombre = input("nombre: ").lower().strip()
        contacto = Contactos.get(Contactos.nombre == nombre)
        titulo = "\n  Nombre    Apellido    Telefono  "
        print(titulo)
        print('*' * len(titulo))
        print("{}    {}    {}\n".format(contacto.nombre,
                                        contacto.apellido,
                                        contacto.telefono))
        borrar = input("Esta seguro [Yn]: ").lower().strip()
        if borrar == 'y':
            Borrar = Contactos.delete().where( Contactos.nombre == nombre )
            Borrar.execute()
            print("El contacto ha sido borrado.\n")
        else:
            print("El contacto no ha sido borrado.")
    except:
        mensaje = "El contacto no existe."
        print('*' * len(mensaje))
        print(mensaje)
        print('*' * len(mensaje))


def exportar_contactos():
    """ Exportar Contactos """

    lista = []
    for fila in Contactos.select():
        nombre = fila.nombre
        apellido = fila.apellido
        telefono = fila.telefono
        print("{}) {} {} {}".format(fila,nombre,apellido,telefono))

        '''lista[fila][x].insertend([nombre])
        lista[fila][x].append(apellido)
        lista[fila][x].append(telefono)'''

    '''documentos = open("contactos.csv", "w")
    csv_agenda = csv.writer(documentos)
    for elemento in lista:
        csv_agenda.writerow(elemento)

    documentos.close()'''


memu = OrderedDict([
    ('a', agregar_contacto),
    ('b', buscar_contacto),
    ('c', ver_contactos),
    ('d', actualizar_contacto),
    ('e', borrar_contacto),
    ('f', exportar_contactos)
])


if __name__ == '__main__':
    crear_conectar()
    tabla_menu()
    db.close()




