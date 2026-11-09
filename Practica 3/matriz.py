import numpy as np

class MatrizFloat:
    "Clase que representa una matriz dinámica 1D/2D."
    
    TIPO_DATO = np.float32
    
    def __init__(self) -> None:
        self._matriz = None
        self._nfil = 0
        self._ncol = 0
