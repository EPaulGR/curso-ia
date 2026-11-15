# Teoría — MLOps en Apple Silicon

## 1. Por qué MLOps
El modelo es una pequeña parte del sistema; la mayor parte del trabajo (y de la deuda técnica) está en datos, configuración, servicio y monitoreo. Un modelo que no se puede reproducir, medir ni revertir no está en producción: está en riesgo.

## 2. Reproducibilidad
Fija semillas (`random`, `numpy`, `torch`, `mx.random.seed`), versiona código, datos y entorno, y registra hiperparámetros y métricas de cada corrida. Ojo: en GPU algunas operaciones no son deterministas.

## 3. Arquitectura de Apple Silicon
- **Memoria unificada**: CPU, GPU y Neural Engine comparten la misma RAM; no hay copias host↔device como en CUDA. MLX aprovecha esto explícitamente.
- **Ancho de banda**: el cuello de botella de la inferencia de LLMs; las variantes Max/Ultra lo multiplican.
- **Neural Engine (ANE)**: muy eficiente para inferencia de redes compatibles vía Core ML; no se programa directamente.
- **MPS** (PyTorch) y **MLX** usan la GPU vía Metal. MLX es perezoso: nada se calcula hasta `mx.eval`.

## 4. Medir bien
Calentamiento (compilación de kernels, cachés), sincronización (las GPU son asíncronas), varias repeticiones, reportar mediana y p95, y comparar contra el límite teórico (FLOPs pico o ancho de banda). Un modelo es *compute-bound* o *memory-bound* según su intensidad aritmética (modelo roofline).

## 5. Servir
- Batch vs. tiempo real; latencia p50/p95/p99 y throughput.
- Validación estricta de entradas, versionado de la API y del modelo, health checks.
- LLMs: streaming, KV cache compartido, batching continuo; servidores con API compatible con OpenAI facilitan cambiar de backend.

## 6. Operar
- **Registro de modelos** con etapas (staging, producción, archivado).
- **Canario/A-B**: enrutado determinista por usuario a un porcentaje pequeño y métricas comparadas.
- **Deriva**: de datos (PSI, KS), de concepto (cae el desempeño con etiquetas nuevas). Alertas y reentrenamiento.
- **CI/CD**: tests de datos y de modelo (umbrales de métricas) antes de promover.

## 7. Core ML
`coremltools` convierte modelos PyTorch (trace/export) a `.mlpackage`; permite cuantización y paletización de pesos, y usa CPU/GPU/ANE automáticamente en macOS/iOS. Ideal para apps nativas en Swift.
