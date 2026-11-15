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
    idx = rng.sample(range(len(poblacion)), k)
    return poblacion[max(idx, key=lambda i: aptitudes[i])][:]


def cruce_un_punto(p1, p2, rng):
    """Corta en un punto aleatorio 1..n-1 y devuelve dos hijos."""
    c = rng.randint(1, len(p1) - 1)
    return p1[:c] + p2[c:], p2[:c] + p1[c:]


def mutacion_bit(x, prob, rng):
    """Invierte cada bit con probabilidad prob. Devuelve nueva lista."""
    return [b ^ 1 if rng.random() < prob else b for b in x]


def cruce_ox(p1, p2, rng):
    """Order crossover: copia p1[i..j] al hijo y rellena el resto con el orden de p2.
    El resultado debe ser una permutación válida."""
    n = len(p1)
    i, j = sorted(rng.sample(range(n), 2))
    hijo = [None] * n
    hijo[i:j + 1] = p1[i:j + 1]
    usados = set(hijo[i:j + 1])
    resto = [g for g in p2 if g not in usados]
    k = 0
    for pos in list(range(j + 1, n)) + list(range(0, i)):
        hijo[pos] = resto[k]
        k += 1
    return hijo


def algoritmo_genetico_mochila(pesos, valores, capacidad, tam_pob=40, generaciones=100,
                               p_cruce=0.9, p_mut=None, semilla=0):
    """Devuelve (mejor_x, mejor_valor). Usa elitismo de 1 individuo y la penalización
    de ej01 (valor − 10·max(v)·exceso)."""
    rng = random.Random(semilla)
    n = len(pesos)
    p_mut = p_mut if p_mut is not None else 1 / n

    def f(x):
        p = sum(w for w, b in zip(pesos, x) if b)
        v = sum(val for val, b in zip(valores, x) if b)
        return v if p <= capacidad else v - 10 * max(valores) * (p - capacidad)

    pob = [[rng.randint(0, 1) for _ in range(n)] for _ in range(tam_pob)]
    for _ in range(generaciones):
        apt = [f(x) for x in pob]
        elite = pob[max(range(tam_pob), key=lambda i: apt[i])][:]
        nueva = [elite]
        while len(nueva) < tam_pob:
            a, b = seleccion_torneo(pob, apt, 3, rng), seleccion_torneo(pob, apt, 3, rng)
            if rng.random() < p_cruce:
                a, b = cruce_un_punto(a, b, rng)
            nueva += [mutacion_bit(a, p_mut, rng), mutacion_bit(b, p_mut, rng)]
        pob = nueva[:tam_pob]
    mejor = max(pob, key=f)
    return mejor, f(mejor)
