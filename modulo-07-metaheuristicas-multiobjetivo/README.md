# Módulo 07 — Búsqueda local, metaheurísticas y optimización multiobjetivo (BUAP Unidad 4)

**Duración estimada:** 4 semanas (≈ 50 h) · **Prerrequisitos:** módulos 02 y 05

## Objetivos
- Modelar problemas de optimización combinatoria (TSP, mochila) y continua.
- Implementar búsqueda local, recocido simulado y búsqueda tabú.
- Implementar algoritmos evolutivos (AG), colonia de hormigas, sistema inmune (CLONALG) y meméticos.
- Entender dominancia de Pareto e implementar NSGA-II.
- Comparar metaheurísticas experimentalmente con rigor estadístico.

## Temario (alineado al programa CCOS 258)
| BUAP | Tema | Dónde |
|---|---|---|
| 4.1 | Introducción a técnicas multiobjetivo | teoria §7, ej08 |
| 4.2 | Búsqueda local y optimización: hill climbing, reinicios, recocido simulado | teoria §1–2, ej01–02 |
| 4.3 | Búsqueda tabú | teoria §3, ej03 |
| 4.4 | Algoritmos genéticos | teoria §4, ej04 |
| 4.5 | Bioinspirados: meméticos, sistema inmune, ACO (+ PSO, DE como extra) | teoria §5–6, ej05–07 |
| 4.6 | Aplicaciones prácticas multiobjetivo | proyecto |

## Lecturas
- **AIMA 4ª ed., cap. 4.1–4.2** (búsqueda local, espacios continuos).
- **Eiben & Smith, *Introduction to Evolutionary Computing* 2ª ed.:** caps. 3 (qué es un AE), 4 (representación y operadores), 5 (selección), 6 (populares: ES, PE, GP, DE, PSO), 10 (híbridos/meméticos), 12 (multiobjetivo), 7–8 (control de parámetros).
- Negnevitsky 3ª ed., cap. 7 (computación evolutiva).
- Luger 6ª ed., cap. 12 (aprendizaje evolutivo).
- Papers: Kirkpatrick et al. (1983) *Optimization by Simulated Annealing*; Glover (1989) *Tabu Search Part I*; Dorigo et al. (1996) *Ant System*; de Castro & Von Zuben (2002) *CLONALG*; Deb et al. (2002) *NSGA-II*.

## Ejercicios
1. `ej01_problemas.py` — representación TSP/mochila, 2-opt, penalizaciones
2. `ej02_hill_climbing_recocido.py` — hill climbing con reinicios, recocido simulado
3. `ej03_tabu.py` — búsqueda tabú con aspiración
4. `ej04_genetico.py` — torneo, cruce un punto, OX, mutación, AG completo
5. `ej05_aco.py` — Ant System para TSP
6. `ej06_clonalg.py` — selección clonal para optimización continua
7. `ej07_memetico.py` — AG + 2-opt para TSP
8. `ej08_nsga2.py` — dominancia, frentes, crowding, NSGA-II

## Evaluación
Ejercicios 30 % · [Quiz](evaluacion/quiz.md) 30 % · [Proyecto](proyecto/README.md) 30 % · Reseña crítica del paper NSGA-II (1–2 págs.) 10 %.
