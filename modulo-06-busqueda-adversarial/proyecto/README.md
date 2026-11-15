# Proyecto 06 — Motor de Conecta-4 y torneo

## Descripción
Construye un motor de Conecta-4 jugable por consola que use alfa-beta con profundización iterativa y límite de tiempo, y compáralo contra MCTS.

## Requisitos
1. Usa tu `ej06_conecta4.py` y `ej04_profundizacion_iterativa.py`.
2. Añade **tabla de transposición** con hashing de Zobrist.
3. Límite de tiempo por jugada (p. ej., 1 s) con profundización iterativa.
4. Modo humano vs. motor en terminal, mostrando el tablero.
5. Torneo de 100 partidas (alternando quién empieza): alfa-beta vs. MCTS (mismo tiempo), alfa-beta vs. aleatorio, MCTS vs. aleatorio. Reporta tabla de resultados y nodos/segundo.
6. Informe (2–3 págs.): diseño de la evaluación, efecto del ordenamiento (nodos con y sin orden), gráfica profundidad vs. nodos.

## Rúbrica (100 pts)
| Criterio | Pts |
|---|---|
| Motor correcto y jugable | 20 |
| Tabla de transposición funcionando (medir ahorro de nodos) | 15 |
| Control de tiempo con ID | 15 |
| Torneo automatizado y resultados reproducibles (semillas) | 20 |
| Análisis experimental con gráficas | 20 |
| Calidad de código y documentación | 10 |

**Reto extra:** reemplaza la evaluación por una pequeña red entrenada con partidas de autojuego (anticipa el módulo 20).
