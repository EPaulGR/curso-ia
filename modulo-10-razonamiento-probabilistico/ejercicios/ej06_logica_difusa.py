"""Ejercicio 06 — Lógica difusa y control de Mamdani (Negnevitsky cap. 4; Zadeh 1965).

Funciones de pertenencia, operadores (AND = min, OR = max, NOT = 1−μ), y sistema de
inferencia Mamdani con defusificación por centroide:
    1. Fusificar entradas.
    2. Evaluar reglas: fuerza = min (AND) / max (OR) de los antecedentes.
    3. Implicación: recortar (min) el consecuente a la fuerza de la regla.
    4. Agregación: max de todos los consecuentes recortados.
    5. Defusificar: centroide  z* = Σ μ(z)·z / Σ μ(z)  sobre una malla.
"""
import numpy as np


def triangular(x, a, b, c):
    """Pertenencia triangular con pico en b (a ≤ b ≤ c). Admite a == b o b == c (hombros)."""
    raise NotImplementedError  # TODO: implementa esta función


def trapezoidal(x, a, b, c, d):
    """Pertenencia trapezoidal: 0 hasta a, sube hasta b, 1 hasta c, baja hasta d."""
    raise NotImplementedError  # TODO: implementa esta función


def mamdani(entradas, conjuntos, reglas, universo_salida, conjuntos_salida):
    """entradas: dict var → valor nítido.
    conjuntos: dict var → dict etiqueta → función μ(x).
    reglas: lista de (lista de (var, etiqueta), 'y'|'o', etiqueta_salida).
    universo_salida: array de puntos; conjuntos_salida: dict etiqueta → μ(z).
    Devuelve el valor nítido (centroide)."""
    raise NotImplementedError  # TODO: implementa esta función


def sistema_propina(servicio, comida):
    """Problema clásico de la propina: servicio y comida en [0,10] → propina en [0,25] %.
    Reglas: (1) servicio malo O comida rancia → baja; (2) servicio bueno → media;
    (3) servicio excelente O comida deliciosa → alta.
    Conjuntos: servicio malo=tri(0,0,5), bueno=tri(0,5,10), excelente=tri(5,10,10);
    comida rancia=tri(0,0,5), deliciosa=tri(5,10,10);
    propina baja=tri(0,0,13), media=tri(0,13,25), alta=tri(13,25,25)."""
    raise NotImplementedError  # TODO: implementa esta función
