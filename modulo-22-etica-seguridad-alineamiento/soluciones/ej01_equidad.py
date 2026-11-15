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
    y_pred, grupo = np.asarray(y_pred), np.asarray(grupo)
    return {g: float(y_pred[grupo == g].mean()) for g in np.unique(grupo)}


def paridad_demografica(y_pred, grupo):
    t = tasa_positivos(y_pred, grupo).values()
    return max(t) - min(t)


def impacto_dispar(y_pred, grupo):
    t = tasa_positivos(y_pred, grupo).values()
    return min(t) / max(t) if max(t) else 1.0


def _tasa_cond(y_true, y_pred, grupo, clase):
    y_true, y_pred, grupo = map(np.asarray, (y_true, y_pred, grupo))
    return [y_pred[(grupo == g) & (y_true == clase)].mean() for g in np.unique(grupo)]


def igualdad_oportunidades(y_true, y_pred, grupo):
    t = _tasa_cond(y_true, y_pred, grupo, 1)
    return float(max(t) - min(t))


def odds_igualados(y_true, y_pred, grupo):
    fpr = _tasa_cond(y_true, y_pred, grupo, 0)
    return max(igualdad_oportunidades(y_true, y_pred, grupo), float(max(fpr) - min(fpr)))
