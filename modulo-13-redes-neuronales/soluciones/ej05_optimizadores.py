"""Ej 05 — SGD con momentum y Adam implementados a mano."""
import numpy as np


class Momentum:
    """v = β·v + g ; θ -= lr·v"""

    def __init__(self, lr=0.01, beta=0.9):
        self.lr, self.beta, self.v = lr, beta, None

    def paso(self, theta, g):
        """Devuelve theta actualizado."""
        if self.v is None:
            self.v = np.zeros_like(theta)
        self.v = self.beta * self.v + g
        return theta - self.lr * self.v


class Adam:
    """Adam (Kingma & Ba, 2015) con corrección de sesgo."""

    def __init__(self, lr=0.001, b1=0.9, b2=0.999, eps=1e-8):
        self.lr, self.b1, self.b2, self.eps = lr, b1, b2, eps
        self.m = self.v = None
        self.t = 0

    def paso(self, theta, g):
        """Devuelve theta actualizado."""
        if self.m is None:
            self.m, self.v = np.zeros_like(theta), np.zeros_like(theta)
        self.t += 1
        self.m = self.b1 * self.m + (1 - self.b1) * g
        self.v = self.b2 * self.v + (1 - self.b2) * g ** 2
        mh = self.m / (1 - self.b1 ** self.t)
        vh = self.v / (1 - self.b2 ** self.t)
        return theta - self.lr * mh / (np.sqrt(vh) + self.eps)


def minimizar_rosenbrock(opt, pasos=5000):
    """Minimiza f(x,y)=(1-x)^2+100(y-x^2)^2 desde (-1.5, 2). Devuelve el punto final."""
    th = np.array([-1.5, 2.0])
    for _ in range(pasos):
        x, y = th
        g = np.array([-2 * (1 - x) - 400 * x * (y - x ** 2), 200 * (y - x ** 2)])
        th = opt.paso(th, g)
    return th
