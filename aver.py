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


root = tk.Tk()
root.title("Prueba - 1")
root.geometry("800x800")
root.configure(bg="midnight blue")

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
entry_nombre = tk.Entry(root, width=100, fg="black")
entry_nombre.pack(pady=10)
placeholder_text_nombres = "Ingresar nombres"
entry_nombre.insert(0, placeholder_text_nombres)
entry_nombre.bind('<FocusIn>', lambda event, entry=entry_nombre, placeholder=placeholder_text_nombres: al_hacer_click(event, entry, placeholder))
entry_nombre.bind('<FocusOut>', lambda event, entry=entry_nombre, placeholder=placeholder_text_nombres: al_salir_click(event, entry, placeholder))


label_apellido = tk.Label(root, text="Ingres apellidos: ")
label_apellido.pack(pady=10)
entry_apellido = tk.Entry(root, width=100, fg="black")
entry_apellido.pack(pady=10)
placeholder_text_apellidos = "Ingresar apellidos"
entry_apellido.insert(0, placeholder_text_apellidos)
entry_apellido.bind('<FocusIn>', lambda event, entry=entry_apellido, placeholder=placeholder_text_apellidos: al_hacer_click(event, entry, placeholder))
entry_apellido.bind('<FocusOut>', lambda event, entry=entry_apellido, placeholder=placeholder_text_apellidos: al_salir_click(event, entry, placeholder))





"""
Quiero validar los campos Entry si vacios o no, ademas de validar que no tengan el mismo texto del placeholder
En caso este vacio o sean el mismo contenido del placeholder, mostrar por pantalla que Entry no se rellenaron hasta que el usuario los llene
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






def validar_entrys():
    "Diccionario de los Entry para obtener su valor que tienen en su campo"
    dict_entry = {
        "Nombres": entry_nombre,
        "Apellidos": entry_apellido
    }
    "Diccionario de los placeholder para realizar la comparación con su valor que tienen"
    dict_placeholder = {
        "Nombres": "Ingresar nombres",
        "Apellidos": "Ingresar apellidos"
    }


    "Aca almacenaremos los Entry que no fueron rellenados por el usuario, llamando a otra función que verifica si están vacios"
    campos_invalidos = validar_entry_vacio(dict_entry, dict_placeholder)


    "Si la lista de campos vacios encontro algo(si existe 'True') mostarmos los mensajes en una ventan para el usuario"
    if campos_invalidos:
        messagebox.showerror("Error", f"Campos inválidos: {', '.join(campos_invalidos)}")
    else:
        messagebox.showinfo("Éxito", "Todos los campos están correctos!")


"----------------------Función validar_solo_letras(texto) para nombres, apellidos, usuario----------------------"


boton = tk.Button(root, text="Probar", command=validar_entrys)
boton.pack(pady=10)

root.mainloop()