"""Ejercicio 05 — Métricas y validación cruzada (Géron cap. 3; ISLP cap. 5).

Clasificación binaria con etiquetas {0,1}:
    precisión = TP/(TP+FP), exhaustividad (recall) = TP/(TP+FN), F1 = 2PR/(P+R)
ROC: TPR vs FPR al variar el umbral; AUC = P(score(+) > score(−)) (empates cuentan 1/2).
k-fold: partir índices (barajados con semilla) en k bloques casi iguales.
"""
import numpy as np


def matriz_confusion(y, y_pred):
    """[[TN, FP], [FN, TP]] como array 2×2 de enteros."""
    raise NotImplementedError  # TODO: implementa esta función


def precision_recall_f1(y, y_pred):
    """Tupla (precisión, recall, f1); 0.0 si el denominador es 0."""
    raise NotImplementedError  # TODO: implementa esta función


def auc(y, scores):
    """Área bajo la curva ROC vía la estadística de Mann–Whitney."""
    raise NotImplementedError  # TODO: implementa esta función


def k_fold_indices(n, k, semilla=0):
    """Lista de k tuplas (idx_entrenamiento, idx_validacion)."""
    raise NotImplementedError  # TODO: implementa esta función


def validacion_cruzada(crear_modelo, X, y, k=5, semilla=0):
    """crear_modelo() devuelve un objeto con fit/predict. Devuelve array de exactitudes por pliegue."""
    raise NotImplementedError  # TODO: implementa esta función
