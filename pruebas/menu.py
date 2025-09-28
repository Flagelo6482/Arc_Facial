from auth import iniciar_sesion

def menu():
    """
    Menu principal para iniciar sesión o crear un administrador
    """
    while True:
        print("\n===SISTEMA DE SEGURIDAD===")
        print("1. Iniciar sesión")
        print("2. Registrar nuevo administrador")
        print("3. Exit(de exitante)")
        
        opcion = input("Seleccione una opción: ").strip()
            
        if not opcion:
            print("Debe seleccionar una opción válida.")
            continue
        elif opcion == "1":
            iniciar_sesion()
        elif opcion == "2":
            print("opcion 2")
        elif opcion == "3":
            print("Bay...")
            break
        else:
            print("Opción inválida.")



if __name__ == "__main__":
    menu()