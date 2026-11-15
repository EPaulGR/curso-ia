"""Ejercicio 08 — Optimización multiobjetivo: dominancia de Pareto y NSGA-II
(BUAP 4.1 y 4.6; Deb et al. 2002; Eiben & Smith cap. 12).

Minimización de todos los objetivos.
a domina a b  ⇔  a_i ≤ b_i ∀i  y  a_j < b_j para algún j.
Frente de Pareto = conjunto de puntos no dominados.
NSGA-II: ordenamiento no dominado rápido + distancia de crowding + selección por
torneo con (rango, −crowding) + elitismo (μ+λ).
"""
import numpy as np


def domina(a, b):
    """True si a domina a b."""
    return all(x <= y for x, y in zip(a, b)) and any(x < y for x, y in zip(a, b))


def frente_pareto(puntos):
    """Índices de los puntos no dominados (orden ascendente)."""
    return [i for i, p in enumerate(puntos) if not any(domina(q, p) for j, q in enumerate(puntos) if j != i)]


def ordenamiento_no_dominado(puntos):
    """Lista de frentes (cada frente = lista de índices ordenada). Frente 0 = no dominados."""
    n = len(puntos)
    S = [[] for _ in range(n)]
    cuenta = [0] * n
    frentes = [[]]
    for p in range(n):
        for q in range(n):
            if domina(puntos[p], puntos[q]):
                S[p].append(q)
            elif domina(puntos[q], puntos[p]):
                cuenta[p] += 1
        if cuenta[p] == 0:
            frentes[0].append(p)
    i = 0
    while frentes[i]:
        sig = []
        for p in frentes[i]:
            for q in S[p]:
                cuenta[q] -= 1
                if cuenta[q] == 0:
                    sig.append(q)
        i += 1
        frentes.append(sorted(sig))
    return [sorted(f) for f in frentes[:-1]]


def distancia_crowding(F):
    """F: array (k, m) con los objetivos de un frente. Devuelve array (k,) con la
    distancia de crowding; los extremos de cada objetivo reciben inf."""
    F = np.asarray(F, dtype=float)
    k, m = F.shape
    d = np.zeros(k)
    if k <= 2:
        return np.full(k, np.inf)
    for j in range(m):
        o = np.argsort(F[:, j])
        d[o[0]] = d[o[-1]] = np.inf
        rango = F[o[-1], j] - F[o[0], j]
        if rango == 0:
            continue
        for t in range(1, k - 1):
            d[o[t]] += (F[o[t + 1], j] - F[o[t - 1], j]) / rango
    return d


def nsga2(objetivos, dim, lim_inf, lim_sup, tam=40, generaciones=60, eta_mut=0.1, semilla=0):
    """objetivos(x) → tupla de valores a minimizar. Devuelve (X, F) de la población final.
    Variación: cruce aritmético aleatorio + mutación gaussiana (σ = eta_mut·rango)."""
    rng = np.random.default_rng(semilla)
    X = rng.uniform(lim_inf, lim_sup, (tam, dim))

    def evaluar(X):
        return np.array([objetivos(x) for x in X])

    def rangos_y_crowding(F):
        rango, crowd = np.zeros(len(F), int), np.zeros(len(F))
        for r, fr in enumerate(ordenamiento_no_dominado(F.tolist())):
            rango[fr] = r
            crowd[fr] = distancia_crowding(F[fr])
        return rango, crowd

    F = evaluar(X)
    for _ in range(generaciones):
        rango, crowd = rangos_y_crowding(F)
        hijos = []
        for _ in range(tam):
            pad = []
            for _ in range(2):
                i, j = rng.integers(tam, size=2)
                mejor_i = (rango[i], -crowd[i]) < (rango[j], -crowd[j])
                pad.append(X[i] if mejor_i else X[j])
            u = rng.random(dim)
            h = u * pad[0] + (1 - u) * pad[1] + rng.normal(0, eta_mut * (lim_sup - lim_inf), dim)
            hijos.append(np.clip(h, lim_inf, lim_sup))
        R = np.vstack([X, hijos])
        FR = np.vstack([F, evaluar(hijos)])
        nuevo = []
        for fr in ordenamiento_no_dominado(FR.tolist()):
            if len(nuevo) + len(fr) <= tam:
                nuevo += fr
            else:
                cd = distancia_crowding(FR[fr])
                nuevo += [fr[k] for k in np.argsort(-cd)[: tam - len(nuevo)]]
                break
        X, F = R[nuevo], FR[nuevo]
    return X, F
