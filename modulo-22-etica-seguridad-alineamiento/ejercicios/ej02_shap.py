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
    raise NotImplementedError  # TODO: implementa esta función


def verificar_eficiencia(f, x, base, phi):
    raise NotImplementedError  # TODO: implementa esta función
