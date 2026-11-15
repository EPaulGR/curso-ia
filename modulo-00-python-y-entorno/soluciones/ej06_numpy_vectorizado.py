"""Ejercicio 06 — Vectorización: piezas que reutilizarás en ML."""
import numpy as np


def distancias_pares(X: np.ndarray, Y: np.ndarray) -> np.ndarray:
    """Matriz D (m x k) con D[i,j] = distancia euclidiana entre X[i] y Y[j]. Sin bucles."""
    d2 = (X ** 2).sum(1)[:, None] + (Y ** 2).sum(1)[None, :] - 2 * X @ Y.T
    return np.sqrt(np.maximum(d2, 0))


def softmax(z: np.ndarray) -> np.ndarray:
    """Softmax estable por filas (si z es 2D) o del vector (si es 1D)."""
    z = z - z.max(axis=-1, keepdims=True)
    e = np.exp(z)
    return e / e.sum(axis=-1, keepdims=True)


def one_hot(etiquetas: np.ndarray, n_clases: int) -> np.ndarray:
    """Codificación one-hot: (n,) -> (n, n_clases)."""
    return np.eye(n_clases, dtype=int)[etiquetas]


def vecino_mas_cercano(X_train: np.ndarray, y_train: np.ndarray, X_test: np.ndarray) -> np.ndarray:
    """Clasificador 1-NN: etiqueta del punto de entrenamiento más cercano a cada punto de prueba."""
    return y_train[distancias_pares(X_test, X_train).argmin(axis=1)]
