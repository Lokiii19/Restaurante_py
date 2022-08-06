import sqlite3
import User
import global_var

User.conectar(None,"admin", "admin")
user= global_var.usr_activo

def connected(user):
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()
    conexion.row_factory = lambda cursor, row: row[0]
    conectado = cursor.execute(
        f'SELECT logeado FROM usuario WHERE nombre="{user}"').fetchall()
    print(f"conectado=  {conectado[0][0]}")
    """if conectado[0] == 1:
        return True
    else:
        return False
"""


connected(user)
