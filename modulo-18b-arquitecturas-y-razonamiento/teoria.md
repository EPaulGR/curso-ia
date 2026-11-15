# Teoría — Arquitecturas modernas y razonamiento

## 1. Del Transformer de 2017 al LLM moderno

| Componente | Transformer original | LLM típico 2024–2026 |
|---|---|---|
| Posición | Senoidal absoluta, sumada | **RoPE** aplicada a q y k |
| Normalización | LayerNorm post-capa | **RMSNorm pre-capa** |
| FFN | ReLU, 4d | **SwiGLU**, ≈ 8/3·d |
| Atención | MHA | **GQA** (o MLA), ventana deslizante en algunas capas |
| Densidad | Densa | Densa **o MoE** (cientos de expertos finos + compartidos) |
| Contexto | 512 | 128k – 1M+ tokens |
| Post-entrenamiento | — | SFT → preferencia (DPO/RLHF) → **RL con recompensas verificables** |

## 2. RoPE
Para cada par de dimensiones $(x_{2i}, x_{2i+1})$ con frecuencia $\theta_i = b^{-2i/d}$:

$$\begin{pmatrix}x'_{2i}\\x'_{2i+1}\end{pmatrix} = \begin{pmatrix}\cos m\theta_i & -\sin m\theta_i\\ \sin m\theta_i & \cos m\theta_i\end{pmatrix}\begin{pmatrix}x_{2i}\\x_{2i+1}\end{pmatrix}$$

Como $R_m^\top R_n = R_{n-m}$, se cumple $\langle R_m q, R_n k\rangle = \langle q, R_{n-m}k\rangle$: la atención depende de la **distancia relativa**. Es una rotación, así que conserva la norma.
**Extensión de contexto:** *Position Interpolation* escala $m \to m\cdot L/L'$; *NTK-aware* y **YaRN** cambian la base $b$ por frecuencia. Así un modelo entrenado con 8k tokens se ajusta a 128k con poco fine-tuning.

## 3. RMSNorm y SwiGLU
$\text{RMSNorm}(x) = \dfrac{x}{\sqrt{\tfrac1d\sum x_i^2+\epsilon}}\odot g$. Es más barata que LayerNorm (no resta la media) y funciona igual de bien.
$\text{SwiGLU}(x) = (\text{SiLU}(xW_1)\odot xW_3)W_2$. La compuerta multiplicativa mejora la perplejidad a igual cómputo.

## 4. GQA y KV cache
Al decodificar, cada token nuevo necesita K y V de **todos** los anteriores, así que se guardan en caché:

$$\text{bytes} = 2\cdot \text{capas}\cdot n_{kv}\cdot d_h\cdot T\cdot \text{bytes por valor}$$

Ejemplo: 80 capas, $n_{kv}=8$, $d_h=128$, $T=128\text{k}$, fp16 → ≈ 42 GB **por secuencia**. Con MHA ($n_{kv}=64$) serían 336 GB. GQA reduce el caché por un factor $n_q/n_{kv}$ con poca pérdida de calidad.
**MLA** (DeepSeek-V2/V3) comprime K y V a un vector latente de baja dimensión y lo reproyecta. El caché queda aún más chico.
En Mac importa mucho, porque el caché compite con los pesos por la memoria unificada.

## 5. Atención eficiente
La atención ingenua escribe la matriz $T\times T$ en memoria (HBM). FlashAttention divide Q, K y V en bloques que caben en SRAM y usa el **softmax en línea**:

```
m ← -∞, l ← 0, o ← 0
para cada bloque (K_j, V_j):
    s  ← Q K_jᵀ/√d
    m' ← max(m, max_fila(s))
    l  ← l·e^{m-m'} + Σ e^{s-m'}
    o  ← o·e^{m-m'} + e^{s-m'} V_j
    m  ← m'
salida = o / l
```

El resultado es **exacto**, no una aproximación. La memoria baja de O(T²) a O(T), y es más rápido porque mueve menos datos. En Apple Silicon: PyTorch ≥ 2.x trae `scaled_dot_product_attention` y FlexAttention con backend MPS, y MLX tiene `mx.fast.scaled_dot_product_attention`.
Otras variantes: atención por ventana deslizante (Mistral, Gemma), atención lineal y atención dispersa.

## 6. Mixture of Experts
Se reemplaza la FFN por $E$ expertos y un router $g(x)=\text{softmax}(\text{topk}(xW_r))$:
$y = \sum_{e\in \text{topk}} g_e(x)\,\text{FFN}_e(x)$.
- **Parámetros totales ≫ parámetros activos.** Un MoE de 600B con 37B activos cuesta por token lo que un modelo denso de ~37B, pero **tiene que caber completo en memoria**. Por eso una Mac Studio con mucha RAM unificada es atractiva para inferencia de MoE.
- **Balanceo de carga.** Sin él, el router colapsa en pocos expertos. La pérdida de Switch es $L_{aux}=E\sum_e f_eP_e$. DeepSeek-V3 usa en cambio un sesgo por experto, sin pérdida auxiliar.
- **Expertos compartidos.** Algunos expertos procesan todos los tokens y otros son finos y especializados.

## 7. Modelos de espacio de estados (SSM)
Versión continua: $h'(t)=Ah(t)+Bx(t)$, $y=Ch$. Discretizada con paso $\Delta$: $\bar A=e^{\Delta A}$, $\bar B\approx\Delta B$.
- **S4 (LTI):** $A$, $B$ y $C$ son fijos, así que el modelo equivale a una convolución con kernel $K_j = C\bar A^j\bar B$. Entrena en paralelo con FFT.
- **Mamba:** $\Delta$, $B$ y $C$ **dependen de la entrada**, lo que permite "seleccionar" qué recordar. Deja de ser una convolución y se calcula con un *scan* paralelo en hardware. Inferencia O(1) por token y sin KV cache.
- **Híbridos** (Jamba, varios modelos de 2025–2026): mezclan capas de atención con capas SSM o de atención lineal para tener contexto largo barato y conservar la recuperación exacta que da la atención.

## 8. Contexto largo
Hay tres problemas: (1) la posición, resuelta con extensión de RoPE; (2) la memoria, que se ataca con GQA/MLA, cuantización del KV cache y ventanas; (3) el uso real del contexto, porque los modelos se "pierden en el medio" (*lost in the middle*). Se evalúa con needle-in-a-haystack, RULER y tareas de varios saltos. Un contexto largo no reemplaza siempre a RAG (módulo 19): compáralos por costo y precisión.

## 9. Leyes de escalamiento
$L(N,D) = E + \dfrac{A}{N^\alpha} + \dfrac{B}{D^\beta}$. Con cómputo $C\approx 6ND$ FLOPs, Chinchilla encontró que lo óptimo es $N\propto C^{0.5}$ y $D\propto C^{0.5}$, es decir **≈ 20 tokens por parámetro**.
En la práctica de 2024–2026 se **sobre-entrena**: modelos de 8B con más de 15T tokens (casi 2000 tokens por parámetro). Sale más caro entrenarlos, pero son mucho más baratos de servir. El óptimo depende de cuánto se va a usar el modelo en inferencia.
Las leyes de escalamiento también se aplican a la inferencia: más cómputo al responder da mejor precisión (sección 11).

## 10. Destilación
$L = (1-\lambda)\,CE(y, s) + \lambda\,T^2\,KL(\text{softmax}(t/T)\,\|\,\text{softmax}(s/T))$.
Variantes con LLMs: destilar **trazas de razonamiento** de un modelo grande en uno pequeño mediante SFT. Las versiones R1-Distill de 1.5B a 70B salieron así. También existe la destilación *on-policy*, donde el alumno genera y el maestro corrige.

## 11. Razonamiento en inferencia (*test-time compute*)
- **Chain-of-thought:** pedir pasos intermedios. Funciona porque los tokens intermedios son "memoria de trabajo" y cómputo adicional.
- **Self-consistency:** muestrear $k$ cadenas con temperatura > 0 y quedarse con la respuesta por **voto de mayoría**.
- **Best-of-N con verificador:** un verificador puntúa cada candidato. Puede ser un ORM (puntúa la respuesta final), un PRM (puntúa cada paso) o un verificador exacto (tests, comprobador de matemáticas).
- **Búsqueda:** beam search guiado por PRM, MCTS sobre pasos de razonamiento. Aquí vuelve el módulo 06.
- **pass@k insesgado:** con $n$ muestras y $c$ correctas, $\text{pass@}k = 1-\binom{n-c}{k}/\binom{n}{k}$.
- **Modelos de razonamiento** (o1, R1 y sucesores): el modelo aprende por RL a generar cadenas largas y a autocorregirse. El "presupuesto de pensamiento" se vuelve un parámetro más de inferencia.

## 12. RLVR y GRPO
**RLVR:** se usa RL con una recompensa que se puede **verificar automáticamente** (respuesta numérica correcta, tests que pasan) en lugar de un modelo de recompensa aprendido. Es difícil de "hackear" y escala. Desde DeepSeek-R1 (2025) es la receta dominante para entrenar razonamiento.

**GRPO:** para cada prompt $q$ se muestrean $G$ respuestas $o_1..o_G$ con recompensas $r_i$.
$$\hat A_i = \frac{r_i-\text{mean}(r)}{\text{std}(r)}$$
$$J = \mathbb E\Big[\tfrac1G\sum_i \min(\rho_i \hat A_i, \text{clip}(\rho_i,1\pm\epsilon)\hat A_i)\Big] - \beta\,KL(\pi_\theta\|\pi_{ref})$$
con $\rho_i=\pi_\theta(o_i)/\pi_{old}(o_i)$. No hace falta un crítico (red de valor) como en PPO, porque la línea base es el promedio del grupo. Variantes: Dr. GRPO, DAPO (clip asimétrico, muestreo dinámico), GSPO.
Detalle práctico: si todas las respuestas del grupo son iguales (todas bien o todas mal), la ventaja es 0 y no hay señal. Por eso importa elegir prompts de dificultad intermedia (*curriculum*).

**PRM vs ORM:** el PRM da señal densa paso a paso pero es caro de etiquetar y más fácil de hackear. El ORM o el verificador exacto es simple y robusto. En 2026 hay mucha investigación sobre señales intermedias más densas (condicionar en planes, PRMs implícitos).

**El debate (2025–2026):** Yue et al. observaron que con $k$ grande, pass@k del modelo base **iguala o supera** al modelo después de RLVR. Su lectura es que RLVR *redistribuye* probabilidad hacia caminos que el modelo ya sabía recorrer, y no *expande* su capacidad. Trabajos posteriores (p. ej. ICLR 2026) responden que, si se mide la corrección del razonamiento y no solo de la respuesta (CoT-Pass@K), y en tareas sin contaminación de datos, sí hay mejora real. Saber argumentar ambos lados es parte de este módulo.

**Extensiones abiertas:** recompensas verificables fuera de matemáticas y código (verificadores universales, recompensas basadas en referencias), RL sin verificador (voto de mayoría, auto-certeza, entropía), RL para agentes de tareas largas (módulo 19b) y RL en preentrenamiento.

## 13. Flow matching
Se define un camino de probabilidad entre ruido $x_0$ y datos $x_1$: $x_t=(1-t)x_0+tx_1$. El campo de velocidad condicional es $u = x_1 - x_0$. Se entrena con
$$\min_\theta \mathbb E_{t,x_0,x_1}\|v_\theta(x_t,t)-(x_1-x_0)\|^2$$
y para generar se resuelve la EDO $\dot x = v_\theta(x,t)$ de $t=0$ a $1$.
Ventajas frente a DDPM: es una regresión simple, tiene trayectorias más rectas (necesita menos pasos) y la **rectificación** iterada las endereza aún más. Es la base de los generadores de imagen y video recientes (p. ej. Stable Diffusion 3, Flux).

## 14. Qué cabe en tu Mac Studio
| Tarea | Memoria aprox. |
|---|---|
| Inferencia de denso 70B en 4 bits | ~40 GB + KV cache |
| Inferencia de MoE de ~600B en 4 bits | ~350 GB (solo con configuraciones de RAM muy grandes) |
| LoRA de 8B en bf16 con MLX | ~20–24 GB |
| GRPO de 0.5–1.5B (política + referencia + rollouts) | 16–40 GB |
| Preentrenar un modelo de 100–300M desde cero | < 16 GB, días de cómputo |
Usa `ej03.bytes_kv_cache` y la calculadora del módulo 18 antes de cada experimento.
