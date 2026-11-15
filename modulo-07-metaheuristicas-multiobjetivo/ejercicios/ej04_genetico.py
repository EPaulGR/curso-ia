"""Ejercicio 04 — Algoritmos genéticos (BUAP 4.4; Eiben & Smith caps. 3–5).

Componentes: representación, población, selección (torneo), cruce, mutación,
reemplazo con elitismo. Implementa:
- seleccion_torneo, cruce_un_punto, mutacion_bit (binario, mochila)
- cruce_ox (order crossover para permutaciones, TSP)
- algoritmo_genetico_mochila
"""
import random


def seleccion_torneo(poblacion, aptitudes, k, rng):
    """Elige k individuos al azar y devuelve (una copia de) el de mayor aptitud."""
    raise NotImplementedError  # TODO: implementa esta función


def cruce_un_punto(p1, p2, rng):
    """Corta en un punto aleatorio 1..n-1 y devuelve dos hijos."""
    raise NotImplementedError  # TODO: implementa esta función


def mutacion_bit(x, prob, rng):
    """Invierte cada bit con probabilidad prob. Devuelve nueva lista."""
    raise NotImplementedError  # TODO: implementa esta función


def cruce_ox(p1, p2, rng):
    """Order crossover: copia p1[i..j] al hijo y rellena el resto con el orden de p2.
    El resultado debe ser una permutación válida."""
    raise NotImplementedError  # TODO: implementa esta función


def algoritmo_genetico_mochila(pesos, valores, capacidad, tam_pob=40, generaciones=100,
                               p_cruce=0.9, p_mut=None, semilla=0):
    """Devuelve (mejor_x, mejor_valor). Usa elitismo de 1 individuo y la penalización
    de ej01 (valor − 10·max(v)·exceso)."""
    raise NotImplementedError  # TODO: implementa esta función
