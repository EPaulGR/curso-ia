"""Ejercicio 05 — Métricas y validación cruzada (Géron cap. 3; ISLP cap. 5).

Clasificación binaria con etiquetas {0,1}:
    precisión = TP/(TP+FP), exhaustividad (recall) = TP/(TP+FN), F1 = 2PR/(P+R)
ROC: TPR vs FPR al variar el umbral; AUC = P(score(+) > score(−)) (empates cuentan 1/2).
k-fold: partir índices (barajados con semilla) en k bloques casi iguales.
"""
import numpy as np


def matriz_confusion(y, y_pred):
    """[[TN, FP], [FN, TP]] como array 2×2 de enteros."""
    y, y_pred = np.asarray(y), np.asarray(y_pred)
    return np.array([[np.sum((y == 0) & (y_pred == 0)), np.sum((y == 0) & (y_pred == 1))],
                     [np.sum((y == 1) & (y_pred == 0)), np.sum((y == 1) & (y_pred == 1))]])


def precision_recall_f1(y, y_pred):
    """Tupla (precisión, recall, f1); 0.0 si el denominador es 0."""
    (_, fp), (fn, tp) = matriz_confusion(y, y_pred)
    p = tp / (tp + fp) if tp + fp else 0.0
    r = tp / (tp + fn) if tp + fn else 0.0
    f = 2 * p * r / (p + r) if p + r else 0.0
    return float(p), float(r), float(f)


def auc(y, scores):
    """Área bajo la curva ROC vía la estadística de Mann–Whitney."""
    y, s = np.asarray(y), np.asarray(scores, float)
    pos, neg = s[y == 1], s[y == 0]
    comp = (pos[:, None] > neg[None, :]).sum() + 0.5 * (pos[:, None] == neg[None, :]).sum()
    return float(comp / (len(pos) * len(neg)))


def k_fold_indices(n, k, semilla=0):
    """Lista de k tuplas (idx_entrenamiento, idx_validacion)."""
    idx = np.random.default_rng(semilla).permutation(n)
    bloques = np.array_split(idx, k)
    return [(np.concatenate([b for j, b in enumerate(bloques) if j != i]), bloques[i]) for i in range(k)]


def validacion_cruzada(crear_modelo, X, y, k=5, semilla=0):
    """crear_modelo() devuelve un objeto con fit/predict. Devuelve array de exactitudes por pliegue."""
    X, y = np.asarray(X), np.asarray(y)
    acc = []
    for tr, va in k_fold_indices(len(y), k, semilla):
        m = crear_modelo().fit(X[tr], y[tr])
        acc.append(np.mean(m.predict(X[va]) == y[va]))
    return np.array(acc)
