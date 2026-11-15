# Respuestas — Módulo 21

1. Código, datos, entorno/dependencias, hiperparámetros/configuración (y semillas).
2. CPU y GPU comparten la RAM: sin copias, y la GPU puede usar casi toda la memoria del sistema para modelos grandes.
3. Las operaciones se encolan de forma asíncrona; sin sincronizar mides el encolado. MLX es perezoso: hay que forzar `mx.eval`.
4. La primera ejecución incluye compilación de kernels, asignación de memoria y cachés frías.
5. Rendimiento máximo = min(FLOPs pico, ancho de banda × intensidad); intensidad = FLOPs / bytes movidos.
6. Memory-bound: con batch pequeño cada token lee todos los pesos y hace pocas operaciones por byte.
7. Mediana vs. cola; la cola (p99) determina la experiencia de los usuarios peor atendidos.
8. Insertar y retirar secuencias del lote en cada paso de generación en lugar de esperar a que todas terminen.
9. Esquema/tipos, tamaño del lote, rangos o dimensiones (y autenticación).
10. Datos: cambia P(X); concepto: cambia P(Y|X).
11. Deriva severa: investigar y probablemente reentrenar.
12. Para que un usuario tenga una experiencia consistente y las métricas sean comparables.
13. Lexicográficamente '1' < '9' en el segundo componente.
14. Acelerador de redes neuronales; solo a través de Core ML (o frameworks de Apple).
15. Fuerza el cómputo del grafo perezoso; permite fusionar y optimizar operaciones.
16. Entrelazamiento de features, bucles de retroalimentación ocultos, código pegamento, dependencias de datos inestables.
17. Abierta.
