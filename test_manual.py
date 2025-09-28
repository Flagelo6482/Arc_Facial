import tkinter as tk
from tkinter import messagebox
import time

# Mock de las clases que importas (para pruebas)
class MockFormularioRegistro:
    def __init__(self, ventana, app):
        self.ventana = ventana
        self.app = app
        self.crear_interfaz()
    
    def crear_interfaz(self):
        # Limpiar ventana
        for widget in self.ventana.winfo_children():
            widget.destroy()
        
        titulo = tk.Label(self.ventana, text="📝 FORMULARIO REGISTRO", 
                         font=("Arial", 25, "bold"), bg="midnight blue", fg="white")
        titulo.pack(pady=50)
        
        btn_volver = tk.Button(self.ventana, text="← Volver al Menú",
                              command=lambda: self.app.mostrar_pantalla("menu_principal"),
                              font=("Arial", 14), bg="green", fg="white")
        btn_volver.pack(pady=20)

class MockFormularioLogin:
    def __init__(self, ventana, app):
        self.ventana = ventana
        self.app = app
        self.crear_interfaz()
    
    def crear_interfaz(self):
        # Limpiar ventana
        for widget in self.ventana.winfo_children():
            widget.destroy()
        
        titulo = tk.Label(self.ventana, text="🔐 INICIAR SESIÓN", 
                         font=("Arial", 25, "bold"), bg="midnight blue", fg="white")
        titulo.pack(pady=50)
        
        btn_volver = tk.Button(self.ventana, text="← Volver al Menú",
                              command=lambda: self.app.mostrar_pantalla("menu_principal"),
                              font=("Arial", 14), bg="blue", fg="white")
        btn_volver.pack(pady=20)

class TestAplication:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("TEST - Sistema de reconocimiento facial v1")
        self.ventana.geometry("800x600")  # Tamaño fijo para pruebas
        self.ventana.configure(bg="midnight blue")
        
        # Contador de pruebas
        self.pruebas_completadas = 0
        self.total_pruebas = 5
        
        self.mostrar_menu_principal()

    def limpiar_pantalla(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()

    def mostrar_pantalla(self, destino):
        self.limpiar_pantalla()
        
        if destino == "menu_principal":
            self.mostrar_menu_principal()
        elif destino == "login":
            self.mostrar_login()
        elif destino == "registro":
            self.mostrar_registro()

    def mostrar_registro(self):
        registro = MockFormularioRegistro(self.ventana, self)
        self.pruebas_completadas += 1
        print(f"✅ Prueba {self.pruebas_completadas}/5: Navegación a Registro - OK")

    def mostrar_login(self):
        iniciar_sesion = MockFormularioLogin(self.ventana, self)
        self.pruebas_completadas += 1
        print(f"✅ Prueba {self.pruebas_completadas}/5: Navegación a Login - OK")

    def mostrar_menu_principal(self):
        # Título
        titulo = tk.Label(self.ventana, text="🧪 MODO PRUEBAS", font=("Arial", 20, "bold"), 
                         bg="midnight blue", fg="yellow")
        titulo.pack(pady=20)
        
        # Info de pruebas
        info = tk.Label(self.ventana, text=f"Pruebas: {self.pruebas_completadas}/{self.total_pruebas}", 
                       font=("Arial", 12), bg="midnight blue", fg="white")
        info.pack(pady=10)

        # Botones de prueba
        frame_botones = tk.Frame(self.ventana, bg="midnight blue")
        frame_botones.pack(pady=30)

        boton_registro = tk.Button(frame_botones, text="1. Probar Registro",
                                  command=lambda: self.mostrar_pantalla("registro"),
                                  font=("Arial", 12), bg="orange", fg="black")
        boton_registro.pack(pady=10)

        boton_login = tk.Button(frame_botones, text="2. Probar Login",
                               command=lambda: self.mostrar_pantalla("login"),
                               font=("Arial", 12), bg="orange", fg="black")
        boton_login.pack(pady=10)

        # Botón para probar salida
        boton_salida = tk.Button(frame_botones, text="3. Probar Confirmación Salida",
                                command=self.probar_salida,
                                font=("Arial", 12), bg="red", fg="white")
        boton_salida.pack(pady=10)
        
        # Botón para finalizar pruebas
        boton_finalizar = tk.Button(self.ventana, text="🎯 Finalizar Pruebas",
                                   command=self.finalizar_pruebas,
                                   font=("Arial", 14), bg="green", fg="white")
        boton_finalizar.pack(pady=20)

    def probar_salida(self):
        respuesta = messagebox.askyesno(
            "Prueba de Salida",
            "¿Esto es una prueba? (Selecciona No para continuar)"
        )
        if not respuesta:
            self.pruebas_completadas += 1
            print(f"✅ Prueba {self.pruebas_completadas}/5: Confirmación de salida - OK")
        else:
            print("⚠️  Prueba de salida cancelada por el usuario")

    def finalizar_pruebas(self):
        print(f"\n🎉 Pruebas completadas: {self.pruebas_completadas}/{self.total_pruebas}")
        if self.pruebas_completadas >= 3:
            print("✅ La aplicación pasa las pruebas básicas")
        else:
            print("❌ La aplicación necesita más pruebas")
        
        self.ventana.quit()

    def ejecutar(self):
        print("🚀 Iniciando pruebas manuales...")
        print("1. Probar navegación a Registro")
        print("2. Probar navegación a Login") 
        print("3. Probar confirmación de salida")
        print("4. Verificar que los botones responden")
        print("5. Verificar que la interfaz se renderiza correctamente\n")
        
        self.ventana.mainloop()

if __name__ == "__main__":
    test_app = TestAplication()
    test_app.ejecutar()