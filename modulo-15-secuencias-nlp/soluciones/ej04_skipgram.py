"""Ej 04 — Word2Vec skip-gram con negative sampling (NumPy)."""
import numpy as np


def pares_skipgram(ids, ventana):
    """Lista de (centro, contexto) para cada posición y cada vecino a distancia ≤ ventana."""
    pares = []
    for i, c in enumerate(ids):
        for j in range(max(0, i - ventana), min(len(ids), i + ventana + 1)):
            if j != i:
                pares.append((c, ids[j]))
    return pares


def entrenar_sgns(pares, V, dim=16, negativos=5, epocas=5, lr=0.05, semilla=0):
    """Pérdida: -log σ(u_o·v_c) - Σ log σ(-u_k·v_c). Devuelve la matriz de embeddings de centro (V, dim)."""
    rng = np.random.default_rng(semilla)
    Vc = rng.normal(0, 0.1, (V, dim))
    U = np.zeros((V, dim))
    sig = lambda z: 1 / (1 + np.exp(-z))
    for _ in range(epocas):
        for idx in rng.permutation(len(pares)):
            c, o = pares[idx]
            ks = rng.integers(0, V, negativos)
            v = Vc[c]
            gp = sig(U[o] @ v) - 1
            gn = sig(U[ks] @ v)
            grad_v = gp * U[o] + gn @ U[ks]
            U[o] -= lr * gp * v
            U[ks] -= lr * gn[:, None] * v
            Vc[c] -= lr * grad_v
    return Vc


def mas_similares(E, i, k=3):
    """Índices de los k vectores más similares (coseno) a E[i], excluyendo i."""
    En = E / np.linalg.norm(E, axis=1, keepdims=True)
    s = En @ En[i]
    s[i] = -np.inf
    return list(np.argsort(-s)[:k])
