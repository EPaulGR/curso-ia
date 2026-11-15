# Proyecto 00 — Analizador de datos y k-NN vectorizado

**Objetivo:** construir un mini-pipeline de datos de punta a punta solo con NumPy, pandas y matplotlib.

1. Descarga un dataset abierto (p. ej. *Iris*, *Palmer Penguins* o datos abiertos de INEGI/CDMX).
2. Limpia con pandas (faltantes, duplicados, tipos) y produce un resumen por grupos.
3. Grafica 3 visualizaciones (histograma, dispersión por clase, matriz de correlación).
4. Implementa k-NN (k configurable, voto mayoritario) **sin bucles sobre muestras** usando tu `distancias_pares`.
5. Divide 80/20, reporta exactitud para k = 1, 3, 5, 7 y grafica exactitud vs k.
6. Entrega un notebook limpio + un `README` con conclusiones.

## Rúbrica (10 pts)
| Criterio | Pts |
|---|---|
| Limpieza correcta y documentada | 2 |
| Visualizaciones claras con títulos/ejes | 2 |
| k-NN vectorizado y correcto | 3 |
| Experimento de k bien diseñado (semilla, división) | 2 |
| Código limpio, con tests mínimos | 1 |
