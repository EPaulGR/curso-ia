"""Ejercicio 08 — Cómputo en inferencia: self-consistency, best-of-N, pass@k.

- Self-consistency (Wang et al., 2022): muestrea varias cadenas de pensamiento y vota la respuesta.
- Best-of-N: genera N candidatos y elige el de mayor puntaje del verificador.
- pass@k insesgado (Chen et al., 2021): 1 - C(n-c, k) / C(n, k).
"""
from collections import Counter
from math import comb


def voto_mayoria(respuestas):
    """Respuesta más frecuente; en empate, la que aparece primero."""
    cuenta = Counter(respuestas)
    maximo = max(cuenta.values())
    for r in respuestas:
        if cuenta[r] == maximo:
            return r


def best_of_n(candidatos, verificador):
    """Devuelve el candidato con mayor verificador(c)."""
    return max(candidatos, key=verificador)


def pass_at_k(n, c, k):
    """Probabilidad de que al menos uno de k muestras (de n con c correctas) sea correcta."""
    if n - c < k:
        return 1.0
    return 1.0 - comb(n - c, k) / comb(n, k)


def extraer_respuesta(cadena):
    """Extrae el texto tras la última aparición de 'Respuesta:' (sin espacios); None si no hay."""
    marca = "Respuesta:"
    if marca not in cadena:
        return None
    return cadena.rsplit(marca, 1)[1].strip()
