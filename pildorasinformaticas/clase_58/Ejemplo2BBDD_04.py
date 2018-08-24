import sqlite3

miConexion = sqlite3.connect("GestionProductos")

miCursor = miConexion.cursor()

miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION = 'confección'")

productos = miCursor.fetchall()

print(productos)

miConexion.commit()

miConexion.close()
