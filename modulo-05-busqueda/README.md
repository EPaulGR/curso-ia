# Módulo 05 — Problemas de búsqueda

**Duración:** 5 semanas (50–60 h) · **Fase 1 · Unidad 2 del programa BUAP CCOS 258**

## Objetivos
- Formular problemas como espacios de estados (estado inicial, acciones, modelo de transición, prueba de meta, costo).
- Implementar y comparar estrategias no informadas e informadas.
- Diseñar heurísticas admisibles y consistentes y medir su calidad (factor de ramificación efectivo).
- Aplicar técnicas para reducir el espacio de búsqueda y mejorar la calidad de los resultados.

## Temario (alineado a la Unidad 2 BUAP)
**2.1 Caracterización de problemas**
- 2.1.1 Tipos de datos: confiables, no confiables (ruido, sensores), variables en el tiempo (entornos dinámicos).
- 2.1.2 Representación mediante estados y enlaces (grafo de estados, árbol de búsqueda, nodos vs estados).
- 2.1.3 Dimensión del espacio y complejidad (b, d, m; 8-puzzle 9!/2, 15-puzzle ~10¹³, Rubik ~4.3×10¹⁹).

**2.2 Funciones de evaluación de estados**
- 2.2.1 Evaluación de estados: g(n), h(n), f(n).
- 2.2.2 Con conocimiento previo: distancias exactas, bases de datos de patrones.
- 2.2.3 Heurísticas: admisibilidad, consistencia, dominancia, problemas relajados.

**2.3 Estrategias de exploración**
- 2.3.1 Profundidad (DFS), profundidad limitada, profundización iterativa (IDDFS)
- 2.3.2 Anchura (BFS), costo uniforme (UCS / Dijkstra)
- 2.3.3 Primero el mejor (voraz)
- 2.3.4 A* e IDA*
- 2.3.5 Nuevas técnicas: búsqueda bidireccional, weighted A*, beam search, RBFS/SMA*, Jump Point Search, búsqueda en tiempo real (LRTA*)

**2.4 Reducción del espacio:** detección de estados repetidos, simetrías, poda, paridad de permutaciones (resolubilidad del 8-puzzle).
**2.5 Calidad de resultados:** optimalidad, heurísticas más informadas, weighted A* con cota (1+ε).
**2.6 Aplicaciones:** rutas en mapas, puzzles, planificación de movimiento de robots, videojuegos (pathfinding).

## Lecturas
- Russell & Norvig, *AIMA* 4ª ed. — **Cap. 3** completo (búsqueda), §4.1–4.2 y §4.5 (búsqueda en línea).
- Nilsson, *AI: A New Synthesis* — Caps. 8–9.
- Ertel — Cap. 6.
- Negnevitsky — Cap. 1 (contexto) y Luger, Caps. 3–4 (búsqueda heurística).
- Hart, Nilsson & Raphael (1968), *A Formal Basis for the Heuristic Determination of Minimum Cost Paths* (artículo original de A*). 🆓
- Korf (1985), *Depth-first iterative-deepening* (IDA*).

## Ejercicios
| Archivo | Tema |
|---|---|
| ej01_problema.py | formulación abstracta + 8-puzzle + resolubilidad |
| ej02_no_informada.py | BFS, DFS, DLS, IDDFS |
| ej03_costo_uniforme.py | UCS en grafo de ciudades (mapa de Rumania) |
| ej04_heuristicas.py | piezas fuera de lugar, Manhattan, conflicto lineal |
| ej05_a_estrella.py | voraz, A*, weighted A* |
| ej06_ida_estrella.py | IDA* |
| ej07_laberinto.py | pathfinding en cuadrícula |
| ej08_bidireccional.py | búsqueda bidireccional |
| ej09_comparativa.py | nodos expandidos y factor de ramificación efectivo |

Aprobación ≥ 8/10.
