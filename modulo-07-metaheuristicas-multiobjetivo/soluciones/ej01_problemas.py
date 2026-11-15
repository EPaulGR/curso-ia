"""Ejercicio 01 — Representación de problemas de optimización combinatoria.

TSP: una solución es una permutación de ciudades; costo = longitud del ciclo cerrado.
Mochila 0/1: una solución es un vector binario x; maximizar Σ v_i x_i s.a. Σ w_i x_i ≤ C.
"""
import math


def matriz_distancias(coords):
    """Matriz (lista de listas) de distancias euclidianas entre coordenadas (x, y)."""
    return [[math.dist(a, b) for b in coords] for a in coords]


def longitud_ruta(ruta, D):
    """Longitud del ciclo que visita `ruta` en orden y regresa al inicio."""
    return sum(D[ruta[i]][ruta[(i + 1) % len(ruta)]] for i in range(len(ruta)))


def dos_opt(ruta, i, j):
    """Movimiento 2-opt: invierte el segmento ruta[i..j] (inclusive). Devuelve nueva lista."""
    return ruta[:i] + ruta[i:j + 1][::-1] + ruta[j + 1:]


def valor_mochila(x, pesos, valores, capacidad):
    """Valor total si es factible; si excede la capacidad devuelve
    valor − 10·max(valores)·exceso (penalización)."""
    p = sum(w for w, b in zip(pesos, x) if b)
    v = sum(val for val, b in zip(valores, x) if b)
    if p <= capacidad:
        return v
    return v - 10 * max(valores) * (p - capacidad)
