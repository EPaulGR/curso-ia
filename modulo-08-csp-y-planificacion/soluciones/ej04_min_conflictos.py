"""Ejercicio 04 — Búsqueda local para CSP: MIN-CONFLICTOS (AIMA 6.4).

    asignación completa aleatoria
    repetir max_pasos:
        si es solución: devolverla
        var ← variable en conflicto elegida al azar
        valor ← el que minimiza conflictos (desempate aleatorio)
Resuelve n-reinas con n = 10^6 en ~50 pasos de media (!).
Aquí se implementa directamente para n reinas con conteo eficiente por fila y diagonales.
"""
import random


def n_reinas_min_conflictos(n, max_pasos=100000, semilla=0):
    """Devuelve lista `filas` (filas[c] = fila de la reina en la columna c) sin ataques,
    o None si no se logró. Usa contadores por fila, diagonal (f−c) y antidiagonal (f+c)."""
    rng = random.Random(semilla)
    fila_cnt = [0] * n
    d1 = [0] * (2 * n)
    d2 = [0] * (2 * n)
    filas = []
    for c in range(n):  # inicialización voraz
        mejor = min(range(n), key=lambda f: (fila_cnt[f] + d1[f - c + n] + d2[f + c], rng.random()))
        filas.append(mejor)
        fila_cnt[mejor] += 1; d1[mejor - c + n] += 1; d2[mejor + c] += 1

    def conf(f, c):
        return fila_cnt[f] + d1[f - c + n] + d2[f + c]

    for _ in range(max_pasos):
        en_conf = [c for c in range(n) if conf(filas[c], c) > 3]
        if not en_conf:
            return filas
        c = rng.choice(en_conf)
        f0 = filas[c]
        fila_cnt[f0] -= 1; d1[f0 - c + n] -= 1; d2[f0 + c] -= 1
        f = min(range(n), key=lambda f: (conf(f, c), rng.random()))
        filas[c] = f
        fila_cnt[f] += 1; d1[f - c + n] += 1; d2[f + c] += 1
    return None
