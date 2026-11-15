"""Ejercicio 06 — Union-Find y Kruskal."""

class UnionFind:

    def __init__(self, elementos):
        self.p = {e: e for e in elementos}
        self.r = {e: 0 for e in elementos}

    def find(self, x):
        """Raíz con compresión de caminos."""
        raise NotImplementedError  # TODO

    def union(self, a, b):
        """Une conjuntos; devuelve False si ya estaban unidos."""
        raise NotImplementedError  # TODO

def kruskal(nodos, aristas):
    """aristas: lista (peso, u, v). Devuelve (peso_total, lista_aristas_mst)."""
    raise NotImplementedError  # TODO
