"""Ejercicio 06 — Métodos de ensamble: AdaBoost con tocones y random forest con scikit-learn
(ISLP cap. 8; Hastie et al. cap. 10; Géron cap. 7).

AdaBoost (etiquetas y ∈ {−1, +1}):
    w_i = 1/n
    para m = 1..M:
        h_m ← tocón (árbol de 1 nivel) que minimiza el error ponderado ε_m
        α_m = ½ ln((1 − ε_m)/ε_m)
        w_i ← w_i · exp(−α_m y_i h_m(x_i));  normalizar
    H(x) = sign(Σ α_m h_m(x))
"""
import numpy as np


def mejor_tocon(X, y, w):
    """Devuelve (j, umbral, polaridad, error) del tocón h(x) = polaridad si x_j ≤ umbral, si no −polaridad."""
    raise NotImplementedError  # TODO: implementa esta función


class AdaBoost:
    def __init__(self, n_estimadores=50):
        """DADO."""
        self.n_estimadores = n_estimadores

    def fit(self, X, y):
        """y en {−1,+1}. Guarda self.tocones = [(j, u, pol, alfa), ...]."""
        raise NotImplementedError  # TODO: implementa esta función

    def decision(self, X):
        """Σ α_m h_m(x)."""
        raise NotImplementedError  # TODO: implementa esta función

    def predict(self, X):
        """sign de decision (0 → +1)."""
        raise NotImplementedError  # TODO: implementa esta función


def comparar_sklearn(X, y, semilla=0):
    """Con scikit-learn, devuelve dict nombre → exactitud media en 5-fold CV para:
    'arbol' (DecisionTreeClassifier), 'bosque' (RandomForestClassifier, 200 árboles),
    'gboost' (GradientBoostingClassifier). Todos con random_state=semilla."""
    raise NotImplementedError  # TODO: implementa esta función
