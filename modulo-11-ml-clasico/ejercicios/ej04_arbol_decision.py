"""Ejercicio 04 — Árboles de decisión (CART para clasificación) (ISLP cap. 8; AIMA 19.3).

Impureza de Gini:  G = 1 − Σ_k p_k²        Entropía: H = −Σ_k p_k log2 p_k
Ganancia: impureza(padre) − Σ (n_hijo/n) impureza(hijo)
Divisiones binarias x_j ≤ umbral con umbrales = puntos medios entre valores únicos
consecutivos. Se detiene con profundidad_max, min_muestras o nodo puro.
"""
import numpy as np


def gini(y):
    """Impureza de Gini de un vector de etiquetas."""
    raise NotImplementedError  # TODO: implementa esta función


def entropia(y):
    """Entropía en bits."""
    raise NotImplementedError  # TODO: implementa esta función


def mejor_division(X, y, criterio=gini):
    """(j, umbral, ganancia) de la mejor división; (None, None, 0.0) si ninguna mejora."""
    raise NotImplementedError  # TODO: implementa esta función


class ArbolDecision:
    def __init__(self, profundidad_max=None, min_muestras=2, criterio="gini"):
        """DADO."""
        self.profundidad_max = profundidad_max
        self.min_muestras = min_muestras
        self.criterio = gini if criterio == "gini" else entropia

    def fit(self, X, y):
        """Construye self.raiz: hoja = {'clase': c}; interno = {'j','umbral','izq','der'}."""
        raise NotImplementedError  # TODO: implementa esta función

    def predict(self, X):
        """Predicciones recorriendo el árbol."""
        raise NotImplementedError  # TODO: implementa esta función

    def profundidad(self):
        """Profundidad del árbol (una hoja sola = 0)."""
        raise NotImplementedError  # TODO: implementa esta función
