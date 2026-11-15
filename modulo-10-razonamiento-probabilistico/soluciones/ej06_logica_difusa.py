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
    x = np.asarray(x, float)
    izq = np.where(b > a, (x - a) / (b - a if b > a else 1), (x >= b).astype(float))
    der = np.where(c > b, (c - x) / (c - b if c > b else 1), (x <= b).astype(float))
    return np.clip(np.minimum(izq, der), 0, 1)


def trapezoidal(x, a, b, c, d):
    """Pertenencia trapezoidal: 0 hasta a, sube hasta b, 1 hasta c, baja hasta d."""
    x = np.asarray(x, float)
    sube = np.where(b > a, (x - a) / (b - a if b > a else 1), (x >= a).astype(float))
    baja = np.where(d > c, (d - x) / (d - c if d > c else 1), (x <= d).astype(float))
    return np.clip(np.minimum(np.minimum(sube, 1), baja), 0, 1)


def mamdani(entradas, conjuntos, reglas, universo_salida, conjuntos_salida):
    """entradas: dict var → valor nítido.
    conjuntos: dict var → dict etiqueta → función μ(x).
    reglas: lista de (lista de (var, etiqueta), 'y'|'o', etiqueta_salida).
    universo_salida: array de puntos; conjuntos_salida: dict etiqueta → μ(z).
    Devuelve el valor nítido (centroide)."""
    agregado = np.zeros_like(universo_salida, dtype=float)
    for antecedentes, op, salida in reglas:
        grados = [float(conjuntos[v][e](entradas[v])) for v, e in antecedentes]
        fuerza = min(grados) if op == "y" else max(grados)
        agregado = np.maximum(agregado, np.minimum(fuerza, conjuntos_salida[salida](universo_salida)))
    if agregado.sum() == 0:
        return float(np.mean(universo_salida))
    return float((agregado * universo_salida).sum() / agregado.sum())


def sistema_propina(servicio, comida):
    """Problema clásico de la propina: servicio y comida en [0,10] → propina en [0,25] %.
    Reglas: (1) servicio malo O comida rancia → baja; (2) servicio bueno → media;
    (3) servicio excelente O comida deliciosa → alta.
    Conjuntos: servicio malo=tri(0,0,5), bueno=tri(0,5,10), excelente=tri(5,10,10);
    comida rancia=tri(0,0,5), deliciosa=tri(5,10,10);
    propina baja=tri(0,0,13), media=tri(0,13,25), alta=tri(13,25,25)."""
    T = lambda a, b, c: (lambda x: triangular(x, a, b, c))
    conj = {"servicio": {"malo": T(0, 0, 5), "bueno": T(0, 5, 10), "excelente": T(5, 10, 10)},
            "comida": {"rancia": T(0, 0, 5), "deliciosa": T(5, 10, 10)}}
    sal = {"baja": T(0, 0, 13), "media": T(0, 13, 25), "alta": T(13, 25, 25)}
    reglas = [([("servicio", "malo"), ("comida", "rancia")], "o", "baja"),
              ([("servicio", "bueno")], "y", "media"),
              ([("servicio", "excelente"), ("comida", "deliciosa")], "o", "alta")]
    return mamdani({"servicio": servicio, "comida": comida}, conj, reglas, np.linspace(0, 25, 501), sal)
