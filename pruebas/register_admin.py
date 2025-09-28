"""
Sección donde se genera un nuevo "administrador" para que tenga una
cuenta e ingrese para guardar los datos sus personas conocidas

Conectarnos a la base de datos para guardar los registros   OKI DOKI
Registraremos los siguientes datos:

  nombres: Añadiendo validaciones de longitud de caracteres, que no se      
     encuentre vacío.
  apellidos: Añadiendo validaciones de longitud de caracteres, que no se
     encuentre vacío.
  numero_telefonico: Añadiendo validaciones de no contener letras,                      contener 9 digitos que sean solo números, que no este vacío
  correo_electronico: Añadiendo validaciones de formato correcto de                                                correo, que no se encuentre vacío
  dni: Añadiendo validaciones de que no se encuentre vacío, que tenga 8       dígitos que sean solo números
  usuario: Añadiendo validaciones de longitud de letras, que no este vacío,    que sea único
  contraseña: Añadiendo validaciones agregando encriptación

  3.Validar el registro del usuario:

  -Confirmar si se registro correctamente o obtuvo un error de por medio
  -Agregar si DNI, Correo, Usuario ya existen en la base de datos
  -Agregar excepciones que capturen errores en el programa
"""

from bbdd import get_connection
from datetime import datetime

def validar_email(email):
    """Valida el formato del email"""
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(patron, email) is not None

def validar_dni(dni):
    """Valida que el DNI tenga 8 dígitos"""
    return dni.isdigit() and len(dni) == 8

def registrar_administrador():
    print("\n===SISTEMA DE SEGURIDAD - REGISTRAR ADMINISTRADOR===")

    nombres = input("Nombres: ").strip()
    apellidos = input("Apellidos: ").strip()
    numero_telefonico = input("Número telefónico: ").strip()
    correo_electronico = input("Correo electrónico: ").strip()
    dni = input("DNI (8 dígitos): ").strip()
    usuario = input("Usuario: ").strip()
    contraseña = input("Contraseña: ").strip()

    #Validaciones de datos
    #Validar nombres
    if not nombres.strip():
        print("Los nombres no puede estar vacio.")
        return
    if len(nombres) < 2:
        print("Debe tener almenos más de 2 caracteres")
        return
    if len(nombres) > 50:
        print("El nombre no puede exceder los 50 caracteres")
        return
    nombres = nombres.title()

    #Validar apellidos
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


    #Validar correo
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














