from matriz import MatrizFloat
from utils import leer_int, crear_menu

def main() -> None:
    """Ejecuta el menú principal de la práctica."""
    
    matriz = MatrizFloat()
    
    opciones_menu = [
        "Construir matriz 1D",
        "Construir matriz 2D",
        "Crear matriz identidad",
        "Introducir matriz",
        "Mostrar matriz",
        "Operaciones con matrices",
        "Terminar",
    ]
    
    while True:
        opcion = crear_menu(opciones_menu)
        
        if opcion == 1:
            nElementos = leer_int("Introduce el número de elementos para la matriz 1D: ")
            matriz.crear_matriz1D(nElementos)
            print("Matriz 1D creada correctamente.")

        elif opcion == 2:
            nfil = leer_int("Introduce el número de filas para la matriz 2D: ")
            ncol = leer_int("Introduce el número de columnas para la matriz 2D: ")
            matriz.crear_matriz2D(nfil, ncol)
            print("Matriz 2D creada correctamente.")
            
        elif opcion == 3:
            n = leer_int("Introduce el tamaño de la matriz identidad: ")
            matriz = MatrizFloat.matriz_identidad(n)
            print("Matriz identidad creada correctamente.")
            
        elif opcion == 4:
            if matriz.existe():
                matriz.introducir()
                print("Valores introducidos correctamente.")
            else:
                print("Primero debes crear una matriz antes de introducir valores.")
        
        elif opcion == 5:
                matriz.mostrar()
        
        elif opcion == 6:
            if not matriz.existe():
                print("Primero debes crear una matriz antes de realizar operaciones.")
                continue
            
            opciones_operaciones = [
                "Sumar matrices",
                "Restar matrices",
                "Volver al menú principal"
            ]
            
            while True:
                operacion = crear_menu(opciones_operaciones)
                
                if operacion == 3:
                    break
                nFil = leer_int("Introduce el número de filas para la segunda matriz: ")
                nCol = leer_int("Introduce el número de columnas para la segunda matriz: ")
                
                if nFil <= 0 or nCol <= 0:
                    print("El número de filas y columnas debe ser mayor que cero.")
                    continue
                
                otra_matriz = MatrizFloat()
                otra_matriz.crear_matriz2D(nFil, nCol)
                
                if not MatrizFloat.mismas_dimensiones(matriz, otra_matriz):
                    print("Las matrices deben tener las mismas dimensiones para realizar la operación.")
                    continue
                
                otra_matriz.introducir()
                if operacion == 1:
                    resultado = matriz.sumar_matrices(otra_matriz)
                elif operacion == 2:
                    resultado = matriz.restar_matrices(otra_matriz)
                
                resultado.mostrar()
                
        if opcion == 7:
            print("Programa finalizado.")
            break
        
        
if __name__ == "__main__":
    main()
    