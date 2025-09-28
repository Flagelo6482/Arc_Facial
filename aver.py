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

"""frame_form = tk.Frame()"""
labeL_nombre = tk.Label(root, text="Ingrese nombres: ")
labeL_nombre.pack(pady=10)

entry_nombre = tk.Entry(root, width=100)
entry_nombre.pack(pady=10)

def solo_letras(texto):
    """FUNCION PARA VALIDAR SOLO LETRAS"""
    patron = re.compile(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$")
    return bool(patron.match(texto))

def validar_entry():
    texto = entry_nombre.get()
    if solo_letras(texto):
        messagebox.showinfo("Exito", "Genial ingresaste caracteres")
    else:
        messagebox.showerror("Error", "Debes ingresar solo carateres")

boton = tk.Button(root, text="Probar",
                  command=validar_entry)
boton.pack(pady=10)

root.mainloop()