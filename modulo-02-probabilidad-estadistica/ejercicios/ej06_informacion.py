"""Ejercicio 06 — Teoría de la información (log base 2 salvo que se indique)."""
import numpy as np

def entropia(p, base=2):
    """H(p); ignora probabilidades cero."""
    raise NotImplementedError  # TODO

def entropia_cruzada(p, q, base=2):
    """H(p, q)."""
    raise NotImplementedError  # TODO

def kl(p, q, base=2):
    """D_KL(p || q)."""
    raise NotImplementedError  # TODO

def informacion_mutua(conjunta, base=2):
    """I(X;Y) a partir de la matriz de probabilidad conjunta."""
    raise NotImplementedError  # TODO

def perplejidad(probs_correctas):
    """Perplejidad = exp(-media log p) de las probabilidades asignadas a los tokens correctos."""
    raise NotImplementedError  # TODO
