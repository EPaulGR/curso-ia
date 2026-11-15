# EJERCICIO: implementa cada función marcada con TODO.
# Verifica con: pytest modulo-17-modelos-generativos

"""Ej 03 — Pérdidas de una GAN (Goodfellow et al., 2014)."""
import numpy as np

def bce(p, y):
    """Entropía cruzada binaria media."""
    raise NotImplementedError  # TODO

def perdida_discriminador(d_real, d_falso):
    """BCE(D(x), 1) + BCE(D(G(z)), 0)."""
    raise NotImplementedError  # TODO

def perdida_generador_nosaturante(d_falso):
    """Versión no saturante: -E[log D(G(z))]."""
    raise NotImplementedError  # TODO

def d_optimo(p_datos, p_gen):
    """Discriminador óptimo D*(x) = p_datos / (p_datos + p_gen)."""
    raise NotImplementedError  # TODO
