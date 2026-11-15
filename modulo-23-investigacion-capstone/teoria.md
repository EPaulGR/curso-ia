# Teoría — Investigar en IA

## 1. Leer papers: método de tres pasadas
1. **5–10 min**: título, resumen, introducción, encabezados, conclusiones, figuras. ¿Categoría? ¿Contexto? ¿Correcto? ¿Contribuciones? ¿Claridad? (las 5 C).
2. **~1 h**: lee todo sin detenerte en las pruebas; anota referencias clave y dudas; entiende figuras y tablas.
3. **4–5 h**: reconstruye el paper mentalmente: ¿podrías reimplementarlo? Identifica supuestos ocultos y debilidades.
Ficha de lectura (1 página): problema, idea clave, método, resultados, limitaciones, qué reutilizarías, preguntas abiertas.

## 2. Reproducir
- Empieza por el código oficial si existe; luego reimplementa la parte central tú mismo.
- Reproduce primero a pequeña escala (un dataset chico, modelo reducido) en tu Mac; escala en la M5 Ultra.
- Documenta todas las diferencias (datos, hiperparámetros, hardware, precisión numérica).
- Reportar "no se pudo reproducir" con evidencia también es una contribución.

## 3. Rigor experimental
- **Varias semillas** (≥ 3, ideal 5–10); reporta media ± desviación o IC bootstrap.
- **Pruebas estadísticas**: permutación o bootstrap para métricas; McNemar para dos clasificadores sobre el mismo test; corrige comparaciones múltiples (Bonferroni/Holm).
- **Baselines fuertes** y ajustados con el mismo presupuesto de búsqueda que tu método.
- **Ablaciones**: quita un componente a la vez para demostrar qué aporta.
- **Separación estricta** train/val/test; cuidado con la contaminación de benchmarks en LLMs.
- Reporta costo: horas de cómputo, hardware, energía.

## 4. Elegir un tema
Intersección de: (a) lo que te apasiona, (b) lo que tu hardware permite (Apple Silicon: inferencia y fine-tuning de LLMs grandes, modelos pequeños eficientes, metaheurísticas masivas, RL en simulación), (c) un problema con impacto local (eje BUAP: salud, medio ambiente, sociedad), (d) un hueco en la literatura.

## 5. Escribir
Estructura: resumen, introducción (problema, por qué importa, contribuciones en viñetas), trabajo relacionado, método, experimentos, resultados, limitaciones, conclusión. Figuras autoexplicativas. Escribe el resumen primero y al último.
