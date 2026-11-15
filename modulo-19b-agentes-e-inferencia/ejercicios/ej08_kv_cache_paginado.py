"""Ejercicio 08 — KV cache paginado (idea de PagedAttention / vLLM).

En vez de reservar memoria contigua del tamaño máximo por secuencia, la caché se
divide en bloques de `tam_bloque` posiciones. Cada secuencia tiene una "tabla de
bloques" (como la memoria virtual de un SO).

- AsignadorBloques(n_bloques): asignar() -> id (MemoryError si no hay), liberar(id), libres().
- CachePaginada(n_bloques, tam_bloque, dim):
    agregar(seq, k, v)        agrega un vector k y v (dim,) a la secuencia
    obtener(seq) -> (K, V)    arrays (longitud, dim) en orden
    liberar(seq)              devuelve sus bloques al asignador
    desperdicio(seq)          posiciones reservadas sin usar (solo en el último bloque)
"""
import numpy as np


class AsignadorBloques:
    def __init__(self, n_bloques):
        self._libres = list(range(n_bloques))[::-1]

    def asignar(self):
        raise NotImplementedError  # TODO

    def liberar(self, id_):
        raise NotImplementedError  # TODO

    def libres(self):
        raise NotImplementedError  # TODO


class CachePaginada:
    def __init__(self, n_bloques, tam_bloque, dim):
        self.tam = tam_bloque
        self.K = np.zeros((n_bloques, tam_bloque, dim))
        self.V = np.zeros((n_bloques, tam_bloque, dim))
        self.asignador = AsignadorBloques(n_bloques)
        self.tablas = {}   # seq -> lista de ids de bloque
        self.longitud = {}

    def agregar(self, seq, k, v):
        raise NotImplementedError  # TODO

    def obtener(self, seq):
        raise NotImplementedError  # TODO

    def liberar(self, seq):
        raise NotImplementedError  # TODO

    def desperdicio(self, seq):
        raise NotImplementedError  # TODO
