import sqlite3
#from typing_extensions import Self


def usuario():
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()
    usuarios = conexion.execute("SELECT * FROM usuario").fetchall()
    conexion.close()
    return usuarios


def conectar(user, contrasenia=None):
    usuarios= usuario()
    user= user
    if contrasenia == None:
        mycontra = input("Ingrese su contraseña:")
    else:
        mycontra = contrasenia
    if mycontra == contraseña_user:
        print("Conectado con exito")
        self.conectado = True
        return True
    else:
        self.intentos -= 1
        if self.intentos > 0:
            print("Contraseña incorrecta")
            if contrasenia != None:
                return False
            print("Intentos restantes", self.intentos)
            self.conectar()
        else:
            print("Error,contactar al administrador")


def desconectado():

    if conectado:
        print("Se cerró sesión con exito")
    else:
        print("Error,sesión no iniciada")


'''def __str__(self):
        if self.conectado:
            connect = "Conectado"
        else:
            connect = "Desconectado"
        return f"Mi nombre de usuario es {self.nombre} y estoy {connect}"
'''

'''
user1 = usuarios(input("Ingrese su usuario:  "),
                 input("Ingrese su contraseña:  "))
print(user1)

user1.conectar()
print(user1)

user1.desconectado()
print(user1)
'''
