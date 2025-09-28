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