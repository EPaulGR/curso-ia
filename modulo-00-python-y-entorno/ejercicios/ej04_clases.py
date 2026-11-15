"""Ejercicio 04 — Clases y dataclasses. Implementa un vector 2D inmutable."""
from dataclasses import dataclass
import math

@dataclass(frozen=True)
class Vector2:
    x: float
    y: float

    def __add__(self, o):
        """Suma de vectores."""
        raise NotImplementedError  # TODO

    def __mul__(self, k):
        """Producto por escalar."""
        raise NotImplementedError  # TODO

    def punto(self, o) -> float:
        """Producto punto."""
        raise NotImplementedError  # TODO

    def norma(self) -> float:
        """Norma euclidiana."""
        raise NotImplementedError  # TODO

    def normalizar(self):
        """Vector unitario en la misma dirección (ValueError si es el vector cero)."""
        raise NotImplementedError  # TODO
