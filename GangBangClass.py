import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Conexión a la base de datos
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="gangclass"
)
cursor = conn.cursor()

def registrar():
    nombre = entry_nombre.get()
    correo = entry_correo.get()
    contraseña = entry_contraseña.get()
    tipo_usuario = var_tipo.get()
    
    if nombre and correo and contraseña and tipo_usuario:
        try:
            if tipo_usuario == "Profesor":
                cursor.execute("INSERT INTO profesores (Nombre, Correo, Contraseña) VALUES (%s, %s, %s)", (nombre, correo, contraseña))
            else:
                cursor.execute("INSERT INTO alumnos (Nombre, Correo, Contraseña) VALUES (%s, %s, %s)", (nombre, correo, contraseña))
            conn.commit()
            messagebox.showinfo("Éxito", "Registro exitoso. Ahora puede iniciar sesión.")
            ventana_registro.destroy()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error en la base de datos: {err}")
    else:
        messagebox.showwarning("Advertencia", "Completa todos los campos")

def abrir_registro():
    global ventana_registro, entry_nombre, entry_correo, entry_contraseña, var_tipo
    ventana_registro = tk.Toplevel()
    ventana_registro.title("Registro")
    
    tk.Label(ventana_registro, text="Nombre:").pack()
    entry_nombre = tk.Entry(ventana_registro)
    entry_nombre.pack()
    
    tk.Label(ventana_registro, text="Correo:").pack()
    entry_correo = tk.Entry(ventana_registro)
    entry_correo.pack()
    
    tk.Label(ventana_registro, text="Contraseña:").pack()
    entry_contraseña = tk.Entry(ventana_registro, show="*")
    entry_contraseña.pack()
    
    var_tipo = tk.StringVar(value="Alumno")
    tk.Radiobutton(ventana_registro, text="Profesor", variable=var_tipo, value="Profesor").pack()
    tk.Radiobutton(ventana_registro, text="Alumno", variable=var_tipo, value="Alumno").pack()
    
    tk.Button(ventana_registro, text="Registrar", command=registrar).pack()

def login():
    usuario = entry_usuario.get()
    contraseña = entry_contraseña.get()
    cursor.execute("SELECT Id, 'Profesor' AS Tipo FROM profesores WHERE Correo=%s AND Contraseña=%s UNION SELECT Id, 'Alumno' AS Tipo FROM alumnos WHERE Correo=%s AND Contraseña=%s", (usuario, contraseña, usuario, contraseña))
    user = cursor.fetchone()
    
    if user:
        user_id, user_type = user
        root.withdraw()
        if user_type == 'Profesor':
            abrir_profesor(user_id)
        else:
            abrir_alumno(user_id)
    else:
        messagebox.showerror("Error", "Credenciales incorrectas")

def abrir_profesor(profesor_id):
    ventana_profesor = tk.Toplevel()
    ventana_profesor.title("Panel del Profesor")
    tk.Label(ventana_profesor, text="Panel de Profesor").pack()
    
    tk.Button(ventana_profesor, text="Crear Proyecto", command=lambda: crear_proyecto(profesor_id)).pack()
    tk.Button(ventana_profesor, text="Asignar Tarea", command=lambda: asignar_tarea(profesor_id)).pack()
    tk.Button(ventana_profesor, text="Enviar Notificación", command=lambda: enviar_notificacion(profesor_id)).pack()

def abrir_alumno(alumno_id):
    ventana_alumno = tk.Toplevel()
    ventana_alumno.title("Panel del Alumno")
    tk.Label(ventana_alumno, text="Panel del Alumno").pack()
    
    tk.Button(ventana_alumno, text="Enviar Tarea", command=lambda: enviar_tarea(alumno_id)).pack()
    tk.Button(ventana_alumno, text="Enviar Mensaje", command=lambda: enviar_mensaje(alumno_id)).pack()

def crear_proyecto(profesor_id):
    pass

def asignar_tarea(profesor_id):
    pass

def enviar_notificacion(profesor_id):
    pass

def enviar_tarea(alumno_id):
    pass

def enviar_mensaje(alumno_id):
    pass

root = tk.Tk()
root.title("Inicio de Sesión")

tk.Label(root, text="Correo:").pack()
entry_usuario = tk.Entry(root)
entry_usuario.pack()

tk.Label(root, text="Contraseña:").pack()
entry_contraseña = tk.Entry(root, show="*")
entry_contraseña.pack()

tk.Button(root, text="Iniciar Sesión", command=login).pack()
tk.Button(root, text="Registrarse", command=abrir_registro).pack()

root.mainloop()