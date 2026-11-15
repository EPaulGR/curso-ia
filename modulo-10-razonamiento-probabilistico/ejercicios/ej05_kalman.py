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
    raise NotImplementedError  # TODO: implementa esta función
