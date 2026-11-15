# Proyecto — Análisis de sentimiento y generación de texto en español

## Parte A: Clasificación
Dataset: reseñas en español (por ejemplo *Amazon Reviews Multi* es, o *MuchoCine*).
1. Línea base TF-IDF (tu implementación) + regresión logística.
2. Embeddings propios (tu SGNS) o preentrenados + promedio + clasificador.
3. LSTM bidireccional en MPS con tu tokenizador BPE.
4. Tabla comparativa con F1 macro y análisis de errores (negaciones, ironía).

## Parte B: Modelo de lenguaje
1. Modelo de trigramas con Kneser-Ney sobre un libro de dominio público en español (Proyecto Gutenberg).
2. LSTM de caracteres que genere texto; compara perplejidades.

## Rúbrica (100 pts)
| Criterio | Pts |
|---|---|
| Tres clasificadores comparados correctamente | 25 |
| Uso de componentes propios (BPE, TF-IDF, SGNS) | 20 |
| Modelos de lenguaje y perplejidad bien calculada | 20 |
| Análisis de errores lingüísticos | 15 |
| Reporte y visualizaciones (p. ej. t-SNE de embeddings) | 10 |
| Reproducibilidad | 10 |
