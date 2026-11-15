"""Ejercicio 01 — Estructuras de datos."""
from collections import Counter


def frecuencias(texto: str) -> dict:
    """Devuelve un dict palabra -> número de apariciones (minúsculas, separando por espacios)."""
    return dict(Counter(texto.lower().split()))


def top_k(texto: str, k: int) -> list:
    """Devuelve las k palabras más frecuentes como lista de tuplas (palabra, cuenta), desempate alfabético."""
    c = Counter(texto.lower().split())
    return sorted(c.items(), key=lambda t: (-t[1], t[0]))[:k]


def invertir_dict(d: dict) -> dict:
    """Invierte un dict valor -> lista ordenada de llaves que tenían ese valor."""
    r = {}
    for k, v in d.items():
        r.setdefault(v, []).append(k)
    return {v: sorted(ks) for v, ks in r.items()}


def pares_que_suman(nums: list, objetivo: int) -> set:
    """Conjunto de tuplas (a, b) con a < b, ambos en nums, tal que a + b == objetivo. Debe ser O(n)."""
    vistos, res = set(), set()
    for x in nums:
        y = objetivo - x
        if y in vistos:
            res.add((min(x, y), max(x, y)))
        vistos.add(x)
    return res
