"""Ejercicio 10 — Flow matching / rectified flow en 2D.

Interpolación lineal x_t = (1-t) x0 + t x1, con x0 ~ N(0, I) y x1 ~ datos.
El campo objetivo es v = x1 - x0. Se aprende v_theta(x_t, t) por regresión
(aquí: regresión ridge sobre características aleatorias de Fourier) y se
genera integrando dx/dt = v_theta(x, t) con Euler desde t=0 hasta t=1.
"""
import numpy as np


def interpolar(x0, x1, t):
    """x_t = (1 - t) x0 + t x1, t de forma (n, 1)."""
    return (1 - t) * x0 + t * x1


def caracteristicas(x, t, W, b):
    """Características aleatorias: cos([x, t] W + b) concatenadas con [x, t, 1]."""
    z = np.hstack([x, t])
    return np.hstack([np.cos(z @ W + b), z, np.ones((len(x), 1))])


def entrenar_campo(datos, n=4000, m=300, lam=1e-3, semilla=0):
    """Ajusta la regresión ridge del campo de velocidad. Devuelve (W, b, beta)."""
    rng = np.random.default_rng(semilla)
    x1 = datos[rng.integers(len(datos), size=n)]
    x0 = rng.standard_normal(x1.shape)
    t = rng.random((n, 1))
    xt = interpolar(x0, x1, t)
    W = rng.standard_normal((3, m)) * 2.0
    b = rng.uniform(0, 2 * np.pi, m)
    F = caracteristicas(xt, t, W, b)
    beta = np.linalg.solve(F.T @ F + lam * np.eye(F.shape[1]), F.T @ (x1 - x0))
    return W, b, beta


def generar(W, b, beta, n=500, pasos=50, semilla=1):
    """Integra con Euler desde ruido gaussiano. Devuelve (n, 2)."""
    rng = np.random.default_rng(semilla)
    x = rng.standard_normal((n, 2))
    dt = 1.0 / pasos
    for i in range(pasos):
        t = np.full((n, 1), i * dt)
        x = x + dt * caracteristicas(x, t, W, b) @ beta
    return x
