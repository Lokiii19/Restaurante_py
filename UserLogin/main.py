from cProfile import label
from email.mime import audio
from lib2to3.pgen2.literals import test
from msilib.schema import Font
from tkinter import *
from tkinter import font
from tkinter import ttk as ttk
from pip import main
from Restaurante_py.UserLogin.Usuarios import usuarios
from tkinter import messagebox as messagebox
from Usuarios import Usuarios

root = Tk()

nombreUsuario = StringVar()
contraseñaUsuario = StringVar()
usuarios = []


def createGUI():
   # Ventana Principal Login
   root = Tk()
   root.title("login usuario")

   # MainFrame
   mainFrame = Frame(root)
   mainFrame.pack()
   mainFrame.config(width=480,height=320)#,bg="lightblue")

  # Textos y Titulos
   titulo = Label(mainFrame,text="Login Restaurante_py",font=("Arial,24"))
   titulo.grid(column=0,row=0,padx=10,pady=10,columnspan=2)

   nombreLabel = Label(mainFrame,text="Nombre:  ")
   nombreLabel.grid(column=0,row=1)
   passLabel = Label(mainFrame,text="Contraseña: ")
   passLabel.grid(column=0,row=2)

   # Entradas de texto
   nombreUsuario = StringVar()
   nombreUsuario.set("")
   nombreEntry = Entry(mainFrame,textvariable=nombreUsuario)
   nombreEntry.grid(column=1,row=1) 

   contraseñaUsuario = StringVar()
   contraseñaUsuario.set("")
   contraseñaEntry = Entry(mainFrame,textvariable=contraseñaUsuario,show="*")
   contraseñaEntry.grid(column=1,row=2)

   # Botones
   newBut = ttk.Button
   iniciarsesionbutton = ttk.Button(mainFrame,text="Iniciar Sesión",command=iniciarSesion)
   iniciarsesionbutton.grid(column=1,row=3,ipadx=5,ipady=5,padx=10,pady=10)

   registrarbutton = ttk.Button(mainFrame,text="Registrar",command=registrarUsuario)
   registrarbutton.grid(column=0,row=3,ipadx=5,ipady=5,padx=10,pady=10)

   root.mainloop()

def iniciarSesion(): 
    for user in usuarios:
        if user.nombre == nombreUsuario.get():
           test = user.conectar(contraseñaUsuario.get())
        if test:
           messagebox.showinfo("Conectado","se inició sesión con exito")
        else:
           messagebox.showerror("Error","Contraseña incorrecta")  
        break
    else:
        messagebox.showerror("Error","Usuario inexistente")


def registrarUsuario():
    name = nombreUsuario.get()
    password = contraseñaUsuario.get()
    newUser = usuarios(name,password)
    usuarios.append(newUser)
    messagebox.showinfo("Registro exitoso","Se registró el usuario [{name}] con exito")
    nombreUsuario.set("")
    contraseñaUsuario.set("")




if __name__=="__main__":
    user1 = usuarios(input("Ingrese su usuario:  "),input("Ingrese su contraseña:  "))
    user1 = usuarios("Grupo4","1234")
    usuarios.append(user1)
    createGUI()


