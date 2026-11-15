# Módulo 03 — Lógica, algoritmos y estructuras de datos

**Duración:** 4 semanas (40–50 h) · **Fase 0** · Repaso de *Lógica Matemática* (asignatura precedente de CCOS 258)

## Objetivos
- Dominar lógica proposicional: tablas de verdad, equivalencias, formas normales, inferencia.
- Analizar complejidad (Big-O) y reconocer clases P, NP, NP-completo (fundamental para entender por qué la IA usa heurísticas).
- Implementar las estructuras y algoritmos que sostienen la búsqueda: pilas, colas, heaps, grafos, recursión, programación dinámica.

## Temario
1. Lógica proposicional: sintaxis, semántica, tautologías, satisfacibilidad, equivalencias (De Morgan, distributividad).
2. Formas normales CNF y DNF; resolución; algoritmo DPLL.
3. Lógica de predicados (intro; se profundiza en módulo 09).
4. Análisis asintótico: O, Ω, Θ; recurrencias; teorema maestro.
5. Estructuras: pila, cola, deque, heap binario, tablas hash, unión-búsqueda.
6. Grafos: representación (lista/matriz de adyacencia), recorridos, orden topológico, Dijkstra, árbol de expansión mínima.
7. Recursión, divide y vencerás, backtracking, programación dinámica.
8. Complejidad computacional: P, NP, NP-completo, reducciones; SAT, TSP, mochila.

## Lecturas
- Russell & Norvig, *AIMA* 4ª ed. — Cap. 7 (agentes lógicos, §7.1–7.6).
- Cormen et al., *CLRS* — Caps. 2–4 (análisis), 6 (heapsort), 15 (programación dinámica), 22–24 (grafos), 34 (NP-completitud).
- Ertel, *Introduction to AI* — Cap. 2 (lógica proposicional).

## Ejercicios
| Archivo | Tema |
|---|---|
| ej01_tablas_verdad.py | evaluación de fórmulas, tautologías |
| ej02_cnf_dpll.py | SAT con DPLL |
| ej03_heap.py | heap binario desde cero |
| ej04_grafos.py | recorridos y orden topológico |
| ej05_dijkstra.py | caminos mínimos |
| ej06_union_find_kruskal.py | MST |
| ej07_programacion_dinamica.py | mochila, LCS, edición |
| ej08_backtracking.py | N-reinas, subconjuntos |

Aprobación ≥ 8/10.
