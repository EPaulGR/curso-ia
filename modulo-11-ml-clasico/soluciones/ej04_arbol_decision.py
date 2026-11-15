"""Ejercicio 04 — Árboles de decisión (CART para clasificación) (ISLP cap. 8; AIMA 19.3).

Impureza de Gini:  G = 1 − Σ_k p_k²        Entropía: H = −Σ_k p_k log2 p_k
Ganancia: impureza(padre) − Σ (n_hijo/n) impureza(hijo)
Divisiones binarias x_j ≤ umbral con umbrales = puntos medios entre valores únicos
consecutivos. Se detiene con profundidad_max, min_muestras o nodo puro.
"""
import numpy as np


def gini(y):
    """Impureza de Gini de un vector de etiquetas."""
    _, c = np.unique(y, return_counts=True)
    p = c / c.sum()
    return float(1 - np.sum(p ** 2))


def entropia(y):
    """Entropía en bits."""
    _, c = np.unique(y, return_counts=True)
    p = c / c.sum()
    return float(-np.sum(p * np.log2(p)))


def mejor_division(X, y, criterio=gini):
    """(j, umbral, ganancia) de la mejor división; (None, None, 0.0) si ninguna mejora."""
    padre = criterio(y)
    mejor = (None, None, 0.0)
    n = len(y)
    for j in range(X.shape[1]):
        vals = np.unique(X[:, j])
        for u in (vals[:-1] + vals[1:]) / 2:
            izq = X[:, j] <= u
            g = padre - (izq.sum() / n * criterio(y[izq]) + (~izq).sum() / n * criterio(y[~izq]))
            if g > mejor[2] + 1e-12:
                mejor = (j, float(u), float(g))
    return mejor


class ArbolDecision:
    def __init__(self, profundidad_max=None, min_muestras=2, criterio="gini"):
        """DADO."""
        self.profundidad_max = profundidad_max
        self.min_muestras = min_muestras
        self.criterio = gini if criterio == "gini" else entropia

    def fit(self, X, y):
        """Construye self.raiz: hoja = {'clase': c}; interno = {'j','umbral','izq','der'}."""
        X = np.asarray(X, float)
        y = np.asarray(y)

        def construir(idx, d):
            vals, c = np.unique(y[idx], return_counts=True)
            hoja = {"clase": vals[np.argmax(c)]}
            if len(vals) == 1 or len(idx) < self.min_muestras or (self.profundidad_max is not None and d >= self.profundidad_max):
                return hoja
            j, u, g = mejor_division(X[idx], y[idx], self.criterio)
            if j is None:
                return hoja
            m = X[idx, j] <= u
            return {"j": j, "umbral": u, "izq": construir(idx[m], d + 1), "der": construir(idx[~m], d + 1)}

        self.raiz = construir(np.arange(len(y)), 0)
        return self

    def predict(self, X):
        """Predicciones recorriendo el árbol."""
        out = []
        for x in np.asarray(X, float):
            n = self.raiz
            while "clase" not in n:
                n = n["izq"] if x[n["j"]] <= n["umbral"] else n["der"]
            out.append(n["clase"])
        return np.array(out)

    def profundidad(self):
        """Profundidad del árbol (una hoja sola = 0)."""
        def p(n):
            return 0 if "clase" in n else 1 + max(p(n["izq"]), p(n["der"]))
        return p(self.raiz)
