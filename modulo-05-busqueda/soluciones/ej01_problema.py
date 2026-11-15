"""Ejercicio 01 — Formulación de problemas.

Todos los algoritmos del módulo trabajan con esta interfaz:
    p.inicial            estado inicial (hashable)
    p.acciones(s)        lista de acciones aplicables
    p.resultado(s, a)    estado sucesor
    p.es_meta(s)         bool
    p.costo(s, a, s2)    costo del paso (por defecto 1)

El 8-puzzle se representa como tupla de 9 enteros leída por filas; 0 es el hueco.
"""

META_8 = (1, 2, 3, 4, 5, 6, 7, 8, 0)
MOVS = {"Arriba": -3, "Abajo": 3, "Izquierda": -1, "Derecha": 1}


class Problema:
    def __init__(self, inicial, meta=None):
        self.inicial, self.meta = inicial, meta

    def acciones(self, s):
        raise NotImplementedError

    def resultado(self, s, a):
        raise NotImplementedError

    def es_meta(self, s):
        return s == self.meta

    def costo(self, s, a, s2):
        return 1


class OchoPuzzle(Problema):
    def __init__(self, inicial, meta=META_8):
        super().__init__(tuple(inicial), tuple(meta))

    def acciones(self, s):
        """Acciones válidas (mover el hueco) en el orden Arriba, Abajo, Izquierda, Derecha."""
        i = s.index(0); f, c = divmod(i, 3); r = []
        if f > 0: r.append("Arriba")
        if f < 2: r.append("Abajo")
        if c > 0: r.append("Izquierda")
        if c < 2: r.append("Derecha")
        return r

    def resultado(self, s, a):
        """Intercambia el hueco con la ficha en la dirección indicada."""
        i = s.index(0); j = i + MOVS[a]; l = list(s)
        l[i], l[j] = l[j], l[i]
        return tuple(l)


def inversiones(s):
    """Número de pares (i<j) con s[i] > s[j], ignorando el 0."""
    v = [x for x in s if x != 0]
    return sum(v[i] > v[j] for i in range(len(v)) for j in range(i + 1, len(v)))


def es_resoluble(s, meta=META_8):
    """En un tablero de ancho impar, resoluble si la paridad de inversiones coincide con la de la meta."""
    return inversiones(s) % 2 == inversiones(meta) % 2


class Grafo(Problema):
    """Problema de rutas en grafo ponderado no dirigido: aristas dict (u, v) -> costo."""

    def __init__(self, inicial, meta, aristas):
        super().__init__(inicial, meta)
        self.ady = {}
        for (u, v), c in aristas.items():
            self.ady.setdefault(u, {})[v] = c
            self.ady.setdefault(v, {})[u] = c

    def acciones(self, s):
        """Vecinos de s en orden alfabético (la acción es 'ir a' ese vecino)."""
        return sorted(self.ady.get(s, {}))

    def resultado(self, s, a):
        return a

    def costo(self, s, a, s2):
        return self.ady[s][s2]


# Mapa de Rumania (AIMA, fig. 3.1) y distancias en línea recta a Bucharest.
RUMANIA = {
    ("Arad", "Zerind"): 75, ("Arad", "Sibiu"): 140, ("Arad", "Timisoara"): 118,
    ("Zerind", "Oradea"): 71, ("Oradea", "Sibiu"): 151, ("Timisoara", "Lugoj"): 111,
    ("Lugoj", "Mehadia"): 70, ("Mehadia", "Drobeta"): 75, ("Drobeta", "Craiova"): 120,
    ("Craiova", "Rimnicu Vilcea"): 146, ("Craiova", "Pitesti"): 138, ("Sibiu", "Fagaras"): 99,
    ("Sibiu", "Rimnicu Vilcea"): 80, ("Rimnicu Vilcea", "Pitesti"): 97, ("Fagaras", "Bucharest"): 211,
    ("Pitesti", "Bucharest"): 101, ("Bucharest", "Giurgiu"): 90, ("Bucharest", "Urziceni"): 85,
    ("Urziceni", "Hirsova"): 98, ("Hirsova", "Eforie"): 86, ("Urziceni", "Vaslui"): 142,
    ("Vaslui", "Iasi"): 92, ("Iasi", "Neamt"): 87,
}
H_BUCHAREST = {
    "Arad": 366, "Bucharest": 0, "Craiova": 160, "Drobeta": 242, "Eforie": 161, "Fagaras": 176,
    "Giurgiu": 77, "Hirsova": 151, "Iasi": 226, "Lugoj": 244, "Mehadia": 241, "Neamt": 234,
    "Oradea": 380, "Pitesti": 100, "Rimnicu Vilcea": 193, "Sibiu": 253, "Timisoara": 329,
    "Urziceni": 80, "Vaslui": 199, "Zerind": 374,
}
