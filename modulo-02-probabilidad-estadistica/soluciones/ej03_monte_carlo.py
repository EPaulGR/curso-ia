"""Ejercicio 03 — Monte Carlo."""
import numpy as np


def estimar_pi(n, semilla=0):
    """Estima pi con n puntos uniformes en [-1,1]^2."""
    p = np.random.default_rng(semilla).uniform(-1, 1, (n, 2))
    return 4 * ((p ** 2).sum(1) <= 1).mean()


def integral_mc(f, a, b, n, semilla=0):
    """Estima la integral de f en [a,b] (f vectorizada)."""
    x = np.random.default_rng(semilla).uniform(a, b, n)
    return (b - a) * f(x).mean()


def muestreo_rechazo(p, a, b, M, n, semilla=0):
    """n muestras de densidad p en [a,b] con p(x) <= M, propuesta uniforme."""
    rng = np.random.default_rng(semilla); res = []
    while len(res) < n:
        x = rng.uniform(a, b, n); u = rng.uniform(0, M, n)
        res.extend(x[u <= p(x)])
    return np.array(res[:n])
