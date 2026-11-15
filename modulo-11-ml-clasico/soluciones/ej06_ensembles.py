"""Ejercicio 06 — Métodos de ensamble: AdaBoost con tocones y random forest con scikit-learn
(ISLP cap. 8; Hastie et al. cap. 10; Géron cap. 7).

AdaBoost (etiquetas y ∈ {−1, +1}):
    w_i = 1/n
    para m = 1..M:
        h_m ← tocón (árbol de 1 nivel) que minimiza el error ponderado ε_m
        α_m = ½ ln((1 − ε_m)/ε_m)
        w_i ← w_i · exp(−α_m y_i h_m(x_i));  normalizar
    H(x) = sign(Σ α_m h_m(x))
"""
import numpy as np


def mejor_tocon(X, y, w):
    """Devuelve (j, umbral, polaridad, error) del tocón h(x) = polaridad si x_j ≤ umbral, si no −polaridad."""
    mejor = (0, 0.0, 1, np.inf)
    for j in range(X.shape[1]):
        vals = np.unique(X[:, j])
        umbrales = np.concatenate([[vals[0] - 1], (vals[:-1] + vals[1:]) / 2])
        for u in umbrales:
            for pol in (1, -1):
                pred = np.where(X[:, j] <= u, pol, -pol)
                e = w[pred != y].sum()
                if e < mejor[3]:
                    mejor = (j, float(u), pol, float(e))
    return mejor


class AdaBoost:
    def __init__(self, n_estimadores=50):
        """DADO."""
        self.n_estimadores = n_estimadores

    def fit(self, X, y):
        """y en {−1,+1}. Guarda self.tocones = [(j, u, pol, alfa), ...]."""
        X = np.asarray(X, float)
        w = np.full(len(y), 1 / len(y))
        self.tocones = []
        for _ in range(self.n_estimadores):
            j, u, pol, e = mejor_tocon(X, y, w)
            e = np.clip(e, 1e-10, 1 - 1e-10)
            a = 0.5 * np.log((1 - e) / e)
            pred = np.where(X[:, j] <= u, pol, -pol)
            w = w * np.exp(-a * y * pred)
            w /= w.sum()
            self.tocones.append((j, u, pol, a))
        return self

    def decision(self, X):
        """Σ α_m h_m(x)."""
        X = np.asarray(X, float)
        return sum(a * np.where(X[:, j] <= u, p, -p) for j, u, p, a in self.tocones)

    def predict(self, X):
        """sign de decision (0 → +1)."""
        return np.where(self.decision(X) >= 0, 1, -1)


def comparar_sklearn(X, y, semilla=0):
    """Con scikit-learn, devuelve dict nombre → exactitud media en 5-fold CV para:
    'arbol' (DecisionTreeClassifier), 'bosque' (RandomForestClassifier, 200 árboles),
    'gboost' (GradientBoostingClassifier). Todos con random_state=semilla."""
    from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
    from sklearn.model_selection import cross_val_score
    from sklearn.tree import DecisionTreeClassifier
    modelos = {"arbol": DecisionTreeClassifier(random_state=semilla),
               "bosque": RandomForestClassifier(n_estimators=200, random_state=semilla),
               "gboost": GradientBoostingClassifier(random_state=semilla)}
    return {k: float(cross_val_score(m, X, y, cv=5).mean()) for k, m in modelos.items()}
