# Teoría — Aprendizaje por refuerzo

## 1. El problema
Un agente observa un estado s, toma una acción a, recibe recompensa r y pasa a s'. Busca maximizar el retorno esperado G = Σ γ^t r_t. A diferencia del aprendizaje supervisado, no hay etiquetas: hay que **explorar** y lidiar con recompensas retrasadas (asignación de crédito).

## 2. MDP y Bellman
MDP = (S, A, P, R, γ). Funciones de valor:
- V^π(s) = E[r + γV^π(s')], Q^π(s,a) = E[r + γ Σ π(a'|s')Q^π(s',a')].
- Óptimas: V*(s) = max_a Σ P(s'|s,a)[r + γV*(s')].
**Iteración de valor** aplica el operador de Bellman óptimo (contracción con factor γ → converge). **Iteración de política** alterna evaluación exacta y mejora greedy; converge en pocas iteraciones.

## 3. Aprendizaje sin modelo
- **Monte Carlo**: promedia retornos completos; sin sesgo, alta varianza.
- **TD(0)**: V(s) ← V(s) + α[r + γV(s') − V(s)]; usa bootstrapping.
- **SARSA** (on-policy) aprende el valor de la política que sigue (incluida su exploración) → más conservador.
- **Q-learning** (off-policy) aprende Q* aunque explore → más agresivo; en "cliff walking" toma el camino óptimo pero cae más durante el aprendizaje.

## 4. Deep RL
La "tríada mortal": aproximación de funciones + bootstrapping + off-policy puede divergir. DQN la estabiliza con **replay buffer** (rompe correlaciones) y **red objetivo** (objetivos estables). Double DQN reduce la sobreestimación del max.

## 5. Gradientes de política
∇J(θ) = E[∇ log π(a|s) · (G − b)]. El baseline b reduce varianza sin introducir sesgo. Actor-crítico usa un crítico V(s) como baseline (ventaja A = Q − V, o GAE). **PPO** limita el cambio de política con un cociente recortado: es el estándar de facto (incluido en RLHF).

## 6. Planificación
MCTS + red de política/valor = AlphaZero (conecta con el módulo 06). MuZero además aprende el modelo del entorno.

## 7. RL para LLMs
1. Se recolectan pares (respuesta preferida, rechazada).
2. Modelo de recompensa con pérdida Bradley-Terry.
3. PPO maximiza recompensa − β·KL(π || π_ref).
**DPO** muestra que la política óptima de ese objetivo tiene forma cerrada y entrena directamente con las preferencias. Los modelos de razonamiento recientes usan RL con recompensas verificables (resultados de matemáticas, tests de código) y variantes como GRPO.

## 8. En tu Mac
Entornos de gymnasium y redes pequeñas: CPU suele ser igual o más rápida que MPS para MLPs diminutos (el costo está en el entorno). Usa entornos vectorizados para aprovechar los núcleos.
