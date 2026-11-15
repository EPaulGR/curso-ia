"""Ej 08 — Byte Pair Encoding (Sennrich et al., 2016) a nivel de caracteres."""
from collections import Counter


def entrenar_bpe(palabras, n_fusiones):
    """palabras: lista de str. Cada palabra empieza como tupla de caracteres + '</w>'.
    En cada paso fusiona el par adyacente más frecuente (empates: el menor lexicográficamente). Devuelve lista de fusiones."""
    corpus = Counter(tuple(w) + ("</w>",) for w in palabras)
    fusiones = []
    for _ in range(n_fusiones):
        pares = Counter()
        for w, f in corpus.items():
            for p in zip(w, w[1:]):
                pares[p] += f
        if not pares:
            break
        mejor = min(pares, key=lambda p: (-pares[p], p))
        fusiones.append(mejor)
        corpus = Counter({_fusionar(w, mejor): f for w, f in corpus.items()})
    return fusiones


def _fusionar(w, par):
    """Reemplaza cada ocurrencia del par en la tupla w por su concatenación."""
    r, i = [], 0
    while i < len(w):
        if i < len(w) - 1 and (w[i], w[i + 1]) == par:
            r.append(w[i] + w[i + 1])
            i += 2
        else:
            r.append(w[i])
            i += 1
    return tuple(r)


def aplicar_bpe(palabra, fusiones):
    """Tokeniza una palabra aplicando las fusiones en orden."""
    w = tuple(palabra) + ("</w>",)
    for f in fusiones:
        w = _fusionar(w, f)
    return list(w)
