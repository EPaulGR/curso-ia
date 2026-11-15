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
        if not self._libres:
            raise MemoryError("sin bloques libres")
        return self._libres.pop()

    def liberar(self, id_):
        self._libres.append(id_)

    def libres(self):
        return len(self._libres)


class CachePaginada:
    def __init__(self, n_bloques, tam_bloque, dim):
        self.tam = tam_bloque
        self.K = np.zeros((n_bloques, tam_bloque, dim))
        self.V = np.zeros((n_bloques, tam_bloque, dim))
        self.asignador = AsignadorBloques(n_bloques)
        self.tablas = {}   # seq -> lista de ids de bloque
        self.longitud = {}

    def agregar(self, seq, k, v):
        tabla = self.tablas.setdefault(seq, [])
        n = self.longitud.get(seq, 0)
        if n % self.tam == 0:
            tabla.append(self.asignador.asignar())
        b, off = tabla[n // self.tam], n % self.tam
        self.K[b, off], self.V[b, off] = k, v
        self.longitud[seq] = n + 1

    def obtener(self, seq):
        n = self.longitud[seq]
        tabla = self.tablas[seq]
        K = np.concatenate([self.K[b] for b in tabla])[:n]
        V = np.concatenate([self.V[b] for b in tabla])[:n]
        return K, V

    def liberar(self, seq):
        for b in self.tablas.pop(seq, []):
            self.asignador.liberar(b)
        self.longitud.pop(seq, None)

    def desperdicio(self, seq):
        return len(self.tablas[seq]) * self.tam - self.longitud[seq]
