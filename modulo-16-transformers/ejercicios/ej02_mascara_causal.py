# EJERCICIO: implementa cada función marcada con TODO.
# Verifica con: pytest modulo-16-transformers

"""Ej 02 — Máscaras causal y de padding."""
import numpy as np

def mascara_causal(T):
    """(T,T) booleana: la posición i puede ver j ≤ i."""
    raise NotImplementedError  # TODO

def mascara_padding(longitudes, T):
    """(N, T) booleana: True en posiciones reales, False en relleno."""
    raise NotImplementedError  # TODO
