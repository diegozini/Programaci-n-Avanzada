import tkinter as tk
from tkinter import messagebox, ttk
import pymysql

# Conexión a la base de datos
def obtener_conexion():
    try:
        conexion = pymysql.connect(
            host="127.0.0.1",
            user="root",
            password="bA4A6A",
            database="BIBLIOTECA",
            port=3306,
            cursorclass=pymysql.cursors.DictCursor
        )
        return conexion
    except Exception as e:
        messagebox.showerror("Error de conexión", f"No se pudo conectar a la base de datos: {e}")
        return None

# Función para insertar un libro
def insertar_libro():
    titulo = entry_titulo.get()
    genero = entry_genero.get()
    fecha_publicacion = entry_fecha.get()

    if titulo and genero and fecha_publicacion:
        try:
            conexion = obtener_conexion()
            if conexion:
                with conexion.cursor() as cursor:
                    sql = "INSERT INTO libro (titulo, genero, fecha_publicacion) VALUES (%s, %s, %s)"
                    cursor.execute(sql, (titulo, genero, fecha_publicacion))
                    conexion.commit()
                    messagebox.showinfo("Éxito", "Libro insertado correctamente.")
                    conexion.close()
        except Exception as e:
            messagebox.showerror("Error al insertar libro", f"Hubo un problema al insertar el libro: {e}")
    else:
        messagebox.showwarning("Campos vacíos", "Por favor, complete todos los campos.")

# Función para actualizar un libro
def actualizar_libro():
    id_libro = entry_id_libro.get()
    nuevo_titulo = entry_nuevo_titulo.get()
    nuevo_genero = entry_nuevo_genero.get()

    if id_libro and nuevo_titulo and nuevo_genero:
        try:
            conexion = obtener_conexion()
            if conexion:
                with conexion.cursor() as cursor:
                    sql = "UPDATE libro SET titulo = %s, genero = %s WHERE id_libro = %s"
                    cursor.execute(sql, (nuevo_titulo, nuevo_genero, id_libro))
                    conexion.commit()
                    messagebox.showinfo("Éxito", "Libro actualizado correctamente.")
                    conexion.close()
        except Exception as e:
            messagebox.showerror("Error al actualizar libro", f"Hubo un problema al actualizar el libro: {e}")
    else:
        messagebox.showwarning("Campos vacíos", "Por favor, complete todos los campos.")

# Función para eliminar un libro
def eliminar_libro():
    id_libro = entry_id_libro_eliminar.get()
    if id_libro:
        try:
            conexion = obtener_conexion()
            if conexion:
                with conexion.cursor() as cursor:
                    sql = "DELETE FROM libro WHERE id_libro = %s"
                    cursor.execute(sql, (id_libro,))
                    conexion.commit()
                    messagebox.showinfo("Éxito", "Libro eliminado correctamente.")
                    conexion.close()
        except Exception as e:
            messagebox.showerror("Error al eliminar libro", f"Hubo un problema al eliminar el libro: {e}")
    else:
        messagebox.showwarning("Campos vacíos", "Por favor, introduce un ID válido.")

# Función para insertar un autor
def insertar_autor():
    nombre_autor = entry_nombre_autor.get()
    nacionalidad = entry_nacionalidad.get()

    if nombre_autor and nacionalidad:
        try:
            conexion = obtener_conexion()
            if conexion:
                with conexion.cursor() as cursor:
                    cursor.execute("SELECT * FROM autor WHERE nombre_autor = %s", (nombre_autor,))
                    autor_existente = cursor.fetchone()

                    if autor_existente:
                        messagebox.showinfo("Autor existente", f"El autor '{nombre_autor}' ya existe en la base de datos.")
                    else:
                        sql = "INSERT INTO autor (nombre_autor, nacionalidad) VALUES (%s, %s)"
                        cursor.execute(sql, (nombre_autor, nacionalidad))
                        conexion.commit()
                        messagebox.showinfo("Éxito", "Autor insertado correctamente.")
                        conexion.close()
        except Exception as e:
            messagebox.showerror("Error al insertar autor", f"Hubo un problema al insertar el autor: {e}")
    else:
        messagebox.showwarning("Campos vacíos", "Por favor, complete todos los campos.")

# Función para mostrar los libros
def mostrar_libros():
    for widget in frame_libros.winfo_children():
        widget.destroy()

    try:
        conexion = obtener_conexion()
        if conexion:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM libro")
                libros = cursor.fetchall()

                if libros:
                    for libro in libros:
                        tk.Label(frame_libros, text=f"{libro['id_libro']}: {libro['titulo']} - {libro['genero']}").pack()
                else:
                    messagebox.showinfo("Sin libros", "No se encontraron libros en la base de datos.")
            conexion.close()
    except Exception as e:
        messagebox.showerror("Error al mostrar libros", f"Hubo un problema al mostrar los libros: {e}")

# Creación de la ventana
ventana = tk.Tk()
ventana.title("Biblioteca Moderna")
ventana.geometry("600x700")
ventana.configure(bg="#D7D2CC")  # Color de fondo suave

# Frame tipo tarjeta centrado
card = tk.Frame(ventana, bg="#FFFFFF", bd=0, relief=tk.RIDGE)
card.place(relx=0.5, rely=0.5, anchor="center", width=500, height=650)

# Ícono superior (puede cambiarse por una imagen)
icono = tk.Label(card, text="📚", font=("Arial", 50), bg="#FFFFFF")
icono.pack(pady=10)

# Sección de Insertar Libro
tk.Label(card, text="Insertar Libro", bg="#FFFFFF", font=("Arial", 16, "bold")).pack(pady=5)
entry_titulo = ttk.Entry(card, width=40)
entry_titulo.insert(0, "Título del libro")
entry_titulo.pack(pady=5)

entry_genero = ttk.Entry(card, width=40)
entry_genero.insert(0, "Género")
entry_genero.pack(pady=5)

entry_fecha = ttk.Entry(card, width=40)
entry_fecha.insert(0, "Fecha de publicación (YYYY-MM-DD)")
entry_fecha.pack(pady=5)

boton_insertar = tk.Button(card, text="Insertar libro", command=insertar_libro, bg="#4CAF50", fg="white", width=30)
boton_insertar.pack(pady=10)

# Sección de Actualizar Libro
tk.Label(card, text="Actualizar Libro", bg="#FFFFFF", font=("Arial", 16, "bold")).pack(pady=5)
entry_id_libro = ttk.Entry(card, width=40)
entry_id_libro.insert(0, "ID del libro")
entry_id_libro.pack(pady=5)

entry_nuevo_titulo = ttk.Entry(card, width=40)
entry_nuevo_titulo.insert(0, "Nuevo título")
entry_nuevo_titulo.pack(pady=5)

entry_nuevo_genero = ttk.Entry(card, width=40)
entry_nuevo_genero.insert(0, "Nuevo género")
entry_nuevo_genero.pack(pady=5)

boton_actualizar = tk.Button(card, text="Actualizar libro", command=actualizar_libro, bg="#2196F3", fg="white", width=30)
boton_actualizar.pack(pady=10)

# Sección de Eliminar Libro
tk.Label(card, text="Eliminar Libro", bg="#FFFFFF", font=("Arial", 16, "bold")).pack(pady=5)
entry_id_libro_eliminar = ttk.Entry(card, width=40)
entry_id_libro_eliminar.insert(0, "ID del libro a eliminar")
entry_id_libro_eliminar.pack(pady=5)

boton_eliminar = tk.Button(card, text="Eliminar libro", command=eliminar_libro, bg="#F44336", fg="white", width=30)
boton_eliminar.pack(pady=10)

# Sección de Insertar Autor
tk.Label(card, text="Insertar Autor", bg="#FFFFFF", font=("Arial", 16, "bold")).pack(pady=5)
entry_nombre_autor = ttk.Entry(card, width=40)
entry_nombre_autor.insert(0, "Nombre del autor")
entry_nombre_autor.pack(pady=5)

entry_nacionalidad = ttk.Entry(card, width=40)
entry_nacionalidad.insert(0, "Nacionalidad del autor")
entry_nacionalidad.pack(pady=5)

boton_insertar_autor = tk.Button(card, text="Insertar autor", command=insertar_autor, bg="#9C27B0", fg="white", width=30)
boton_insertar_autor.pack(pady=10)

# Botón para mostrar los libros
boton_mostrar = tk.Button(card, text="Mostrar libros", command=mostrar_libros, bg="#FF9800", fg="white", width=30)
boton_mostrar.pack(pady=10)

# Frame para mostrar los libros
frame_libros = tk.Frame(card, bg="#EDEDED")
frame_libros.pack(fill="both", expand=True, pady=10)

ventana.mainloop()
