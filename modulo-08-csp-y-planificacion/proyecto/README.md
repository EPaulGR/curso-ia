# Proyecto 08 — Generador de horarios universitarios

Construye un sistema que genere horarios para una facultad (inspírate en la FCC-BUAP).

## Requisitos
1. **Modelo:** materias (horas/semana, grupo), profesores (disponibilidad, materias que imparten), salones (capacidad, laboratorio sí/no), bloques horarios.
2. **Restricciones duras:** un profesor/salón/grupo no puede estar en dos lugares a la vez; capacidad; laboratorios.
3. **Restricciones blandas** (minimizar): huecos de los alumnos, clases después de las 19:00, preferencias de profesores.
4. Resolver con: (a) tu backtracking + MAC para las duras; (b) recocido simulado o tabú (módulo 07) para optimizar las blandas; (c) comparar con `OR-Tools CP-SAT`.
5. Exportar el horario a HTML/CSV por grupo, profesor y salón.
6. **Planificación (extra):** modela en PDDL un problema de logística y resuélvelo con Fast Downward; compara con tu planificador A*.

## Rúbrica (100 pts)
| Criterio | Pts |
|---|---|
| Modelo CSP correcto y documentado | 20 |
| Solución factible en instancia de ≥ 30 materias | 25 |
| Optimización de restricciones blandas con métricas | 20 |
| Comparación con CP-SAT (tiempo y calidad) | 15 |
| Visualización/exportación y calidad del código | 20 |
