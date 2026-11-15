"""Ejercicio 1 — Métricas de equidad (fairness) para clasificación binaria.

Arrays y_true, y_pred (0/1) y grupo (valores categóricos).
- `tasa_positivos(y_pred, grupo)`: dict grupo -> P(ŷ=1 | grupo).
- `paridad_demografica(y_pred, grupo)`: max - min de las tasas de positivos.
- `impacto_dispar(y_pred, grupo)`: min / max de tasas (regla del 80 %: < 0.8 es alerta).
- `igualdad_oportunidades(y_true, y_pred, grupo)`: max - min del TPR por grupo.
- `odds_igualados(y_true, y_pred, grupo)`: máximo entre la brecha de TPR y la de FPR.
Barocas, Hardt & Narayanan, *Fairness and Machine Learning* (fairmlbook.org).
"""
import numpy as np


def tasa_positivos(y_pred, grupo):
    raise NotImplementedError  # TODO: implementa esta función


def paridad_demografica(y_pred, grupo):
    raise NotImplementedError  # TODO: implementa esta función


def impacto_dispar(y_pred, grupo):
    raise NotImplementedError  # TODO: implementa esta función


def _tasa_cond(y_true, y_pred, grupo, clase):
    y_true, y_pred, grupo = map(np.asarray, (y_true, y_pred, grupo))
    return [y_pred[(grupo == g) & (y_true == clase)].mean() for g in np.unique(grupo)]


def igualdad_oportunidades(y_true, y_pred, grupo):
    raise NotImplementedError  # TODO: implementa esta función


def odds_igualados(y_true, y_pred, grupo):
    raise NotImplementedError  # TODO: implementa esta función
