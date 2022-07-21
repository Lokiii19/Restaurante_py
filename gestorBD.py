import sqlite3
from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox

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


def selec_categoria():

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


def mostrar_menu():

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
            Label(popup, text=f"\t{plato[1]}",
                  width=30, justify="left", bg='green').grid(row=r, column=2, columnspan=2)
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
    Button(BDFrame, text="Agregar un plato", command=selec_categoria).pack()
    Button(BDFrame, text="Mostrar el Menu", command=mostrar_menu).pack()
    # Button(root, text="Salir del Gestor", command=ToDO).pack()
