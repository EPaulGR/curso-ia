"""Ejercicio 07 — Programación dinámica."""


def mochila(pesos, valores, capacidad):
    """Valor máximo de la mochila 0/1."""
    V = [0] * (capacidad + 1)
    for p, v in zip(pesos, valores):
        for w in range(capacidad, p - 1, -1):
            V[w] = max(V[w], V[w - p] + v)
    return V[capacidad]


def lcs(a, b):
    """Longitud de la subsecuencia común más larga."""
    D = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            D[i][j] = D[i - 1][j - 1] + 1 if a[i - 1] == b[j - 1] else max(D[i - 1][j], D[i][j - 1])
    return D[-1][-1]


def distancia_edicion(a, b):
    """Distancia de Levenshtein."""
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]
