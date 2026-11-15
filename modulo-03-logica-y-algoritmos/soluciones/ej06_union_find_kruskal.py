"""Ejercicio 06 — Union-Find y Kruskal."""


class UnionFind:
    def __init__(self, elementos):
        self.p = {e: e for e in elementos}; self.r = {e: 0 for e in elementos}

    def find(self, x):
        """Raíz con compresión de caminos."""
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]; x = self.p[x]
        return x

    def union(self, a, b):
        """Une conjuntos; devuelve False si ya estaban unidos."""
        a, b = self.find(a), self.find(b)
        if a == b:
            return False
        if self.r[a] < self.r[b]: a, b = b, a
        self.p[b] = a; self.r[a] += self.r[a] == self.r[b]
        return True


def kruskal(nodos, aristas):
    """aristas: lista (peso, u, v). Devuelve (peso_total, lista_aristas_mst)."""
    uf = UnionFind(nodos); mst = []
    for w, u, v in sorted(aristas):
        if uf.union(u, v):
            mst.append((w, u, v))
    return sum(w for w, _, _ in mst), mst
