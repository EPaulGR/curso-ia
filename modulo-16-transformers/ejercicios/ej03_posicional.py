# EJERCICIO: implementa cada función marcada con TODO.
# Verifica con: pytest modulo-16-transformers

"""Ej 03 — Codificación posicional sinusoidal (Vaswani et al., 2017)."""
import numpy as np

def codificacion_posicional(T, d):
    """PE[pos, 2i] = sin(pos / 10000^{2i/d}), PE[pos, 2i+1] = cos(...). Devuelve (T, d)."""
    raise NotImplementedError  # TODO
