# Respuestas — Quiz 18b

1. **b**. La rotación compuesta depende solo de la diferencia de ángulos.
2. **b**.
3. 4 consultas por cada K/V. El caché se reduce 4× (32/8).
4. 2·40·8·128·32768·2 B = 5 368 709 120 B ≈ **5.4 GB** (5 GiB).
5. **b**.
6. Porque el máximo de la fila cambió: las exponenciales acumuladas se calcularon con el máximo viejo $m$ y hay que reescalarlas al nuevo $m'$ para que todo quede en la misma referencia. Esto mantiene la estabilidad numérica y la exactitud.
7. El cómputo por token es aproximadamente el de un denso de 20B, pero **los 400B tienen que estar en memoria** (≈ 200 GB en 4 bits). La memoria es el cuello de botella, no los FLOPs.
8. El router colapsa: pocos expertos reciben casi todos los tokens, el resto no se entrena, la capacidad efectiva baja y, en sistemas distribuidos, se desbalancea la carga y hay desbordes de capacidad.
9. Si $A$, $B$ y $C$ son constantes, la salida es $y_t=\sum_j C\bar A^j\bar B x_{t-j}$, que es una convolución con un kernel fijo. En Mamba los parámetros dependen de $x_t$, así que el "kernel" cambia en cada posición y no existe un kernel único. Se calcula con un *scan*.
10. **b**.
11. $N=\sqrt{C/(6\cdot20)}=\sqrt{10^{23}/120}\approx 2.9\times10^{10}$ (≈ 29B parámetros) y $D\approx 5.8\times10^{11}$ tokens.
12. Chinchilla solo optimiza el costo de entrenamiento. Si el modelo se va a servir miles de millones de veces, conviene un modelo más chico (inferencia más barata y más rápida) entrenado con más datos, aunque el entrenamiento cueste más.
13. $T>1$ suaviza las distribuciones y expone la "conocimiento oscuro" (las probabilidades relativas de las clases incorrectas). Los gradientes escalan como $1/T^2$, así que multiplicar por $T^2$ mantiene su magnitud comparable a la de la pérdida dura.
14. **b**.
15. pass@1 = 4/20 = **0.2**. pass@5 = 1 − C(16,5)/C(20,5) = 1 − 4368/15504 ≈ **0.718**.
16. La línea base es el **promedio de recompensas del grupo** de respuestas al mismo prompt, normalizado por su desviación estándar.
17. Todas tienen ventaja 0, así que el gradiente es nulo y el prompt no aporta nada. Se filtran o se muestrean prompts de dificultad intermedia (muestreo dinámico en DAPO).
18. **ORM:** puntúa la respuesta final. Es simple, pero da señal escasa y puede premiar razonamiento incorrecto con respuesta correcta. **PRM:** puntúa cada paso. Da señal densa y mejor asignación de crédito, pero etiquetar es caro y es más hackeable. **Verificador exacto:** comprueba la respuesta (por ejemplo, tests). Es robusto y barato, pero solo existe en dominios verificables (matemáticas, código).
19. **Redistribuye** (Yue et al. 2025): con k grande, pass@k del modelo base iguala o supera al modelo con RL, y las soluciones del modelo RL ya estaban en la distribución del base. RLVR mejora pass@1 concentrando probabilidad. **Expande** (trabajos de 2026, p. ej. ICLR 2026 con CoT-Pass@K): midiendo que el *razonamiento* sea correcto, y no solo la respuesta, en tareas sin contaminación y difíciles para el base, el modelo RL mejora de verdad. Una respuesta completa menciona las métricas, la contaminación y la dificultad de la tarea.
20. Se minimiza $\|v_\theta(x_t,t)-(x_1-x_0)\|^2$ con $x_t=(1-t)x_0+tx_1$. Para generar, se toma $x_0\sim\mathcal N(0,I)$ y se integra $\dot x=v_\theta(x,t)$ de 0 a 1 (Euler o un integrador mejor).
