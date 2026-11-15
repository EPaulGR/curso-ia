"""Ejercicio 03 — Búsqueda tabú para la mochila 0/1 (BUAP 4.3; Glover 1986).

Vecindario: (a) invertir un bit, (b) intercambio: sacar un objeto i y meter un objeto j.
Lista tabú: los bits modificados quedan prohibidos `tenencia` iteraciones. Criterio de aspiración: un movimiento tabú se permite si produce una
solución mejor que la mejor encontrada. Se toma SIEMPRE el mejor vecino no tabú
(aunque empeore) — eso permite escapar de óptimos locales.
"""
import random


def _valor(x, pesos, valores, cap):
    p = sum(w for w, b in zip(pesos, x) if b)
    v = sum(val for val, b in zip(valores, x) if b)
    return v if p <= cap else v - 10 * max(valores) * (p - cap)


def busqueda_tabu_mochila(pesos, valores, capacidad, iteraciones=200, tenencia=3, semilla=0):
    """Devuelve (mejor_x, mejor_valor) con x lista de 0/1."""
    raise NotImplementedError  # TODO: implementa esta función
