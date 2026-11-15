# EJERCICIO: implementa cada función marcada con TODO.
# Verifica con: pytest modulo-12-no-supervisado

"""Ej 03 — PCA vía SVD."""
import numpy as np

def pca(X, n_componentes):
    """Centra X y devuelve (Z, componentes, varianza_explicada_ratio).
    Z: (n, n_componentes) proyección; componentes: (n_componentes, d) filas ortonormales."""
    raise NotImplementedError  # TODO

def reconstruir(Z, componentes, media):
    """Reconstruye X aproximado desde la proyección."""
    raise NotImplementedError  # TODO
