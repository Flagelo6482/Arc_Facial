import bcrypt
from bbdd import get_connection

def iniciar_sesion():
    """Iniciamos sesion con las credenciales de un administrador registrado"""
    print("\n--- INICAR SESIÓN ---")
    
    usuario = input("Usuario: ").strip()
    contraseña = input("Contraseña: ").strip()
    
    if not usuario or not contraseña:
        print("Debe ingresar el usuario y contraseña.")
        return None
    
    #Llamamos a la función para conectarnos a la base de datos en caso no tengamos respuesta no retornaremos nada
    conn = get_connection()
    if conn is None:
        return None
        
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombres, apellidos, contraseña_encriptada FROM administradores WHERE usuario = %s", (usuario,))
        resultado = cursor.fetchone()
        
        if resultado is None:
            print("❌ Usuario no encontrado")
            return None
        
        id_admin, nombres, apellidos, contraseña_encriptada_db = resultado
        if bcrypt.checkpw(contraseña.encode('utf-8'), contraseña_encriptada_db.encode('utf-8')):
            print(f"✅ ¡Bienvenido {nombres} {apellidos}!")
            #Retornamos el "id_admin" para usarlo para navegar por las entradas que se requieran
            return id_admin
        else:
            print("❌ Contraseña incorrecta")
            return None

    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        return None
    finally:
        if cursor: cursor.close()
        if conn: conn.close()