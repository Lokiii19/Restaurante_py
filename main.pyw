import sqlite3
from tkinter import *
from menu import *
from gestorBD import *
from login import *

root = Tk()
root.title("Gestor de restaurante")
root.resizable(0, 0)
root.config(bd=25, relief="sunken")

frame = Frame(root)
frame.pack()

lgn_btn = Button(frame, text="Login", command=lambda: crear_login(
    root)).grid(column=0, row=0, padx=10, pady=10, columnspan=2, sticky=W)
manager = Button(frame, text="Acceder al gestor",
                 command=lambda: crear_manager(root)).grid(column=4, row=0, padx=10, pady=10, columnspan=2, sticky=E)

crear_menu(root)
calcular_precio(root)


root.mainloop()
