# Respuestas — Quiz módulo 11
1. Riesgo: pérdida esperada sobre la distribución real; empírico: promedio sobre la muestra de entrenamiento.
2. J = (1/n)(Xθ−y)ᵀ(Xθ−y) → ∇J = (2/n)Xᵀ(Xθ−y).
3. Costoso (O(d³)) y numéricamente inestable si está mal condicionada; se usa QR/SVD/Cholesky.
4. Ridge = MAP con prior gaussiano sobre θ; lasso = MAP con prior de Laplace.
5. La región ‖θ‖₁ ≤ t tiene esquinas sobre los ejes donde suele tocar el contorno de la pérdida.
6. ∂J/∂w = (1/n)Σ(σ(wᵀx_i) − y_i)x_i.
7. En alta dimensión las distancias se concentran y los vecinos dejan de ser "cercanos"; se necesitan muchísimos datos.
8. Generativo: Naive Bayes modela P(x|y)P(y). Discriminativo: regresión logística modela P(y|x).
9. Precisión cuando los falsos positivos cuestan (filtro de spam); recall cuando los falsos negativos cuestan (detección de cáncer, fraude).
10. Probabilidad de ordenar correctamente un positivo y un negativo aleatorios; con muchos negativos el FPR se mantiene bajo aunque haya muchos FP, PR lo refleja.
11. Escalar con media/desviación de todo el conjunto antes de partir; usar Pipeline dentro de la validación.
12. E[(y−ĥ)²] = (E[ĥ]−f)² + Var(ĥ) + σ².
13. p=0.75: Gini = 1 − (0.5625+0.0625) = 0.375; H = −0.75log₂0.75 − 0.25log₂0.25 ≈ 0.811.
14. Para decorrelacionar los árboles y que el promedio reduzca más la varianza.
15. Error estimado en las muestras que no entraron al bootstrap de cada árbol (≈ 36.8 %).
16. Bagging reduce varianza (modelos complejos en paralelo); boosting reduce sesgo (modelos débiles secuenciales).
17. α = 0: el clasificador no aporta (igual que adivinar).
18. Ejemplos sobre o dentro del margen (α>0). C controla la penalización de violaciones: C grande → margen estrecho, menos sesgo, más varianza.
19. Sustituir productos punto por K(x,x') = φ(x)ᵀφ(x') para trabajar implícitamente en un espacio de características de alta dimensión.
20. Manejan heterogeneidad, escalas distintas, faltantes e interacciones no suaves con pocos datos; las redes necesitan más datos y tienen sesgos inductivos menos adecuados a tablas.
