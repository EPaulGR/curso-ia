"""Ejercicio 1 — Rigor estadístico al comparar modelos.

- `intervalo_bootstrap(valores, n=2000, alpha=0.05, seed=0)`: IC percentil de la media.
- `prueba_permutacion(a, b, n=5000, seed=0)`: p-valor bilateral de la diferencia de medias
  (|media(a)-media(b)| permutando etiquetas; p = (conteo_extremos + 1) / (n + 1)).
- `mcnemar(pred_a, pred_b, y)`: estadístico chi² con corrección de continuidad
  (|b01 - b10| - 1)^2 / (b01 + b10), donde b01 = A acierta y B falla, b10 al revés. 0 si no hay discordantes.
- `bonferroni(pvalores, alpha=0.05)`: lista de bool (rechaza H0).
"""
import numpy as np


def intervalo_bootstrap(valores, n=2000, alpha=0.05, seed=0):
    v = np.asarray(valores, float)
    rng = np.random.default_rng(seed)
    medias = rng.choice(v, (n, len(v))).mean(1)
    return float(np.quantile(medias, alpha / 2)), float(np.quantile(medias, 1 - alpha / 2))


def prueba_permutacion(a, b, n=5000, seed=0):
    a, b = np.asarray(a, float), np.asarray(b, float)
    rng = np.random.default_rng(seed)
    obs = abs(a.mean() - b.mean())
    todo = np.concatenate([a, b])
    c = 0
    for _ in range(n):
        rng.shuffle(todo)
        c += abs(todo[:len(a)].mean() - todo[len(a):].mean()) >= obs
    return (c + 1) / (n + 1)


def mcnemar(pred_a, pred_b, y):
    ca, cb = np.asarray(pred_a) == y, np.asarray(pred_b) == y
    b01, b10 = int(np.sum(ca & ~cb)), int(np.sum(~ca & cb))
    if b01 + b10 == 0:
        return 0.0
    return (abs(b01 - b10) - 1) ** 2 / (b01 + b10)


def bonferroni(pvalores, alpha=0.05):
    return [p < alpha / len(pvalores) for p in pvalores]
