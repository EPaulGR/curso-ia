"""Ej 07 — Coeficiente de silueta y método del codo."""
import numpy as np


def silueta(X, etiquetas):
    """Silueta media: s = (b - a) / max(a, b)."""
    D = np.sqrt(((X[:, None] - X[None]) ** 2).sum(-1))
    s = []
    for i in range(len(X)):
        mismo = etiquetas == etiquetas[i]
        mismo[i] = False
        if mismo.sum() == 0:
            s.append(0.0)
            continue
        a = D[i, mismo].mean()
        b = min(D[i, etiquetas == c].mean() for c in set(etiquetas) if c != etiquetas[i])
        s.append((b - a) / max(a, b))
    return float(np.mean(s))
