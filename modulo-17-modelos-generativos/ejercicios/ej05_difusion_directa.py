# EJERCICIO: implementa cada función marcada con TODO.
# Verifica con: pytest modulo-17-modelos-generativos

"""Ej 05 — Proceso de difusión directo (DDPM, Ho et al., 2020)."""
import numpy as np

def calendario_lineal(T, b0=0.0001, b1=0.02):
    """Devuelve (betas, alphas, alpha_barras) de longitud T."""
    raise NotImplementedError  # TODO

def q_muestra(x0, t, alpha_barras, ruido):
    """x_t = √ᾱ_t·x0 + √(1-ᾱ_t)·ε (salto directo a cualquier t)."""
    raise NotImplementedError  # TODO

def snr(alpha_barras):
    """Relación señal/ruido ᾱ/(1-ᾱ)."""
    raise NotImplementedError  # TODO
