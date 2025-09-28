from tkinter import *

def on_entry_click(event, entry_widget, placeholder):
    if entry_widget.get() == placeholder:
        entry_widget.delete(0, "end")
        entry_widget.config(fg='black')

def on_entry_leave(event, entry_widget, placeholder):
    if not entry_widget.get():
        entry_widget.insert(0, placeholder)
        entry_widget.config(fg='grey')

def main_window():
    root = Tk()
    root.title("Ejemplo de Placeholders")
    root.geometry("400x300")
    
    # Campo 1
    placeholder_text1 = "Escribe tu nombre de usuario"
    user_entry = Entry(root, width=40, fg='grey')
    user_entry.insert(0, placeholder_text1)
    user_entry.bind('<FocusIn>', lambda event, entry=user_entry, placeholder=placeholder_text1: on_entry_click(event, entry, placeholder))
    user_entry.bind('<FocusOut>', lambda event, entry=user_entry, placeholder=placeholder_text1: on_entry_leave(event, entry, placeholder))
    user_entry.pack(pady=10)
    
    # Campo 2
    placeholder_text2 = "Escribe tu contraseña"
    pass_entry = Entry(root, width=40, fg='grey', show="*")
    pass_entry.insert(0, placeholder_text2)
    pass_entry.bind('<FocusIn>', lambda event, entry=pass_entry, placeholder=placeholder_text2: on_entry_click(event, entry, placeholder))
    pass_entry.bind('<FocusOut>', lambda event, entry=pass_entry, placeholder=placeholder_text2: on_entry_leave(event, entry, placeholder))
    pass_entry.pack(pady=10)
    
    # Campo 3
    placeholder_text3 = "Escribe tu correo electrónico"
    email_entry = Entry(root, width=40, fg='grey')
    email_entry.insert(0, placeholder_text3)
    email_entry.bind('<FocusIn>', lambda event, entry=email_entry, placeholder=placeholder_text3: on_entry_click(event, entry, placeholder))
    email_entry.bind('<FocusOut>', lambda event, entry=email_entry, placeholder=placeholder_text3: on_entry_leave(event, entry, placeholder))
    email_entry.pack(pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    main_window()