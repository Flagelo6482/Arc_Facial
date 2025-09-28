import re
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

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

class FormularioRegistro:
    def __init__(self, ventana_principal, aplicacion_principal):
        """
        Args:
            ventana_principal (_type_): Es la ventana Tk principal
            aplicacion_principal (_type_): Instancia de la clase Aplication para volver al menú
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
                entry_widget.config(fg='black')

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
        entry_nombres = tk.Entry(formulario_frame, font=("Arial", 15), width=30)
        entry_nombres.grid(row=2, column=1, sticky="w", pady=20)
        placeholder_text_nombres = "Ingresar nombres"
        entry_nombres.insert(0, placeholder_text_nombres)
        entry_nombres.bind('<FocusIn>', lambda event, entry=entry_nombres, placeholder=placeholder_text_nombres: al_hacer_click(event, entry, placeholder))
        entry_nombres.bind('<FocusOut>', lambda event, entry=entry_nombres, placeholder=placeholder_text_nombres: al_hacer_salir(event, entry, placeholder))

        #APELLIDOS
        labe_apellidos = tk.Label(formulario_frame, text="Apellidos: ",
                                  bg="midnight blue", fg="white", font=("Arial", 15, "bold"))
        labe_apellidos.grid(row=3, column=0, sticky="w", padx=10, pady=5)
        entry_apellidos = tk.Entry(formulario_frame, font=("Arial", 15), width=30)
        entry_apellidos.grid(row=3, column=1, sticky="w", pady=20)
        placeholder_text_apellidos = "Ingresar apellidos"
        entry_apellidos.insert(0, placeholder_text_apellidos)
        entry_apellidos.bind('<FocusIn>', lambda event, entry=entry_apellidos, placeholder=placeholder_text_apellidos: al_hacer_click(event, entry, placeholder))
        entry_apellidos.bind('<FocusOut>', lambda event, entry=entry_apellidos, placeholder=placeholder_text_apellidos: al_hacer_salir(event, entry, placeholder))

        #NUMERO
        label_numero = tk.Label(formulario_frame, text="Número de contacto:",
                                bg="midnight blue", fg="white", font=("Arial", 15, "bold"))
        label_numero.grid(row=4, column=0, sticky="w", padx=10, pady=5)
        entry_numero = tk.Entry(formulario_frame, font=("Arial", 15), width=30)
        entry_numero.grid(row=4, column=1, sticky="w", pady=20)
        placeholder_text_numero = "Ingrese su número de contacto"
        entry_numero.insert(0, placeholder_text_numero)
        entry_numero.bind('<FocusIn>', lambda event, entry=entry_numero, placeholder=placeholder_text_numero: al_hacer_click(event, entry, placeholder))
        entry_numero.bind('<FocusOut>', lambda event, entry=entry_numero, placeholder=placeholder_text_numero: al_hacer_salir(event, entry, placeholder))

        #CORREO
        label_correo = tk.Label(formulario_frame, text="Correo electrónico:",
                                bg="midnight blue", fg="white", font=("Arial", 15, "bold"))
        label_correo.grid(row=5, column=0, sticky="w", padx=10, pady=5)
        entry_correo = tk.Entry(formulario_frame, font=("Arial", 15), width=30)
        entry_correo.grid(row=5, column=1, sticky="w", pady=20)
        placeholder_text_correo = "Ingrese su correo electrónico"
        entry_correo.insert(0, placeholder_text_correo)
        entry_correo.bind('<FocusIn>', lambda event, entry=entry_correo, placeholder=placeholder_text_correo: al_hacer_click(event, entry, placeholder))
        entry_correo.bind('<FocusOut>', lambda event, entry=entry_correo, placeholder=placeholder_text_correo: al_hacer_salir(event, entry, placeholder))

        #USUARIO
        label_usuario = tk.Label(formulario_frame, text="Nombre de usuario:",
                                 bg="midnight blue", fg="white", font=("Arial", 15, "bold"))
        label_usuario.grid(row=6, column=0, sticky="w", padx=10, pady=5)
        entry_usuario = tk.Entry(formulario_frame, font=("Arial", 15), width=30)
        entry_usuario.grid(row=6, column=1, sticky="w", pady=20)
        placeholder_text_usuario = "Ingrese un nombre de usuario"
        entry_usuario.insert(0, placeholder_text_usuario)
        entry_usuario.bind('<FocusIn>', lambda event, entry=entry_usuario, placeholder=placeholder_text_usuario: al_hacer_click(event, entry, placeholder))
        entry_usuario.bind('<FocusOut>', lambda event, entry=entry_usuario, placeholder=placeholder_text_usuario: al_hacer_salir(event, entry, placeholder))


        #CONTRASEÑA
        label_contrasena = tk.Label(formulario_frame, text="Contraseña",
                                 bg="midnight blue", fg="white", font=("Arial", 15, "bold"))
        label_contrasena.grid(row=7, column=0, sticky="w", padx=10, pady=5)
        entry_contrasena = tk.Entry(formulario_frame, font=("Arial", 15), width=30)
        entry_contrasena.grid(row=7, column=1, sticky="w", pady=20)
        placeholder_text_contrasena = "Ingrese una nueva contraseña"
        entry_contrasena.insert(0, placeholder_text_contrasena)
        entry_contrasena.bind('<FocusIn>', lambda event, entry=entry_contrasena, placeholder=placeholder_text_contrasena: al_hacer_click(event, entry, placeholder))
        entry_contrasena.bind('<FocusOut>', lambda event, entry=entry_contrasena, placeholder=placeholder_text_contrasena: al_hacer_salir(event, entry, placeholder))



        #FRAME PARA LOS BOTONES
        frame_botones = tk.Frame(formulario_frame, bg="midnight blue")
        frame_botones.grid(row=10, column=0, columnspan=2, pady=100)

        # Botones dentro del frame usando pack
        btn_volver = tk.Button(frame_botones, text="Regresar al menú principal",
                            command=self.volver_menu_principal,
                            font=("Arial", 14), bg="black", fg="white")
        btn_volver.pack(side="left", padx=(0, 50))  # Espacio a la derecha
        



        #Validamos que contengan caracteres los campos indicados(nombres, apellidos y usuario)
        def solo_caracteres(texto):
            """
            Validamos que contengan solo caracteres
            """
            # Expresión regular que permite:
            # ^ : Inicio de la cadena
            # [a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+ : Una o más letras, mayúsculas/minúsculas, con tildes, ñ, o espacios en blanco.
            # $ : Fin de la cadena
            patron = re.compile(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$")
            return bool(patron.match(texto))

        #Validamos multiples entries
        def validar_entries(entries_dict, placeholders_dict=None):
            resultados = {}
            todos_validos = True

            #Campos que deben tener solo caracteres
            campos_solo_caracteres = ["Nombres", "Apellidos", "Usuario"]

            for nombre, entry in entries_dict.items():
                valor = entry.get().strip()
                valido = True
                mensaje_error = ""

                #1.Validar si el valor del entrie es igual al paceholder
                if placeholders_dict and nombre in placeholders_dict:
                    placeholder = placeholders_dict[nombre]
                    #Consideramos si es igual al placeholder o esta vacio
                    if not valor or valor == placeholder:
                        valido = False
                        mensaje_error = f"El campo {nombre} está vacío o tiene el texto por defecto."
                else:
                    if not valor:
                        valido = False
                        mensaje_error = f"El campo {nombre} está vacío."

                # 2. Validar solo caracteres (si el campo ya es considerado "válido" hasta este punto)
                if valido and nombre in campos_solo_caracteres:
                    if not solo_caracteres(valor):
                        valido = False
                        mensaje_error = f"El campo {nombre} solo debe contener letras y espacios."


                resultados[nombre] = {
                    "valido": valido,
                    "valor": valor,
                    "mensaje": f"{nombre}: {'✓' if valido else '✗'}"
                }

                if not valido:
                    todos_validos = False
            resultados["todos_validos"] = todos_validos
            return resultados
        
        #Función para validar campos vacios
        def validar():
            #Validamos los objetos ENTRY

            placeholders = {
                "Nombres": "Ingresar nombres",
                "Apellidos": "Ingresar apellidos",
                "Numero": "Ingrese su número de contacto",
                "Correo": "Ingrese su correo electrónico",
                "Usuario": "Ingrese un nombre de usuario",
                "Contrasena": "Ingrese una nueva contraseña"
            }
            entries = {
                "Nombres": entry_nombres,
                "Apellidos": entry_apellidos,
                "Numero": entry_numero,
                "Correo": entry_correo,
                "Usuario": entry_usuario,
                "Contrasena": entry_contrasena
            }

            resultados = validar_entries(entries, placeholders)

            if resultados["todos_validos"]:
                messagebox.showinfo("Éxito", "Todos los campos estan llenos")
            else:
                # Encontramos el primer campo inválido y usamos su mensaje de error específico
                primer_error = None
                campos_vacios_o_invalidos = []

                for campo, info in resultados.items():
                    if campo != "todos_validos" and not info["valido"]:
                        campos_vacios_o_invalidos.append(campo)
                        if primer_error is None and "mensaje_error" in info:
                            primer_error = info["mensaje_error"]
                
                # Mostrar un mensaje de error detallado (priorizando el primer error encontrado)
                if primer_error:
                    # Mostramos el error específico del primer campo encontrado
                    messagebox.showerror("Error de Validación", primer_error)
                else:
                    # Mensaje genérico si no se capturó un error específico (debería ser raro con la implementación anterior)
                    messagebox.showerror("Error", f"Uno o más campos son inválidos: {', '.join(campos_vacios_o_invalidos)}")

            

        btn_registrarse = tk.Button(frame_botones, text="Registrarse!",
                                    font=("Arial", 14), bg="black", fg="white",
                                    command=validar)
        btn_registrarse.pack(side="left", padx=(50, 0))  # Espacio a la izquierda


        

    
    #Funcion para volver al menu principal
    def volver_menu_principal(self):
        """Volvemos al menú anterior(principal)"""
        self.aplicacion_principal.mostrar_pantalla("menu_principal")