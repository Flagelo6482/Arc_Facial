import psycopg2
import bcrypt
from datetime import datetime
import re  # Para validar email

# Configuración de la base de datos (modifica con tus datos)
DB_CONFIG = {
    "host": "localhost",
    "database": "demo",
    "user": "postgres",
    "password": "1234",
    "port": "5432"
}

def validar_email(email):
    """Valida el formato del email"""
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(patron, email) is not None

def validar_dni(dni):
    """Valida que el DNI tenga 8 dígitos"""
    return dni.isdigit() and len(dni) == 8

def registrar_administrador():
    """Registra un nuevo administrador en la base de datos"""
    print("\n--- REGISTRO DE ADMINISTRADOR ---")
    
    # Capturar datos
    nombres = input("Nombres: ").strip()
    apellidos = input("Apellidos: ").strip()
    numero_telefonico = input("Número telefónico: ").strip()
    correo_electronico = input("Correo electrónico: ").strip()
    dni = input("DNI (8 dígitos): ").strip()
    usuario = input("Usuario: ").strip()
    contraseña = input("Contraseña: ").strip()

    # Validaciones
    if not nombres.strip():
        print("Los nombres no puede estar vacio.")
        return
    if len(nombres) < 2:
        print("Debe tener almenos más de 2 caracteres")
        return
    if len(nombres) > 50:
        print("El nombre no puede exceder los 50 caracteres")
        return
    nombres = nombres.title()  # Convierte "juan perez" en "Juan Perez"
    
    #Validar apellido
    if not apellidos.strip():
        print("Los apellidos no puede estar vacio.")
        return
    if len(apellidos) < 2:
        print("Debe tener almenos más de 2 caracteres")
        return
    if len(apellidos) > 50:
        print("Los apellidos no puede exceder los 50 caracteres")
        return
    apellidos = apellidos.title()
    
    #Validar telefono
    if not numero_telefonico.isdigit():
        print("Error: El numero telefonico no puede contener letras")
        return None
    if len(numero_telefonico) != 9:
        print("Error: El numero telefonico debe contener 9 digítos")
    
    #Validar Correo Electronico
    if not validar_email(correo_electronico):
        print("❌ Error: Formato de email inválido")
        return

    #Validar DNI
    if not validar_dni(dni):
        print("❌ Error: DNI debe tener 8 dígitos numéricos")
        return

    #Validar contraseña
    if len(contraseña) < 6:
        print("❌ Error: La contraseña debe tener al menos 6 caracteres")
        return

    # Encriptar contraseña
    contraseña_encriptada = bcrypt.hashpw(contraseña.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    fecha_registro = datetime.now()

    # Conexión a la BD
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()

        # Insertar datos
        cursor.execute("""
            INSERT INTO administradores 
            (nombres, apellidos, numero_telefonico, correo_electronico, dni, usuario, contraseña_encriptada, fecha_registro)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (nombres, apellidos, numero_telefonico, correo_electronico, dni, usuario, contraseña_encriptada, fecha_registro))
        
        conn.commit()
        print("✅ Administrador registrado exitosamente!")

    except psycopg2.IntegrityError as e:
        print("❌ Error: El correo, DNI o usuario ya existen en la base de datos")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def listar_administradores():
    """Muestra todos los administradores registrados en la base de datos"""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM administradores ORDER BY id")
        administradores = cursor.fetchall()
        
        if not administradores:
            print("❌ No hay administradores registrados")
            return
        
        print("\n--- LISTA DE ADMINISTRADORES ---")
        for admin in administradores:
            print(f"""
ID: {admin[0]}
Nombres: {admin[1]}
Apellidos: {admin[2]}
Teléfono: {admin[3]}
Email: {admin[4]}
DNI: {admin[5]}
Usuario: {admin[6]}
Fecha Registro: {admin[8]}
            """)
            
    except Exception as e:
        print(f"❌ Error al listar administradores: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    #registrar_administrador()
    listar_administradores()