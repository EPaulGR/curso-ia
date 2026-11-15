"""Ejercicio 08 — Cómputo en inferencia: self-consistency, best-of-N, pass@k.

- Self-consistency (Wang et al., 2022): muestrea varias cadenas de pensamiento y vota la respuesta.
- Best-of-N: genera N candidatos y elige el de mayor puntaje del verificador.
- pass@k insesgado (Chen et al., 2021): 1 - C(n-c, k) / C(n, k).
"""
from collections import Counter
from math import comb


def voto_mayoria(respuestas):
    """Respuesta más frecuente; en empate, la que aparece primero."""
    raise NotImplementedError  # TODO


def best_of_n(candidatos, verificador):
    """Devuelve el candidato con mayor verificador(c)."""
    raise NotImplementedError  # TODO


def pass_at_k(n, c, k):
    """Probabilidad de que al menos uno de k muestras (de n con c correctas) sea correcta."""
    raise NotImplementedError  # TODO


def extraer_respuesta(cadena):
    """Extrae el texto tras la última aparición de 'Respuesta:' (sin espacios); None si no hay."""
    raise NotImplementedError  # TODO
