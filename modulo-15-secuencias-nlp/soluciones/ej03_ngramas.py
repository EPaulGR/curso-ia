"""Ej 03 — Modelo de lenguaje de bigramas con suavizado de Laplace y perplejidad."""
import math
from collections import Counter


class Bigramas:
    """P(w_i | w_{i-1}) = (c(w_{i-1}, w_i) + 1) / (c(w_{i-1}) + |V|). Usa '<s>' y '</s>' como marcas."""

    def __init__(self, oraciones):
        """oraciones: lista de listas de tokens."""
        self.uni, self.bi = Counter(), Counter()
        vocab = set()
        for o in oraciones:
            o = ["<s>"] + o + ["</s>"]
            vocab.update(o)
            self.uni.update(o[:-1])
            self.bi.update(zip(o[:-1], o[1:]))
        self.V = len(vocab)

    def prob(self, prev, w):
        """Probabilidad suavizada."""
        return (self.bi[(prev, w)] + 1) / (self.uni[prev] + self.V)

    def perplejidad(self, oraciones):
        """exp(-promedio de log p) sobre todos los tokens predichos (incluye '</s>')."""
        lp, n = 0.0, 0
        for o in oraciones:
            o = ["<s>"] + o + ["</s>"]
            for a, b in zip(o[:-1], o[1:]):
                lp += math.log(self.prob(a, b))
                n += 1
        return math.exp(-lp / n)
