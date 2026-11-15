"""Ejercicio 07 — Leyes de escalamiento (Chinchilla) y destilación.

Ley de potencias: L(N) = A * N^(-alpha). En log: log L = log A - alpha log N,
un ajuste lineal. Chinchilla (Hoffmann et al., 2022): con cómputo C ≈ 6 N D,
lo óptimo es ~20 tokens por parámetro (D ≈ 20 N).
Destilación (Hinton et al., 2015): KL(softmax(t/T) || softmax(s/T)) * T^2.
"""
import numpy as np


def ajustar_ley_potencias(N, L):
    """Devuelve (A, alpha) ajustando log L = log A - alpha log N por mínimos cuadrados."""
    raise NotImplementedError  # TODO


def chinchilla_optimo(C, tokens_por_parametro=20.0):
    """Con C = 6 N D y D = r N: N = sqrt(C / (6 r)). Devuelve (N, D)."""
    raise NotImplementedError  # TODO


def _softmax(z):
    z = z - z.max(axis=-1, keepdims=True)
    e = np.exp(z)
    return e / e.sum(axis=-1, keepdims=True)


def perdida_destilacion(logits_alumno, logits_maestro, T=2.0):
    """KL(p_maestro || p_alumno) con temperatura T, promediada por fila y multiplicada por T^2."""
    raise NotImplementedError  # TODO
