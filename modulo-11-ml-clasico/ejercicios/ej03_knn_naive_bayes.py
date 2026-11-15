"""Ejercicio 03 — k vecinos más cercanos y Naive Bayes gaussiano.

kNN: predecir por voto mayoritario de los k más cercanos (distancia euclidiana);
desempate: la clase con menor etiqueta.
NB gaussiano: P(c|x) ∝ P(c) Π_j N(x_j; μ_cj, σ²_cj). Trabaja en log para estabilidad;
añade var_suavizado·max(var) a las varianzas (como scikit-learn, 1e-9).
"""
import numpy as np


def knn_predecir(X_tr, y_tr, X_te, k=3):
    """Array de predicciones para X_te."""
    raise NotImplementedError  # TODO: implementa esta función


class NaiveBayesGaussiano:
    def __init__(self, var_suavizado=1e-9):
        """DADO."""
        self.var_suavizado = var_suavizado

    def fit(self, X, y):
        """Estima clases_, log_prior_, media_ (C, d) y var_ (C, d). Devuelve self."""
        raise NotImplementedError  # TODO: implementa esta función

    def log_verosimilitud_conjunta(self, X):
        """Array (n, C) con log P(c) + Σ_j log N(x_j | c)."""
        raise NotImplementedError  # TODO: implementa esta función

    def predict(self, X):
        """Clase de mayor posterior."""
        raise NotImplementedError  # TODO: implementa esta función
