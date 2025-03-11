import pymysql
import pymysql.cursors

# Conexión a la base de datos
conexion = pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="bA4A6A",
    database="BIBLIOTECA",
    port=3306,
    cursorclass=pymysql.cursors.DictCursor
)

print("Conexión exitosa a la base de datos")

#C R U D

# Función para insertar un autor, comprobando si ya existe
def insertar_autor(nombre_autor, nacionalidad):
    try:
        with conexion.cursor() as cursor:
            # Comprobar si el autor ya existe
            cursor.execute("SELECT * FROM autor WHERE nombre_autor = %s", (nombre_autor,))
            autor_existente = cursor.fetchone()

            if autor_existente:
                print(f"El autor '{nombre_autor}' ya existe en la base de datos")
            else:
                # SQL para insertar un autor
                sql = "INSERT INTO autor (nombre_autor, nacionalidad) VALUES (%s, %s)"
                cursor.execute(sql, (nombre_autor, nacionalidad))
                conexion.commit()  # Confirma la transacción
                print(f"✅ Autor '{nombre_autor}' insertado correctamente")
    except Exception as e:
        print(f"Error al insertar autor: {e}")


# Función para insertar un libro
def insertar_libro(titulo, genero, id_autor, fecha_publicacion):
    try:
        with conexion.cursor() as cursor:
            # SQL para insertar un libro
            sql = "INSERT INTO libro (titulo, genero, id_autor, fecha_publicacion) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (titulo, genero, id_autor, fecha_publicacion))
            conexion.commit()  # Confirma la transacción
            print("✅ Libro insertado correctamente")
    except Exception as e:
        print(f"Error al insertar libro: {e}")


# Llamar a la función para insertar el autor solo si no existe
insertar_autor("Miguel de Cervantes", "Española")

# Llamada a la función para insertar un libro (con id_autor = 1, que es el autor que insertaste)
insertar_libro("El Quijote", "Novela", 1, "1605-01-16")


# Leer (Obtener todos los libros)
def obtener_libros():
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM libro")
    libros = cursor.fetchall()
    return libros


# Actualizar (Modificar un libro)
def actualizar_libro(id_libro, nuevo_titulo, nuevo_genero):
    cursor = conexion.cursor()
    sql = "UPDATE libro SET titulo = %s, genero = %s WHERE id_libro = %s"
    cursor.execute(sql, (nuevo_titulo, nuevo_genero, id_libro))
    conexion.commit()
    print("✅ Libro actualizado")


# Eliminar (Borrar un libro)
def eliminar_libro(id_libro):
    cursor = conexion.cursor()
    sql = "DELETE FROM libro WHERE id_libro = %s"
    cursor.execute(sql, (id_libro,))
    conexion.commit()
    print("✅ Libro eliminado")


# 🔹 Pruebas del CRUD
# Solo insertar una vez el libro
print(obtener_libros())
actualizar_libro(1, "Don Quijote de la Mancha", "Clásico")
eliminar_libro(1)

# Cerrar la conexión
conexion.close()
