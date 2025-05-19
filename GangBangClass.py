import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from datetime import datetime

# Conexión a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="bA4A6A",
    database="gangclass"
)
cursor = conexion.cursor()

# ----------------- PANEL PROFESOR -----------------
def abrir_panel_profesor(root, profesor_id):
    for widget in root.winfo_children():
        widget.destroy()
    root.geometry("800x600")
    root.title("Panel del Profesor")

    tabControl = ttk.Notebook(root)
    tab_proyectos = ttk.Frame(tabControl)
    tab_tareas = ttk.Frame(tabControl)
    tab_notificaciones = ttk.Frame(tabControl)
    tabControl.add(tab_proyectos, text='Proyectos')
    tabControl.add(tab_tareas, text='Tareas')
    tabControl.add(tab_notificaciones, text='Notificaciones')
    tabControl.pack(expand=1, fill='both')

    # --- CRUD Proyectos ---
    def cargar_proyectos():
        for row in tree_proyectos.get_children():
            tree_proyectos.delete(row)
        cursor.execute("SELECT Id, Nombre, Descripcion, Fecha_inicio, Fecha_fin FROM proyectos WHERE Creador_tipo='Profesor' AND Creador_id=%s", (profesor_id,))
        for row in cursor.fetchall():
            tree_proyectos.insert('', 'end', values=row)

    def crear_proyecto():
        nombre = entry_nombre.get().strip()
        descripcion = entry_desc.get().strip()
        inicio = entry_inicio.get().strip()
        fin = entry_fin.get().strip()
        # Validaciones básicas fechas
        try:
            datetime.strptime(inicio, '%Y-%m-%d')
            datetime.strptime(fin, '%Y-%m-%d')
        except ValueError:
            messagebox.showerror("Error", "Fecha inválida, usa formato YYYY-MM-DD")
            return
        if not nombre or not descripcion:
            messagebox.showerror("Error", "Completa nombre y descripción")
            return
        cursor.execute(
            "INSERT INTO proyectos (Nombre, Descripcion, Fecha_inicio, Fecha_fin, Creador_tipo, Creador_id) VALUES (%s, %s, %s, %s, 'Profesor', %s)",
            (nombre, descripcion, inicio, fin, profesor_id)
        )
        conexion.commit()
        cargar_proyectos()

    def eliminar_proyecto():
        seleccionado = tree_proyectos.selection()
        if seleccionado:
            proyecto_id = tree_proyectos.item(seleccionado)['values'][0]
            cursor.execute("DELETE FROM proyectos WHERE Id=%s", (proyecto_id,))
            conexion.commit()
            cargar_proyectos()

    tk.Label(tab_proyectos, text="Nombre").pack()
    entry_nombre = tk.Entry(tab_proyectos)
    entry_nombre.pack()
    tk.Label(tab_proyectos, text="Descripción").pack()
    entry_desc = tk.Entry(tab_proyectos)
    entry_desc.pack()
    tk.Label(tab_proyectos, text="Fecha Inicio (YYYY-MM-DD)").pack()
    entry_inicio = tk.Entry(tab_proyectos)
    entry_inicio.pack()
    tk.Label(tab_proyectos, text="Fecha Fin (YYYY-MM-DD)").pack()
    entry_fin = tk.Entry(tab_proyectos)
    entry_fin.pack()

    tk.Button(tab_proyectos, text="Crear Proyecto", command=crear_proyecto).pack(pady=5)
    tk.Button(tab_proyectos, text="Eliminar Proyecto", command=eliminar_proyecto).pack()

    tree_proyectos = ttk.Treeview(tab_proyectos, columns=("Id", "Nombre", "Descripcion", "Inicio", "Fin"), show='headings')
    for col in tree_proyectos["columns"]:
        tree_proyectos.heading(col, text=col)
    tree_proyectos.pack(expand=True, fill='both')
    cargar_proyectos()

    # --- CRUD Tareas ---
    def cargar_tareas():
        for row in tree_tareas.get_children():
            tree_tareas.delete(row)
        cursor.execute("SELECT Id, Descripcion, Estado, Fecha_limite, Proyecto_id FROM tareas WHERE Asignado_tipo='Profesor' AND Asignado_id=%s", (profesor_id,))
        for row in cursor.fetchall():
            tree_tareas.insert('', 'end', values=row)

    def crear_tarea():
        desc = entry_desc_tarea.get().strip()
        fecha_lim = entry_fecha_limite.get().strip()
        proyecto_id = entry_proyecto_id.get().strip()
        # Validar fecha y datos
        try:
            datetime.strptime(fecha_lim, '%Y-%m-%d')
        except ValueError:
            messagebox.showerror("Error", "Fecha límite inválida")
            return
        if not desc or not proyecto_id.isdigit():
            messagebox.showerror("Error", "Completa todos los campos correctamente")
            return
        cursor.execute(
            "INSERT INTO tareas (Descripcion, Estado, Fecha_limite, Proyecto_id, Asignado_tipo, Asignado_id) VALUES (%s, 'Pendiente', %s, %s, 'Profesor', %s)",
            (desc, fecha_lim, int(proyecto_id), profesor_id)
        )
        conexion.commit()
        cargar_tareas()

    def eliminar_tarea():
        seleccionado = tree_tareas.selection()
        if seleccionado:
            tarea_id = tree_tareas.item(seleccionado)['values'][0]
            cursor.execute("DELETE FROM tareas WHERE Id=%s", (tarea_id,))
            conexion.commit()
            cargar_tareas()

    tk.Label(tab_tareas, text="Descripción").pack()
    entry_desc_tarea = tk.Entry(tab_tareas)
    entry_desc_tarea.pack()
    tk.Label(tab_tareas, text="Fecha Límite (YYYY-MM-DD)").pack()
    entry_fecha_limite = tk.Entry(tab_tareas)
    entry_fecha_limite.pack()
    tk.Label(tab_tareas, text="ID Proyecto").pack()
    entry_proyecto_id = tk.Entry(tab_tareas)
    entry_proyecto_id.pack()

    tk.Button(tab_tareas, text="Crear Tarea", command=crear_tarea).pack(pady=5)
    tk.Button(tab_tareas, text="Eliminar Tarea", command=eliminar_tarea).pack()

    tree_tareas = ttk.Treeview(tab_tareas, columns=("Id", "Descripcion", "Estado", "Fecha_limite", "Proyecto_id"), show='headings')
    for col in tree_tareas["columns"]:
        tree_tareas.heading(col, text=col)
    tree_tareas.pack(expand=True, fill='both')
    cargar_tareas()

    # --- CRUD Notificaciones ---
    def cargar_notificaciones():
        for row in tree_notif.get_children():
            tree_notif.delete(row)
        cursor.execute("SELECT Id, Mensaje, Fecha, Leido FROM notificaciones WHERE Usuario_tipo='Profesor' AND Usuario_id=%s", (profesor_id,))
        for row in cursor.fetchall():
            tree_notif.insert('', 'end', values=row)

    def enviar_notificacion():
        msg = entry_notif.get().strip()
        if not msg:
            messagebox.showerror("Error", "Escribe un mensaje para enviar")
            return
        cursor.execute("INSERT INTO notificaciones (Mensaje, Usuario_tipo, Usuario_id, Fecha, Leido) VALUES (%s, 'Profesor', %s, NOW(), 0)", (msg, profesor_id))
        conexion.commit()
        cargar_notificaciones()
        entry_notif.delete(0, tk.END)

    def eliminar_notificacion():
        seleccionado = tree_notif.selection()
        if seleccionado:
            notif_id = tree_notif.item(seleccionado)['values'][0]
            cursor.execute("DELETE FROM notificaciones WHERE Id=%s", (notif_id,))
            conexion.commit()
            cargar_notificaciones()

    tk.Label(tab_notificaciones, text="Mensaje").pack()
    entry_notif = tk.Entry(tab_notificaciones, width=50)
    entry_notif.pack()
    tk.Button(tab_notificaciones, text="Enviar", command=enviar_notificacion).pack(pady=5)
    tk.Button(tab_notificaciones, text="Eliminar", command=eliminar_notificacion).pack()

    tree_notif = ttk.Treeview(tab_notificaciones, columns=("Id", "Mensaje", "Fecha", "Leido"), show='headings')
    for col in tree_notif["columns"]:
        tree_notif.heading(col, text=col)
    tree_notif.pack(expand=True, fill='both')
    cargar_notificaciones()

# ----------------- PANEL ALUMNO -----------------
def abrir_panel_alumno(root, alumno_id):
    for widget in root.winfo_children():
        widget.destroy()
    root.geometry("700x500")
    root.title("Panel del Alumno")

    # Mostrar tareas asignadas al alumno (simplificado)
    tk.Label(root, text="Tareas asignadas:", font=("Arial", 14)).pack(pady=10)

    tree_tareas = ttk.Treeview(root, columns=("Id", "Descripcion", "Estado", "Fecha_limite", "Proyecto_id"), show='headings')
    for col in tree_tareas["columns"]:
        tree_tareas.heading(col, text=col)
    tree_tareas.pack(expand=True, fill='both')

    def cargar_tareas_alumno():
        for row in tree_tareas.get_children():
            tree_tareas.delete(row)
        # Aquí se asume que las tareas se asignan con Asignado_tipo='Alumno' y Asignado_id = alumno_id
        cursor.execute("SELECT Id, Descripcion, Estado, Fecha_limite, Proyecto_id FROM tareas WHERE Asignado_tipo='Alumno' AND Asignado_id=%s", (alumno_id,))
        for row in cursor.fetchall():
            tree_tareas.insert('', 'end', values=row)

    cargar_tareas_alumno()

# ----------------- REGISTRO Y LOGIN -----------------

def registrar_profesor(root):
    for widget in root.winfo_children():
        widget.destroy()
    root.geometry("350x300")
    root.title("Registrar Profesor")

    tk.Label(root, text="Nombre:").pack(pady=5)
    entry_nombre = tk.Entry(root)
    entry_nombre.pack(pady=5)

    tk.Label(root, text="Correo:").pack(pady=5)
    entry_correo = tk.Entry(root)
    entry_correo.pack(pady=5)

    tk.Label(root, text="Contraseña:").pack(pady=5)
    entry_contra = tk.Entry(root, show="*")
    entry_contra.pack(pady=5)

    def guardar():
        nombre = entry_nombre.get().strip()
        correo = entry_correo.get().strip()
        contra = entry_contra.get().strip()

        if not nombre or not correo or not contra:
            messagebox.showwarning("Campos vacíos", "Completa todos los campos.")
            return
        
        try:
            cursor.execute("INSERT INTO profesores (Nombre, Correo, Contraseña) VALUES (%s, %s, %s)", (nombre, correo, contra))
            conexion.commit()
            messagebox.showinfo("Éxito", "Profesor registrado correctamente.")
            iniciar_sesion(root)
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"No se pudo registrar: {err}")

    tk.Button(root, text="Registrar", command=guardar).pack(pady=10)
    tk.Button(root, text="Volver", command=lambda: iniciar_sesion(root)).pack()

def registrar_alumno(root):
    for widget in root.winfo_children():
        widget.destroy()
    root.geometry("350x300")
    root.title("Registrar Alumno")

    tk.Label(root, text="Nombre:").pack(pady=5)
    entry_nombre = tk.Entry(root)
    entry_nombre.pack(pady=5)

    tk.Label(root, text="Correo:").pack(pady=5)
    entry_correo = tk.Entry(root)
    entry_correo.pack(pady=5)

    tk.Label(root, text="Contraseña:").pack(pady=5)
    entry_contra = tk.Entry(root, show="*")
    entry_contra.pack(pady=5)

    def guardar():
        nombre = entry_nombre.get().strip()
        correo = entry_correo.get().strip()
        contra = entry_contra.get().strip()

        if not nombre or not correo or not contra:
            messagebox.showwarning("Campos vacíos", "Completa todos los campos.")
            return
        
        try:
            cursor.execute("INSERT INTO alumnos (Nombre, Correo, Contraseña) VALUES (%s, %s, %s)", (nombre, correo, contra))
            conexion.commit()
            messagebox.showinfo("Éxito", "Alumno registrado correctamente.")
            iniciar_sesion(root)
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"No se pudo registrar: {err}")

    tk.Button(root, text="Registrar", command=guardar).pack(pady=10)
    tk.Button(root, text="Volver", command=lambda: iniciar_sesion(root)).pack()

def iniciar_sesion(root):
    for widget in root.winfo_children():
        widget.destroy()
    root.geometry("300x250")
    root.title("Iniciar Sesión")

    tk.Label(root, text="Correo:").pack(pady=5)
    entry_correo = tk.Entry(root)
    entry_correo.pack(pady=5)

    tk.Label(root, text="Contraseña:").pack(pady=5)
    entry_contra = tk.Entry(root, show="*")
    entry_contra.pack(pady=5)

    def login():
        correo = entry_correo.get().strip()
        contra = entry_contra.get().strip()

        if not correo or not contra:
            messagebox.showwarning("Campos vacíos", "Por favor ingresa correo y contraseña.")
            return

        cursor.execute("SELECT Id, Nombre FROM profesores WHERE Correo=%s AND Contraseña=%s", (correo, contra))
        prof = cursor.fetchone()
        if prof:
            messagebox.showinfo("Bienvenido", f"Profesor {prof[1]} ha iniciado sesión.")
            abrir_panel_profesor(root, prof[0])
            return

        cursor.execute("SELECT Id, Nombre FROM alumnos WHERE Correo=%s AND Contraseña=%s", (correo, contra))
        alum = cursor.fetchone()
        if alum:
            messagebox.showinfo("Bienvenido", f"Alumno {alum[1]} ha iniciado sesión.")
            abrir_panel_alumno(root, alum[0])
            return

        messagebox.showerror("Error", "Correo o contraseña incorrectos.")

    tk.Button(root, text="Iniciar Sesión", command=login).pack(pady=10)

    tk.Button(root, text="Registrar Profesor", command=lambda: registrar_profesor(root)).pack(pady=5)
    tk.Button(root, text="Registrar Alumno", command=lambda: registrar_alumno(root)).pack(pady=5)

# --------- MAIN -----------
if __name__ == "__main__":
    root = tk.Tk()
    iniciar_sesion(root)
    root.mainloop()
