import pymysql.cursors


class Conexion:

    def conectar(self):
        con = pymysql.connect(host='localhost', user="root", password="root", db="observatoriumPantitlan")
        return con

    def cerrar(self, conexion):
        conexion.close()