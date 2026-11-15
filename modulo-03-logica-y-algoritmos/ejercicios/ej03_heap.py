"""Ejercicio 03 — Heap binario mínimo desde cero (sin heapq)."""

class MinHeap:

    def __init__(self):
        self.datos = []

    def __len__(self):
        """Número de elementos."""
        raise NotImplementedError  # TODO

    def push(self, x):
        """Inserta x (sift-up)."""
        raise NotImplementedError  # TODO

    def peek(self):
        """Mínimo sin extraer."""
        raise NotImplementedError  # TODO

    def pop(self):
        """Extrae el mínimo (sift-down). IndexError si está vacío."""
        raise NotImplementedError  # TODO

def heapsort(xs):
    """Ordena usando MinHeap."""
    raise NotImplementedError  # TODO
