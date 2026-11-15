"""Ejercicio 03 — Heap binario mínimo desde cero (sin heapq)."""


class MinHeap:
    def __init__(self):
        self.datos = []

    def __len__(self):
        """Número de elementos."""
        return len(self.datos)

    def push(self, x):
        """Inserta x (sift-up)."""
        d = self.datos; d.append(x); i = len(d) - 1
        while i > 0 and d[(i - 1) // 2] > d[i]:
            p = (i - 1) // 2; d[i], d[p] = d[p], d[i]; i = p

    def peek(self):
        """Mínimo sin extraer."""
        return self.datos[0]

    def pop(self):
        """Extrae el mínimo (sift-down). IndexError si está vacío."""
        d = self.datos
        if not d:
            raise IndexError("heap vacío")
        d[0], d[-1] = d[-1], d[0]; m = d.pop(); i = 0
        while True:
            l, r, s = 2 * i + 1, 2 * i + 2, i
            if l < len(d) and d[l] < d[s]: s = l
            if r < len(d) and d[r] < d[s]: s = r
            if s == i: return m
            d[i], d[s] = d[s], d[i]; i = s


def heapsort(xs):
    """Ordena usando MinHeap."""
    h = MinHeap()
    for x in xs:
        h.push(x)
    return [h.pop() for _ in range(len(h))]
