"""Ejercicio 04 — Encadenamiento hacia adelante y hacia atrás con cláusulas de Horn (AIMA 7.5.4).

Regla de Horn: (premisas, conclusion) con premisas una lista de átomos; un hecho es ([], q).
- Hacia adelante (PL-FC-ENTAILS): contador de premisas no satisfechas por regla; agenda de
  hechos conocidos. Tiempo lineal en el tamaño de la KB. Dirigido por datos.
- Hacia atrás: para probar q, buscar reglas con conclusión q y probar sus premisas
  recursivamente, evitando ciclos. Dirigido por metas (como Prolog).
"""
from collections import deque


def encadenamiento_adelante(reglas, q):
    """True si q se deriva. Devuelve además el conjunto de átomos inferidos: (bool, set)."""
    raise NotImplementedError  # TODO: implementa esta función


def encadenamiento_atras(reglas, q, _pila=None):
    """True si q se puede probar."""
    raise NotImplementedError  # TODO: implementa esta función
