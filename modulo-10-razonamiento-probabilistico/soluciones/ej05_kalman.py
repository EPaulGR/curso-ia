"""Ejercicio 05 — Filtro de Kalman (AIMA 14.4).

Modelo lineal-gaussiano:
    x_{t+1} = F x_t + w,   w ~ N(0, Q)
    z_t     = H x_t + v,   v ~ N(0, R)
Predicción:   x⁻ = F x;      P⁻ = F P Fᵀ + Q
Corrección:   K = P⁻ Hᵀ (H P⁻ Hᵀ + R)⁻¹
              x = x⁻ + K (z − H x⁻);   P = (I − K H) P⁻
"""
import numpy as np


def kalman(z, F, H, Q, R, x0, P0):
    """z: array (T, m) de observaciones. Devuelve (X, Ps) con las estimaciones (T, n)
    y covarianzas (T, n, n) tras cada corrección."""
    x, P = np.asarray(x0, float), np.asarray(P0, float)
    I = np.eye(len(x))
    X, Ps = [], []
    for zt in np.atleast_2d(z):
        x = F @ x
        P = F @ P @ F.T + Q
        K = P @ H.T @ np.linalg.inv(H @ P @ H.T + R)
        x = x + K @ (zt - H @ x)
        P = (I - K @ H) @ P
        X.append(x.copy())
        Ps.append(P.copy())
    return np.array(X), np.array(Ps)
