# Proyecto 09 — Sistema experto de diagnóstico con explicación

## Descripción
Desarrolla un sistema experto para un dominio que conozcas (diagnóstico de fallas de una computadora/Mac, orientación de trámites universitarios, recomendación de cultivos en Puebla, triaje de soporte técnico…).

## Requisitos
1. ≥ 40 reglas con variables escritas tras "entrevistar" a un experto o fuentes confiables (cítalas).
2. **Dos implementaciones:** (a) en SWI-Prolog; (b) en Python usando tu `ej06_sistema_experto.py`.
3. Manejo de incertidumbre con factores de certeza estilo MYCIN.
4. Subsistema de explicación: "¿por qué me preguntas esto?" y "¿cómo llegaste a esta conclusión?".
5. Interfaz conversacional por terminal que pregunte solo lo necesario (encadenamiento hacia atrás).
6. **Extensión moderna:** usa un LLM local (Ollama/MLX) para traducir la descripción en lenguaje natural del usuario a hechos de la KB; el razonamiento lo hace el motor lógico. Discute ventajas de este enfoque neurosimbólico.
7. Validación: 15 casos de prueba con respuesta esperada.

## Rúbrica (100 pts)
| Criterio | Pts |
|---|---|
| Calidad y cobertura de la base de conocimiento | 25 |
| Implementación Prolog | 15 |
| Implementación Python con CF y explicación | 25 |
| Integración LLM → hechos | 15 |
| Casos de prueba y reporte | 20 |
