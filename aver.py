"""from turtle import *

speed(0)

bgcolor("black")

setheading(45)

for i in range(235):
    color('#ff8fab')
    circle(270-i, 90), lt(90)
    circle(270-i, 90), lt(18)

mainloop()"""

import re
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def validar_limite(nuevo_texto, limite):
    """
    Verifica que la longitud del texto propuesto NO exceda el límite.
    Se llama automáticamente por Tkinter al presionar una tecla.
    """
    # El límite se pasa como string, lo convertimos a int
    limite = int(limite)
    # Retorna False para rechazar la tecla si se excede el limite
    return len(nuevo_texto) <= limite


root = tk.Tk()
root.title("Prueba - 1")
root.geometry("800x800")
root.configure(bg="midnight blue")


# 1. REGISTRAR LA FUNCIÓN DE VALIDACIÓN
# 'vcmd' es el ID de comando que se usará en los Entrys
# (%P = El texto completo que resultaría si se acepta la tecla)
# (%d = Un argumento que pasaremos, será el límite)
vcmd = root.register(validar_limite)

# --- LÍMITES GLOBALES RECOMENDADOS (Colócalos cerca de la definición de root) ---
LIMITE_NOMBRE = 20
LIMITE_APELLIDO = 20
LIMITE_USUARIO = 10
LIMITE_NUMERO = 9 # Exactamente 9 dígitos para Perú


def al_hacer_click(event, entry_widget, placeholder):
    if entry_widget.get() == placeholder:
        entry_widget.delete(0, "end")
        entry_widget.config(fg='grey')

def al_salir_click(event, entry_widget, placeholder):
    if not entry_widget.get():
        entry_widget.insert(0, placeholder)
        entry_widget.config(fg="grey")



labeL_nombre = tk.Label(root, text="Ingrese nombres: ")
labeL_nombre.pack(pady=10)
entry_nombre = tk.Entry(root, width=100, fg="black",
                        validate="key",
                        validatecommand=(vcmd, '%P', LIMITE_NOMBRE) #Llamamos a la función con el nuevo texto %P y el limite 50
)
entry_nombre.pack(pady=10)
placeholder_text_nombres = "Ingresar nombres"
entry_nombre.insert(0, placeholder_text_nombres)
entry_nombre.bind('<FocusIn>', lambda event, entry=entry_nombre, placeholder=placeholder_text_nombres: al_hacer_click(event, entry, placeholder))
entry_nombre.bind('<FocusOut>', lambda event, entry=entry_nombre, placeholder=placeholder_text_nombres: al_salir_click(event, entry, placeholder))


label_apellido = tk.Label(root, text="Ingrese apellidos: ")
label_apellido.pack(pady=10)
entry_apellido = tk.Entry(root, width=100, fg="black")
entry_apellido.pack(pady=10)
placeholder_text_apellidos = "Ingresar apellidos"
entry_apellido.insert(0, placeholder_text_apellidos)
entry_apellido.bind('<FocusIn>', lambda event, entry=entry_apellido, placeholder=placeholder_text_apellidos: al_hacer_click(event, entry, placeholder))
entry_apellido.bind('<FocusOut>', lambda event, entry=entry_apellido, placeholder=placeholder_text_apellidos: al_salir_click(event, entry, placeholder))


label_numero = tk.Label(root, text="Ingrese su número telefónico: ")
label_numero.pack(pady=10)
entry_numero = tk.Entry(root, width=100, fg="black")
entry_numero.pack(pady=10)
placeholder_text_numero = "Ingrese su numero de contacto"
entry_numero.insert(0, placeholder_text_numero)
entry_numero.bind('<FocusIn>', lambda event, entry=entry_numero, placeholder=placeholder_text_numero: al_hacer_click(event, entry, placeholder))
entry_numero.bind('<FocusOut>', lambda event, entry=entry_numero, placeholder=placeholder_text_numero: al_salir_click(event, entry, placeholder))


label_usuario = tk.Label(root, text="Nombre de usuario:")
label_usuario.pack(pady=10)
entry_usuario = tk.Entry(root, width=100, fg="black")
entry_usuario.pack(pady=10)
placeholder_text_usuario = "Ingrese un nombre de usuario"
entry_usuario.insert(0, placeholder_text_usuario)
entry_usuario.bind('<FocusIn>', lambda event, entry=entry_usuario, placeholder=placeholder_text_usuario: al_hacer_click(event, entry, placeholder))
entry_usuario.bind('<FocusOut>', lambda event, entry=entry_usuario, placeholder=placeholder_text_usuario: al_salir_click(event, entry, placeholder))



"""
1.Primero validaremos que todos los Entrys no esten vacios, en caso de que alguno o más de 1 lo este, lo guardamos en una lista para enviarlo a otra función posterior
"""
def validar_entry_vacio_2(dic_entry, dic_place):
    """Función que valida si los Entry estan vacios o son iguales al placeholder

    Args:
        dic_entry (_type_): Diccionario de los Entry para obtener sus valores
        dic_place (_type_): Diccionario de los placeholder que contienen sus valores 
    """

    campos_invalidos = []   #Lista de objetos Entry invalidos

    """
    dic_tentry = {
        "Nombres": entry_nombre,
        "Apellidos": entry_apellido,
        "Numero": entry_numero
    }

    "Diccionario de los placeholder para realizar la comparación con su valor que tienen"
    dic_place = {
        "Nombres": "Ingresar nombres",
        "Apellidos": "Ingresar apellidos",
        "Numero": "Ingrese su numero de contacto"
    }
    """
    for nombre_campo, entry in dic_entry.items():
        placeholder = dic_place[nombre_campo]       #placeholder = "Ingresar nombres"
        valor_actual_entry = entry.get().strip()    #valor_actual_entry = 'valor del entry'

        """
        Comparamos el valor del entry si esta vacio o es igual al placeholder = esta vacío
        Si es así agregamos el campo del entry a la lista de Entry invalidos
        """
        if valor_actual_entry == "" or valor_actual_entry == placeholder:
            campos_invalidos.append(nombre_campo)

    return campos_invalidos
"""
2.Validaremos que los Entry Nombre, Apellido y Usuario solo contengan caracteres
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



def validar_entrys():
    "Diccionario de los Entry para obtener su valor que tienen en su campo"
    dict_entry = {
        "Nombres": entry_nombre,
        "Apellidos": entry_apellido,
        "Numero": entry_numero,
        "Usuario": entry_usuario
    }

    "Diccionario de los placeholder para realizar la comparación con su valor que tienen"
    dict_placeholder = {
        "Nombres": "Ingresar nombres",
        "Apellidos": "Ingresar apellidos",
        "Numero": "Ingrese su numero de contacto",
        "Usuario": "Ingrese un nombre de usuario"
    }

    #Validamos si los entrys se encuentran vacios
    campos_vacios = validar_entry_vacio_2(dict_entry, dict_placeholder)
    entry_set = set(dict_entry.keys())
    campos_vacios_set = set(campos_vacios)

    

    #Si todos los entrys estan vacios ingresamos al mensaje de error para todos, True si es verdadero que todo estan ahi
    if entry_set.issubset(campos_vacios_set):
        messagebox.showerror("Error", "Todos los campos están vacíos.")
        return False
    #Si no todos estan vacios, validamos cuantos lo están
    elif campos_vacios: #Si contiene algo
        if len(campos_vacios) == 1: #Si solo encuentra un Entry vacio
            messagebox.showerror("Error", f"El campo '{campos_vacios[0]}' está vacío.")
        else:   #Si encuentra más de 1
            campos_texto = "\n• "+"\n• ".join(campos_vacios)    #Creamos un mensaje con los objetos vacios de 'campos_vacios'
            messagebox.showerror("Error", f"Los campos están vacíos: {campos_texto}")
        return False
    
    """
    Si pasamos la validación de todos los Entry vacios, validamos otras condiciones
    """
    errores_formato = validar_entry_solo_caracter(dict_entry)

    if errores_formato:
        if len(errores_formato) == 1:
            messagebox.showerror("Error", f"Error de formato:\n{errores_formato[0]}")
        else:
            errores_texto = "\n• " + "\n• ".join(errores_formato)
            messagebox.showerror("Error", f"Errores de formato:{errores_texto}")
        return False
    
    
    #Si todos los campos pasaron las validaciones correctamente
    messagebox.showinfo("Éxito", "Campos validados.")
    return True

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





boton = tk.Button(root, text="Probar", command=validar_entrys)
boton.pack(pady=10)

root.mainloop()