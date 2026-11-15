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
    return np.linalg.lstsq(_con_unos(X), y, rcond=None)[0]


def ridge(X, y, lam):
    """θ de ridge sin penalizar θ[0]."""
    Xb = _con_unos(X)
    I = np.eye(Xb.shape[1])
    I[0, 0] = 0
    return np.linalg.solve(Xb.T @ Xb + lam * I, Xb.T @ y)


def descenso_gradiente(X, y, lr=0.1, epocas=1000):
    """θ por descenso de gradiente por lotes desde θ = 0. Devuelve (θ, historial_mse)."""
    Xb = _con_unos(X)
    n = len(y)
    th = np.zeros(Xb.shape[1])
    hist = []
    for _ in range(epocas):
        r = Xb @ th - y
        hist.append(float(np.mean(r ** 2)))
        th -= lr * 2 / n * Xb.T @ r
    return th, hist


def predecir(theta, X):
    """ŷ = θ0 + X θ[1:]."""
    return _con_unos(X) @ theta


def r2(y, y_pred):
    """Coeficiente de determinación R² = 1 − SS_res/SS_tot."""
    y = np.asarray(y, float)
    return 1 - np.sum((y - y_pred) ** 2) / np.sum((y - y.mean()) ** 2)
