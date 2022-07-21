import sqlite3
from tkinter import *
from tkinter import ttk as ttk
from tkinter import messagebox as messagebox
from Usuarios import Usuarios as User


'''Cambiar esta generacion local por una BD'''
conexion = sqlite3.connect("restaurante.db")
cursor = conexion.cursor()
usuarios = conexion.execute("SELECT * FROM usuario").fetchall()
conexion.close()

root = ""

# Funciones


def iniciarSesion(nombreUsuario, contraseñaUsuario):
    logeado = False
    error = ""
    for user in usuarios:
        if user.nombre == nombreUsuario.get():
            logeado = user.conectar(contraseñaUsuario.get())
        if logeado == True:
            nombreUsuario.set("")
            contraseñaUsuario.set("")
            return messagebox.showinfo("Conectado", "se inició sesión con exito")
        else:
            error = "password"
    else:
        error = "usuario"
    if error == "password":
        contraseñaUsuario.set("")
        messagebox.showerror("Error", "Contraseña incorrecta")
    elif error == "usuario":
        contraseñaUsuario.set("")
        messagebox.showerror("Error", "Usuario inexistente")


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


# MainFrame


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
    newBut = ttk.Button
    iniciarsesionbutton = ttk.Button(
        mainFrame, text="Iniciar Sesión", command=lambda: iniciarSesion(nombreUsuario, contraseñaUsuario))
    iniciarsesionbutton.grid(column=1, row=3, ipadx=5,
                             ipady=5, padx=10, pady=10)

    registrarbutton = ttk.Button(
        mainFrame, text="Registrar", command=lambda: registrarUsuario(nombreUsuario, contraseñaUsuario))
    registrarbutton.grid(column=0, row=3, ipadx=5, ipady=5, padx=10, pady=10)
