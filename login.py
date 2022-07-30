"""
import sqlite3
from tkinter import *
from tkinter import ttk as ttk
from tkinter import messagebox as messagebox


# Funciones


def registrarUsuario(nombreUsuario, contraseñaUsuario):
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()
    name = nombreUsuario.get()
    password = contraseñaUsuario.get()
    newUser = User(name, password)
    error = 0
    for user in usuarios:
        if user.nombre == newUser.nombre:
            error += 1
        nombreUsuario.set("")
        contraseñaUsuario.set("")
    if error != 0:
        messagebox.showinfo("Registro fallido",
                            f"El usuario [{name}] ya existe")
        error = 0
    else:
        cursor.execute("INSERT INTO usuario VALUES (null, '{}', {})".format(
            nombreUsuario, contraseñaUsuario))
        messagebox.showinfo("Registro exitoso",
                            f"Se registró el usuario [{name}] con exito")
    conexion.close()


"""
