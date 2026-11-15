# Quiz — Módulo 19b (20 preguntas)

Tiempo sugerido: 60 min, sin consultar. Aprobado: ≥ 16/20.

1. ¿Qué diferencia hay entre un *workflow* y un agente según "Building effective agents"?
2. En MCP, ¿qué tres tipos de capacidades puede exponer un servidor?
3. ¿Por qué una notificación JSON-RPC no recibe respuesta? ¿Cómo se reconoce?
4. Una herramienta MCP lanza una excepción. ¿Se responde con `error` o con `isError: true`? ¿Por qué?
5. Nombra los dos transportes estándar de MCP y cuándo usar cada uno.
6. Explica cómo funciona la memoria de largo plazo de un agente y qué tres criterios usa *Generative Agents* para recuperar recuerdos.
7. ¿Qué ventaja y qué costo tiene el patrón orquestador-trabajadores?
8. ¿Por qué los agentes de código son especialmente adecuados para entrenarse con RL?
9. Con n = 10 muestras y c = 3 correctas, calcula pass@1 y pass^2.
10. ¿Por qué pass^k es más relevante que pass@k para un agente en producción?
11. Define la "trifecta letal" de la seguridad de agentes.
12. ¿Qué es *tool poisoning* en MCP?
13. Menciona cuatro mitigaciones contra la *prompt injection* indirecta y explica por qué ninguna basta sola.
14. ¿Por qué la decodificación con *batch* 1 está limitada por el ancho de banda de memoria?
15. En la decodificación especulativa, ¿de qué distribución se muestrea tras un rechazo? ¿Por qué el resultado sigue exactamente a p?
16. Si p = [0.5, 0.3, 0.2] y q = [0.2, 0.4, 0.4], ¿cuál es la tasa de aceptación esperada?
17. ¿Qué problema resuelve PagedAttention y qué analogía con los sistemas operativos usa?
18. ¿Por qué el batching continuo reduce la latencia media frente al estático?
19. Compara GGUF Q4_K_M con la cuantización de 4 bits de MLX: ¿qué tienen en común?
20. Describe cómo un VLM tipo LLaVA convierte una imagen en tokens que el LLM entiende, y qué optimiza la pérdida de CLIP.

**Pregunta abierta (bonus):** diseña la defensa en capas para un agente que lee tu correo y puede enviar mensajes.
