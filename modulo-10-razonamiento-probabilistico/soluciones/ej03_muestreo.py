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
    a = {}
    for v in red["variables"]:
        a[v] = rng.random() < _p(red, v, True, a)
    return a


def muestreo_rechazo(red, X, evidencia, n=10000, semilla=0):
    """Estimación de P(X=True | evidencia)."""
    rng = random.Random(semilla)
    c = {True: 0, False: 0}
    for _ in range(n):
        a = muestra_previa(red, rng)
        if all(a[k] == v for k, v in evidencia.items()):
            c[a[X]] += 1
    total = c[True] + c[False]
    return c[True] / total if total else float("nan")


def ponderacion_verosimilitud(red, X, evidencia, n=10000, semilla=0):
    """Estimación de P(X=True | evidencia)."""
    rng = random.Random(semilla)
    w = {True: 0.0, False: 0.0}
    for _ in range(n):
        a, peso = {}, 1.0
        for v in red["variables"]:
            if v in evidencia:
                a[v] = evidencia[v]
                peso *= _p(red, v, a[v], a)
            else:
                a[v] = rng.random() < _p(red, v, True, a)
        w[a[X]] += peso
    return w[True] / (w[True] + w[False])


def gibbs(red, X, evidencia, n=20000, quemado=1000, semilla=0):
    """Estimación de P(X=True | evidencia) con muestreo de Gibbs."""
    rng = random.Random(semilla)
    hijos = {v: [w for w in red["variables"] if v in red["padres"][w]] for v in red["variables"]}
    a = {v: evidencia.get(v, rng.random() < 0.5) for v in red["variables"]}
    libres = [v for v in red["variables"] if v not in evidencia]
    cuenta = 0
    for t in range(n + quemado):
        for v in libres:
            pesos = {}
            for val in (True, False):
                a[v] = val
                p = _p(red, v, val, a)
                for h in hijos[v]:
                    p *= _p(red, h, a[h], a)
                pesos[val] = p
            a[v] = rng.random() < pesos[True] / (pesos[True] + pesos[False])
        if t >= quemado and a[X]:
            cuenta += 1
    return cuenta / n
