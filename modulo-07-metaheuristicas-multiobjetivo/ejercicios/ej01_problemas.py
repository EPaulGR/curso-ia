"""Ejercicio 01 — Representación de problemas de optimización combinatoria.

TSP: una solución es una permutación de ciudades; costo = longitud del ciclo cerrado.
Mochila 0/1: una solución es un vector binario x; maximizar Σ v_i x_i s.a. Σ w_i x_i ≤ C.
"""
import math


def matriz_distancias(coords):
    """Matriz (lista de listas) de distancias euclidianas entre coordenadas (x, y)."""
    raise NotImplementedError  # TODO: implementa esta función


def longitud_ruta(ruta, D):
    """Longitud del ciclo que visita `ruta` en orden y regresa al inicio."""
    raise NotImplementedError  # TODO: implementa esta función


def dos_opt(ruta, i, j):
    """Movimiento 2-opt: invierte el segmento ruta[i..j] (inclusive). Devuelve nueva lista."""
    raise NotImplementedError  # TODO: implementa esta función


def valor_mochila(x, pesos, valores, capacidad):
    """Valor total si es factible; si excede la capacidad devuelve
    valor − 10·max(valores)·exceso (penalización)."""
    raise NotImplementedError  # TODO: implementa esta función
