"""Ejercicio 07 — pandas."""
import pandas as pd

def limpiar(df: pd.DataFrame) -> pd.DataFrame:
    """Elimina filas duplicadas y rellena NaN numéricos con la mediana de su columna."""
    raise NotImplementedError  # TODO

def resumen_por_grupo(df: pd.DataFrame, grupo: str, valor: str) -> pd.DataFrame:
    """DataFrame indexado por `grupo` con columnas 'media' y 'conteo' de `valor`, ordenado por media desc."""
    raise NotImplementedError  # TODO
