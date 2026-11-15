"""Ejercicio 06 — Vectorización: piezas que reutilizarás en ML."""
import numpy as np

def distancias_pares(X: np.ndarray, Y: np.ndarray) -> np.ndarray:
    """Matriz D (m x k) con D[i,j] = distancia euclidiana entre X[i] y Y[j]. Sin bucles."""
    raise NotImplementedError  # TODO

def softmax(z: np.ndarray) -> np.ndarray:
    """Softmax estable por filas (si z es 2D) o del vector (si es 1D)."""
    raise NotImplementedError  # TODO

def one_hot(etiquetas: np.ndarray, n_clases: int) -> np.ndarray:
    """Codificación one-hot: (n,) -> (n, n_clases)."""
    raise NotImplementedError  # TODO

def vecino_mas_cercano(X_train: np.ndarray, y_train: np.ndarray, X_test: np.ndarray) -> np.ndarray:
    """Clasificador 1-NN: etiqueta del punto de entrenamiento más cercano a cada punto de prueba."""
    raise NotImplementedError  # TODO
