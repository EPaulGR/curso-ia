"""Ejercicio 03 — Inferencia aproximada por muestreo (AIMA 13.4).

Usa el mismo formato de red que ej02.
- Muestreo previo (prior sampling): muestrear cada variable dados sus padres en orden topológico.
- Muestreo por rechazo: descartar muestras inconsistentes con la evidencia.
- Ponderación por verosimilitud: fijar la evidencia y ponderar cada muestra por Π P(e_i | padres).
- Gibbs (MCMC): re-muestrear cada variable no evidencia dada su manta de Markov.
"""
import random


def _p(red, var, valor, a):
    p = red["cpt"][var][tuple(a[x] for x in red["padres"][var])]
    return p if valor else 1 - p


def muestra_previa(red, rng):
    """Una muestra completa (dict) de la conjunta."""
    raise NotImplementedError  # TODO: implementa esta función


def muestreo_rechazo(red, X, evidencia, n=10000, semilla=0):
    """Estimación de P(X=True | evidencia)."""
    raise NotImplementedError  # TODO: implementa esta función


def ponderacion_verosimilitud(red, X, evidencia, n=10000, semilla=0):
    """Estimación de P(X=True | evidencia)."""
    raise NotImplementedError  # TODO: implementa esta función


def gibbs(red, X, evidencia, n=20000, quemado=1000, semilla=0):
    """Estimación de P(X=True | evidencia) con muestreo de Gibbs."""
    raise NotImplementedError  # TODO: implementa esta función
