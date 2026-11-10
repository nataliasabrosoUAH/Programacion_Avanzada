def leer_int(mensaje: str = "Introduce un número entero: ") -> int:
    """Solicita un número entero hasta que sea válido."""
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("Error: Introducir un número entero válido.")

def leer_float(mensaje: str = "Introduce un número decimal: ") -> float:
    """Solicita un número decimal hasta que sea válido."""
    while True:
        try:
            numero = float(input(mensaje))
            return numero
        except ValueError:
            print("Error: Introducir un número decimal válido.")
            
def crear_menu(opciones_menu: list[str]) -> int:
    """Muestra un menú y solicita una opción válida."""
    while True:
        for numero, opcion in enumerate(opciones_menu, start=1):
            print(f"{numero}. {opcion}")
            
        seleccion = leer_int("Elige una opción:")
        if 1 <= seleccion <= len(opciones_menu):
                return seleccion
            
        print("Opción no válida. Inténtalo de nuevo.")