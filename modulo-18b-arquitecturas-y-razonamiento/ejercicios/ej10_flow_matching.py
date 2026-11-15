"""Ejercicio 10 — Flow matching / rectified flow en 2D.

Interpolación lineal x_t = (1-t) x0 + t x1, con x0 ~ N(0, I) y x1 ~ datos.
El campo objetivo es v = x1 - x0. Se aprende v_theta(x_t, t) por regresión
(aquí: regresión ridge sobre características aleatorias de Fourier) y se
genera integrando dx/dt = v_theta(x, t) con Euler desde t=0 hasta t=1.
"""
import numpy as np


def interpolar(x0, x1, t):
    """x_t = (1 - t) x0 + t x1, t de forma (n, 1)."""
    raise NotImplementedError  # TODO


def caracteristicas(x, t, W, b):
    """Características aleatorias: cos([x, t] W + b) concatenadas con [x, t, 1]."""
    raise NotImplementedError  # TODO


def entrenar_campo(datos, n=4000, m=300, lam=1e-3, semilla=0):
    """Ajusta la regresión ridge del campo de velocidad. Devuelve (W, b, beta)."""
    raise NotImplementedError  # TODO


def generar(W, b, beta, n=500, pasos=50, semilla=1):
    """Integra con Euler desde ruido gaussiano. Devuelve (n, 2)."""
    raise NotImplementedError  # TODO
