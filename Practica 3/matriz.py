import numpy as np

class MatrizFloat:
    "Clase que representa una matriz dinámica 1D/2D."
    
    TIPO_DATO = np.float32
    
    def __init__(self) -> None:
        self._matriz = None
        self._nfil = 0
        self._ncol = 0
        
    @classmethod

    def matriz_identidad(cls, n: int) -> "MatrizFloat":
        """Crea una matriz identidad de tamaño n x n."""
        matriz = cls()
        matriz._matriz = np.eye(n, dtype=cls.TIPO_DATO)
        matriz._nfil = n
        matriz._ncol = n
        
        return matriz
    
    @staticmethod 
    
    def mismas_dimensiones(m1: "MatrizFloat", m2: "MatrizFloat") -> bool:
        """Compruebo si dos matrices tienen las mismas dimensiones."""
        
        if m1._matriz is None or m2._matriz is None:
            return False
        return m1._nfil == m2._nfil and m1._ncol == m2._ncol
    
    def crear_matriz2D(self, nfil: int, ncol: int) -> None:
        """Crea una matriz bidimensional de ceros."""
        
        self._matriz = np.zeros((nfil, ncol), dtype=self.TIPO_DATO)
        self._nfil = nfil
        self._ncol = ncol

    def crear_matriz1D(self, nElementos: int) -> None:
        
        """Crea una matriz de una fila y nElementos columnas."""
        
        self.crear_matriz2D(1, nElementos)
        
    def existe(self) -> bool:
        """"Comprueba si la matriz existe y no está vacía"""
        
        return self._matriz is not None and self._matriz.size > 0
    
    def introducir(self) -> None:
        """Permite al usuario introducir los valores de la matriz."""
        
        if not self.existe():
            raise ValueError("La matriz no está creada.")
        from utils import leer_float
        for i in range(self._nfil):
            for j in range(self._ncol):
                self._matriz[i, j] = leer_float(f"Introduce el elemento [{i}, {j}]: ")
    
    def mostrar(self) -> None:
        """Muestra las dimensiones y los elementos de la matriz en pantalla."""
        
        if not self.existe():
            print("La matriz no está creada.")
            return
        
        print(f"Dimensiones: {self._nfil} x {self._ncol}")
        print(self._matriz)
        
    # ===========================================================
    # OPERACIONES ALGEBRAICAS
    # ===========================================================

    def sumar_matrices(self, otra_matriz: "MatrizFloat") -> "MatrizFloat":
        """Suma dos matrices y devuelve una nueva matriz."""
        if not self.mismas_dimensiones(self, otra_matriz):
            raise ValueError("Las matrices no tienen las mismas dimensiones.")
        resultado = MatrizFloat()
        resultado._matriz = self._matriz + otra_matriz._matriz
        resultado._nfil = self._nfil
        resultado._ncol = self._ncol
        return resultado