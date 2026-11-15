"""Ejercicio 05 — Bootstrap y prueba A/B por permutación."""
import numpy as np


def ic_bootstrap(x, estadistico=np.mean, B=2000, nivel=0.95, semilla=0):
    """Intervalo percentil bootstrap (lo, hi)."""
    rng = np.random.default_rng(semilla); x = np.asarray(x)
    est = [estadistico(rng.choice(x, len(x), replace=True)) for _ in range(B)]
    a = (1 - nivel) / 2
    return float(np.quantile(est, a)), float(np.quantile(est, 1 - a))


def prueba_permutacion(a, b, n_perm=5000, semilla=0):
    """p-valor bilateral de diferencia de medias por permutación."""
    rng = np.random.default_rng(semilla); a = np.asarray(a); b = np.asarray(b)
    obs = abs(a.mean() - b.mean()); todo = np.concatenate([a, b]); c = 0
    for _ in range(n_perm):
        rng.shuffle(todo)
        c += abs(todo[:len(a)].mean() - todo[len(a):].mean()) >= obs
    return (c + 1) / (n_perm + 1)
