# Proyecto 19b — Agente de código local en tu Mac, con MCP y evaluación

## Objetivo
Construir un agente de programación que corre **100 % local** en tu Mac. Usa un LLM servido por **Ollama** o **mlx_lm.server**, se conecta a sus herramientas mediante **un servidor MCP propio** y se mide con una **suite de evaluación** reproducible.

## Requisitos
1. **Servidor MCP** con el SDK oficial (`pip install mcp`, `FastMCP`), con las herramientas `leer_archivo`, `escribir_archivo`, `listar_directorio` y `ejecutar_tests`, todas confinadas a una carpeta sandbox. Reutiliza `ruta_segura` del ej06.
2. **Cliente/agente:** bucle de agente (ej02) que habla con el LLM local a través de la API compatible con OpenAI de Ollama (`http://localhost:11434/v1`) o de mlx-lm, y traduce las herramientas MCP a *tool calls*.
3. **Seguridad:** política de permisos (ej06), confirmación antes de escribir fuera de `src/` y límite de pasos y de tokens. Sin red dentro del sandbox: los tests se ejecutan en un subproceso con tiempo límite.
4. **Suite de evaluación:** al menos 15 tareas (función a implementar más tests ocultos), 5 corridas por tarea. Reporta pass@1, pass@5, pass^5, pasos medios, errores de herramienta y tokens/s.
5. **Experimento de inferencia:** compara al menos dos configuraciones, por ejemplo modelo 7B frente a 14B, Q4 frente a Q8, o con y sin decodificación especulativa (`llama-server --model-draft`). Mide la latencia y la calidad.
6. **Red teaming:** 5 tareas con *prompt injection* escondida en archivos del repositorio. Reporta cuántas veces el agente obedeció.

## Entregables
- `servidor_mcp.py`, `agente.py`, `evaluar.py`, carpeta `tareas/`.
- `REPORTE.md`: arquitectura (diagrama), tablas de resultados, análisis de fallos (lee al menos 10 trayectorias), qué harías para subir pass^5.

## Rúbrica (100 pts)
| Criterio | Pts |
|---|---|
| Servidor MCP correcto (schemas, errores, sandbox) | 20 |
| Agente funcional con LLM local | 20 |
| Suite de evaluación reproducible y métricas correctas (pass@k, pass^k) | 20 |
| Experimento de inferencia bien diseñado y medido | 15 |
| Seguridad y red teaming documentados | 15 |
| Calidad del reporte y análisis de errores | 10 |

Aprobado: ≥ 80 pts.
