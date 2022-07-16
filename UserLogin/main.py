from tkinter import *
from tkinter import ttk as ttk
from tkinter import messagebox as messagebox
from Usuarios import Usuarios as User

root = Tk()

'''Cambiar esta generacion local por una BD'''
usuarios = []
admin = User("admin", "1234")
usuarios.append(admin)


# def createGUI():
# Ventana Principal Login

root.title("login usuario")


# Funciones

def iniciarSesion():
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


def registrarUsuario():
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
        usuarios.append(newUser)
        messagebox.showinfo("Registro exitoso",
                            f"Se registró el usuario [{name}] con exito")


# MainFrame
mainFrame = Frame(root)
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
nombreEntry = Entry(mainFrame, textvariable=nombreUsuario)
nombreEntry.grid(column=1, row=1)

contraseñaUsuario = StringVar()
contraseñaUsuario.set("")
contraseñaEntry = Entry(
    mainFrame, textvariable=contraseñaUsuario, show="*")
contraseñaEntry.grid(column=1, row=2)

# Botones
newBut = ttk.Button
iniciarsesionbutton = ttk.Button(
    mainFrame, text="Iniciar Sesión", command=iniciarSesion)
iniciarsesionbutton.grid(column=1, row=3, ipadx=5,
                         ipady=5, padx=10, pady=10)

registrarbutton = ttk.Button(
    mainFrame, text="Registrar", command=registrarUsuario)
registrarbutton.grid(column=0, row=3, ipadx=5, ipady=5, padx=10, pady=10)

# root.mainloop()


'''if __name__ == "__main__":
    user1 = usuarios(input("Ingrese su usuario:  "),
                     input("Ingrese su contraseña:  "))
    user1 = usuarios("Grupo4", "1234")
    usuarios.append(user1)
    createGUI()
'''


root.mainloop()
