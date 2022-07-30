import sqlite3
from tkinter import *
from tkinter import messagebox
import global_var


def conectar(mainFrame, user, contrasenia=None):

    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()
    conexion.row_factory = lambda cursor, row: row[0]

    user = user.get()
    contrasenia = contrasenia.get()

    try:
        cursor.execute(f"SELECT * FROM usuario WHERE nombre={user}")
    except:
        messagebox.showerror("Error", "Usuario incorrecto")

    if user != None or user != "":
        if contrasenia != None or contrasenia != "":
            paswd = cursor.execute(
                f'SELECT contraseña FROM usuario WHERE nombre="{user}"').fetchone()
            retry = cursor.execute(
                f'SELECT retry FROM usuario WHERE nombre="{user}"').fetchone()
            if retry[0] > 0:
                if contrasenia == paswd[0]:
                    loguear(user)
                    global_var.usr_activo = user
                    
                else:
                    cursor.execute(
                        f'UPDATE usuario SET retry=retry-1 WHERE usuario.nombre="{user}"')
                    conexion.commit()
                    messagebox.showerror(
                        "Error", f"Constraseña incorrecta, le quedan {retry[0]} intentos")
            else:
                messagebox.showerror(
                    "Error", "Excedido el limite de reintentos, contacte a un administrador")
        else:
            messagebox.showerror("Error", "contraseña incorrecta")
    else:
        messagebox.showerror("Error", "Usuario incorrecto")
    conexion.close()


def loguear(user):
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()
    conexion.row_factory = lambda cursor, row: row[0]
    user = user
    conectado = cursor.execute(
        f'SELECT logeado FROM usuario WHERE nombre="{user}"').fetchall()
    if conectado[0][0] == 1:
        cursor.execute(
            f'UPDATE usuario SET logeado="0" WHERE usuario.nombre="{user}"')
        conexion.commit()
        messagebox.showinfo(
            "Deslogueado", f"'{user}' Ha cerrado sesion con exito")
    else:
        cursor.execute(
            f'UPDATE usuario SET logeado="1" WHERE usuario.nombre="{user}"')
        conexion.commit()
        messagebox.showinfo(
            "Logueado", f"'{user}' Ha Iniciado sesion con exito")


def connected(user):
    user = user
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()
    conexion.row_factory = lambda cursor, row: row[0]
    conectado = cursor.execute(
        f'SELECT logeado FROM usuario WHERE nombre="{user}"').fetchall()
    print(f"conectado = {conectado[0][0]}")
    if conectado[0][0] == 1:
        return True
    else:
        return False


def crear_login(root):

    root = root
    popup = Toplevel(root)
    mainFrame = Frame(popup)
    mainFrame.pack()
    mainFrame.config(width=480, height=320)  # ,bg="lightblue")

# Textos y Titulos
    titulo = Label(mainFrame, text="Login Restaurante_py", font=("Arial,24"))
    titulo.grid(column=0, row=0, padx=10, pady=10, columnspan=2)

    nombreLabel = Label(mainFrame, text="Nombre:  ")
    nombreLabel.grid(column=0, row=1)
    passLabel = Label(mainFrame, text="Contraseña: ")
    passLabel.grid(column=0, row=2)


# Entradas de texto
    nombreUsuario = StringVar()
    nombreUsuario.set("")
    contraseñaUsuario = StringVar()
    contraseñaUsuario.set("")
    nombreEntry = Entry(mainFrame, textvariable=nombreUsuario)
    nombreEntry.grid(column=1, row=1)

    contraseñaEntry = Entry(
        mainFrame, textvariable=contraseñaUsuario, show="*")
    contraseñaEntry.grid(column=1, row=2)

# Botones
    iniciarsesionbutton = Button(mainFrame, text="Iniciar Sesión", command=lambda: conectar(
        mainFrame, nombreUsuario, contraseñaUsuario)).grid(column=1, row=3, ipadx=5, ipady=5, padx=10, pady=10)
    print(f"variable global={global_var.usr_activo}")


""" if connected(global_var.usr_activo) == True:
        cerrarsesionbutton = Button(mainFrame, text="Cerrar Sesion", command=lambda: loguear(
            global_var.usr_activo)).grid(column=1, row=3, ipadx=5, ipady=5, padx=10, pady=10)
"""

"""
    registrarbutton = Button(
        mainFrame, text="Registrar", command=lambda: registrarUsuario(nombreUsuario, contraseñaUsuario))
    registrarbutton.grid(column=0, row=3, ipadx=5, ipady=5, padx=10, pady=10)
"""
