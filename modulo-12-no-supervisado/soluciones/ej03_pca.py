"""Ej 03 — PCA vía SVD."""
import numpy as np


def pca(X, n_componentes):
    """Centra X y devuelve (Z, componentes, varianza_explicada_ratio).
    Z: (n, n_componentes) proyección; componentes: (n_componentes, d) filas ortonormales."""
    Xc = X - X.mean(0)
    U, S, Vt = np.linalg.svd(Xc, full_matrices=False)
    var = S ** 2 / (len(X) - 1)
    comp = Vt[:n_componentes]
    return Xc @ comp.T, comp, var[:n_componentes] / var.sum()


def reconstruir(Z, componentes, media):
    """Reconstruye X aproximado desde la proyección."""
    return Z @ componentes + media
