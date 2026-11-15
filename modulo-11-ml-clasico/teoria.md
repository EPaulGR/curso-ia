# Teoría — Machine Learning clásico

## 1. Planteamiento
Datos `D = {(x_i, y_i)}` i.i.d. de una distribución desconocida P. Buscamos `h ∈ H` que minimice el **riesgo** `R(h) = E[L(h(x), y)]`; solo podemos minimizar el **riesgo empírico** `R̂(h) = (1/n) Σ L(h(x_i), y_i)`. La brecha entre ambos es la **generalización**. Principio de Ockham y regularización: `min R̂(h) + λ Ω(h)`.

## 2. Regresión lineal
`ŷ = Xθ`. MSE: `J(θ) = (1/n)‖Xθ − y‖²`. Gradiente: `∇J = (2/n)Xᵀ(Xθ − y)`. Ecuación normal: `θ = (XᵀX)⁻¹Xᵀy` (O(d³); usar QR/SVD → `lstsq`). Interpretación probabilística: MSE = máxima verosimilitud con ruido gaussiano.
- **Ridge (L2):** `θ = (XᵀX + λI)⁻¹Xᵀy` — encoge coeficientes, maneja colinealidad; = MAP con prior gaussiano.
- **Lasso (L1):** induce esparsidad (selección de variables); = prior de Laplace.
- Descenso de gradiente: por lotes, estocástico, mini-lotes; tasa de aprendizaje; escalar características.

## 3. Clasificación
**Regresión logística:** `p = σ(wᵀx + b)`; pérdida = entropía cruzada (convexa); `∇ = Xᵀ(p − y)/n`. Multiclase: softmax `p_k = e^{z_k}/Σ e^{z_j}`.
**kNN:** no paramétrico, perezoso; k pequeño → varianza alta; maldición de la dimensionalidad; escalar características.
**Naive Bayes:** generativo; muy rápido; bueno en texto (multinomial).
**Discriminativo vs. generativo:** modelar `P(y|x)` vs. `P(x|y)P(y)`.

## 4. Evaluación
- Separar **entrenamiento / validación / prueba**; la prueba se usa una sola vez.
- **k-fold CV** (estratificado para clasificación; por grupos o temporal cuando aplica).
- Confusión: TP, FP, TN, FN. Precisión `TP/(TP+FP)`, recall `TP/(TP+FN)`, F1, especificidad.
- **ROC** (TPR vs. FPR) y **AUC** = probabilidad de que un positivo aleatorio puntúe más que un negativo. Con desbalance fuerte, preferir **curva PR**.
- Regresión: MAE, RMSE, R², MAPE.
- **Fuga de datos:** ajustar el escalador o la imputación con todo el conjunto antes de partir → resultados optimistas. Solución: `Pipeline`.

## 5. Sesgo–varianza
`E[(y − ĥ(x))²] = sesgo² + varianza + ruido`. Modelos simples: alto sesgo (subajuste); complejos: alta varianza (sobreajuste). Herramientas: curvas de aprendizaje y de validación, regularización, más datos, ensambles. **Teoría PAC:** con |H| finito, `n ≥ (1/ε)(ln|H| + ln(1/δ))`. **Dimensión VC.** El "doble descenso" en modelos sobreparametrizados (anticipa deep learning).

## 6. Árboles de decisión
Particiones recursivas eje-paralelas. Elegir la división que maximiza la reducción de impureza:
- Gini `1 − Σp_k²`, entropía `−Σ p_k log p_k`, ganancia de información; regresión: reducción de varianza.
- Controlar profundidad, mínimo de muestras, poda por costo-complejidad (`ccp_alpha`).
- Ventajas: interpretables, sin escalar, mixtos; desventajas: alta varianza, inestables.

## 7. Ensambles
- **Bagging:** promediar modelos entrenados en muestras bootstrap → reduce varianza; error *out-of-bag*.
- **Random forest:** bagging + subconjunto aleatorio de √d características por división → decorrelaciona árboles.
- **AdaBoost:** reponderar ejemplos mal clasificados; `α_m = ½ ln((1−ε)/ε)`; minimiza pérdida exponencial.
- **Gradient boosting:** ajustar cada árbol al gradiente negativo de la pérdida (residuos), con tasa de aprendizaje; **XGBoost/LightGBM/CatBoost** dominan datos tabulares (aún hoy suelen superar a las redes en tablas).
- Stacking y votación.

## 8. Máquinas de vectores de soporte
Margen máximo: `min ½‖w‖² s.a. y_i(wᵀx_i + b) ≥ 1`. Margen suave con C: `min ½‖w‖² + C Σ ξ_i` ≡ pérdida bisagra `max(0, 1 − y f(x))`. Dual: `max Σα_i − ½ ΣΣ α_iα_j y_iy_j K(x_i,x_j)`, `0 ≤ α_i ≤ C`; solo los vectores de soporte tienen α > 0. **Truco del kernel:** RBF `K = exp(−γ‖x−x'‖²)`. γ grande → frontera muy flexible. Pegasos: SGD primal, O(1/(λε)).

## 9. Práctica profesional
Exploración (EDA) → limpieza → características → línea base simple → modelos → validación → análisis de errores → interpretabilidad → despliegue. Desbalance: pesos de clase, re-muestreo (SMOTE), umbral. Interpretabilidad: importancia por permutación, PDP, **SHAP**.

En Mac: scikit-learn, XGBoost y LightGBM corren en CPU y aprovechan bien los núcleos de Apple Silicon (`n_jobs=-1`).
