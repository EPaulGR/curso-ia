# Módulo 12 — Aprendizaje no supervisado y reducción de dimensionalidad

**Fase 3 · Machine Learning** · Duración: 3 semanas (~35 h) · Prerrequisitos: módulos 01, 02, 11

## Objetivos
- Implementar desde cero K-means, k-means++, PCA, GMM con EM, DBSCAN y clustering jerárquico.
- Elegir número de clusters (codo, silueta, BIC) y evaluar sin etiquetas.
- Entender cuándo usar PCA, t-SNE o UMAP y sus trampas de interpretación.

## Temario
1. Problema no supervisado: clustering, densidad, reducción, detección de anomalías.
2. K-means: función objetivo, Lloyd, convergencia a mínimos locales, k-means++.
3. Modelos de mezcla y algoritmo EM (E-step, M-step, ELBO).
4. Clustering por densidad: DBSCAN, HDBSCAN.
5. Clustering jerárquico: enlaces simple, completo, promedio, Ward; dendrogramas.
6. PCA: varianza, SVD, reconstrucción; PCA kernel.
7. Manifold learning: t-SNE, UMAP; visualización de embeddings.
8. Evaluación: inercia, silueta, Davies–Bouldin, ARI/NMI cuando hay etiquetas.
9. Detección de anomalías: Isolation Forest, LOF.

## Lecturas
- James et al., *ISLP*, cap. 12 (Unsupervised Learning).
- Hastie et al., *ESL*, cap. 14.1–14.5.
- Bishop, *PRML* cap. 9 (Mixture Models and EM) y 12 (PCA); o Bishop & Bishop 2024 cap. 15–16.
- Géron, *Hands-On ML*, cap. 8 y 9.
- Deisenroth, *MML*, cap. 10 (PCA) y 11 (GMM).
- Paper: van der Maaten & Hinton (2008), *Visualizing Data using t-SNE*.

## Ejercicios
| # | Archivo | Tema |
|---|---|---|
| 01 | ej01_kmeans.py | K-means (Lloyd) |
| 02 | ej02_kmeanspp.py | Inicialización k-means++ |
| 03 | ej03_pca.py | PCA con SVD y reconstrucción |
| 04 | ej04_gmm_em.py | GMM 1D con EM |
| 05 | ej05_dbscan.py | DBSCAN |
| 06 | ej06_jerarquico.py | Aglomerativo (enlace simple) |
| 07 | ej07_silhouette.py | Silueta (se compara contra scikit-learn) |

```bash
pytest modulo-12-no-supervisado
```

## Evaluación
Ejercicios 30 % · [Quiz](evaluacion/quiz.md) 30 % · [Proyecto](proyecto/README.md) 30 % · Lecturas 10 %. Aprobado ≥ 8.
