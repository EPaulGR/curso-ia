# Teoría — Aprendizaje no supervisado

## 1. ¿Qué es?
Sin etiquetas `y`: buscamos estructura en `X`. Tareas: **agrupar** (clustering), **comprimir** (reducción de dimensionalidad), **estimar densidad** y **detectar anomalías**.

## 2. K-means
Minimiza la inercia  J = Σᵢ ‖xᵢ − μ_{c(i)}‖².
Algoritmo de Lloyd: (1) asignar cada punto al centroide más cercano; (2) recalcular centroides como medias. Cada paso no aumenta J → converge, pero a un **mínimo local**. Por eso se reinicia varias veces (`n_init`) y se usa **k-means++**: el siguiente centroide se elige con probabilidad ∝ D(x)², lo que da una aproximación O(log k) al óptimo esperado.
Supuestos implícitos: clusters convexos, de tamaño y varianza parecidos. Falla con lunas, anillos o densidades distintas. Escala las variables antes.

## 3. Mezclas de gaussianas y EM
p(x) = Σₖ πₖ 𝒩(x | μₖ, Σₖ). La verosimilitud no tiene forma cerrada por la suma dentro del log. EM introduce variables latentes z:
- **E-step**: responsabilidades r_{ik} = πₖ𝒩(xᵢ|μₖ,Σₖ) / Σⱼ πⱼ𝒩(xᵢ|μⱼ,Σⱼ).
- **M-step**: Nₖ = Σᵢ r_{ik}; πₖ = Nₖ/N; μₖ = Σᵢ r_{ik}xᵢ / Nₖ; Σₖ = Σᵢ r_{ik}(xᵢ−μₖ)(xᵢ−μₖ)ᵀ / Nₖ.
EM maximiza una cota inferior (ELBO) y la log-verosimilitud nunca baja. K-means es el límite de GMM con varianzas iguales → 0 (asignación "dura"). Elegir k con BIC = −2 log L + p log N.

## 4. DBSCAN
Parámetros ε y minPts. Punto **núcleo**: ≥ minPts vecinos en radio ε. Los clusters son componentes conexas de núcleos alcanzables por densidad; los puntos no alcanzables son **ruido**. Ventajas: formas arbitrarias, no pide k, detecta outliers. Desventaja: una sola densidad global (HDBSCAN lo resuelve). Elige ε con la gráfica de k-distancias.

## 5. Jerárquico aglomerativo
Empieza con n clusters y une los dos más cercanos. Enlace **simple** (mínimo; produce "cadenas"), **completo** (máximo), **promedio**, **Ward** (minimiza aumento de varianza; el más usado). El dendrograma permite cortar a cualquier k. Costo O(n²) memoria, O(n³) ingenuo.

## 6. PCA
Busca direcciones ortogonales de máxima varianza. Con Xc centrada, SVD: Xc = UΣVᵀ. Las componentes son filas de Vᵀ, la varianza de cada una σᵢ²/(n−1). Proyección Z = XcVₖ; reconstrucción X̂ = ZVₖᵀ + μ. Equivale a minimizar el error de reconstrucción cuadrático. **Siempre estandariza** si las unidades difieren. PCA es lineal; kernel PCA y autoencoders (módulo 17) son la versión no lineal.

## 7. t-SNE y UMAP
Preservan vecindades locales para **visualizar** en 2D. t-SNE: distribuciones de similitud gaussianas en alta dimensión y t-Student en baja, minimiza KL. Hiperparámetro clave: perplejidad (5–50). Cuidado: las distancias entre clusters y sus tamaños **no** tienen significado. UMAP es más rápido y preserva algo más de estructura global.

## 8. Evaluación
- Sin etiquetas: inercia (método del codo), **silueta** s(i) = (b−a)/max(a,b) ∈ [−1,1], Davies–Bouldin.
- Con etiquetas de referencia: ARI, NMI (invariantes a permutar etiquetas).

## 9. Anomalías
Isolation Forest: las anomalías se aíslan con menos cortes aleatorios. LOF: compara densidad local con la de los vecinos.

## 10. En Mac
scikit-learn corre en CPU y es muy rápido en Apple Silicon. Para millones de puntos usa `MiniBatchKMeans` o implementa K-means en PyTorch con `device="mps"`.
