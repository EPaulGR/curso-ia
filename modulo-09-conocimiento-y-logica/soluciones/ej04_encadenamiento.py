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
    cuenta = [len(p) for p, _ in reglas]
    agenda = deque(c for p, c in reglas if not p)
    inferido = set()
    while agenda:
        a = agenda.popleft()
        if a in inferido:
            continue
        inferido.add(a)
        for i, (p, c) in enumerate(reglas):
            if a in p:
                cuenta[i] -= 1
                if cuenta[i] == 0:
                    agenda.append(c)
    return q in inferido, inferido


def encadenamiento_atras(reglas, q, _pila=None):
    """True si q se puede probar."""
    pila = _pila or set()
    if q in pila:
        return False
    pila = pila | {q}
    return any(all(encadenamiento_atras(reglas, p, pila) for p in prem)
               for prem, c in reglas if c == q)
