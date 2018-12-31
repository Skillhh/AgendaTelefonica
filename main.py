
from peewee import *
from collections import OrderedDict


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
        tablaMenu = "     Tabla de Menu     "
        print(tablaMenu)
        print('*' *len(tablaMenu))
        for llave, valor in memu.items():
            print("{}) {}".format(llave, valor.__doc__))

        print("presione 'q' para salir")
        opcion = input("Opcion: ").lower().strip()

        if opcion in memu:
            memu[opcion]()


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
    nombre = input("Ingrese nombre: ").lower().strip()
    contacto = Contactos.get( Contactos.nombre == nombre )
    titulo = "\n  Nombre    Apellido    Telefono  "
    print(titulo)
    print('*' * len(titulo))
    print("{}    {}    {}\n".format(contacto.nombre,
                                  contacto.apellido,
                                  contacto.telefono))


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


def borrar_contacto():
    """ Borrar Contacto """

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


memu = OrderedDict([
    ('a', agregar_contacto),
    ('b', buscar_contacto),
    ('c', ver_contactos),
    ('d', actualizar_contacto),
    ('e', borrar_contacto)
])


if __name__ == '__main__':
    crear_conectar()
    tabla_menu()
    db.close()




