from hashlib import new
import sqlite3
from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox


def selec_user(root):
    popup = Toplevel(root)
    mainFrame = Frame(popup)
    mainFrame.pack()
    mainFrame.config(width=480, height=320)

# Textos y Titulos
    titulo = Label(mainFrame, text="Creacion de Usuario", font=("Arial,24"))
    titulo.grid(column=0, row=0, padx=10, pady=10, columnspan=2)

    nombreLabel = Label(mainFrame, text="Nombre:  ")
    nombreLabel.grid(column=0, row=1)
    passLabel = Label(mainFrame, text="Contraseña: ")
    passLabel.grid(column=0, row=2)
    nombreUsuario = StringVar()
    nombreUsuario.set("")
    contraseñaUsuario = StringVar()
    contraseñaUsuario.set("")
    nombreEntry = Entry(mainFrame, textvariable=nombreUsuario)
    nombreEntry.grid(column=1, row=1)

    contraseñaEntry = Entry(
        mainFrame, textvariable=contraseñaUsuario, show="*")
    contraseñaEntry.grid(column=1, row=2)
    Button(mainFrame, text="Aceptar", command=lambda: crear_user(
        nombreUsuario, contraseñaUsuario)).grid(column=0, row=3, columnspan=3)


def crear_user(nombreUsuario, contraseñaUsuario):
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()
    name = nombreUsuario.get()
    password = contraseñaUsuario.get()
    usuarios = cursor.execute('SELECT * FROM usuario').fetchall()
    error = 0
    for user in usuarios:
        if user[1] == name:
            error += 1
        nombreUsuario.set("")
        contraseñaUsuario.set("")
    if error != 0:
        messagebox.showinfo("Registro fallido",
                            f"El usuario [{user[1]}] ya existe")
        error = 0
    else:
        cursor.execute(
            f"INSERT INTO usuario VALUES (null, '{name}', '{password}', 0, 3)")
        messagebox.showinfo("Registro exitoso",
                            f"Se registró el usuario [{name}] con exito")
    conexion.commit()
    conexion.close()


def reiniciar_retry():
    usuario = categoria = simpledialog.askstring(
        "Seleccionar usuario", "Por favor inserte el nombre del usuario")
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()
    usuarios = cursor.execute("SELECT * FROM usuario").fetchall()
    e = 0
    for user in usuarios:
        if usuario != user[1]:
            e -= 1
        else:
            cursor.execute(
                f'UPDATE usuario SET retry="3" WHERE usuario.nombre="{usuario}"')
            messagebox.showinfo(
                "Actualizado", f"Los reintentos del user: '{usuario}' se han reiniciado con exito")
            e = 0
            conexion.commit()
    if e != 0:
        messagebox.showerror("Error", "Usuario incorrecto")

    conexion.close()


def select_user(root):
    popup = Toplevel(root)
    mainFrame = Frame(popup)
    mainFrame.pack()
    mainFrame.config(width=480, height=320)

# Textos y Titulos
    titulo = Label(mainFrame, text="Creacion de Usuario", font=("Arial,24"))
    titulo.grid(column=0, row=0, padx=10, pady=10, columnspan=2)

    nombreLabel = Label(mainFrame, text="Nombre:  ")
    nombreLabel.grid(column=0, row=1)
    passLabel = Label(mainFrame, text="Contraseña: ")
    passLabel.grid(column=0, row=2)
    Label(mainFrame, text="Nuevo Nombre: ").grid(column=0, row=3)
    nombreUsuario = StringVar()
    nombreUsuario.set("")
    contraseñaUsuario = StringVar()
    contraseñaUsuario.set("")
    nuevoNombre = StringVar()
    nuevoNombre.set("")
    nombreEntry = Entry(mainFrame, textvariable=nombreUsuario)
    nombreEntry.grid(column=1, row=1)

    contraseñaEntry = Entry(
        mainFrame, textvariable=contraseñaUsuario, show="*")
    contraseñaEntry.grid(column=1, row=2)
    nuevoNombreEntry = Entry(mainFrame, textvariable=nuevoNombre)
    nuevoNombreEntry.grid(column=1, row=3)
    Button(mainFrame, text="Aceptar", command=lambda: modificar_user(
        nombreUsuario, contraseñaUsuario, nuevoNombre)).grid(column=0, row=4, columnspan=3)


def modificar_user(nombreUsuario, contraseñaUsuario, nuevoNombre):
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()
    name = nombreUsuario.get()
    nombre_provisorio = nuevoNombre.get()
    new_name = ""
    password = contraseñaUsuario.get()
    usuarios = cursor.execute('SELECT * FROM usuario').fetchall()
    error = 0
    if nombre_provisorio == "" or nombre_provisorio == None or nombre_provisorio == "none":
        new_name = name
    else:
        new_name = nombre_provisorio

    print(new_name)
    for user in usuarios:
        if user[1] != name:
            error += 1
        else:
            nombreUsuario.set("")
            contraseñaUsuario.set("")
            nuevoNombre.set("")
            error = 0
    print(name)
    print(new_name)
    print(error)
    if error != 0:
        messagebox.showinfo("Actualizacion fallida",
                            f"El usuario [{name}] no existe")
        error = 0
    else:
        cursor.execute(
            f'UPDATE usuario SET nombre="{new_name}", contraseña="{password}", logeado=0, retry=3 WHERE usuario.nombre="{name}"')
        messagebox.showinfo("Actualizacion exitosa",
                            f"Se Actualizo el usuario [{name}] con exito")
        error = 0
    conexion.commit()
    conexion.close()
