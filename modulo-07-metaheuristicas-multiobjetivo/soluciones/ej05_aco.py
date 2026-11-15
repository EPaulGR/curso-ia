"""Ejercicio 05 — Optimización por colonia de hormigas, Ant System (BUAP 4.5; Dorigo 1996).

Probabilidad de que la hormiga en i vaya a j no visitada:
    p_ij = τ_ij^α · η_ij^β / Σ_k τ_ik^α · η_ik^β,      η_ij = 1/d_ij
Evaporación y depósito:
    τ_ij ← (1−ρ)·τ_ij + Σ_hormigas Q / L_h   (si la hormiga usó la arista ij)
"""
import random


def aco_tsp(D, hormigas=10, iteraciones=50, alfa=1.0, beta=3.0, rho=0.5, Q=1.0, semilla=0):
    """Devuelve (mejor_ruta, longitud)."""
    rng = random.Random(semilla)
    n = len(D)
    tau = [[1.0] * n for _ in range(n)]
    mejor, mejor_l = None, float("inf")

    def long(r):
        return sum(D[r[i]][r[(i + 1) % n]] for i in range(n))

    for _ in range(iteraciones):
        rutas = []
        for _ in range(hormigas):
            r = [rng.randrange(n)]
            libres = set(range(n)) - {r[0]}
            while libres:
                i = r[-1]
                cand = list(libres)
                pesos = [tau[i][j] ** alfa * (1 / max(D[i][j], 1e-12)) ** beta for j in cand]
                j = rng.choices(cand, weights=pesos)[0]
                r.append(j)
                libres.remove(j)
            rutas.append((r, long(r)))
        for i in range(n):
            for j in range(n):
                tau[i][j] *= 1 - rho
        for r, l in rutas:
            for k in range(n):
                a, b = r[k], r[(k + 1) % n]
                tau[a][b] += Q / l
                tau[b][a] += Q / l
            if l < mejor_l:
                mejor, mejor_l = r, l
    return mejor, mejor_l
