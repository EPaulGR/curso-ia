# Quiz — Módulo 18b (20 preguntas, 30 % del módulo)

Responde sin consultar. Opción múltiple: 1 punto. Abiertas: 2 puntos. Total: 28 puntos. Aprobado: ≥ 22.

1. ¿Qué propiedad hace que RoPE codifique posición relativa?
   a) Suma un vector a cada token · b) $R_m^\top R_n = R_{n-m}$ · c) Normaliza q y k · d) Usa frecuencias aprendidas
2. ¿Qué diferencia a RMSNorm de LayerNorm?
   a) No tiene parámetros · b) No resta la media · c) Normaliza por lote · d) Usa la mediana
3. Un modelo tiene 32 cabezas de consulta y 8 de K/V. ¿Cuántas consultas comparten cada K/V y en qué factor se reduce el KV cache frente a MHA?
4. Calcula el KV cache en GB (fp16) para 40 capas, $n_{kv}=8$, $d_h=128$, 32k tokens.
5. FlashAttention es:
   a) Una aproximación de baja precisión · b) Atención exacta que evita materializar la matriz T×T · c) Atención lineal · d) Un tipo de cuantización
6. En el softmax en línea, ¿por qué se multiplica el acumulador por $e^{m-m'}$?
7. Un MoE tiene 400B parámetros totales y 20B activos por token. ¿Cuál es su costo de cómputo por token y cuánta memoria necesita para inferencia? (cualitativo)
8. ¿Qué pasa sin pérdida (o mecanismo) de balanceo de carga en un MoE?
9. ¿Por qué un SSM LTI equivale a una convolución, y por qué Mamba ya no?
10. Ventaja de Mamba en inferencia frente a la atención:
    a) Mejor recuperación exacta · b) Estado de tamaño constante por token, sin KV cache · c) Menos parámetros · d) No necesita entrenamiento
11. Con $C = 6ND$ y 20 tokens por parámetro, ¿qué $N$ es óptimo para $C = 10^{23}$ FLOPs?
12. ¿Por qué los laboratorios entrenan modelos pequeños con muchos más tokens que el óptimo de Chinchilla?
13. ¿Para qué sirve la temperatura $T$ en la destilación y por qué se multiplica la pérdida por $T^2$?
14. Self-consistency requiere:
    a) Decodificación greedy · b) Muestreo con temperatura > 0 y voto de la respuesta final · c) Un PRM · d) Fine-tuning
15. Con $n=20$ muestras y $c=4$ correctas, calcula pass@1 y pass@5 (fórmula insesgada).
16. En GRPO, ¿qué reemplaza a la red de valor de PPO?
17. Si las 8 respuestas de un grupo son correctas, ¿cuál es la ventaja de cada una y qué implica para el entrenamiento?
18. Diferencia entre ORM, PRM y verificador exacto. Da una ventaja y una desventaja de cada uno.
19. Resume el debate "RLVR redistribuye vs. expande" y qué evidencia usa cada lado.
20. En flow matching con interpolación lineal, ¿cuál es el objetivo de regresión para $v_\theta(x_t, t)$ y cómo se genera una muestra?
