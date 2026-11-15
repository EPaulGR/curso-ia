"""Ejercicio 05 — Optimización por colonia de hormigas, Ant System (BUAP 4.5; Dorigo 1996).

Probabilidad de que la hormiga en i vaya a j no visitada:
    p_ij = τ_ij^α · η_ij^β / Σ_k τ_ik^α · η_ik^β,      η_ij = 1/d_ij
Evaporación y depósito:
    τ_ij ← (1−ρ)·τ_ij + Σ_hormigas Q / L_h   (si la hormiga usó la arista ij)
"""
import random


def aco_tsp(D, hormigas=10, iteraciones=50, alfa=1.0, beta=3.0, rho=0.5, Q=1.0, semilla=0):
    """Devuelve (mejor_ruta, longitud)."""
    raise NotImplementedError  # TODO: implementa esta función
