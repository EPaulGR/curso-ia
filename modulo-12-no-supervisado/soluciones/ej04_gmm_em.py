"""Ej 04 — Mezcla de gaussianas 1D con el algoritmo EM."""
import numpy as np


def normal_pdf(x, mu, var):
    """Densidad normal N(mu, var) evaluada en x."""
    return np.exp(-(x - mu) ** 2 / (2 * var)) / np.sqrt(2 * np.pi * var)


def em_gmm_1d(x, k, iters=200, semilla=0):
    """EM para GMM 1D. Inicializa medias en cuantiles equiespaciados de x. Devuelve (pesos, medias, varianzas, log_verosimilitud_final)."""
    pi = np.full(k, 1 / k)
    mu = np.quantile(x, (np.arange(k) + 0.5) / k)
    var = np.full(k, x.var())
    for _ in range(iters):
        p = pi * normal_pdf(x[:, None], mu, var)
        r = p / p.sum(1, keepdims=True)
        nk = r.sum(0)
        pi = nk / len(x)
        mu = (r * x[:, None]).sum(0) / nk
        var = (r * (x[:, None] - mu) ** 2).sum(0) / nk + 1e-6
    ll = float(np.log((pi * normal_pdf(x[:, None], mu, var)).sum(1)).sum())
    return pi, mu, var, ll
