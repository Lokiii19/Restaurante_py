import sqlite3
from tkinter import *


def crear_menu(root):

    Label(root, text="   Restaurante   ", fg="lightgreen",
          font=("Calibri", 28, "bold italic")).pack()
    Label(root, text="Menu del dia", fg="lightgreen",
          font=("Calibri", 24, "bold italic")).pack()

    Label(root, text="").pack()

    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()

# buscar categorias y platos de DB

    categorias = cursor.execute("SELECT * FROM categoria").fetchall()
    for categoria in categorias:
        Label(root, text=categoria[1], fg="black",
              font=("Calibri", 20, "bold italic")).pack()
    platos = cursor.execute(
        "SELECT * FROM plato WHERE categoria_id={}".format(categoria[0])).fetchall()
    for plato in platos:
        Label(root, text=plato[1], fg="grey",
              font=("Verdana", 15, "italic")).pack()
    Label(root, text="")

    conexion.close()
    # precio del menu


def calcular_precio(root):
    Label(root, text="$$$$", fg="darkgreen", font=(
        "Calibri", 20, "bold")).pack(side="right")
