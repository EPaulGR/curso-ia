# Respuestas — Módulo 12

1. J = Σᵢ ‖xᵢ − μ_{c(i)}‖² (suma de distancias cuadradas al centroide asignado).
2. Cada paso de Lloyd no incrementa J y hay finitas particiones → converge; pero J no es convexa, así que puede quedar en un mínimo local.
3. Elige el primer centro al azar y cada siguiente con probabilidad ∝ D(x)²; separa los centros iniciales y garantiza aproximación O(log k) esperada.
4. Clusters no convexos (lunas, anillos) → DBSCAN/espectral; densidades o tamaños muy distintos → GMM/HDBSCAN.
5. E: responsabilidades r_{ik} (probabilidad posterior de cada componente). M: re-estimar π, μ, Σ ponderados por r.
6. K-means es GMM con covarianzas σ²I iguales y σ→0 (asignaciones duras).
7. Núcleo: ≥ minPts vecinos en ε. Frontera: dentro de ε de un núcleo sin serlo. Ruido: ninguno de los anteriores.
8. Gráfica ordenada de distancia al k-ésimo vecino (k = minPts) y tomar el "codo".
9. Simple usa la distancia mínima y produce cadenas; Ward une los que menos aumentan la varianza intra-cluster y da clusters compactos.
10. Centrar: PCA mide varianza alrededor de la media; sin centrar la primera componente apunta a la media. Estandarizar: evita que variables con grandes unidades dominen.
11. 100 / (100+25+1) = 0.794.
12. Falso.
13. Cohesión vs separación de cada punto; rango [−1, 1], cerca de 1 = bien agrupado.
14. Penaliza la complejidad para elegir el número de componentes: BIC = −2 log L + p log N, menor es mejor.
15. Es invariante a la permutación de etiquetas y corrige por azar.
16. Árboles con cortes aleatorios; los puntos anómalos quedan aislados a poca profundidad promedio.
17. Ejemplo esperado: imputación, one-hot / codificación de categóricas, estandarización, PCA o UMAP para inspección, K-means/GMM con selección de k por silueta y BIC, perfilado de segmentos y validación de estabilidad (bootstrap).
