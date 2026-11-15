"""Ejercicio 02 — Búsqueda local: ascenso de colinas y recocido simulado (BUAP 4.2, AIMA 4.1).

Hill climbing (mejor mejora, vecindario 2-opt) con reinicios aleatorios.
Recocido simulado: acepta un vecino peor con probabilidad exp(−Δ/T); T ← α·T.
Las funciones de ej01 se reescriben aquí para que el archivo sea autocontenido.
"""
import math
import random


def _longitud(ruta, D):
    return sum(D[ruta[i]][ruta[(i + 1) % len(ruta)]] for i in range(len(ruta)))


def hill_climbing_tsp(D, reinicios=5, semilla=0):
    """Devuelve (mejor_ruta, longitud). Cada reinicio parte de una permutación aleatoria
    y aplica el mejor movimiento 2-opt mientras mejore."""
    raise NotImplementedError  # TODO: implementa esta función


def recocido_simulado_tsp(D, T0=10.0, alfa=0.995, iteraciones=20000, semilla=0):
    """Devuelve (mejor_ruta, longitud). Vecino = 2-opt aleatorio."""
    raise NotImplementedError  # TODO: implementa esta función
