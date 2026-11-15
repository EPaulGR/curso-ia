"""Ejercicio 07 — Metropolis-Hastings con propuesta gaussiana."""
import numpy as np


def metropolis(log_p, x0, n, paso=1.0, semilla=0):
    """Devuelve (muestras np.array de longitud n, tasa_aceptacion). log_p: log-densidad no normalizada."""
    rng = np.random.default_rng(semilla); x = x0; lp = log_p(x); out = np.empty(n); acc = 0
    for i in range(n):
        xp = x + paso * rng.normal(); lpp = log_p(xp)
        if np.log(rng.uniform()) < lpp - lp:
            x, lp = xp, lpp; acc += 1
        out[i] = x
    return out, acc / n
