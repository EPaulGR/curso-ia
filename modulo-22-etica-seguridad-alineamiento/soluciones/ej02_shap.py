"""Ejercicio 2 — Valores de Shapley exactos para explicar un modelo.

- `valores_shapley(f, x, base)`: f recibe un vector y devuelve un escalar. Para cada subconjunto S
  de features, el "modelo restringido" evalúa f en un vector con x en S y `base` fuera de S.
  phi_i = sum_{S ⊆ N - {i}} |S|!(n-|S|-1)!/n! * [v(S ∪ {i}) - v(S)].
  Devuelve np.ndarray de n valores. (Exponencial: solo para n pequeño.)
- `verificar_eficiencia(f, x, base, phi)`: True si sum(phi) ≈ f(x) - f(base).
Lundberg & Lee 2017 (SHAP). La librería `shap` aproxima esto para modelos grandes.
"""
import itertools
import math
import numpy as np


def valores_shapley(f, x, base):
    x, base = np.asarray(x, float), np.asarray(base, float)
    n = len(x)

    def v(S):
        z = base.copy()
        z[list(S)] = x[list(S)]
        return f(z)

    phi = np.zeros(n)
    for i in range(n):
        otros = [j for j in range(n) if j != i]
        for k in range(n):
            w = math.factorial(k) * math.factorial(n - k - 1) / math.factorial(n)
            for S in itertools.combinations(otros, k):
                phi[i] += w * (v(S + (i,)) - v(S))
    return phi


def verificar_eficiencia(f, x, base, phi):
    return bool(np.isclose(np.sum(phi), f(np.asarray(x, float)) - f(np.asarray(base, float))))
