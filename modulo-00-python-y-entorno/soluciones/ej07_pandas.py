"""Ejercicio 07 — pandas."""
import pandas as pd


def limpiar(df: pd.DataFrame) -> pd.DataFrame:
    """Elimina filas duplicadas y rellena NaN numéricos con la mediana de su columna."""
    df = df.drop_duplicates().copy()
    num = df.select_dtypes("number").columns
    df[num] = df[num].fillna(df[num].median())
    return df


def resumen_por_grupo(df: pd.DataFrame, grupo: str, valor: str) -> pd.DataFrame:
    """DataFrame indexado por `grupo` con columnas 'media' y 'conteo' de `valor`, ordenado por media desc."""
    r = df.groupby(grupo)[valor].agg(media="mean", conteo="count")
    return r.sort_values("media", ascending=False)
