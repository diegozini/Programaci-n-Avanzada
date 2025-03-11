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
        database="PLAZA_COMERCIAL"
    )

# Función para actualizar la lista de tiendas en el Listbox
def show_all_tiendas():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tienda")
    tiendas = cursor.fetchall()
    listbox_tiendas.delete(0, tk.END)  # Limpia el listbox antes de mostrar los datos
    for tienda in tiendas:
        listbox_tiendas.insert(tk.END, f"{tienda[0]} - {tienda[1]}")
    conn.close()

# Función para agregar tienda
def add_tienda():
    conn = connect_db()
    cursor = conn.cursor()
    
    nombre = entry_nombre_tienda.get()
    sector = entry_sector_tienda.get()
    direccion = entry_direccion_tienda.get()
    
    if nombre and sector and direccion:
        cursor.execute("INSERT INTO tienda (nombre_tienda, sector, dir_tienda) VALUES (%s, %s, %s)",
                       (nombre, sector, direccion))
        conn.commit()
        messagebox.showinfo("Éxito", "Tienda agregada exitosamente.")
        show_all_tiendas()  # Refresca la lista de tiendas
        clear_entries_tienda()  # Limpia los campos
    else:
        messagebox.showerror("Error", "Todos los campos son obligatorios.")
    
    conn.close()

# Función para eliminar tienda
def delete_tienda():
    selected = listbox_tiendas.curselection()
    if selected:
        tienda_id = listbox_tiendas.get(selected[0]).split(" - ")[0]
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tienda WHERE id_tienda = %s", (tienda_id,))
        conn.commit()
        show_all_tiendas()  # Refresca la lista
        messagebox.showinfo("Éxito", "Tienda eliminada exitosamente.")
        conn.close()
    else:
        messagebox.showerror("Error", "Selecciona una tienda para eliminar.")

# Función para actualizar tienda
def update_tienda():
    selected = listbox_tiendas.curselection()
    if selected:
        tienda_id = listbox_tiendas.get(selected[0]).split(" - ")[0]
        nombre = entry_nombre_tienda.get()
        sector = entry_sector_tienda.get()
        direccion = entry_direccion_tienda.get()
        
        if nombre and sector and direccion:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE tienda
                SET nombre_tienda = %s, sector = %s, dir_tienda = %s
                WHERE id_tienda = %s
            """, (nombre, sector, direccion, tienda_id))
            conn.commit()
            show_all_tiendas()  # Refresca la lista
            messagebox.showinfo("Éxito", "Tienda actualizada exitosamente.")
            clear_entries_tienda()  # Limpia los campos
            conn.close()
        else:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
    else:
        messagebox.showerror("Error", "Selecciona una tienda para actualizar.")

# Función para limpiar los campos de entrada
def clear_entries_tienda():
    entry_nombre_tienda.delete(0, tk.END)
    entry_sector_tienda.delete(0, tk.END)
    entry_direccion_tienda.delete(0, tk.END)

# Interfaz gráfica con Tkinter
root = tk.Tk()
root.title("Gestión Plaza Comercial")

# Configuración para las tiendas
frame_tienda = tk.LabelFrame(root, text="Gestión Tiendas", padx=10, pady=10)
frame_tienda.pack(padx=10, pady=10)

# Entradas de la tienda
tk.Label(frame_tienda, text="Nombre de la tienda:").grid(row=0, column=0, padx=5, pady=5)
entry_nombre_tienda = tk.Entry(frame_tienda)
entry_nombre_tienda.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_tienda, text="Sector:").grid(row=1, column=0, padx=5, pady=5)
entry_sector_tienda = tk.Entry(frame_tienda)
entry_sector_tienda.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_tienda, text="Dirección:").grid(row=2, column=0, padx=5, pady=5)
entry_direccion_tienda = tk.Entry(frame_tienda)
entry_direccion_tienda.grid(row=2, column=1, padx=5, pady=5)

# Botones de acción
tk.Button(frame_tienda, text="Agregar Tienda", command=add_tienda).grid(row=3, column=0, padx=5, pady=5)
tk.Button(frame_tienda, text="Eliminar Tienda", command=delete_tienda).grid(row=3, column=1, padx=5, pady=5)
tk.Button(frame_tienda, text="Actualizar Tienda", command=update_tienda).grid(row=3, column=2, padx=5, pady=5)

# Listbox para mostrar tiendas
listbox_tiendas = tk.Listbox(frame_tienda, height=10, width=50)
listbox_tiendas.grid(row=4, column=0, columnspan=3, padx=5, pady=5)
show_all_tiendas()  # Muestra todas las tiendas al iniciar

# Empaque final de la interfaz
root.mainloop()
