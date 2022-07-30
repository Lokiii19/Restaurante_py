import sqlite3
from tkinter import *


def crear_menu(root):
    container = Frame(root).grid(row=1)

    Label(container, text="   Restaurante   ", fg="lightgreen",
          font=("Calibri", 28, "bold italic")).grid(row=2, columnspan=4)
    Label(container, text="Menu del dia", fg="lightgreen",
          font=("Calibri", 24, "bold italic")).grid(row=3, columnspan=4)

    Label(container, text="").grid(row=4, columnspan=4)

    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()

# buscar categorias y platos de DB

    categorias = cursor.execute("SELECT * FROM categoria").fetchall()

    r = 5
    for categoria in categorias:
        Label(container, text=categoria[1], fg="black",
              font=("Calibri", 20, "bold italic")).grid(row=r, column=0)
        platos = cursor.execute(
            f"SELECT * FROM plato JOIN precios ON plato.id = precios.id_plato WHERE plato.categoria_id={categoria[0]} ").fetchall()

        for plato in platos:
            Label(container, text=plato[1], fg="grey",
                  font=("Verdana", 15, "italic")).grid(row=r, column=2, columnspan=2)
            Label(container, text=plato[4], fg="grey",
                  font=("Verdana", 15, "italic")).grid(row=r, column=4, columnspan=2)
            r = r+1

        Label(container, text="")

    conexion.close()
    return r
    # precio del menu


def calcular_precio(root):
    frame = Frame(root).grid(row=20)
    r = 21
    Label(frame, text="$$$$", fg="darkgreen", font=(
        "Calibri", 20, "bold")).grid(row=r, column=4, columnspan=4)
