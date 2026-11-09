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
