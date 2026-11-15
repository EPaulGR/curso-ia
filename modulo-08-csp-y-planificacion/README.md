# Módulo 08 — Satisfacción de restricciones y planificación

**Duración estimada:** 3 semanas (≈ 35 h) · **Prerrequisitos:** 05, 07
Ampliación del temario BUAP (cubre 2.4 "técnicas para reducir el espacio de búsqueda" con propagación de restricciones).

## Objetivos
- Modelar problemas como CSP (variables, dominios, restricciones).
- Implementar backtracking con MRV, grado, LCV y forward checking.
- Implementar AC-3 y entender niveles de consistencia.
- Resolver CSP grandes con búsqueda local (min-conflictos).
- Representar problemas de planificación en STRIPS/PDDL y resolverlos con búsqueda hacia adelante y heurísticas relajadas.

## Temario
1. CSP: definición, tipos de restricciones (unarias, binarias, globales: AllDiff), CSP continuos
2. Propagación: consistencia de nodo, de arco (AC-3), de camino, k-consistencia
3. Backtracking y heurísticas de orden; forward checking, MAC; backjumping dirigido por conflictos
4. Búsqueda local: min-conflictos, ponderación de restricciones
5. Estructura: árboles (O(nd²)), conjunto de corte, descomposición en árbol
6. Planificación clásica: STRIPS, PDDL, búsqueda hacia adelante/atrás
7. Heurísticas: ignorar precondiciones, ignorar borrados (h_add, h_max, h_FF), grafos de planificación (GraphPlan)
8. Planificación jerárquica (HTN), planificación como SAT, planificación con LLMs

## Lecturas
- **AIMA 4ª ed., cap. 6** (CSP) y **cap. 11** (Automated Planning).
- Nilsson, *A New Synthesis*, caps. 21–22 (planificación STRIPS).
- Ghallab, Nau & Traverso — *Automated Planning and Acting* (2016) 🆓, caps. 2–3 (opcional).

## Ejercicios
1. `ej01_csp_modelo.py` — clase CSP, coloreo de Australia, n-reinas
2. `ej02_backtracking.py` — backtracking + MRV + LCV + forward checking
3. `ej03_ac3.py` — consistencia de arcos
4. `ej04_min_conflictos.py` — n-reinas con min-conflictos (n grande)
5. `ej05_sudoku.py` — sudoku con propagación y búsqueda
6. `ej06_strips.py` — planificador STRIPS (BFS, A* con heurística relajada), mundo de bloques

## Evaluación
Ejercicios 30 % · [Quiz](evaluacion/quiz.md) 30 % · [Proyecto](proyecto/README.md) 30 % · Lectura: resumen de AIMA 11.3 10 %.
