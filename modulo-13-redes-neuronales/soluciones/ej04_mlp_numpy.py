"""Ej 04 — MLP de una capa oculta con backprop manual en NumPy (clasificación multiclase)."""
import numpy as np


class MLP:
    """x → Linear(d,h) → ReLU → Linear(h,c) → softmax + entropía cruzada."""

    def __init__(self, d, h, c, semilla=0):
        """Inicialización He para W1, Xavier para W2; sesgos en cero."""
        rng = np.random.default_rng(semilla)
        self.W1 = rng.normal(0, np.sqrt(2 / d), (d, h))
        self.b1 = np.zeros(h)
        self.W2 = rng.normal(0, np.sqrt(1 / h), (h, c))
        self.b2 = np.zeros(c)

    def forward(self, X):
        """Devuelve logits (n, c) y guarda la caché necesaria para backward."""
        self.X = X
        self.z1 = X @ self.W1 + self.b1
        self.a1 = np.maximum(0, self.z1)
        return self.a1 @ self.W2 + self.b2

    def perdida(self, logits, y):
        """Entropía cruzada media con etiquetas enteras y; guarda probabilidades."""
        z = logits - logits.max(1, keepdims=True)
        self.p = np.exp(z) / np.exp(z).sum(1, keepdims=True)
        self.y = y
        return float(-np.log(self.p[np.arange(len(y)), y] + 1e-12).mean())

    def backward(self):
        """Calcula y devuelve dict de gradientes {'W1','b1','W2','b2'}."""
        n = len(self.y)
        dz2 = self.p.copy()
        dz2[np.arange(n), self.y] -= 1
        dz2 /= n
        g = {"W2": self.a1.T @ dz2, "b2": dz2.sum(0)}
        da1 = dz2 @ self.W2.T
        dz1 = da1 * (self.z1 > 0)
        g["W1"] = self.X.T @ dz1
        g["b1"] = dz1.sum(0)
        return g

    def paso(self, g, lr):
        """Descenso de gradiente sobre los parámetros."""
        for k, v in g.items():
            setattr(self, k, getattr(self, k) - lr * v)


def entrenar(X, y, h=32, epocas=300, lr=0.5, semilla=0):
    """Entrena un MLP con gradiente completo; devuelve (modelo, historial_de_perdidas)."""
    m = MLP(X.shape[1], h, int(y.max()) + 1, semilla)
    hist = []
    for _ in range(epocas):
        hist.append(m.perdida(m.forward(X), y))
        m.paso(m.backward(), lr)
    return m, hist
