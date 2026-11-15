# Proyecto — Segmentación y visualización de un dataset real

Usa un dataset sin etiquetas (por ejemplo *Online Retail* de UCI o *Mall Customers*), o MNIST ignorando las etiquetas.

## Entregables
1. Notebook con limpieza, escalado y análisis exploratorio.
2. PCA: varianza explicada acumulada y proyección 2D.
3. Comparación de K-means (tus implementaciones), GMM, DBSCAN y jerárquico con silueta, Davies–Bouldin y (si hay etiquetas) ARI.
4. Visualización con t-SNE y UMAP; discusión de lo que **no** se puede concluir de ellas.
5. Informe de 1–2 páginas con la interpretación de los segmentos.

## Rúbrica (100 pts)
| Criterio | Pts |
|---|---|
| Preprocesamiento correcto y justificado | 15 |
| Uso de implementaciones propias + comparación con scikit-learn | 20 |
| Selección de k / hiperparámetros con evidencia | 20 |
| Calidad de visualizaciones | 15 |
| Interpretación y limitaciones | 20 |
| Código limpio y reproducible (semillas, requirements) | 10 |
