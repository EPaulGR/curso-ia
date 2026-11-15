# Teoría — Agentes modernos, inferencia avanzada y multimodalidad

## Parte I · Agentes

### 1. ¿Qué es un agente basado en LLM?
Un **agente** es un LLM ejecutado en un bucle: observa el estado (historial, resultados de herramientas), decide una acción (llamar a una herramienta o responder), la ejecuta y repite. Es el agente racional de Russell & Norvig (módulo 04) con un modelo de lenguaje como función de decisión.

```
historial ← [tarea]
repetir hasta max_pasos:
    acción ← LLM(historial)
    si acción es "final": devolver respuesta
    resultado ← ejecutar(acción.herramienta, acción.args)
    historial ← historial + [acción, resultado]
```

Anthropic distingue entre **flujos de trabajo** (*workflows*: el código decide los pasos, como encadenar prompts, enrutar o paralelizar) y **agentes** (el LLM decide dinámicamente). La regla práctica es usar la solución más simple que funcione. Un agente cuesta más tokens y es menos predecible.

### 2. Model Context Protocol (MCP)
MCP es un estándar abierto (propuesto por Anthropic en noviembre de 2024 y adoptado por los principales proveedores) que separa **quién usa** las herramientas de **quién las ofrece**:

- **Host / cliente:** la aplicación con el LLM (Claude Code, un IDE, tu agente).
- **Servidor:** un proceso que expone capacidades:
  - *tools*: funciones que el modelo puede llamar, con un JSON Schema de entrada.
  - *resources*: datos que se pueden leer (archivos, filas de una base de datos).
  - *prompts*: plantillas reutilizables.
- **Transporte:** *stdio* (el cliente lanza el servidor como subproceso, una línea JSON por mensaje) o *Streamable HTTP* para servidores remotos.
- **Mensajes:** JSON-RPC 2.0. Una petición lleva `id`; una notificación no lleva `id` y no recibe respuesta.

Ciclo de vida:
1. `initialize`: el cliente y el servidor negocian la `protocolVersion` y las `capabilities`.
2. `notifications/initialized`: el cliente avisa que está listo.
3. `tools/list`: el cliente descubre herramientas (nombre, descripción, `inputSchema`).
4. `tools/call` con `{name, arguments}`: el servidor responde `{content: [...], isError}`.

Hay dos tipos de error. Los errores de **protocolo** (JSON inválido −32700, método inexistente −32601, parámetros inválidos −32602) van en `error`. Los errores de **ejecución** de la herramienta van como resultado con `isError: true`, para que el LLM los vea y pueda corregirse.

En la práctica se usa el SDK oficial: `pip install mcp` y el patrón `FastMCP`:
```python
from mcp.server.fastmcp import FastMCP
mcp = FastMCP("mis-herramientas")

@mcp.tool()
def sumar(a: int, b: int) -> int:
    """Suma dos enteros."""
    return a + b

if __name__ == "__main__":
    mcp.run()          # transporte stdio
```
El SDK genera el JSON Schema a partir de las anotaciones de tipo. En el ejercicio 01 lo implementas a mano para entender qué viaja por el cable.

### 3. Memoria y planificación
- **Memoria de trabajo:** el contexto. Es finito: hay que compactarlo (resumir lo antiguo) o recortarlo.
- **Memoria de largo plazo:** almacén externo (vectorial o de palabras clave) del que se recupera lo relevante (RAG sobre la propia experiencia del agente). *Generative Agents* puntúa los recuerdos por recencia, importancia y relevancia.
- **Planificación:**
  - ReAct intercala razonamiento y acción.
  - *Plan-and-execute* genera primero un plan (a menudo un DAG de subtareas) y luego lo ejecuta en orden topológico, lo que conecta con STRIPS del módulo 08.
  - Reflexion añade autocrítica después de fallar.

### 4. Multi-agente
Patrones comunes:
- **Orquestador-trabajadores:** un LLM divide la tarea, varios subagentes la resuelven en paralelo con contexto propio y el orquestador sintetiza. Es más rápido y aísla contextos, pero gasta más tokens.
- **Evaluador-optimizador:** un agente propone y otro critica.
- **Enrutamiento:** un clasificador decide qué especialista atiende.

Riesgos: errores que se propagan, duplicación de trabajo y costo. Siempre hay que capturar los fallos de cada trabajador sin tumbar el sistema.

### 5. Agentes de código y *computer use*
Un **agente de código** cierra el ciclo con señales verificables: edita un archivo, ejecuta los tests y lee el error para corregir. Es exactamente lo que permite entrenar con RL de recompensas verificables (módulo 18b). SWE-bench mide si el agente resuelve *issues* reales de GitHub haciendo pasar los tests ocultos.

Un agente de **computer use** recibe capturas de pantalla y emite acciones de ratón y teclado. Es más general que las herramientas, pero más lento y frágil. OSWorld evalúa tareas reales en sistemas operativos. OSWorld-MCP (ICLR 2026) muestra que dar herramientas MCP a estos agentes mejora su tasa de éxito, aunque el rendimiento cae cuando la tarea exige combinar muchas herramientas. Combinar GUI y herramientas es la tendencia actual.

### 6. Evaluación de agentes
- **pass@k** (Chen et al., 2021): probabilidad de que al menos uno de k intentos sea correcto. El estimador insesgado, con n muestras de las que c son correctas, es `1 − C(n−c,k)/C(n,k)`. Mide **capacidad**.
- **pass^k** (τ-bench): probabilidad de que **los k** intentos sean correctos, `C(c,k)/C(n,k)`. Mide **confiabilidad**, que es lo que importa en producción. Un agente con pass@1 = 0.6 tiene pass^8 muy bajo.
- **Métricas de trayectoria:** número de pasos frente al óptimo, errores de herramienta, costo en tokens, tiempo y acciones peligrosas.
- **Buenas prácticas:**
  - Usar entornos reproducibles.
  - Repetir varias corridas con semillas distintas.
  - Revisar la contaminación del benchmark.
  - Leer trayectorias a mano.
  - Usar LLM como juez solo con rúbricas claras y validación humana.

### 7. Seguridad de agentes
- **Prompt injection indirecta:** instrucciones maliciosas escondidas en una página web, un correo, un *issue* o en la descripción de una herramienta MCP (*tool poisoning*). El modelo no distingue de forma confiable los datos de las órdenes.
- **"Trifecta letal":** acceso a datos privados + exposición a contenido no confiable + capacidad de comunicarse hacia fuera. Si las tres coinciden, la exfiltración es posible.
- **Mitigaciones (en capas, ninguna basta sola):**
  1. Mínimo privilegio y *allowlist* de herramientas.
  2. Confirmación humana para acciones irreversibles.
  3. Sandbox: contenedor o máquina virtual, sin red o con red restringida, raíz de archivos confinada (cuidado con `../`).
  4. *Spotlighting*: marcar los datos no confiables con delimitadores.
  5. Detectores (heurísticos o clasificadores).
  6. Separar los planificadores privilegiados de los lectores en cuarentena.
  7. Registrar y auditar.
- Existen benchmarks específicos como MCP-SafetyBench y MCPHunt (propagación de datos entre servidores MCP).

## Parte II · Ingeniería de inferencia

### 8. Por qué la inferencia es lenta
La generación autoregresiva produce **un token por pasada** del modelo. Con *batch* pequeño, cada pasada está limitada por el **ancho de banda de memoria** (hay que leer todos los pesos), no por el cómputo. Una cota aproximada: tokens/s ≈ ancho de banda / bytes de los pesos. Por eso el ancho de banda alto de la memoria unificada de un M-Ultra importa tanto como su RAM.

### 9. Decodificación especulativa
Un modelo **borrador** pequeño q propone γ tokens; el modelo **objetivo** p los evalúa todos en **una** pasada en paralelo. Cada token x se acepta con probabilidad min(1, p(x)/q(x)). Al primer rechazo se muestrea de la distribución residual `norm(max(0, p − q))`. Si se aceptan todos, se toma un token extra de p.

**Teorema:** la salida sigue exactamente la distribución p. La prueba: P(x) = q(x)·min(1, p/q) + (1 − β)·residual(x) = p(x), donde β = Σ min(p, q) es la tasa de aceptación esperada. El número esperado de tokens por pasada del modelo grande es (1 − β^{γ+1})/(1 − β).

Variantes:
- **Medusa:** varias cabezas que predicen tokens futuros.
- **EAGLE:** borrador sobre las características ocultas del objetivo.
- **Lookahead / n-gramas:** sin borrador.
- Los **MTP** (*multi-token prediction*) de modelos como DeepSeek-V3 también se usan como borrador.

### 10. KV cache y PagedAttention
Para cada token pasado se guardan K y V en cada capa:

`memoria = 2 · capas · cabezas_kv · d_cabeza · longitud · bytes`

Reservar memoria contigua por el máximo desperdicia mucho (fragmentación). **PagedAttention** (vLLM) divide la caché en **bloques** de tamaño fijo con una tabla de bloques por secuencia, igual que la memoria virtual paginada:
- El desperdicio queda acotado a menos de un bloque por secuencia.
- Se pueden **compartir** prefijos (el *system prompt*) entre peticiones con *copy-on-write*.
- *Prefix caching*: se reutiliza el KV de un prefijo ya visto.

### 11. Batching continuo
El batching estático espera a que termine la secuencia más larga del lote, así que las cortas quedan bloqueadas. El **batching continuo** (Orca, vLLM) decide el lote **en cada iteración**: cuando una secuencia termina, otra entra. Sube la utilización y baja la latencia. Se complementa con *chunked prefill*, que intercala el procesamiento del prompt con la decodificación, y con la desagregación prefill/decode en clústeres.

### 12. Cuantización moderna
- **Post-entrenamiento (PTQ):**
  - **GPTQ:** minimiza el error capa por capa con información de segundo orden.
  - **AWQ:** protege los canales con activaciones grandes, escalándolos antes de cuantizar.
  - **GGUF** (llama.cpp): formato de archivo con esquemas por bloques (Q4_K_M, Q5_K_M, Q8_0…). Los "K-quants" usan superbloques con escalas cuantizadas.
  - **MLX:** cuantización afín por grupos (p. ej. 4 bits, grupo de 64) con escala y sesgo por grupo.
- **Formatos de hardware nuevos:** FP8 y FP4 (MXFP4/NVFP4) en GPUs recientes. En Apple Silicon lo práctico son los enteros de 4–8 bits de MLX/GGUF.
- **KV cache cuantizado** para contextos largos.
- **Regla práctica:** 4 bits con un buen método pierde poco en modelos grandes. Los modelos pequeños sufren más.

### 13. Servir LLMs en Mac
| Herramienta | Formato | Uso |
|---|---|---|
| `mlx_lm.server` | MLX (safetensors cuantizados) | API compatible con OpenAI, fine-tuning LoRA en la misma pila |
| llama.cpp (`llama-server`) | GGUF | Muy optimizado en Metal, decodificación especulativa con `--model-draft` |
| Ollama | GGUF | Lo más fácil, gestor de modelos, API local en :11434 |
| LM Studio | MLX o GGUF | Interfaz gráfica |

```bash
python -m mlx_lm.server --model mlx-community/Qwen2.5-7B-Instruct-4bit --port 8080
```

### 14. Multimodalidad
- **ViT:** la imagen se corta en parches p×p, cada parche se aplana y se proyecta linealmente a d dimensiones, y así obtienes una secuencia de "tokens visuales" más embeddings de posición.
- **CLIP:** un codificador de imagen y uno de texto entrenados con pérdida **contrastiva** (InfoNCE simétrica). Los pares correctos están en la diagonal de la matriz de similitudes escalada por una temperatura. Permite clasificación *zero-shot* y búsqueda de imágenes.
- **VLMs** (LLaVA y la mayoría de los modelos frontera): codificador visual (a menudo de tipo CLIP/SigLIP) → proyector (MLP) → tokens que entran al LLM junto con el texto. Los modelos nativamente multimodales se entrenan desde el inicio con tokens de varias modalidades.
- **Generación:** difusión y *flow matching* para imágenes y video (módulo 17), y tokenizadores de audio para voz.

### 15. Datos sintéticos y curación
- **Curación:**
  - Deduplicación exacta (hash) y aproximada (MinHash/LSH sobre n-gramas, Jaccard).
  - Filtros de calidad con heurísticas o clasificadores.
  - Eliminación de datos personales.
  - **Decontaminación:** quitar los ejemplos de benchmarks.
- **Datos sintéticos:**
  - Un modelo fuerte genera instrucciones, soluciones o diálogos (Self-Instruct, Evol-Instruct, textbooks "Phi").
  - Las soluciones se verifican con ejecución o tests (*rejection sampling*).
  - Riesgos: colapso del modelo si se entrena solo con datos sintéticos recursivos, sesgos heredados y licencias. Hay que mezclarlos con datos reales y verificarlos.

## Resumen
| Concepto | Idea clave |
|---|---|
| MCP | JSON-RPC estándar para conectar herramientas a cualquier LLM |
| pass^k | Confiabilidad: todos los intentos correctos |
| Prompt injection | Los datos se confunden con órdenes: defensa en capas |
| Especulativa | Borrador barato + verificación exacta = mismo resultado, más rápido |
| PagedAttention | KV cache en bloques: sin fragmentación, prefijos compartidos |
| Batching continuo | El lote se rearma en cada iteración |
| CLIP | Alinear imagen y texto con pérdida contrastiva |
