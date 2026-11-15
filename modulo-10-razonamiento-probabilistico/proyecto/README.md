# Proyecto 10 — Rastreo y diagnóstico bajo incertidumbre

Elige **una** de las dos opciones (o ambas para puntos extra).

## Opción A: Localización de un robot (HMM + partículas)
1. Mapa de cuadrícula con obstáculos; el robot se mueve con ruido y tiene sensores de distancia ruidosos en 4 direcciones.
2. Implementa filtrado HMM exacto sobre la cuadrícula y un filtro de partículas en espacio continuo.
3. Visualiza la creencia en cada paso (animación con matplotlib).
4. Compara error de localización vs. número de partículas y costo computacional.

## Opción B: Red bayesiana de diagnóstico médico o de fallas
1. Diseña una red de ≥ 12 nodos (justifica estructura y CPTs con literatura).
2. Inferencia exacta (tu enumeración + eliminación de variables con `pgmpy`) y aproximada (Gibbs).
3. Analiza convergencia de Gibbs y compara contra la exacta.
4. Implementa valor de la información para sugerir la siguiente prueba a realizar.
5. Compárala con un controlador/diagnosticador difuso de Mamdani para el mismo problema.

## Rúbrica (100 pts)
| Criterio | Pts |
|---|---|
| Modelado justificado | 20 |
| Inferencia correcta (exacta y aproximada) | 30 |
| Experimentos y visualizaciones | 25 |
| Discusión (limitaciones, supuestos) | 15 |
| Código y reproducibilidad | 10 |
