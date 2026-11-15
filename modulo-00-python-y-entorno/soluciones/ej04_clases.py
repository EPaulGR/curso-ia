"""Ejercicio 04 — Clases y dataclasses. Implementa un vector 2D inmutable."""
from dataclasses import dataclass
import math


@dataclass(frozen=True)
class Vector2:
    x: float
    y: float

    def __add__(self, o):
        """Suma de vectores."""
        return Vector2(self.x + o.x, self.y + o.y)

    def __mul__(self, k):
        """Producto por escalar."""
        return Vector2(self.x * k, self.y * k)

    def punto(self, o) -> float:
        """Producto punto."""
        return self.x * o.x + self.y * o.y

    def norma(self) -> float:
        """Norma euclidiana."""
        return math.hypot(self.x, self.y)

    def normalizar(self):
        """Vector unitario en la misma dirección (ValueError si es el vector cero)."""
        n = self.norma()
        if n == 0:
            raise ValueError("vector cero")
        return Vector2(self.x / n, self.y / n)
