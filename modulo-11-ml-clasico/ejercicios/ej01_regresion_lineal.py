"""Ejercicio 01 — Regresión lineal desde cero (ISLP cap. 3; Géron cap. 4).

Modelo ŷ = Xw + b. Pérdida MSE: J(w) = (1/n)‖Xw − y‖².
- Ecuación normal:  w = (XᵀX)⁻¹Xᵀy  (añadiendo columna de unos para el sesgo)
- Ridge (L2):       w = (XᵀX + λI')⁻¹Xᵀy   (sin penalizar el sesgo)
- Descenso de gradiente: ∇J = (2/n) Xᵀ(Xw − y)
Todas devuelven un vector θ de tamaño d+1 con θ[0] = sesgo.
"""
import numpy as np


def _con_unos(X):
    """DADO: antepone una columna de unos."""
    X = np.asarray(X, float)
    return np.hstack([np.ones((len(X), 1)), X])


def ecuacion_normal(X, y):
    """θ por mínimos cuadrados (usa np.linalg.lstsq o solve)."""
    raise NotImplementedError  # TODO: implementa esta función


def ridge(X, y, lam):
    """θ de ridge sin penalizar θ[0]."""
    raise NotImplementedError  # TODO: implementa esta función


def descenso_gradiente(X, y, lr=0.1, epocas=1000):
    """θ por descenso de gradiente por lotes desde θ = 0. Devuelve (θ, historial_mse)."""
    raise NotImplementedError  # TODO: implementa esta función


def predecir(theta, X):
    """ŷ = θ0 + X θ[1:]."""
    raise NotImplementedError  # TODO: implementa esta función


def r2(y, y_pred):
    """Coeficiente de determinación R² = 1 − SS_res/SS_tot."""
    raise NotImplementedError  # TODO: implementa esta función
