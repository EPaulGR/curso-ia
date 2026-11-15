"""Ejercicio 03 — Consistencia de arcos: AC-3 (AIMA 6.2.2).

Un arco (Xi, Xj) es consistente si para cada valor de Di existe algún valor en Dj
que satisface la restricción.

    AC-3(csp):
        cola ← todos los arcos (Xi, Xj)
        mientras cola no vacía:
            (Xi, Xj) ← sacar(cola)
            si REVISAR(Xi, Xj):
                si Di vacío: devolver falso
                para cada Xk en vecinos(Xi) − {Xj}: meter (Xk, Xi)
        devolver verdadero
Complejidad O(c·d³) con c arcos y dominios de tamaño d.
"""
from collections import deque


def revisar(csp, Xi, Xj):
    """Elimina de dominios[Xi] los valores sin soporte en Xj. Devuelve True si eliminó algo."""
    raise NotImplementedError  # TODO: implementa esta función


def ac3(csp):
    """Aplica AC-3 modificando csp.dominios. Devuelve False si detecta inconsistencia."""
    raise NotImplementedError  # TODO: implementa esta función
