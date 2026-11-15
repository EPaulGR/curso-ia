# EJERCICIO: implementa cada función marcada con TODO.
# Verifica con: pytest modulo-12-no-supervisado

"""Ej 04 — Mezcla de gaussianas 1D con el algoritmo EM."""
import numpy as np

def normal_pdf(x, mu, var):
    """Densidad normal N(mu, var) evaluada en x."""
    raise NotImplementedError  # TODO

def em_gmm_1d(x, k, iters=200, semilla=0):
    """EM para GMM 1D. Inicializa medias en cuantiles equiespaciados de x. Devuelve (pesos, medias, varianzas, log_verosimilitud_final)."""
    raise NotImplementedError  # TODO
