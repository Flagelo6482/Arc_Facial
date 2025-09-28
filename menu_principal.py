"""
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from formulario import FormularioRegistro
from iniciar_sesion import FormularioLogin
import time



class Aplication:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Sistema de reconocimiento facial v1")
        self.ventana.state('zoomed')
        self.ventana.configure(bg="midnight blue")
        self.mostrar_menu_principal()

    def limpiar_pantalla(self):
        """Eliminamos todos los widgets de la ventana"""
        for widget in self.ventana.winfo_children():
            widget.destroy()

    def mostrar_pantalla(self, destino):
        """Mostramos la otra pantalla donde se rediriga el usuario"""
        self.limpiar_pantalla()

        if destino == "menu_principal":
            self.mostrar_menu_principal()
        elif destino == "login":
            self.mostrar_login()
        elif destino == "registro":
            self.mostrar_registro()

    
    #Función para irnos al formulario
    def mostrar_registro(self):
        """Creamos una instancia de la clase FormularioRegistro"""
        registro = FormularioRegistro(self.ventana, self)

    #Funcion para irnos a iniciar sesión
    def mostrar_login(self):
        """Creamos la instancia de la clase de Inicio de sesión"""
        iniciar_sesion = FormularioLogin(self.ventana, self)


    def mostrar_menu_principal(self):
        """Pantalla principal con los 3 botones, iniciar sesión, registrarse y cerrar"""

        #HEADER
        titulo = tk.Label(self.ventana, text="🛡️Arc Facial V1.1", font=("Arial", 35, "bold"), bg="midnight blue", fg="white")
        titulo.pack(pady=80)    #Añadimos espacios verticalmente y pack() centro por defecto

        frame_botones = tk.Frame(self.ventana, bg="midnight blue")
        frame_botones.pack(pady=30)

        #Boton para iniciar sesión
        boton_iniciar_sesion = tk.Button(frame_botones, text="🔐 Iniciar sesión",
                                         command=lambda: self.mostrar_pantalla("login"),
                                          font=("Arial", 14), bg="black", fg="white")
        boton_iniciar_sesion.pack(side="left", padx=20)

        #Boton para registrarse
        boton_registrarse = tk.Button(frame_botones, text="📝 Registrarse",
                                      command=lambda: self.mostrar_pantalla("registro"),
                                       font=("Arial", 14), bg="black", fg="white")
        boton_registrarse.pack(side="left", padx=20)

        #Boton para cerrar aplicación
        boton_cerrar = tk.Button(self.ventana, text="❌ Cerrar aplicación",
                                command=self.confirmar_salida,
                                font=("Arial", 14), bg="black", fg="white")
        boton_cerrar.pack(pady=30)

    def confirmar_salida(self):
        """Texto para confirmar la salida del programa"""
        respuesta = messagebox.askyesno(
            "Confirmar salida",
            "¿Está seguro de que desea salir del sistema?"
        )
        if respuesta:
            self.ventana.quit() #CIERRE GRACEFUL
        
    def ejecutar(self):
        self.ventana.mainloop()

if __name__ == "__main__":
    app = Aplication()
    app.ejecutar()