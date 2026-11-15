"""Ejercicio 07 — Máquinas de vectores de soporte y pipelines (ISLP cap. 9; Géron cap. 5).

1) SVM lineal con Pegasos (subgradiente estocástico de la pérdida bisagra), y ∈ {−1,+1}:
    min_w (λ/2)‖w‖² + (1/n) Σ max(0, 1 − y_i wᵀx_i)
    en el paso t (η_t = 1/(λt)), con un ejemplo i aleatorio:
        si y_i wᵀx_i < 1:  w ← (1 − η_t λ) w + η_t y_i x_i
        si no:             w ← (1 − η_t λ) w
   (el sesgo se maneja añadiendo una característica constante 1)
2) Pipeline de scikit-learn: StandardScaler + SVC(RBF) con GridSearchCV sobre C y gamma.
"""
import numpy as np


def pegasos(X, y, lam=0.01, iteraciones=20000, semilla=0):
    """Devuelve w de tamaño d+1 (último componente = sesgo)."""
    rng = np.random.default_rng(semilla)
    Xb = np.hstack([np.asarray(X, float), np.ones((len(X), 1))])
    w = np.zeros(Xb.shape[1])
    for t in range(1, iteraciones + 1):
        i = rng.integers(len(y))
        eta = 1 / (lam * t)
        if y[i] * (Xb[i] @ w) < 1:
            w = (1 - eta * lam) * w + eta * y[i] * Xb[i]
        else:
            w = (1 - eta * lam) * w
    return w


def predecir_svm(w, X):
    """sign(wᵀ[x, 1]) con 0 → +1."""
    Xb = np.hstack([np.asarray(X, float), np.ones((len(X), 1))])
    return np.where(Xb @ w >= 0, 1, -1)


def busqueda_svm_rbf(X, y):
    """Devuelve (mejores_parametros: dict, mejor_puntaje_cv: float) de GridSearchCV(cv=5) sobre
    C ∈ {0.1, 1, 10, 100} y gamma ∈ {'scale', 0.01, 0.1, 1} con un Pipeline escalado+SVC."""
    from sklearn.model_selection import GridSearchCV
    from sklearn.pipeline import Pipeline
    from sklearn.preprocessing import StandardScaler
    from sklearn.svm import SVC
    pipe = Pipeline([("esc", StandardScaler()), ("svc", SVC(kernel="rbf"))])
    g = GridSearchCV(pipe, {"svc__C": [0.1, 1, 10, 100], "svc__gamma": ["scale", 0.01, 0.1, 1]}, cv=5)
    g.fit(X, y)
    return g.best_params_, float(g.best_score_)
