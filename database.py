# Crear base de datos en SQLite
import sqlite3

# Establecer la conexión a la base de datos (si no existe, se creará)
conexion = sqlite3.connect('bbdd.db')

# Crear un cursor para ejecutar comandos SQL
cursor = conexion.cursor()

# Crear una tabla llamada 'clientes' con columnas 'id', 'nombre' y 'edad'
cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        edad INTEGER
    )
''')

# Guardar los cambios y cerrar la conexión
conexion.commit()
conexion.close()