import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Configuración de la conexión a MySQL
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = ""
DB_NAME = "BANCO"

def conectar_bd():
    return mysql.connector.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)

# Función para insertar un cliente
def insertar_cliente():
    nombre = entry_nombre.get()
    apellidos = entry_apellidos.get()
    direccion = entry_direccion.get()
    telefono = entry_telefono.get()
    
    if nombre and apellidos and telefono:
        conexion = conectar_bd()
        cursor = conexion.cursor()
        sql = "INSERT INTO cliente (nombre_cliente, apellidos_cliente, direccion, telefono) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (nombre, apellidos, direccion, telefono))
        conexion.commit()
        conexion.close()
        messagebox.showinfo("Éxito", "Cliente agregado correctamente")
        listar_clientes()
    else:
        messagebox.showwarning("Error", "Completa todos los campos obligatorios")

# Función para listar clientes
def listar_clientes():
    conexion = conectar_bd()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM cliente")
    registros = cursor.fetchall()
    conexion.close()
    
    listbox_clientes.delete(0, tk.END)
    for cliente in registros:
        listbox_clientes.insert(tk.END, f"{cliente[0]} - {cliente[1]} {cliente[2]} - {cliente[3]}")

# Función para eliminar un cliente
def eliminar_cliente():
    seleccion = listbox_clientes.curselection()
    if seleccion:
        cliente_id = listbox_clientes.get(seleccion).split(" - ")[0]
        conexion = conectar_bd()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM cliente WHERE id_cliente = %s", (cliente_id,))
        conexion.commit()
        conexion.close()
        messagebox.showinfo("Éxito", "Cliente eliminado correctamente")
        listar_clientes()
    else:
        messagebox.showwarning("Error", "Selecciona un cliente para eliminar")

# Función para actualizar un cliente
def actualizar_cliente():
    seleccion = listbox_clientes.curselection()
    if seleccion:
        cliente_id = listbox_clientes.get(seleccion).split(" - ")[0]
        nuevo_nombre = entry_nombre.get()
        nuevos_apellidos = entry_apellidos.get()
        nueva_direccion = entry_direccion.get()
        nuevo_telefono = entry_telefono.get()
        
        if nuevo_nombre and nuevos_apellidos and nuevo_telefono:
            conexion = conectar_bd()
            cursor = conexion.cursor()
            sql = """UPDATE cliente 
                     SET nombre_cliente = %s, apellidos_cliente = %s, direccion = %s, telefono = %s 
                     WHERE id_cliente = %s"""
            valores = (nuevo_nombre, nuevos_apellidos, nueva_direccion, nuevo_telefono, cliente_id)
            cursor.execute(sql, valores)
            conexion.commit()
            conexion.close()
            messagebox.showinfo("Éxito", "Cliente actualizado correctamente")
            listar_clientes()
        else:
            messagebox.showwarning("Error", "Completa todos los campos obligatorios")
    else:
        messagebox.showwarning("Error", "Selecciona un cliente para actualizar")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("CRUD Clientes")
ventana.geometry("400x400")

# Etiquetas y campos de entrada
tk.Label(ventana, text="Nombre:").pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

tk.Label(ventana, text="Apellidos:").pack()
entry_apellidos = tk.Entry(ventana)
entry_apellidos.pack()

tk.Label(ventana, text="Dirección:").pack()
entry_direccion = tk.Entry(ventana)
entry_direccion.pack()

tk.Label(ventana, text="Teléfono:").pack()
entry_telefono = tk.Entry(ventana)
entry_telefono.pack()

# Botones
tk.Button(ventana, text="Agregar Cliente", command=insertar_cliente).pack()
tk.Button(ventana, text="Eliminar Cliente", command=eliminar_cliente).pack()
tk.Button(ventana, text="Actualizar Cliente", command=actualizar_cliente).pack()

# Listbox para mostrar clientes
listbox_clientes = tk.Listbox(ventana)
listbox_clientes.pack(fill=tk.BOTH, expand=True)

# Cargar lista de clientes al inicio
listar_clientes()

# Ejecutar aplicación
ventana.mainloop()
