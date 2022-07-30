import sqlite3
from tkinter import *
from menu import *
from gestorBD import *
from User import *
import global_var

root = Tk()
root.title("Gestor de restaurante")
root.resizable(0, 0)
root.config(bd=25, relief="sunken")


frame = Frame(root).grid(row=0)

conexion = sqlite3.connect("restaurante.db")
cursor = conexion.cursor()

print(global_var.usr_activo)
lgn_btn = Button(frame, text="Login", command=lambda: crear_login(
    root)).grid(column=0, row=1, padx=10, pady=10, columnspan=2, sticky=W)

if global_var.usr_activo != "" and global_var.usr_activo != None:
    conectado = cursor.execute(
        f"SELECT logueado FROM usuario WHERE nombre={global_var.usr_activo}").fetchall()
    if conectado:
        manager = Button(frame, text="Acceder al gestor",
                         command=lambda: crear_manager(root)).grid(column=4, row=1, padx=10, pady=10, columnspan=2, sticky=E)
conexion.close()

menu_frame = Frame(root).grid(row=2)
crear_menu(menu_frame)
calcular_precio(menu_frame)


root.mainloop()
