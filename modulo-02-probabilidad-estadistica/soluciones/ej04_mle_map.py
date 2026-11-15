"""Ejercicio 04 — Estimación MLE y MAP."""
import numpy as np


def mle_normal(x):
    """(mu, sigma2) de máxima verosimilitud (sigma2 con divisor n)."""
    x = np.asarray(x, float); mu = x.mean()
    return mu, ((x - mu) ** 2).mean()


def log_verosimilitud_normal(x, mu, sigma2):
    """Suma de log-densidades normales."""
    x = np.asarray(x, float)
    return float(-0.5 * len(x) * np.log(2 * np.pi * sigma2) - ((x - mu) ** 2).sum() / (2 * sigma2))


def map_bernoulli(k, n, alfa, beta):
    """Moda posterior de p con prior Beta(alfa, beta) y k éxitos en n."""
    return (k + alfa - 1) / (n + alfa + beta - 2)


def posterior_beta(k, n, alfa, beta):
    """Parámetros (alfa', beta') de la posterior Beta."""
    return alfa + k, beta + n - k
