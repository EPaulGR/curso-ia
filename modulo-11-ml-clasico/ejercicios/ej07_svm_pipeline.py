"""Ejercicio 07 — Máquinas de vectores de soporte y pipelines (ISLP cap. 9; Géron cap. 5).

1) SVM lineal con Pegasos (subgradiente estocástico de la pérdida bisagra), y ∈ {−1,+1}:
    min_w (λ/2)‖w‖² + (1/n) Σ max(0, 1 − y_i wᵀx_i)
    en el paso t (η_t = 1/(λt)), con un ejemplo i aleatorio:
        si y_i wᵀx_i < 1:  w ← (1 − η_t λ) w + η_t y_i x_i
        si no:             w ← (1 − η_t λ) w
   (el sesgo se maneja añadiendo una característica constante 1)
2) Pipeline de scikit-learn: StandardScaler + SVC(RBF) con GridSearchCV sobre C y gamma.
"""
import numpy as np


def pegasos(X, y, lam=0.01, iteraciones=20000, semilla=0):
    """Devuelve w de tamaño d+1 (último componente = sesgo)."""
    raise NotImplementedError  # TODO: implementa esta función


def predecir_svm(w, X):
    """sign(wᵀ[x, 1]) con 0 → +1."""
    raise NotImplementedError  # TODO: implementa esta función


def busqueda_svm_rbf(X, y):
    """Devuelve (mejores_parametros: dict, mejor_puntaje_cv: float) de GridSearchCV(cv=5) sobre
    C ∈ {0.1, 1, 10, 100} y gamma ∈ {'scale', 0.01, 0.1, 1} con un Pipeline escalado+SVC."""
    raise NotImplementedError  # TODO: implementa esta función
