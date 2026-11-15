# Proyecto 21 — Del notebook a producción local

Toma un modelo de un módulo previo (p. ej. el clasificador del 11 o el modelo ajustado del 18) y:
1. Entrenamiento reproducible con configuración y rastreo (tu rastreador o MLflow).
2. Servicio FastAPI con validación, `/salud`, `/predecir`, versionado; tests de integración con `TestClient`.
3. Benchmark de latencia p50/p95 y throughput en CPU vs MPS/MLX.
4. Exportación a Core ML y una mini app/script que la use.
5. Monitoreo de deriva con datos simulados desplazados y alerta.
6. Registro con staging → producción y canario al 10 %.

## Rúbrica (100 pts)
| Criterio | Pts |
|---|---|
| Reproducibilidad y rastreo | 15 |
| Servicio robusto y probado | 25 |
| Benchmark riguroso | 20 |
| Core ML funcionando | 15 |
| Monitoreo y despliegue seguro | 15 |
| Documentación | 10 |
