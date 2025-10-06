import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class FormularioLogin:
    def __init__(self, ventana_principal, aplicacion_principal):
        """
        Args:
            ventana_principal (_type_): Es la ventana Tk principal
            aplicacion_principal (_type_): Instancia de la clase Aplication para volver al menu
        """
        self.ventana_principal = ventana_principal
        self.aplicacion_principal = aplicacion_principal

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

        #Boton para volver
        btn_volver = tk.Button(self.ventana_principal, text="Regresar al menú principal",
                               command=self.volver_menu_principal,
                               font=("Arial", 14), bg="black", fg="white")
        btn_volver.pack(pady=30)

    def volver_menu_principal(self):
        """Volvemos al menú anterior"""
        self.aplicacion_principal.mostrar_pantalla("menu_principal")

    
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
                                 text="Usuario: ",
                                 bg="midnight blue",
                                 fg="white",
                                 font=("Arial", 20, "bold")
                                 )
        label_usuario.grid(row=1, column=0, sticky="w", padx=10, pady=100)
        entry_usuario = tk.Entry(
            inicio_sesion_frame,
            font=("Arial", 15),
            width=30,
            fg="grey",
        )
        entry_usuario.grid(row=1, column=1, sticky="w", pady=50)
        placeholder_usuario = "Ingresar usuario"
        entry_usuario.insert(0, placeholder_usuario)
        entry_usuario.bind('<FocusIn>', lambda event, entry=entry_usuario, placeholder=placeholder_usuario: al_hacer_click(event, entry, placeholder))
        entry_usuario.bind('<FocusOut>', lambda event, entry=entry_usuario, placeholder=placeholder_usuario: al_hacer_salir(event, entry, placeholder))

        #2. Segundo campo para ingresar su "Contraseña"
        label_contrasena = tk.Label(inicio_sesion_frame,
                                    text="Contraseña: ",
                                    bg="midnight blue",
                                    fg="white",
                                    font=("Arial", 20, "bold")
                                    )
        label_contrasena.grid(row=2, column=0, sticky="w", padx=10)
        entry_contrasena = tk.Entry(
            inicio_sesion_frame,
            font=("Arial", 15),
            width=30,
            fg="grey",
        )
        entry_contrasena.grid(row=2, column=1, sticky="w", pady=20)
        
        #3. Botón para iniciar sesión, en caso no coincida con la base de datos mostrar un mensaje
        #4. Botón para regresar al menú principal con un mensaje de confirmación