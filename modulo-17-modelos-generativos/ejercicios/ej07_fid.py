# EJERCICIO: implementa cada función marcada con TODO.
# Verifica con: pytest modulo-17-modelos-generativos

"""Ej 07 — Distancia de Fréchet entre gaussianas (base de la métrica FID)."""
import numpy as np
from scipy import linalg

def frechet(mu1, S1, mu2, S2):
    """‖μ1-μ2‖² + Tr(S1 + S2 - 2(S1 S2)^{1/2})."""
    raise NotImplementedError  # TODO

def fid_desde_features(A, B):
    """A, B (n, d) activaciones; ajusta gaussianas y devuelve la distancia de Fréchet."""
    raise NotImplementedError  # TODO
