import mysql.connector
from tkinter import *
from tkinter import messagebox

# Conexión a la base de datos MySQL
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # tu usuario de MySQL
        password="",  # tu contraseña de MySQL
        database="hospital"
    )

# Función para mostrar todos los registros de la tabla paciente
def show_all():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM paciente")
    rows = cursor.fetchall()
    
    # Limpiar la lista antes de mostrar
    listbox.delete(0, END)
    
    for row in rows:
        listbox.insert(END, row)
    
    conn.close()

# Función para agregar un nuevo paciente
def add_paciente():
    conn = connect_db()
    cursor = conn.cursor()
    
    # Obtiene los valores de los campos de entrada
    nombre = entry_nombre.get()
    apellidos = entry_apellidos.get()
    fecha_nacimiento = entry_fecha_nacimiento.get()
    direccion = entry_direccion.get()
    telefono = entry_telefono.get()
    
    if nombre and apellidos:
        # Inserta el nuevo paciente en la base de datos
        cursor.execute("INSERT INTO paciente (nombre_paciente, apellidos_paciente, fecha_nacimiento, direccion, telefono) VALUES (%s, %s, %s, %s, %s)",
                       (nombre, apellidos, fecha_nacimiento, direccion, telefono))
        conn.commit()
        
        # Muestra el mensaje de éxito
        messagebox.showinfo("Éxito", "Paciente agregado exitosamente.")
        
        # Limpia los campos de entrada
        clear_entries()
        
        # Actualiza el Listbox con la lista de pacientes actualizada
        listbox.delete(0, END)  # Borra el contenido anterior
        show_all()  # Recarga los pacientes desde la base de datos
        
    else:
        messagebox.showerror("Error", "Nombre y apellidos son obligatorios.")
    
    conn.close()


# Función para eliminar un paciente
def delete_paciente():
    try:
        selected = listbox.get(listbox.curselection())
        id_paciente = selected[0]
        
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM paciente WHERE id_paciente = %s", (id_paciente,))
        conn.commit()
        messagebox.showinfo("Éxito", "Paciente eliminado exitosamente.")
        
        # Limpiar y recargar la lista
        listbox.delete(0, END)
        show_all()
        
        conn.close()
    except IndexError:
        messagebox.showerror("Error", "Selecciona un paciente para eliminar.")

# Función para actualizar los datos del paciente
def update_paciente():
    try:
        selected = listbox.get(listbox.curselection())
        id_paciente = selected[0]
        
        conn = connect_db()
        cursor = conn.cursor()
        
        nombre = entry_nombre.get()
        apellidos = entry_apellidos.get()
        fecha_nacimiento = entry_fecha_nacimiento.get()
        direccion = entry_direccion.get()
        telefono = entry_telefono.get()
        
        cursor.execute("""
        UPDATE paciente
        SET nombre_paciente = %s, apellidos_paciente = %s, fecha_nacimiento = %s, direccion = %s, telefono = %s
        WHERE id_paciente = %s
        """, (nombre, apellidos, fecha_nacimiento, direccion, telefono, id_paciente))
        
        conn.commit()
        messagebox.showinfo("Éxito", "Paciente actualizado exitosamente.")
        
        # Limpiar y recargar la lista
        listbox.delete(0, END)
        show_all()
        
        conn.close()
    except IndexError:
        messagebox.showerror("Error", "Selecciona un paciente para actualizar.")

# Función para limpiar los campos de entrada
def clear_entries():
    entry_nombre.delete(0, END)
    entry_apellidos.delete(0, END)
    entry_fecha_nacimiento.delete(0, END)
    entry_direccion.delete(0, END)
    entry_telefono.delete(0, END)

# Interfaz gráfica con Tkinter
root = Tk()
root.title("Gestión de Pacientes")

frame = Frame(root)
frame.pack(padx=10, pady=10)

# Campos de entrada
Label(frame, text="Nombre").grid(row=0, column=0, padx=5, pady=5)
entry_nombre = Entry(frame)
entry_nombre.grid(row=0, column=1, padx=5, pady=5)

Label(frame, text="Apellidos").grid(row=1, column=0, padx=5, pady=5)
entry_apellidos = Entry(frame)
entry_apellidos.grid(row=1, column=1, padx=5, pady=5)

Label(frame, text="Fecha de Nacimiento").grid(row=2, column=0, padx=5, pady=5)
entry_fecha_nacimiento = Entry(frame)
entry_fecha_nacimiento.grid(row=2, column=1, padx=5, pady=5)

Label(frame, text="Dirección").grid(row=3, column=0, padx=5, pady=5)
entry_direccion = Entry(frame)
entry_direccion.grid(row=3, column=1, padx=5, pady=5)

Label(frame, text="Teléfono").grid(row=4, column=0, padx=5, pady=5)
entry_telefono = Entry(frame)
entry_telefono.grid(row=4, column=1, padx=5, pady=5)

# Botones CRUD
Button(frame, text="Agregar Paciente", command=add_paciente).grid(row=5, column=0, padx=5, pady=5)
Button(frame, text="Actualizar Paciente", command=update_paciente).grid(row=5, column=1, padx=5, pady=5)
Button(frame, text="Eliminar Paciente", command=delete_paciente).grid(row=5, column=2, padx=5, pady=5)

# Listbox para mostrar los pacientes
listbox = Listbox(root, width=60)
listbox.pack(padx=10, pady=10)
listbox.bind("<Double-1>", lambda event: load_selected_data())

# Cargar los registros
show_all()

def load_selected_data():
    try:
        selected = listbox.get(listbox.curselection())
        entry_nombre.delete(0, END)
        entry_apellidos.delete(0, END)
        entry_fecha_nacimiento.delete(0, END)
        entry_direccion.delete(0, END)
        entry_telefono.delete(0, END)
        
        entry_nombre.insert(0, selected[1])
        entry_apellidos.insert(0, selected[2])
        entry_fecha_nacimiento.insert(0, selected[3])
        entry_direccion.insert(0, selected[4])
        entry_telefono.insert(0, selected[5])
    except IndexError:
        pass

# Ejecutar la interfaz gráfica
root.mainloop()
