import sqlite3
from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox
from xml.dom import NoModificationAllowedErr

root = ""


def crear_bd():
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()
    try:
        cursor.execute('''CREATE TABLE categoria(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(100) UNIQUE NOT NULL)''')
    except sqlite3.OperationalError:
        print("La tabla de Categorías ya existe.")
    else:
        print("La tabla de Categorías se ha creado correctamente.")

    try:
        cursor.execute('''CREATE TABLE plato(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(100) UNIQUE NOT NULL,
                categoria_id INTEGER NOT NULL,
                FOREIGN KEY(categoria_id) REFERENCES categoria(id))''')
    except sqlite3.OperationalError:
        print("La tabla de Platos ya existe.")
    else:
        print("La tabla de Platos se ha creado correctamente.")

    try:
        cursor.execute('''CREATE TABLE precios (
            id	INTEGER NOT NULL,
            precio	INTEGER NOT NULL,
            id_plato	INTEGER NOT NULL UNIQUE,
            PRIMARY KEY(id AUTOINCREMENT),
            FOREIGN KEY(id_plato) REFERENCES plato (id))''')
    except sqlite3.OperationalError:
        print("La tabla de precios ya existe.")
    else:
        print("La tabla de Precios se ha creado correctamente.")

    try:
        cursor.execute('''CREATE TABLE usuario(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(50) UNIQUE NOT NULL,
                contrasenia VARCHAR(50) NOT NULL,
                logeado INT(1) NOT NULL DEFAULT 0,
                retry	INT(1) NOT NULL DEFAULT 3,
                )''')

    except sqlite3.OperationalError:
        print("La tabla de usuarios ya existe.")
    else:
        print("La tabla de Usuarios se ha creado correctamente.")

    conexion.close()


def agregar_categoria():
    categoria = simpledialog.askstring(
        "Insertar categoria", "Por favor inserte una categoria para agregar")

    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()

    try:
        cursor.execute(
            "INSERT INTO categoria VALUES (null, '{}')".format(categoria))
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", f"La categoria'{categoria}' ya existe")
        # print("La categoría '{}' ya existe.".format(categoria))
    else:
        messagebox.showinfo(
            "Correcto", f"Categoria'{categoria}' creada correctamente")
        # print("Categoría '{}' creada correctamente.".format(categoria))

    conexion.commit()
    conexion.close()


def selec_categoria(root):

    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()

    categorias = cursor.execute("SELECT * FROM categoria").fetchall()
    popup = Toplevel(root)
    Label(popup, text="Categorias Disponibles", width=50).pack()
    for categoria in categorias:
        Button(popup, text=f"[{categoria[0]}] {categoria[1]}",
               command=lambda: agregar_plato(categoria[0]), width=50).pack()


def agregar_plato(categoria_usuario):
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()
    categoria_usuario = categoria_usuario
    plato = simpledialog.askstring(
        "Insertar Plato", f"Por favor inserte el plato para agregar a la categoria {categoria_usuario}")

    try:
        cursor.execute("INSERT INTO plato VALUES (null, '{}', {})".format(
            plato, categoria_usuario))
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", f"El plato '{plato}' ya existe")
    else:
        messagebox.showinfo(
            "Correcto", f"Plato '{plato}' creado correctamente")

    conexion.commit()
    conexion.close()


def selec_plato(root):

    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()

    platos = cursor.execute("SELECT * FROM plato").fetchall()
    popup = Toplevel(root)
    Label(popup, text="Platos Disponibles", width=50).pack()
    for plato in platos:
        Button(popup, text=f"[{plato[0]}] {plato[1]}",
               command=lambda: agregar_precio(plato[0], plato[1]), width=50).pack()


def agregar_precio(plato_usuario, nom_plato_usuario):
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()
    plato_usuario = plato_usuario
    nom_plato_usuario = nom_plato_usuario
    precio = simpledialog.askstring(
        "Insertar Precio", f"Por favor inserte el precio para agregar al plato {nom_plato_usuario}")
    try:
        cursor.execute("INSERT INTO precios VALUES (null, '{}', {})".format(
            precio, plato_usuario))
    except sqlite3.IntegrityError:
        messagebox.showerror(
            "Error", f"El plato '{nom_plato_usuario}' ya tiene precio")
    else:
        messagebox.showinfo(
            "Correcto", f"Precio '{precio}' agregado correctamente al plato {nom_plato_usuario}")

    conexion.commit()
    conexion.close()


def mostrar_menu(root):

    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()

    categorias = cursor.execute("SELECT * FROM categoria").fetchall()
    popup = Toplevel(root)
    Label(popup, text="Lista de Platos", width=50).grid(
        row=0, column=0, columnspan=3)
    Label(popup, text="Categorias").grid(row=1, column=0)
    Label(popup, text="Platos").grid(row=1, column=1, columnspan=2)
    r = 2
    for categoria in categorias:
        Label(popup, text=f"{categoria[1]}",
              justify="left", width=50, bg='red').grid(row=r, column=0)
        platos = cursor.execute(
            "SELECT * FROM plato WHERE categoria_id={}".format(categoria[0])).fetchall()
        for plato in platos:
            precio = cursor.execute(
                f"SELECT * FROM precios WHERE id_plato={plato[0]}").fetchall()
            Label(popup, text=f"\t{plato[1]}",
                  width=30, justify="left", bg='green').grid(row=r, column=2, columnspan=2)
            Label(popup, text=f"\t$ {precio[1]}",
                  width=30, justify="left", bg='green').grid(row=r, column=4, columnspan=2)
            precio = ""
            r = r+1

    conexion.close()


# Menú de opciones del programa
def crear_manager(root):
    root = root
    popup = Toplevel(root)
    BDFrame = Frame(popup)
    BDFrame.pack()
    # Crear la base de datos
    crear_bd()

    Label(BDFrame, text="   Manejo de la BD   ", fg="green",
          font=("Calibri", 20, "bold italic")).pack()
    Label(BDFrame, fg="lightgreen", font=("Calibri", 20, "bold italic"),
          text="Bienvenido al gestor del restaurante!").pack()
    Label(BDFrame, fg="red", font=("Calibri", 15, "bold italic"),
          text="Por Favor seleccione una opcion:").pack()
    Button(BDFrame, text="Agregar una categoría",
           command=agregar_categoria).pack()
    Button(BDFrame, text="Agregar un plato",
           command=lambda: selec_categoria(root)).pack()
    Button(BDFrame, text="Agregar un precio",
           command=lambda: selec_plato(root)).pack()
    Button(BDFrame, text="Mostrar el Menu",
           command=lambda: mostrar_menu(root)).pack()
    # Button(root, text="Salir del Gestor", command=ToDO).pack()
