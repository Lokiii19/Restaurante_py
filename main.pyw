import sqlite3
from tkinter import *
from restaurant import *
from gestorBD import *
from login import *

root = Tk()
root.title("Gestor de restaurante")
root.resizable(0, 0)
root.config(bd=25, relief="sunken")


lgn_btn = Button(root, text="Login", command=lambda: crear_login(root)).pack()
manager = Button(root, text="Acceder al gestor",
                 command=lambda: crear_manager(root)).pack()

crear_menu(root)
calcular_precio(root)


root.mainloop()
