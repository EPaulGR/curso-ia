# Proyecto 07 — Laboratorio de metaheurísticas

## Parte A: TSP (60 %)
1. Descarga 3 instancias de TSPLIB (p. ej. `berlin52`, `kroA100`, `ch150`) y escribe un lector.
2. Compara recocido simulado, AG (OX), ACO (MMAS) y memético (GA + 2-opt) con el **mismo presupuesto de evaluaciones**.
3. 30 corridas por algoritmo e instancia; reporta media, desviación, mejor, % de error respecto al óptimo conocido.
4. Prueba de Friedman + post-hoc de Wilcoxon (`scipy.stats`).
5. Gráficas de convergencia (mediana e intervalo intercuartil) y la mejor ruta dibujada.

## Parte B: Multiobjetivo aplicado (40 %)
Escoge un problema real con objetivos en conflicto (sugerencias: cartera de inversión riesgo/rendimiento con datos históricos, ruteo de reparto costo/tiempo, selección de características precisión/nº de variables). Resuélvelo con tu NSGA-II, calcula hipervolumen y compáralo con `pymoo`.

## Entregables
Código + `informe.pdf` (6–10 págs.) con metodología, tablas, gráficas y conclusiones.

## Rúbrica (100 pts)
| Criterio | Pts |
|---|---|
| Implementaciones correctas y eficientes (Δ incremental en 2-opt) | 25 |
| Diseño experimental justo (presupuesto, semillas, 30 corridas) | 20 |
| Análisis estadístico correcto | 15 |
| Parte B: modelado y resultados | 25 |
| Informe claro, gráficas, conclusiones | 15 |
