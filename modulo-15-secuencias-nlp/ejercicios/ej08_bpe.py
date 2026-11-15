# EJERCICIO: implementa cada función marcada con TODO.
# Verifica con: pytest modulo-15-secuencias-nlp

"""Ej 08 — Byte Pair Encoding (Sennrich et al., 2016) a nivel de caracteres."""
from collections import Counter

def entrenar_bpe(palabras, n_fusiones):
    """palabras: lista de str. Cada palabra empieza como tupla de caracteres + '</w>'.
    En cada paso fusiona el par adyacente más frecuente (empates: el menor lexicográficamente). Devuelve lista de fusiones."""
    raise NotImplementedError  # TODO

def _fusionar(w, par):
    """Reemplaza cada ocurrencia del par en la tupla w por su concatenación."""
    raise NotImplementedError  # TODO

def aplicar_bpe(palabra, fusiones):
    """Tokeniza una palabra aplicando las fusiones en orden."""
    raise NotImplementedError  # TODO
