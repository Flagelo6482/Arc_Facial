import re
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from db_manager import DBManager
import datetime
import bcrypt

"""
Criterios de aceptación:

Diseño profesional con paleta de colores: blanco, azul oscuro, gris
Formulario con campos claramente separados y etiquetas intuitivas
Validación en tiempo real para nombres, apellidos y usuario (solo letras sin tildes)
Validación de teléfono (9-15 dígitos, solo números)
Validación de email (formato usuario@dominio.com)
Campos obligatorios marcados con asterisco (*) y mensajes de error en rojo
Verificación en BD de unicidad de usuario y email
Límites de longitud para cada campo (ej: usuario máximo 15 caracteres)
Botón "Volver al Menú" visible y funcional
Confirmación de registro exitoso con redirección automática
"""


def validar_limite(nuevo_texto, limite):
    """
    Función que verifica que la longitud del texto propuesto NO exceda el límite.
    Se llama automáticamente por Tkinter al presionar una tecla.
    """
    # El límite se pasa como string, lo convertimos a int
    limite = int(limite)
    # Retorna False para rechazar la tecla si se excede el limite
    return len(nuevo_texto) <= limite


class FormularioRegistro:
    def __init__(self, ventana_principal, aplicacion_principal):
        """
        Args:
            ventana_principal (_type_): Es la ventana Tk principal
            aplicacion_principal (_type_): Instancia de la clase Aplication para volver al menú
        """
        self.ventana_principal = ventana_principal
        self.aplicacion_principal = aplicacion_principal

        #Registramos el comando de validación
        self.vcmd_limite = self.ventana_principal.register(validar_limite)

        #Definimos los limites que usaremos en la interfaz
        self.LIMITE_NOMBRE = 30
        self.LIMITE_APELIIDO = 30
        self.LIMITE_NUMERO = 30
        self.LIMITE_CORREO = 30
        self.LIMITE_USUARIO = 30
        self.LIMITE_CONTRASENA = 30

        #Iniciamos el gestor de DB
        self.db_manager = DBManager(
            dbname="demo",
            user="postgres",
            password="1234"
        )

        #Limpiamos la ventana principal
        self.limpiar_ventana()
        self.crear_interfaz()

    
    def limpiar_ventana(self):
        """Limpia todos los widgets de la ventana principal(la anterior)"""
        for widget in self.ventana_principal.winfo_children():
            widget.destroy()

    """5.Función para encriptar la contraseña D:
    """
    def encriptar_contrasena(self, contrasena):
        """Generamos un hash seguro para la contraseña usando bcrypt"""
        #Generamos un 'salt' (valor aleatorio)
        salt = bcrypt.gensalt()

        #Codificamos la contraseña a bytes y hashearla
        hashed_contrasena = bcrypt.hashpw(contrasena.encode('utf-8'), salt)

        #Devolvemos el hash (lo que guardaremos en la BD)
        return hashed_contrasena.decode('utf-8')


    """6.Función para enviar los datos del formulario a nuestra base de datos
    """
    def obtener_datos_formulario(self, dict_entry):
        """
        Extraemos todos los valores del diccionario dict_entry y los retornaremos en un diccinario
        con nombres de columnas amigables :D para la BD
        """
        contrasena_plana = dict_entry["Contraseña"].get().strip()

        datos = {
            "nombres": dict_entry["Nombres"].get().strip(),
            "apellidos": dict_entry["Apellidos"].get().strip(),
            "numero_telefonico": dict_entry["Numero"].get().strip(),
            "correo_electronico": dict_entry["Correo"].get().strip(),
            "usuario": dict_entry["Usuario"].get().strip(),
            # 🌟 ENCRIPTAMOS AQUÍ 🌟
            "contrasena_encriptada": self.encriptar_contrasena(contrasena_plana),
            # 🌟 GENERAMOS LA FECHA Y HORA 🌟
            "fecha_registro": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        return datos
    

    def crear_interfaz(self):
        """Crea la interfaz de registro"""
        # Título
        titulo = tk.Label(self.ventana_principal, text="Registro de Administrador", 
                         font=("Arial", 30, "bold"), bg="midnight blue", fg="white")
        titulo.pack(pady=50)


        #FORMULARIO

        "Funciones para los placeholder de los campos del formulario"
        def al_hacer_click(event, entry_widget, placeholder):
            if entry_widget.get() == placeholder:
                entry_widget.delete(0, "end")
                entry_widget.config(fg='grey')

        def al_hacer_salir(event, entry_widget, placeholder):
            if not entry_widget.get():
                entry_widget.insert(0, placeholder)
                entry_widget.config(fg='grey')


        """
        Usaremos GRID para organizar mejor

        explicame lo siguiente, hasta ahora entiendo que tengo un frame que es formulario_frame, quiero saber que hace su parametro highlightthickness, luego que hace pack_propagate y grid_propagate
        siguiente que hace el metodo de este frame que es grid_columnconfigure con sus parametros 0, weight=0, minsize=100 y 1, weight=0
        """
        formulario_frame = tk.Frame(self.ventana_principal, width=600, height=800 ,bg="midnight blue",highlightbackground="black", highlightthickness=2)
        formulario_frame.pack(pady=10)
        formulario_frame.pack_propagate(False)
        formulario_frame.grid_propagate(False)

        formulario_frame.grid_columnconfigure(0, weight=0, minsize=150)
        formulario_frame.grid_columnconfigure(1, weight=1)

        #Titulo
        label_titulo = tk.Label(formulario_frame, text="Formulario de registro",
                                bg="midnight blue", fg="white", font=("Arial", 20, "bold"))
        label_titulo.grid(row=1, column=0, columnspan=2, sticky="ew", padx=10, pady=20)
        

        #Campos para rellenar
        #NOMBRES
        label_nombres = tk.Label(formulario_frame, text="Nombres: ",
                                 bg="midnight blue", fg="white", font=("Arial", 15, "bold"))
        label_nombres.grid(row=2, column=0, sticky="w", padx=10, pady=20)
        entry_nombres = tk.Entry(
            formulario_frame,
            font=("Arial", 15),
            width=30,
            fg="grey",
            validate="key", #Validamos con cada pulsación de tecla
            validatecommand=(self.vcmd_limite, '%P', self.LIMITE_NOMBRE)    #Usamos el ID registrado para pasar el limite
        )
        entry_nombres.grid(row=2, column=1, sticky="w", pady=20)
        placeholder_text_nombres = "Ingresar nombres"
        entry_nombres.insert(0, placeholder_text_nombres)
        entry_nombres.bind('<FocusIn>', lambda event, entry=entry_nombres, placeholder=placeholder_text_nombres: al_hacer_click(event, entry, placeholder))
        entry_nombres.bind('<FocusOut>', lambda event, entry=entry_nombres, placeholder=placeholder_text_nombres: al_hacer_salir(event, entry, placeholder))

        #APELLIDOS
        labe_apellidos = tk.Label(formulario_frame, text="Apellidos: ",
                                  bg="midnight blue", fg="white", font=("Arial", 15, "bold"))
        labe_apellidos.grid(row=3, column=0, sticky="w", padx=10, pady=5)
        entry_apellidos = tk.Entry(
            formulario_frame,
            font=("Arial", 15),
            width=30,
            fg="grey",
            validate="key",
            validatecommand=(self.vcmd_limite, '%P', self.LIMITE_APELIIDO)
        )
        entry_apellidos.grid(row=3, column=1, sticky="w", pady=20)
        placeholder_text_apellidos = "Ingresar apellidos"
        entry_apellidos.insert(0, placeholder_text_apellidos)
        entry_apellidos.bind('<FocusIn>', lambda event, entry=entry_apellidos, placeholder=placeholder_text_apellidos: al_hacer_click(event, entry, placeholder))
        entry_apellidos.bind('<FocusOut>', lambda event, entry=entry_apellidos, placeholder=placeholder_text_apellidos: al_hacer_salir(event, entry, placeholder))

        #NUMERO
        label_numero = tk.Label(formulario_frame, text="Número de contacto:",
                                bg="midnight blue", fg="white", font=("Arial", 15, "bold"))
        label_numero.grid(row=4, column=0, sticky="w", padx=10, pady=5)
        entry_numero = tk.Entry(
            formulario_frame,
            font=("Arial", 15),
            width=30,
            fg="grey",
            validate="key",
            validatecommand=(self.vcmd_limite, '%P', self.LIMITE_NUMERO)
        )
        entry_numero.grid(row=4, column=1, sticky="w", pady=20)
        placeholder_text_numero = "Ingrese su número de contacto"
        entry_numero.insert(0, placeholder_text_numero)
        entry_numero.bind('<FocusIn>', lambda event, entry=entry_numero, placeholder=placeholder_text_numero: al_hacer_click(event, entry, placeholder))
        entry_numero.bind('<FocusOut>', lambda event, entry=entry_numero, placeholder=placeholder_text_numero: al_hacer_salir(event, entry, placeholder))

        #CORREO
        label_correo = tk.Label(formulario_frame, text="Correo electrónico:",
                                bg="midnight blue", fg="white", font=("Arial", 15, "bold"))
        label_correo.grid(row=5, column=0, sticky="w", padx=10, pady=5)
        entry_correo = tk.Entry(
            formulario_frame,
            font=("Arial", 15),
            width=30,
            fg="grey",
            validate="key",
            validatecommand=(self.vcmd_limite, '%P', self.LIMITE_CORREO)
        )
        entry_correo.grid(row=5, column=1, sticky="w", pady=20)
        placeholder_text_correo = "Ingrese su correo electrónico"
        entry_correo.insert(0, placeholder_text_correo)
        entry_correo.bind('<FocusIn>', lambda event, entry=entry_correo, placeholder=placeholder_text_correo: al_hacer_click(event, entry, placeholder))
        entry_correo.bind('<FocusOut>', lambda event, entry=entry_correo, placeholder=placeholder_text_correo: al_hacer_salir(event, entry, placeholder))

        #USUARIO
        label_usuario = tk.Label(formulario_frame, text="Nombre de usuario:",
                                 bg="midnight blue", fg="white", font=("Arial", 15, "bold"))
        label_usuario.grid(row=6, column=0, sticky="w", padx=10, pady=5)
        entry_usuario = tk.Entry(
            formulario_frame,
            font=("Arial", 15),
            width=30,
            fg="grey",
            validate="key",
            validatecommand=(self.vcmd_limite, '%P', self.LIMITE_USUARIO)
        )
        entry_usuario.grid(row=6, column=1, sticky="w", pady=20)
        placeholder_text_usuario = "Ingrese un nombre de usuario"
        entry_usuario.insert(0, placeholder_text_usuario)
        entry_usuario.bind('<FocusIn>', lambda event, entry=entry_usuario, placeholder=placeholder_text_usuario: al_hacer_click(event, entry, placeholder))
        entry_usuario.bind('<FocusOut>', lambda event, entry=entry_usuario, placeholder=placeholder_text_usuario: al_hacer_salir(event, entry, placeholder))


        #CONTRASEÑA
        label_contrasena = tk.Label(formulario_frame, text="Contraseña",
                                 bg="midnight blue", fg="white", font=("Arial", 15, "bold"))
        label_contrasena.grid(row=7, column=0, sticky="w", padx=10, pady=5)
        entry_contrasena = tk.Entry(
            formulario_frame,
            font=("Arial", 15),
            width=30,
            fg="grey",
            show="*",
            validate="key",
            validatecommand=(self.vcmd_limite, '%P', self.LIMITE_NUMERO)
        )
        entry_contrasena.grid(row=7, column=1, sticky="w", pady=20)
        """placeholder_text_contrasena = "Ingrese una nueva contraseña"
        entry_contrasena.insert(0, placeholder_text_contrasena)
        entry_contrasena.bind('<FocusIn>', lambda event, entry=entry_contrasena, placeholder=placeholder_text_contrasena: al_hacer_click(event, entry, placeholder))
        entry_contrasena.bind('<FocusOut>', lambda event, entry=entry_contrasena, placeholder=placeholder_text_contrasena: al_hacer_salir(event, entry, placeholder))"""



        #FRAME PARA LOS BOTONES
        frame_botones = tk.Frame(formulario_frame, bg="midnight blue")
        frame_botones.grid(row=10, column=0, columnspan=2, pady=100)

        # Botones dentro del frame usando pack
        btn_volver = tk.Button(frame_botones, text="Regresar al menú principal",
                            command=self.volver_menu_principal,
                            font=("Arial", 14), bg="black", fg="white")
        btn_volver.pack(side="left", padx=(0, 50))  # Espacio a la derecha
        


        """1.Función para validar si un Entry está vacío o no fue rellenado(por defecto tiene el placeholder)
        """
        def validar_entry_vacio(dic_entry, dic_place):
            """Función que valida si los Entry estan vacios o son iguales al placeholder

            Args:
                dic_entry (_type_): Diccionario de los Entry para obtener sus valores
                dic_place (_type_): Diccionario de los placeholder que contienen sus valores 
            """
            "Aca almacenaremos los campos que no fueron rellenados"
            campos_invalidos = []

            """Realizaremos un bucle para comprobar que entry esta vacio o no fue rellenado
            
            nombre_campo -> "Nombres"(string)
            entry -> entry_nombre(objeto Entry que contiene el placeholder)
            """
            for nombre_campo, entry in dic_entry.items():
                """Aca tendremos el valor del primer placeholder que tengamos para compararlo"""
                placeholder = dic_place[nombre_campo]       #Contiene -> "Ingresar nombres"
                """Aca tendremos el primer valor del entry del diccionario"""
                valor_actual_entry = entry.get().strip()    #Contiene -> "Ingresar nombres"
                

                """
                Realizamos la comparación si el Entry esta vacio o es igual al placeholder(no se relleno)
                """
                if valor_actual_entry == "" or valor_actual_entry == placeholder:
                    "Si encontramos el campo vacio/con el mismo placeholder, lo agregamos a la lista de campos vacios 'campos_invalidos' para mostrarlo en un mensaje despues"
                    campos_invalidos.append(nombre_campo)

            "Retornamos la lista de los campos vacios para mostrar en un mensaje"
            return campos_invalidos


        """2.Función para validar Entry que solo tengan caracteres
        """
        def solo_caracteres(texto):
            """Valida que el texto contenga solo letras y espacios"""
            if not texto:  # Si está vacío (aunque ya validamos esto antes)
                return False
            
            # Permite letras, espacios y acentos
            return all(caracter.isalpha() or caracter.isspace() for caracter in texto)
        def validar_entry_solo_caracter(dic_entry):
            """
            Por ahora tendremos el diccionario de Entry para saber que tipo de Entry serán los que tengan solo caracteres
            """
            errores = []

            #VALIDAMOS EL ENTRY 'NOMBRES'
            if "Nombres" in dic_entry:
                nombre = dic_entry["Nombres"].get().strip()
                if not solo_caracteres(nombre):
                    errores.append("El campo 'Nombres' solo puede contener letras y espacios.")
            #VALIDAMOS LOS APELLIDOS
            if "Apellidos" in dic_entry:
                apellido = dic_entry["Apellidos"].get().strip()
                if not solo_caracteres(apellido):
                    errores.append("El campo 'Apellidos' solo puede contener letras y espacios.")
            #VALIDAMOS EL USUARIO
            if "Usuario" in dic_entry:
                usuario = dic_entry["Usuario"].get().strip()
                if not solo_caracteres(usuario):
                    errores.append("El campo 'Usuario' solo puede contener letras y espacios.")

            return errores

        """3.Función para validar el Entry de número que tiene que tener 9 dígitos y solo números
        """
        def validar_entry_numeros(texto):
            """
            Valida si una cadena es un número de teléfono de Perú, 
            verificando que tenga EXACTAMENTE 9 dígitos numéricos.

            Args:
            texto: La variable (cadena) a validar, obtenida de un Entry.

            Returns:
            True si la cadena contiene solo 9 dígitos, False en caso contrario.
            """
            texto_limpio = texto.strip()
            return len(texto_limpio) == 9 and texto_limpio.isdigit()

        """4.Función para validar el campo Correo para que tenga el formato correcto 'ejemplo@gmail.com'
        """
        def validar_entry_correo(text_correo):
            """
            Valida si la cadena tiene un formato de correo electrónico básico y correcto.
            
            Args:
            texto: La cadena (email) a validar.
            
            Returns:
            True si el formato es correcto, False en caso contrario.
            """
            # Patrón de Expresión Regular para un email común:
            # ^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$
            # Explicación:
            # ^             : Inicio de la cadena
            # [a-zA-Z0-9._-]+: Una o más letras, números, puntos, guiones bajos o guiones (-)
            # @             : El símbolo arroba (requerido)
            # [a-zA-Z0-9.-]+: Una o más letras, números, puntos o guiones (-) para el dominio
            # \.            : Un punto (requerido)
            # [a-zA-Z]{2,}  : Dos o más letras para la extensión (ej: com, net, org, pe, etc.)
            # $             : Fin de la cadena
            
            patron_correo = r"^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
            
            if not isinstance(text_correo, str):    #Si no es un String retornamos Falso
                return False
                
            # re.fullmatch() asegura que el patrón coincida con toda la cadena, no solo una parte.
            return bool(re.fullmatch(patron_correo, text_correo.strip()))

        


        """
        Función para validar diferentes tipos de errores en los objetos Entry
        """
        def validar_entrys():
            "Diccionario de los Entry para obtener su valor que tienen en su campo"
            dict_entry = {
                "Nombres": entry_nombres,
                "Apellidos": entry_apellidos,
                "Numero": entry_numero,
                "Correo": entry_correo,
                "Usuario": entry_usuario,
                "Contraseña": entry_contrasena
            }
            "Diccionario de los placeholder para realizar la comparación con su valor que tienen"
            dict_placeholder = {
                "Nombres": "Ingresar nombres",
                "Apellidos": "Ingresar apellidos",
                "Numero": "Ingrese su número de contacto",
                "Correo": "Ingrese su correo electrónico",
                "Usuario": "Ingrese un nombre de usuario",
                "Contraseña": "Ingrese una nueva contraseña"
            }


            """1.Aca almacenaremos los Entry que no fueron rellenados por el usuario, llamando a otra función que verifica si están vacios"""
            campos_invalidos_vacios = validar_entry_vacio(dict_entry, dict_placeholder)
            entry_set = set(dict_entry.keys())
            campos_vacios_set = set(campos_invalidos_vacios)

            if entry_set.issubset(campos_vacios_set):
                messagebox.showerror("Erro", "Todos los campos están vacíos.")
                return False
            elif campos_invalidos_vacios:
                if len(campos_invalidos_vacios) == 1:
                    messagebox.showerror("Error", f"El campo '{campos_invalidos_vacios[0]}' está vacío.")
                else:
                    campos_texto = "\n• "+"\n• ".join(campos_invalidos_vacios)    #Creamos un mensaje con los objetos vacios de 'campos_vacios'
                    messagebox.showerror("Error", f"Los campos están vacíos: {campos_texto}")
                return False
            
            """2.Validaremos los Entrys que solo deben contener caracteres"""
            errores_formato = validar_entry_solo_caracter(dict_entry)
            if errores_formato:
                if len(errores_formato) == 1:
                    messagebox.showerror("Error", f"Error de formato:\n{errores_formato[0]}")
                else:
                    errores_texto = "\n• " + "\n• ".join(errores_formato)
                    messagebox.showerror("Error", f"Errores de formato:{errores_texto}")
                return False
            
            """4.Validamos el Entry del Correo para que tenga el formato correcto"""
            texto_correo = dict_entry["Correo"].get().strip()
            if not validar_entry_correo(texto_correo):
                messagebox.showerror("Error", "El campo de Correo tiene un formato incorrecto(debe ser 'nombre@dominio.tld').")
                return False

            """3.Validamos el Entry que sean solo números y largo de 9 digitos"""
            validar_numero = validar_entry_numeros(dict_entry["Numero"].get().strip())
            if not validar_numero:
                messagebox.showerror("Error", "El campos de 'Número de contacto' debe ser de exactamente 9 dígitos numéricos.")
                return False
            
            
            #---------PASOS FINALES-----------
            #1.Obtenemos y procesamos todos los datos (incluyendo hash y fecha)
            datos_administrador = self.obtener_datos_formulario(dict_entry)
            """print(datos_administrador)"""

            #2.Llamamos a la función para insertar los datos en la BD
            exito, mensaje = self.db_manager.insertar_administrador(datos_administrador)
            if exito:
                messagebox.showinfo("Éxito", "Administrador registrado exitosamente.")
                # Opcional: Redirigir al menú principal después del registro
                self.aplicacion_principal.mostrar_pantalla("login") 
                return True
            else:
                # Mostrar el mensaje de error retornado por la base de datos (ej: usuario ya existe)
                messagebox.showerror("Error de Registro", mensaje)
                return False


        btn_registrarse = tk.Button(frame_botones, text="Registrarse!",
                                    font=("Arial", 14), bg="black", fg="white", command=validar_entrys)
        btn_registrarse.pack(side="left", padx=(50, 0))  # Espacio a la izquierda


        

    
    #Funcion para volver al menu principal
    def volver_menu_principal(self):
        #Mostramos un mensaje de confirmación
        respuesta = messagebox.askyesno(
            "Confirmar",
            "¿Estás seguro que quieres regresar al menú principal?\nLos cambios no guardados se perderán."
        )
        if respuesta:
            """Volvemos al menú anterior(principal)"""
            self.aplicacion_principal.mostrar_pantalla("menu_principal")

        

