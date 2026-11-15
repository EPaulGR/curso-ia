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
    raise NotImplementedError  # TODO: implementa esta función
