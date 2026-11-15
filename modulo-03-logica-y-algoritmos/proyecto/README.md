# Proyecto 03 — Mini SAT solver y resolvedor de Sudoku

1. Extiende tu DPLL para leer archivos DIMACS CNF.
2. Añade una heurística de selección de variable (p. ej. la más frecuente / MOMS) y compárala contra la elección ingenua en instancias 3-SAT aleatorias con razón cláusulas/variables 3.0, 4.26 y 5.5. Grafica tiempo y % satisfacible (verás la "transición de fase" en 4.26).
3. Codifica Sudoku 9×9 como SAT (729 variables) y resuélvelo con tu solver.
4. Informe de 2 páginas: complejidad, transición de fase, por qué los SAT solvers son prácticos pese a la NP-completitud.

## Rúbrica (10 pts)
| Criterio | Pts |
|---|---|
| Lector DIMACS + DPLL correcto | 2 |
| Heurística y experimento de transición de fase | 3 |
| Codificación Sudoku correcta | 3 |
| Informe con análisis | 2 |
