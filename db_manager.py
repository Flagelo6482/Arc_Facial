import psycopg2

class DBManager:
    def __init__(self, dbname, user, password, host="localhost", port="5432"):
        """
        Inicializa el gestor de la base de datos con los parámetros de conexión.
        """
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.conn = None # La conexión se establecerá al usar un método
        self.cursor = None

    def conectar(self):
        """Establece la conexión con la base de datos PostgreSQL."""
        try:
            self.conn = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            self.conn.autocommit = True # Hace que los cambios sean permanentes inmediatamente
            self.cursor = self.conn.cursor()
            return True
        except psycopg2.Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            return False

    def cerrar(self):
        """Cierra el cursor y la conexión a la base de datos."""
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

    def insertar_administrador(self, datos):
        """
        Inserta un nuevo registro de administrador en la tabla 'administrador'.

        Args:
            datos (dict): Diccionario con los datos del administrador procesados.
        """
        if not self.conectar():
            return False, "No se pudo conectar a la base de datos."

        try:
            # 1. Definir la consulta de inserción
            sql = """
            INSERT INTO administrador (
                nombres, apellidos, numero_telefonico, correo_electronico, 
                usuario, contrasena_encriptada, fecha_registro
            ) VALUES (
                %s, %s, %s, %s, %s, %s, %s
            );
            """

            # 2. Preparar la tupla de datos en el ORDEN de la consulta SQL
            data_to_insert = (
                datos['nombres'],
                datos['apellidos'],
                datos['numero_telefonico'],
                datos['correo_electronico'],
                datos['usuario'],
                datos['contrasena_encriptada'],
                datos['fecha_registro']
            )

            # 3. Ejecutar la consulta
            self.cursor.execute(sql, data_to_insert)
            self.cerrar()
            return True, "Registro exitoso."
        
        except psycopg2.IntegrityError as e:
            # Manejar errores comunes de unicidad (usuario o correo ya existen)
            self.cerrar()
            if "usuario" in str(e):
                return False, "El nombre de usuario ya existe."
            elif "correo_electronico" in str(e):    
                return False, "El correo electrónico ya está registrado."
            elif "numero_telefonico" in str(e):
                return False, "El número de contacto ingresado ya fue registrado."
            else:
                return False, f"Error de integridad: {e}"
                
        except psycopg2.Error as e:
            print(f"Error al insertar en la base de datos: {e}")
            self.cerrar()
            return False, f"Error desconocido al registrar: {e}"