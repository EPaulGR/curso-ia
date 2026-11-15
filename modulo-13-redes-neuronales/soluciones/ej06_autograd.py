"""Ej 06 — Mini motor de autodiferenciación escalar (estilo micrograd)."""
import math


class Valor:
    """Nodo de un grafo computacional con gradiente."""

    def __init__(self, dato, hijos=(), op=""):
        self.dato = float(dato)
        self.grad = 0.0
        self._hijos = hijos
        self._back = lambda: None

    def __add__(self, o):
        """Suma."""
        o = o if isinstance(o, Valor) else Valor(o)
        r = Valor(self.dato + o.dato, (self, o))

        def b():
            self.grad += r.grad
            o.grad += r.grad
        r._back = b
        return r

    def __mul__(self, o):
        """Producto."""
        o = o if isinstance(o, Valor) else Valor(o)
        r = Valor(self.dato * o.dato, (self, o))

        def b():
            self.grad += o.dato * r.grad
            o.grad += self.dato * r.grad
        r._back = b
        return r

    def __pow__(self, k):
        """Potencia con exponente numérico."""
        r = Valor(self.dato ** k, (self,))

        def b():
            self.grad += k * self.dato ** (k - 1) * r.grad
        r._back = b
        return r

    def tanh(self):
        """Tangente hiperbólica."""
        t = math.tanh(self.dato)
        r = Valor(t, (self,))

        def b():
            self.grad += (1 - t ** 2) * r.grad
        r._back = b
        return r

    def exp(self):
        """Exponencial."""
        e = math.exp(self.dato)
        r = Valor(e, (self,))

        def b():
            self.grad += e * r.grad
        r._back = b
        return r

    def backward(self):
        """Orden topológico y propagación hacia atrás desde este nodo."""
        orden, vistos = [], set()

        def topo(v):
            if id(v) not in vistos:
                vistos.add(id(v))
                for h in v._hijos:
                    topo(h)
                orden.append(v)
        topo(self)
        self.grad = 1.0
        for v in reversed(orden):
            v._back()

    def __radd__(self, o):
        """o + self."""
        return self + o

    def __rmul__(self, o):
        """o * self."""
        return self * o

    def __neg__(self):
        """-self."""
        return self * -1

    def __sub__(self, o):
        """self - o."""
        return self + (-o if isinstance(o, Valor) else -o)

    def __truediv__(self, o):
        """self / o."""
        return self * (o ** -1 if isinstance(o, Valor) else 1 / o)
