# Teoría — LLMs

## 1. Qué es un LLM
Un modelo que estima P(x_t | x_<t) sobre secuencias de tokens, entrenado con máxima verosimilitud (entropía cruzada) en billones de tokens. La pérdida promedio L se reporta como **perplejidad** = exp(L). Generar texto = muestrear repetidamente de esa distribución.

## 2. Tokenización
- **BPE**: empieza con bytes (256 símbolos) y fusiona iterativamente el par más frecuente. El vocabulario final (32k–200k) equilibra longitud de secuencia y tamaño de embedding.
- Consecuencias prácticas: los números, el código y los idiomas distintos al inglés suelen requerir más tokens ("impuesto del tokenizador" para el español). Muchos errores raros de LLMs (contar letras, aritmética) vienen de la tokenización.

## 3. Leyes de escalamiento
La pérdida baja como ley de potencia en parámetros N, datos D y cómputo C ≈ 6·N·D FLOPs. Chinchilla: para un presupuesto fijo, lo óptimo es D ≈ 20·N tokens. Hoy se "sobreentrena" (D ≫ 20N) porque la inferencia barata importa más.

## 4. Arquitectura moderna (decoder-only)
Embeddings → N bloques [RMSNorm → atención causal multi-cabeza con RoPE y GQA → residual → RMSNorm → MLP SwiGLU → residual] → norma final → proyección al vocabulario.
- **GQA** (grouped-query attention): varias cabezas de query comparten K/V → KV cache más pequeño.
- **MoE**: el MLP se divide en expertos y un router activa k de ellos por token: muchos parámetros totales, pocos activos. Excelente para Mac: la memoria unificada guarda todos los expertos, el cómputo solo usa los activos.

## 5. Del modelo base al asistente
1. **SFT**: ajuste supervisado con pares instrucción→respuesta.
2. **RLHF**: modelo de recompensa entrenado con preferencias humanas + PPO con penalización KL respecto al modelo SFT.
3. **DPO**: optimiza directamente las preferencias sin modelo de recompensa explícito; más simple y estable.

## 6. PEFT y LoRA
En lugar de ajustar W (d×d), se aprende ΔW = B·A con rango r ≪ d. Para d=4096 y r=16: 131k parámetros contra 16.7M por matriz (≈0.8 %). B se inicializa en cero para que el modelo inicial sea idéntico. Tras entrenar se puede **fusionar** W + (α/r)BA: sin costo de inferencia. **QLoRA** = modelo base cuantizado en 4-bit + adaptadores LoRA en alta precisión.

## 7. Inferencia
- **KV cache**: guarda K y V de los tokens previos; memoria = 2 · capas · contexto · d_kv · bytes. Con contextos largos puede superar a los pesos.
- **Muestreo**: temperatura (aplana/afila), top-k, top-p (núcleo), min-p; greedy y beam search para tareas deterministas.
- **Decodificación especulativa**: un modelo pequeño propone k tokens, el grande verifica en una pasada.
- **Cuantización**: int8 simétrica, 4-bit por grupos con escala y cero (GGUF Q4_K, MLX 4-bit). Pérdida típica de calidad pequeña a 4-bit, notable a 2–3 bits.

## 8. LLMs en Apple Silicon
- La inferencia está limitada por **ancho de banda de memoria**: tokens/s ≈ ancho de banda / bytes de pesos leídos por token. Por eso las Ultra (ancho de banda muy alto) son tan buenas para LLMs.
- MLX: arrays perezosos, memoria unificada, `mlx_lm.lora` para ajustar, `mlx_lm.fuse` para fusionar, `mlx_lm.convert -q` para cuantizar.
- Ollama/llama.cpp usan GGUF + Metal.

## 9. Riesgos y límites
Alucinaciones, contaminación de benchmarks, sesgos de los datos, inyección de prompts (ver módulos 19 y 22).
