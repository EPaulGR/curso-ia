# Módulo 21 — MLOps y despliegue en Apple Silicon

**Duración:** 3 semanas (~40 h) · **Prerrequisitos:** 11, 13, 18

## Objetivos
- Hacer experimentos reproducibles y rastreables.
- Medir rendimiento correctamente en CPU, GPU (MPS) y MLX.
- Servir modelos como API, versionarlos, monitorearlos y desplegarlos de forma segura.
- Llevar modelos a dispositivos Apple con Core ML.

## Temario
1. Reproducibilidad: semillas, entornos (`uv`, lockfiles), versionado de datos (DVC), configuración (Hydra).
2. Rastreo de experimentos: MLflow, Weights & Biases, TensorBoard.
3. Rendimiento en Apple Silicon: memoria unificada, ancho de banda, sincronización (`torch.mps.synchronize`, `mx.eval`), Instruments/Metal System Trace, `torch.profiler`.
4. Optimización: precisión mixta, `torch.compile`, cuantización, lotes dinámicos.
5. Servir modelos: FastAPI, colas, streaming de tokens, servidores LLM (Ollama, `mlx_lm.server`, llama.cpp server con API compatible).
6. Core ML: coremltools, Neural Engine, cuantización de paletas, integración Swift.
7. Operación: registro de modelos, canario/A-B, monitoreo de deriva, alertas, CI/CD de modelos.

## Lecturas
- Chip Huyen, *Designing Machine Learning Systems*: caps. 1, 6–10.
- Chip Huyen, *AI Engineering*: caps. 9–10 (optimización de inferencia, arquitectura).
- Google, "Rules of Machine Learning" (Zinkevich); Sculley et al. 2015 "Hidden Technical Debt in ML Systems".
- Documentación: PyTorch MPS backend, MLX, coremltools, MLflow.

## Ejercicios
| # | Archivo | Tema |
|---|---|---|
| 1 | ej01_tracking.py | Rastreador de experimentos |
| 2 | ej02_benchmark.py | Medición con calentamiento y sincronización |
| 3 | ej03_servicio.py | Servicio de inferencia (+ `servidor_fastapi.py`) |
| 4 | ej04_drift.py | PSI y KS para deriva |
| 5 | ej05_dispositivo.py | Dispositivo y plan de precisión |
| 6 | ej06_registro.py | Registro y canario |
| 7 | practica-benchmark.md | Benchmark CPU vs MPS vs MLX en tu Mac |

## Criterios
Tests (30 %), quiz (30 %), proyecto (30 %), reporte de benchmark (10 %).
