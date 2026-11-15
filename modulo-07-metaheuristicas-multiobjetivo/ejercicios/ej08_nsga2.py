"""Ejercicio 08 — Optimización multiobjetivo: dominancia de Pareto y NSGA-II
(BUAP 4.1 y 4.6; Deb et al. 2002; Eiben & Smith cap. 12).

Minimización de todos los objetivos.
a domina a b  ⇔  a_i ≤ b_i ∀i  y  a_j < b_j para algún j.
Frente de Pareto = conjunto de puntos no dominados.
NSGA-II: ordenamiento no dominado rápido + distancia de crowding + selección por
torneo con (rango, −crowding) + elitismo (μ+λ).
"""
import numpy as np


def domina(a, b):
    """True si a domina a b."""
    raise NotImplementedError  # TODO: implementa esta función


def frente_pareto(puntos):
    """Índices de los puntos no dominados (orden ascendente)."""
    raise NotImplementedError  # TODO: implementa esta función


def ordenamiento_no_dominado(puntos):
    """Lista de frentes (cada frente = lista de índices ordenada). Frente 0 = no dominados."""
    raise NotImplementedError  # TODO: implementa esta función


def distancia_crowding(F):
    """F: array (k, m) con los objetivos de un frente. Devuelve array (k,) con la
    distancia de crowding; los extremos de cada objetivo reciben inf."""
    raise NotImplementedError  # TODO: implementa esta función


def nsga2(objetivos, dim, lim_inf, lim_sup, tam=40, generaciones=60, eta_mut=0.1, semilla=0):
    """objetivos(x) → tupla de valores a minimizar. Devuelve (X, F) de la población final.
    Variación: cruce aritmético aleatorio + mutación gaussiana (σ = eta_mut·rango)."""
    raise NotImplementedError  # TODO: implementa esta función
