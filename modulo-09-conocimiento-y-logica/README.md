# Módulo 09 — Representación del conocimiento, lógica y sistemas expertos

**Duración estimada:** 3 semanas (≈ 35 h) · **Prerrequisitos:** 03 (lógica), 08
Ampliación del paradigma **simbólico** (BUAP 1.7.1).

## Objetivos
- Dominar sintaxis, semántica e inferencia en lógica proposicional y de primer orden.
- Implementar verificación de modelos, resolución, DPLL, encadenamiento y unificación.
- Construir un sistema experto basado en reglas con capacidad de explicación.
- Programar en Prolog y conocer ontologías, marcos y redes semánticas.

## Temario
1. Agentes basados en conocimiento; KB, TELL/ASK
2. Lógica proposicional: sintaxis, semántica, consecuencia lógica, validez, satisfacibilidad
3. Inferencia: verificación de modelos, resolución, FNC, completitud
4. SAT: DPLL, WalkSAT, CDCL (solvers modernos)
5. Cláusulas de Horn, encadenamiento hacia adelante/atrás
6. Lógica de primer orden: cuantificadores, modelos, ingeniería del conocimiento
7. Unificación, Modus Ponens generalizado, resolución de primer orden, skolemización
8. Prolog: SLD, corte, negación como falla
9. Sistemas expertos: arquitectura, motor de inferencia, factores de certeza (MYCIN)
10. Ontologías, marcos, redes semánticas, lógicas descriptivas, grafos de conocimiento
11. Neurosimbólico: LLMs + lógica, razonamiento verificable

## Lecturas
- **AIMA 4ª ed., caps. 7, 8, 9, 10.**
- Negnevitsky 3ª ed., caps. 2–3 (sistemas expertos basados en reglas, incertidumbre).
- Ertel 2ª ed., caps. 2–5 (lógica proposicional, primer orden, Prolog).
- Bratko — *Prolog Programming for Artificial Intelligence* (4ª ed.), caps. 1–3 (opcional).
- Boden, *Inteligencia artificial*, cap. 2 (contexto filosófico de la IA simbólica).

## Ejercicios
1. `ej01_logica_proposicional.py` — evaluación, TT-ENTAILS, validez
2. `ej02_fnc_resolucion.py` — FNC y resolución por refutación
3. `ej03_dpll.py` — SAT solver DPLL
4. `ej04_encadenamiento.py` — Horn: adelante y atrás
5. `ej05_unificacion.py` — unificación con occurs check
6. `ej06_sistema_experto.py` — FOL forward chaining, consultas tipo Prolog, explicación

Instala SWI-Prolog para el proyecto:
```bash
brew install swi-prolog
```

## Evaluación
Ejercicios 30 % · [Quiz](evaluacion/quiz.md) 30 % · [Proyecto](proyecto/README.md) 30 % · Ensayo: "¿Murió la IA simbólica?" 10 %.
