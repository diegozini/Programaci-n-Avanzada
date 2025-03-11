import mysql.connector
from tkinter import *
from tkinter import messagebox


# Conexión a la base de datos MySQL
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # tu usuario de MySQL
        password="",  # tu contraseña de MySQL
        database="escuela"
    )


# Función para mostrar todos los registros de la tabla
def show_all():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM alumno")
    rows = cursor.fetchall()
    
    for row in rows:
        listbox.insert(END, row)
    
    conn.close()


# Función para insertar un nuevo alumno
def add_alumno():
    conn = connect_db()
    cursor = conn.cursor()
    nombre = entry_nombre.get()
    apellidos = entry_apellidos.get()
    correo = entry_correo.get()
    telefono = entry_telefono.get()
    
    if nombre and apellidos:
        cursor.execute("INSERT INTO alumno (nombre_alumno, apellidos_alumno, correo, telefono) VALUES (%s, %s, %s, %s)",
                       (nombre, apellidos, correo, telefono))
        conn.commit()
        messagebox.showinfo("Éxito", "Alumno agregado exitosamente.")
        clear_entries()
    else:
        messagebox.showerror("Error", "Nombre y apellidos son obligatorios.")
    
    conn.close()


# Función para eliminar un alumno
def delete_alumno():
    try:
        selected = listbox.get(listbox.curselection())
        id_alumno = selected[0]
        
        conn = connect_db()
        cursor = conn.cursor()
        
        # Eliminar las inscripciones relacionadas
        cursor.execute("DELETE FROM inscripcion WHERE id_alumno = %s", (id_alumno,))
        
        # Ahora eliminar el alumno
        cursor.execute("DELETE FROM alumno WHERE id_alumno = %s", (id_alumno,))
        conn.commit()
        
        messagebox.showinfo("Éxito", "Alumno y sus inscripciones eliminados exitosamente.")
        
        # Limpiar y recargar la lista
        listbox.delete(0, END)
        show_all()
        
        conn.close()
    except IndexError:
        messagebox.showerror("Error", "Selecciona un alumno para eliminar.")


# Función para actualizar los datos del alumno
def update_alumno():
    try:
        selected = listbox.get(listbox.curselection())
        id_alumno = selected[0]
        
        conn = connect_db()
        cursor = conn.cursor()
        
        nombre = entry_nombre.get()
        apellidos = entry_apellidos.get()
        correo = entry_correo.get()
        telefono = entry_telefono.get()
        
        cursor.execute("""
        UPDATE alumno
        SET nombre_alumno = %s, apellidos_alumno = %s, correo = %s, telefono = %s
        WHERE id_alumno = %s
        """, (nombre, apellidos, correo, telefono, id_alumno))
        
        conn.commit()
        messagebox.showinfo("Éxito", "Alumno actualizado exitosamente.")
        
        # Limpiar y recargar la lista
        listbox.delete(0, END)
        show_all()
        
        conn.close()
    except IndexError:
        messagebox.showerror("Error", "Selecciona un alumno para actualizar.")


# Función para limpiar los campos de entrada
def clear_entries():
    entry_nombre.delete(0, END)
    entry_apellidos.delete(0, END)
    entry_correo.delete(0, END)
    entry_telefono.delete(0, END)


# Interfaz gráfica con Tkinter
root = Tk()
root.title("Gestión de Alumnos")

frame = Frame(root)
frame.pack(padx=10, pady=10)

# Campos de entrada
Label(frame, text="Nombre").grid(row=0, column=0, padx=5, pady=5)
entry_nombre = Entry(frame)
entry_nombre.grid(row=0, column=1, padx=5, pady=5)

Label(frame, text="Apellidos").grid(row=1, column=0, padx=5, pady=5)
entry_apellidos = Entry(frame)
entry_apellidos.grid(row=1, column=1, padx=5, pady=5)

Label(frame, text="Correo").grid(row=2, column=0, padx=5, pady=5)
entry_correo = Entry(frame)
entry_correo.grid(row=2, column=1, padx=5, pady=5)

Label(frame, text="Teléfono").grid(row=3, column=0, padx=5, pady=5)
entry_telefono = Entry(frame)
entry_telefono.grid(row=3, column=1, padx=5, pady=5)

# Botones CRUD
Button(frame, text="Agregar Alumno", command=add_alumno).grid(row=4, column=0, padx=5, pady=5)
Button(frame, text="Actualizar Alumno", command=update_alumno).grid(row=4, column=1, padx=5, pady=5)
Button(frame, text="Eliminar Alumno", command=delete_alumno).grid(row=4, column=2, padx=5, pady=5)

# Listbox para mostrar los alumnos
listbox = Listbox(root, width=50)
listbox.pack(padx=10, pady=10)
listbox.bind("<Double-1>", lambda event: load_selected_data())

# Cargar los registros
show_all()

def load_selected_data():
    try:
        selected = listbox.get(listbox.curselection())
        entry_nombre.delete(0, END)
        entry_apellidos.delete(0, END)
        entry_correo.delete(0, END)
        entry_telefono.delete(0, END)
        
        entry_nombre.insert(0, selected[1])
        entry_apellidos.insert(0, selected[2])
        entry_correo.insert(0, selected[3])
        entry_telefono.insert(0, selected[4])
    except IndexError:
        pass

# Ejecutar la interfaz gráfica
root.mainloop()
