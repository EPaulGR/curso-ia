# EJERCICIO: implementa cada función marcada con TODO.
# Verifica con: pytest modulo-15-secuencias-nlp

"""Ej 03 — Modelo de lenguaje de bigramas con suavizado de Laplace y perplejidad."""
import math
from collections import Counter

class Bigramas:
    """P(w_i | w_{i-1}) = (c(w_{i-1}, w_i) + 1) / (c(w_{i-1}) + |V|). Usa '<s>' y '</s>' como marcas."""

    def __init__(self, oraciones):
        """oraciones: lista de listas de tokens."""
        raise NotImplementedError  # TODO

    def prob(self, prev, w):
        """Probabilidad suavizada."""
        raise NotImplementedError  # TODO

    def perplejidad(self, oraciones):
        """exp(-promedio de log p) sobre todos los tokens predichos (incluye '</s>')."""
        raise NotImplementedError  # TODO
