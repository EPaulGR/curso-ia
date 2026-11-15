"""Ejercicio 05 — SVD y aproximación de rango bajo (puedes usar np.linalg.svd)."""
import numpy as np

def rango_bajo(A, k):
    """Mejor aproximación de rango k de A (Eckart-Young)."""
    raise NotImplementedError  # TODO

def energia_retenida(A, k):
    """Fracción de la suma de valores singulares al cuadrado retenida por los k primeros."""
    raise NotImplementedError  # TODO

def k_minimo(A, umbral=0.9):
    """Menor k que retiene al menos `umbral` de la energía."""
    raise NotImplementedError  # TODO
