# Curso: De cero a experto en Inteligencia Artificial

Curso autodidacta construido a partir del programa oficial **CCOS 258 – Inteligencia Artificial (BUAP, FCC, actualización 2022)** y ampliado hasta cubrir la IA moderna completa: fundamentos matemáticos, IA clásica, machine learning, deep learning, LLMs, aprendizaje por refuerzo, MLOps e investigación.

Todo está pensado para **Mac con Apple Silicon** (sin NVIDIA), con vista a la Mac Studio M5 Ultra.

---

## 1. Empieza aquí

1. Lee [00-guia/libros-recomendados.md](00-guia/libros-recomendados.md) y consigue los libros de prioridad **A**.
2. Configura tu Mac con [00-guia/setup-mac.md](00-guia/setup-mac.md).
3. Lleva tu avance en [00-guia/progreso.md](00-guia/progreso.md).
4. Avanza módulo por módulo, en orden. No saltes la Fase 0: es lo que separa a un usuario de IA de un experto.

## 2. ¿Qué lenguaje usar en Mac?

**Python** es la respuesta, sin discusión, para el 95 % del curso:

| Necesidad | Herramienta en Mac | Por qué |
|---|---|---|
| Lenguaje principal | **Python 3.13** (3.11–3.13) | Todo el ecosistema de IA (papers, librerías, modelos) vive aquí |
| Deep learning general | **PyTorch + backend MPS** | Usa la GPU de Apple Silicon vía Metal (`device="mps"`) |
| LLMs, entrenamiento y fine-tuning local | **MLX / mlx-lm** (Apple) | Diseñado para memoria unificada: en un M5 Ultra con mucha RAM puedes cargar modelos que en GPUs de consumo NVIDIA no caben |
| Inferencia local de LLMs | **Ollama, llama.cpp (Metal), LM Studio** | Corren modelos cuantizados (GGUF/MLX) muy rápido |
| ML clásico | scikit-learn, XGBoost/LightGBM | CPU de Apple es excelente para esto |
| Despliegue en dispositivos Apple | **Core ML + coremltools**, Swift | Neural Engine |
| Rendimiento extremo (opcional, Fase 6) | C++ / Metal / Swift | Kernels propios |

**Qué evitar:** tutoriales que dependan de CUDA (`.cuda()`, bitsandbytes, flash-attn de NVIDIA, vLLM en GPU). En el curso siempre se indica la alternativa (MPS, MLX, o alquilar GPU en la nube por horas cuando de verdad haga falta).

## 3. Mapa del curso (26 módulos, ~14–20 meses a 10–15 h/semana)

| Fase | Módulo | Tema | Relación BUAP |
|---|---|---|---|
| **0. Fundamentos** | [00](modulo-00-python-y-entorno) | Python para IA y entorno Mac | Prerrequisito |
| | [01](modulo-01-matematicas) | Álgebra lineal, cálculo y optimización | Prerrequisito |
| | [02](modulo-02-probabilidad-estadistica) | Probabilidad, estadística, teoría de la información | Prerrequisito |
| | [03](modulo-03-logica-y-algoritmos) | Lógica, algoritmos y estructuras de datos | Lógica Matemática (precedente) |
| **1. Temario BUAP** | [04](modulo-04-introduccion-ia) | Historia, conceptos y paradigmas de la IA | **Unidad 1** |
| | [05](modulo-05-busqueda) | Búsqueda: BFS, DFS, primero el mejor, A*, IDA* | **Unidad 2** |
| | [06](modulo-06-busqueda-adversarial) | Minimax, poda α-β, MCTS | **Unidad 3** |
| | [07](modulo-07-metaheuristicas-multiobjetivo) | Búsqueda local, tabú, AG, ACO, inmunes, NSGA-II | **Unidad 4** |
| **2. IA clásica avanzada** | [08](modulo-08-csp-y-planificacion) | Satisfacción de restricciones y planificación | Ampliación |
| | [09](modulo-09-conocimiento-y-logica) | Lógica de primer orden, sistemas expertos, Prolog | Ampliación |
| | [10](modulo-10-razonamiento-probabilistico) | Redes bayesianas, HMM, lógica difusa | Ampliación |
| **3. Machine Learning** | [11](modulo-11-ml-clasico) | Regresión, clasificación, árboles, SVM, ensembles | Aprendizaje Automático (consecuente) |
| | [12](modulo-12-no-supervisado) | Clustering, PCA, t-SNE/UMAP | |
| | [13](modulo-13-redes-neuronales) | Redes neuronales desde cero y PyTorch en MPS | |
| **4. Deep Learning** | [14](modulo-14-vision-cnn) | CNNs y visión por computadora | |
| | [15](modulo-15-secuencias-nlp) | RNN/LSTM, embeddings, NLP | |
| | [16](modulo-16-transformers) | Atención y Transformers (mini-GPT) | |
| | [17](modulo-17-modelos-generativos) | VAE, GAN, difusión | |
| **5. IA moderna** | [18](modulo-18-llms) | LLMs, tokenización, LoRA con MLX, cuantización | |
| | [18b](modulo-18b-arquitecturas-y-razonamiento) | Arquitecturas modernas (RoPE, MoE, Mamba), razonamiento, RLVR/GRPO, flow matching | Actualización 2025–26 |
| | [19](modulo-19-rag-y-agentes) | RAG, agentes, tool use, evaluación | |
| | [19b](modulo-19b-agentes-e-inferencia) | MCP, agentes de código y computer use, decodificación especulativa, multimodal | Actualización 2025–26 |
| | [20](modulo-20-aprendizaje-refuerzo) | MDP, Q-learning, DQN, policy gradients, RLHF | |
| **6. Experto** | [21](modulo-21-mlops-apple-silicon) | MLOps y despliegue en Apple Silicon | |
| | [22](modulo-22-etica-seguridad-alineamiento) | Ética, interpretabilidad, alineamiento | Eje transversal BUAP |
| | [23](modulo-23-investigacion-capstone) | Leer y reproducir papers, proyecto final | Educación para la investigación |

## 4. Estructura de cada módulo

```
modulo-XX-nombre/
  README.md          objetivos, temario, lecturas (capítulos), duración, criterios
  teoria.md          apuntes del módulo
  ejercicios/        enunciados + esqueletos con TODO  ← aquí trabajas tú
  soluciones/        soluciones de referencia (ábrelas solo después de intentarlo)
  evaluacion/
    quiz.md          examen teórico
    respuestas.md    clave de respuestas
    test_*.py        tests automáticos de tus ejercicios
  proyecto/README.md proyecto integrador con rúbrica
```

## 5. Cómo evaluarte

Calificación por módulo (inspirada en los criterios BUAP):

| Componente | Peso |
|---|---|
| Ejercicios (tests en verde) | 30 % |
| Quiz teórico | 30 % |
| Proyecto del módulo (rúbrica) | 30 % |
| Lecturas / ensayo / explicación en voz alta | 10 % |

Aprobar un módulo = **≥ 8/10** (más exigente que el 6 de la universidad: la meta es ser experto).

```bash
# Ejecuta los tests de un módulo contra TU código
pytest modulo-05-busqueda

# Verifica que las soluciones de referencia pasan
SOLUCIONES=1 pytest modulo-05-busqueda
```

## 6. Regla de oro
Implementa primero desde cero (NumPy / Python puro), después usa la librería. Si puedes explicar un algoritmo en una pizarra y programarlo sin mirar, lo dominas.
