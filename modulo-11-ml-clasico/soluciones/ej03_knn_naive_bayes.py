"""Ejercicio 03 — k vecinos más cercanos y Naive Bayes gaussiano.

kNN: predecir por voto mayoritario de los k más cercanos (distancia euclidiana);
desempate: la clase con menor etiqueta.
NB gaussiano: P(c|x) ∝ P(c) Π_j N(x_j; μ_cj, σ²_cj). Trabaja en log para estabilidad;
añade var_suavizado·max(var) a las varianzas (como scikit-learn, 1e-9).
"""
import numpy as np


def knn_predecir(X_tr, y_tr, X_te, k=3):
    """Array de predicciones para X_te."""
    X_tr, X_te = np.asarray(X_tr, float), np.asarray(X_te, float)
    d = ((X_te[:, None, :] - X_tr[None, :, :]) ** 2).sum(-1)
    idx = np.argsort(d, axis=1, kind="stable")[:, :k]
    pred = []
    for fila in y_tr[idx]:
        vals, cuentas = np.unique(fila, return_counts=True)
        pred.append(vals[np.argmax(cuentas)])
    return np.array(pred)


class NaiveBayesGaussiano:
    def __init__(self, var_suavizado=1e-9):
        """DADO."""
        self.var_suavizado = var_suavizado

    def fit(self, X, y):
        """Estima clases_, log_prior_, media_ (C, d) y var_ (C, d). Devuelve self."""
        X = np.asarray(X, float)
        self.clases_ = np.unique(y)
        eps = self.var_suavizado * X.var(axis=0).max()
        self.media_ = np.array([X[y == c].mean(0) for c in self.clases_])
        self.var_ = np.array([X[y == c].var(0) for c in self.clases_]) + eps
        self.log_prior_ = np.log(np.array([np.mean(y == c) for c in self.clases_]))
        return self

    def log_verosimilitud_conjunta(self, X):
        """Array (n, C) con log P(c) + Σ_j log N(x_j | c)."""
        X = np.asarray(X, float)
        ll = -0.5 * (np.log(2 * np.pi * self.var_)[None] + (X[:, None, :] - self.media_[None]) ** 2 / self.var_[None]).sum(-1)
        return ll + self.log_prior_

    def predict(self, X):
        """Clase de mayor posterior."""
        return self.clases_[np.argmax(self.log_verosimilitud_conjunta(X), axis=1)]
