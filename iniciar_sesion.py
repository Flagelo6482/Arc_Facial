import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from db_manager import DBManager

class FormularioLogin:
    def __init__(self, ventana_principal, aplicacion_principal):
        """
        Args:
            ventana_principal (_type_): Es la ventana Tk principal
            aplicacion_principal (_type_): Instancia de la clase Aplication para volver al menu
        """
        self.ventana_principal = ventana_principal
        self.aplicacion_principal = aplicacion_principal
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

    def crear_interfaz(self):
        """Creamos la interfaz del formulario de Inicio de sesión"""
        titulo = tk.Label(self.ventana_principal, text="Inicio de sesión",
                          font=("Arial", 30, "bold"), bg="midnight blue", fg="white")
        titulo.pack(pady=50)


    def toggle_contrasena_visibility(self, entry_widget):
        """Alternamremos el argumento 'show' del Entry de contraseña >:D

        Args:
            entry_widget (_type_): Widget que pasaremos
        """
        current_show = entry_widget.cget('show')

        if current_show == '*':
            #Mostramos la contraseña cambiando a show=''
            entry_widget.config(show='')
        else:
            #Ocultamos la contraseña cambiando a show='*'
            entry_widget.config(show='*')
    
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

    #Funcion para redirigirnos a la pantalla para registrarnos
    def volver_registrarse(self):
        self.aplicacion_principal.mostrar_pantalla("registro")

    """
    Función para llamar a la lógico para iniciar sesión con las credenciales del usuario
    """
    def manejar_intento_login(self, entry_usuario, entry_contrasena):
        usuario = entry_usuario.get().strip()
        contrasena = entry_contrasena.get().strip()

        #Llamamos al método del DBManager para la lógica de autenticación
        exito, mensaje = self.db_manager.verificar_credenciales(usuario, contrasena)

        if exito:
            """ACA DEBEMOS AGREGAR LA FUNCIONALIDAD DE LLAMAR A LA OTRA PANTALLA DASHBOARD"""
            messagebox.showinfo("Éxito", mensaje)
        else:
            messagebox.showerror("Error de login", mensaje)

    """
    Función para validar si un Entry está vacío o no fue rellenado(por defecto tiene el placeholder)
    """
    def validar_entry_vacio(self, dic_entry, dic_place):
        """Función que valida si los Entry estan vacios o son iguales al placeholder

        Args:
            dic_entry (_type_): Diccionario de los Entry para obtener sus valores
            dic_place (_type_): Diccionario de los placeholder que contienen sus valores 
        """
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



    """
    Función PADRE para validar diferentes tipos de errores en los objetos Entry
    """
    def validar_entrys(self):
        "Diccionario de los Entry para obtener su valor que tienen en su campo"
        dict_entry = {
            "Usuario": self.entry_usuario,
            "Contraseña": self.entry_contrasena
        }
        "Diccionario de los placeholder para realizar la comparación con su valor que tienen"
        dict_placeholder = {
            "Usuario": "Ingresar usuario",
            "Contraseña": "Ingrese una nueva contraseña"
        }

        #Resultados de la validación de Entry vacios o no
        campos_vacios = self.validar_entry_vacio(dict_entry, dict_placeholder)

        if len(campos_vacios) > 0:
            if len(campos_vacios) == 1:
                messagebox.showerror("Error", f"El campo '{campos_vacios[0]}' está vacío.")
            else:
                campos_texto = "\n• "+"\n• ".join(campos_vacios)
                messagebox.showerror("Error", f"Los campos están vacíos: {campos_texto}")
            return False
        else:
            return self.manejar_intento_login(self.entry_usuario, self.entry_contrasena)
            """messagebox.showinfo("Éxito", "Sesión iniciada, Bienvenido.")"""


    def crear_interfaz(self):
        """Creamos la interfaz para que el usuario inicie sesión"""
        titulo = tk.Label(self.ventana_principal,
                          text="Iniciar Sesión",
                          font=("Arial", 30, "bold"),
                          bg="midnight blue",
                          fg="white"
                          )
        titulo.pack(pady=50)


        "Funciones para los placeholder de los campos del formulario"
        def al_hacer_click(event, entry_widget, placeholder):
            if entry_widget.get() == placeholder:
                entry_widget.delete(0, "end")
                entry_widget.config(fg='grey')

        def al_hacer_salir(event, entry_widget, placeholder):
            if not entry_widget.get():
                entry_widget.insert(0, placeholder)
                entry_widget.config(fg='grey')


        #Campos para que ingrese el usuario

        #Frame para almacenar todos los objetos de entrada de datos del formulario de inicio sesión
        inicio_sesion_frame = tk.Frame(self.ventana_principal, width=600, height=800, bg="midnight blue",highlightbackground="black", highlightthickness=2)
        inicio_sesion_frame.pack(pady=10)
        inicio_sesion_frame.pack_propagate(False)   #Se usa pack_propagate(False) para que no se adapte a los tamaños de sus hijos que contendra, sino que tenga un tamaño fijo
        inicio_sesion_frame.grid_propagate(False)

        inicio_sesion_frame.grid_columnconfigure(0, weight=0, minsize=150)
        inicio_sesion_frame.grid_columnconfigure(1, weight=1)

        #Campo del titulo
        label_titulo = tk.Label(inicio_sesion_frame,
                                text="Ingresar Credenciales para Iniciar Sesión",
                                bg="midnight blue",
                                fg="white",
                                font=("Arial", 18, "bold")
                                )
        label_titulo.grid(row=0, column=0, columnspan=2, sticky="ew", padx=10, pady=20)

        #1. Primer campo para ingresar su "Nombre de usuario"
        label_usuario = tk.Label(inicio_sesion_frame,
                                 text="Usuario 👤: ",
                                 bg="midnight blue",
                                 fg="white",
                                 font=("Arial", 20, "bold")
                                 )
        label_usuario.grid(row=1, column=0, sticky="w", padx=10, pady=100)
        self.entry_usuario = tk.Entry(
            inicio_sesion_frame,
            font=("Arial", 15),
            width=30,
            fg="grey",
        )
        self.entry_usuario.grid(row=1, column=1, sticky="w", pady=50)
        placeholder_usuario = "Ingresar usuario"
        self.entry_usuario.insert(0, placeholder_usuario)
        self.entry_usuario.bind('<FocusIn>', lambda event, entry=self.entry_usuario, placeholder=placeholder_usuario: al_hacer_click(event, entry, placeholder))
        self.entry_usuario.bind('<FocusOut>', lambda event, entry=self.entry_usuario, placeholder=placeholder_usuario: al_hacer_salir(event, entry, placeholder))

        #2. Segundo campo para ingresar su "Contraseña"
        label_contrasena = tk.Label(inicio_sesion_frame,
                                    text="Contraseña 🔒: ",
                                    bg="midnight blue",
                                    fg="white",
                                    font=("Arial", 20, "bold")
                                    )
        label_contrasena.grid(row=2, column=0, sticky="w", padx=10)

        #Creamos un Frame para contener el Entry y el Boton, para que esten juntos
        contrasena_container = tk.Frame(inicio_sesion_frame, bg="midnight blue")
        contrasena_container.grid(row=2, column=1, sticky="w", pady=20)
        #Creamos el Entry y el Boton dentro de este Frame, >:D
        self.entry_contrasena = tk.Entry(
            contrasena_container,
            font=("Arial", 15),
            width=25,
            fg="black",
            show="*"
        )
        self.entry_contrasena.grid(row=0, column=0, sticky="w")
        btn_toggle = tk.Button(
            contrasena_container,
            text="👁️",
            font=("Arial", 12),
            width=3,
            command=lambda: self.toggle_contrasena_visibility(self.entry_contrasena)
            )
        btn_toggle.grid(row=0, column=1, sticky="w", padx=3)
        
        
        #Frame para los botones
        frame_btn = tk.Frame(
            inicio_sesion_frame,
            bg="midnight blue"
            )
        frame_btn.grid(row=10, column=0, columnspan=2, pady=100)
        #---------------------------------------------------------------------------------------------
        # 1. Creamos un FRAME para los 2 botones (Iniciar Sesión y Regresar al Menú principal)
        #---------------------------------------------------------------------------------------------
        frame_btn_fila1 = tk.Frame(frame_btn, bg="midnight blue")   #Usaremos pack sin "side" para que lo centre por defecto
        frame_btn_fila1.pack(pady=(0, 20))  #Padding inferior/abajo para separarlo del botón de registro
        #3. Botón para iniciar sesión, en caso no coincida con la base de datos mostrar un mensaje
        btn_ingresar = tk.Button(
            frame_btn_fila1,
            text="Iniciar sesión 🔐",
            font=("Arial", 14),
            bg="black",
            fg="white",
            command=self.validar_entrys
            )
        btn_ingresar.pack(side="left", padx=10)
        #4. Botón para regresar al menú principal con un mensaje de confirmación
        btn_regresar = tk.Button(
            frame_btn_fila1,
            text="Regresar al menún principal",
            font=("Arial", 14),
            bg="black",
            fg="white",
            command=self.volver_menu_principal
        )
        btn_regresar.pack(side="left", padx=10)
        #---------------------------------------------------------------------------------------------
        # 2. Botón para Registrarse(lo agregamos al frame padre directamente, debajo de frame_btn_fila1)
        #---------------------------------------------------------------------------------------------
        #5.Botón para ir a registrarnos en caso no tengamos una cuenta
        btn_registrarse = tk.Button(
            frame_btn,
            text="¿No tienes una cuenta?, ¡Registrate!",
            font=("Arial", 14),
            bg="black",
            fg="white",
            command=self.volver_registrarse
        )
        #No usamos "side" para que se coloque en una nueva línea y se centre
        btn_registrarse.pack(pady=10)   #Se centra por defecto con pack