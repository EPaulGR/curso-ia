# Proyecto 02 — Filtro bayesiano de spam y análisis A/B

**Parte A – Naive Bayes desde cero**
1. Usa el dataset *SMS Spam Collection* (UCI).
2. Implementa Naive Bayes multinomial con suavizado de Laplace en log-espacio.
3. Reporta exactitud, precisión, recall y matriz de confusión; las 20 palabras más indicativas de spam (razón de log-probabilidades).

**Parte B – Prueba A/B**
1. Simula dos variantes con tasas de conversión 10 % y 11 %. ¿Qué tamaño de muestra detecta la diferencia con potencia 80 %? (simulación).
2. Compara enfoque frecuentista (permutación) vs bayesiano (posteriores Beta, P(B>A) por Monte Carlo).

## Rúbrica (10 pts)
| Criterio | Pts |
|---|---|
| Naive Bayes correcto y en log-espacio | 3 |
| Métricas y análisis de errores | 2 |
| Cálculo de tamaño de muestra por simulación | 2 |
| Comparación frecuentista vs bayesiano argumentada | 3 |
