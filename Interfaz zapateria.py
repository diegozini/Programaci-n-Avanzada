import tkinter as tk
from tkinter import messagebox
import mysql.connector
from tkinter import ttk

# Conexión a la base de datos MySQL
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # Usa tu contraseña aquí
        database="ZAPATERIA"
    )

# Función para mostrar todos los registros de la tabla seleccionada
def show_all(table, listbox):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table}")
    records = cursor.fetchall()
    listbox.delete(0, tk.END)
    for record in records:
        listbox.insert(tk.END, record)
    conn.close()

# Función para agregar cliente
def add_cliente():
    nombre = entry_nombre_cliente.get()
    apellidos = entry_apellidos_cliente.get()
    correo = entry_correo_cliente.get()
    telefono = entry_telefono_cliente.get()
    
    if nombre and apellidos and correo and telefono:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO cliente (nombre_cliente, apellidos_cliente, correo, telefono) VALUES (%s, %s, %s, %s)", 
                       (nombre, apellidos, correo, telefono))
        conn.commit()
        show_all("cliente", listbox_cliente)
        clear_entries_cliente()
        messagebox.showinfo("Éxito", "Cliente agregado exitosamente.")
        conn.close()
    else:
        messagebox.showerror("Error", "Todos los campos son obligatorios.")

# Función para eliminar cliente
def delete_cliente():
    selected = listbox_cliente.curselection()
    if selected:
        cliente_id = listbox_cliente.get(selected[0])[0]
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM cliente WHERE id_cliente = %s", (cliente_id,))
        conn.commit()
        show_all("cliente", listbox_cliente)
        messagebox.showinfo("Éxito", "Cliente eliminado exitosamente.")
        conn.close()
    else:
        messagebox.showerror("Error", "Selecciona un cliente para eliminar.")

# Función para limpiar los campos de cliente
def clear_entries_cliente():
    entry_nombre_cliente.delete(0, tk.END)
    entry_apellidos_cliente.delete(0, tk.END)
    entry_correo_cliente.delete(0, tk.END)
    entry_telefono_cliente.delete(0, tk.END)

# Función para actualizar los datos del cliente
def update_cliente():
    selected = listbox_cliente.curselection()
    if selected:
        cliente_id = listbox_cliente.get(selected[0])[0]  # Obtener el id del cliente seleccionado
        nombre = entry_nombre_cliente.get()
        apellidos = entry_apellidos_cliente.get()
        correo = entry_correo_cliente.get()
        telefono = entry_telefono_cliente.get()

        if nombre and apellidos and correo and telefono:
            conn = connect_db()
            cursor = conn.cursor()
            # Hacer la actualización en la base de datos
            cursor.execute("""
                UPDATE cliente
                SET nombre_cliente = %s, apellidos_cliente = %s, correo = %s, telefono = %s
                WHERE id_cliente = %s
            """, (nombre, apellidos, correo, telefono, cliente_id))  # Asegúrate de que el cliente_id esté bien
            conn.commit()
            show_all("cliente", listbox_cliente)
            clear_entries_cliente()  # Limpiar los campos después de la actualización
            messagebox.showinfo("Éxito", "Cliente actualizado exitosamente.")
            conn.close()
        else:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
    else:
        messagebox.showerror("Error", "Selecciona un cliente para actualizar.")

# Función para cargar los datos del cliente seleccionado en los campos
def load_cliente_data(event):
    selected = listbox_cliente.curselection()
    if selected:
        cliente_id = listbox_cliente.get(selected[0])[0]  # Obtener el id del cliente seleccionado
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM cliente WHERE id_cliente = %s", (cliente_id,))
        record = cursor.fetchone()  # Obtener el primer (y único) registro
        if record:
            # Llenar los campos con los datos del cliente seleccionado
            entry_nombre_cliente.delete(0, tk.END)
            entry_apellidos_cliente.delete(0, tk.END)
            entry_correo_cliente.delete(0, tk.END)
            entry_telefono_cliente.delete(0, tk.END)
            entry_nombre_cliente.insert(0, record[1])  # record[1] es el nombre
            entry_apellidos_cliente.insert(0, record[2])  # record[2] es el apellido
            entry_correo_cliente.insert(0, record[3])  # record[3] es el correo
            entry_telefono_cliente.insert(0, record[4])  # record[4] es el teléfono
        conn.close()

# Interfaz gráfica con Tkinter
root = tk.Tk()
root.title("Gestión Zapatería")

# Crear pestañas
tab_control = ttk.Notebook(root)
tab_cliente = ttk.Frame(tab_control)
tab_control.add(tab_cliente, text="Clientes")
tab_control.pack(expand=1, fill="both")

# Gestión de clientes
frame_cliente = tk.LabelFrame(tab_cliente, text="Clientes", padx=10, pady=10)
frame_cliente.pack(padx=10, pady=10)

# Entradas de cliente
tk.Label(frame_cliente, text="Nombre:").grid(row=0, column=0, padx=5, pady=5)
entry_nombre_cliente = tk.Entry(frame_cliente)
entry_nombre_cliente.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_cliente, text="Apellidos:").grid(row=1, column=0, padx=5, pady=5)
entry_apellidos_cliente = tk.Entry(frame_cliente)
entry_apellidos_cliente.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_cliente, text="Correo:").grid(row=2, column=0, padx=5, pady=5)
entry_correo_cliente = tk.Entry(frame_cliente)
entry_correo_cliente.grid(row=2, column=1, padx=5, pady=5)

tk.Label(frame_cliente, text="Teléfono:").grid(row=3, column=0, padx=5, pady=5)
entry_telefono_cliente = tk.Entry(frame_cliente)
entry_telefono_cliente.grid(row=3, column=1, padx=5, pady=5)

# Botones de acción
tk.Button(frame_cliente, text="Agregar Cliente", command=add_cliente).grid(row=4, column=0, padx=5, pady=5)
tk.Button(frame_cliente, text="Eliminar Cliente", command=delete_cliente).grid(row=4, column=1, padx=5, pady=5)
tk.Button(frame_cliente, text="Actualizar Cliente", command=update_cliente).grid(row=4, column=2, padx=5, pady=5)

# Listbox para mostrar clientes
listbox_cliente = tk.Listbox(frame_cliente, height=10, width=50)
listbox_cliente.grid(row=5, column=0, columnspan=3, padx=5, pady=5)
listbox_cliente.bind("<<ListboxSelect>>", load_cliente_data)  # Cargar los datos al seleccionar un cliente
show_all("cliente", listbox_cliente)  # Mostrar todos los clientes al iniciar

# Empaque final de la interfaz
root.mainloop()
