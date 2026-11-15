# Módulo 06 — Búsqueda con adversarios (BUAP Unidad 3)

**Duración estimada:** 3 semanas (≈ 35 h) · **Prerrequisitos:** módulo 05

## Objetivos
- Formalizar un juego de suma cero con información perfecta.
- Implementar MINIMAX y poda alfa-beta y demostrar que la poda no cambia el resultado.
- Diseñar funciones de evaluación y usar corte de profundidad, ordenamiento de jugadas y profundización iterativa.
- Implementar Monte Carlo Tree Search (UCT) y entender su relación con AlphaZero.
- Construir un motor de Conecta-4 competitivo.

## Temario (alineado al programa CCOS 258)
| BUAP | Tema | Dónde |
|---|---|---|
| 3.1 | Introducción: juegos como búsqueda, árbol de juego, suma cero | teoria §1, ej01 |
| 3.2 | Funciones de evaluación considerando oponentes | teoria §4, ej06 |
| 3.3.1 | MINIMAX | teoria §2, ej02 |
| 3.3.2 | Poda alfa-beta | teoria §3, ej03 |
| 3.4 | Nuevas técnicas: MCTS, expectiminimax, búsqueda con redes (AlphaZero) | teoria §6–7, ej05 |
| 3.5 | Reducir el espacio: ordenamiento, tablas de transposición, killer moves | teoria §5, ej04 |
| 3.6 | Mejorar calidad: profundización iterativa, búsqueda de quiescencia, aperturas/finales | teoria §5 |
| 3.7 | Aplicaciones: ajedrez, Go, póker, Conecta-4 | proyecto |

## Lecturas
- **AIMA 4ª ed., cap. 5** completo (Adversarial Search and Games). Obligatorio.
- Luger 6ª ed., cap. 4.4 (minimax, alfa-beta).
- Rich & Knight 3ª ed., cap. 12 (Game Playing).
- Opcional: Silver et al. (2017) *Mastering the game of Go without human knowledge* (Nature); Browne et al. (2012) *A Survey of MCTS Methods*.

## Ejercicios (`ejercicios/`)
1. `ej01_gato.py` — interfaz de juego para el gato
2. `ej02_minimax.py` — minimax genérico con conteo de nodos
3. `ej03_alfabeta.py` — poda alfa-beta
4. `ej04_profundizacion_iterativa.py` — corte, evaluación, ordenamiento, ID
5. `ej05_mcts.py` — MCTS con UCB1
6. `ej06_conecta4.py` — juego y heurística de Conecta-4

```bash
pytest modulo-06-busqueda-adversarial
```

## Evaluación
Ejercicios 30 % · [Quiz](evaluacion/quiz.md) 30 % · [Proyecto](proyecto/README.md) 30 % · Ensayo corto (1 pág.) sobre "Deep Blue vs AlphaZero" 10 %.
