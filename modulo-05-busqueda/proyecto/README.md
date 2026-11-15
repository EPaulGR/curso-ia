# Proyecto 05 — Laboratorio de búsqueda

## Parte A — Comparativa en el 8-puzzle y el 15-puzzle (40 %)
1. Genera 100 instancias resolubles para cada profundidad d = 2, 4, …, 24 (usa `estado_aleatorio` y verifica la profundidad óptima con A*).
2. Compara BFS, IDDFS, A*(h1), A*(h2), A*(conflicto lineal), IDA*(h2), bidireccional y weighted A* (w = 1.5, 3).
3. Tabla y gráficas como AIMA fig. 3.26: nodos generados promedio, b*, tiempo y costo de solución.
4. Extiende a 15-puzzle con IDA* + conflicto lineal (y, como reto, una base de datos de patrones 6-6-3).

## Parte B — Planificador de rutas reales (40 %)
1. Descarga un grafo de calles de Puebla con `osmnx` (o un CSV de OpenStreetMap).
2. Implementa A* con distancia haversine como heurística; compara contra Dijkstra en nodos expandidos.
3. Visualiza en un mapa la ruta y los nodos explorados por cada algoritmo.

## Parte C — Informe (20 %)
Conecta los resultados con la teoría: admisibilidad, dominancia, compromiso memoria/tiempo, cuándo usar cada algoritmo.

## Rúbrica (10 pts)
| Criterio | Pts |
|---|---|
| Implementaciones correctas y reutilizables | 2 |
| Diseño experimental (instancias, repeticiones) | 2 |
| Gráficas y tabla de b* | 2 |
| Rutas reales con visualización | 2 |
| Informe con análisis teórico | 2 |
