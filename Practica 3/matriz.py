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