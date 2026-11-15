# EJERCICIO: implementa cada función marcada con TODO.
# Verifica con: pytest modulo-13-redes-neuronales

"""Ej 03 — Verificación de gradientes por diferencias finitas."""
import numpy as np

def gradiente_numerico(f, x, h=1e-05):
    """Gradiente de f escalar respecto a x (array) con diferencias centrales."""
    raise NotImplementedError  # TODO

def error_relativo(a, b):
    """‖a−b‖ / max(‖a‖+‖b‖, 1e-12)."""
    raise NotImplementedError  # TODO
