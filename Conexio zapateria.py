import mysql.connector

# Datos de conexión a la base de datos
DB_HOST = "localhost"  
DB_USER = "root" 
DB_PASSWORD = ""  
DB_NAME = "ZAPATERIA"

try:
    # Conectar a MySQL
    conexion = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    
    if conexion.is_connected():
        print("Conexión exitosa a la base de datos")
        cursor = conexion.cursor()
        
        # Mostrar tablas disponibles
        cursor.execute("SHOW TABLES;")
        tablas = cursor.fetchall()
        print("Tablas en la base de datos:")
        for tabla in tablas:
            print(tabla[0])
        
        cursor.close()
        conexion.close()

except mysql.connector.Error as error:
    print(f"Error al conectar a MySQL: {error}")
