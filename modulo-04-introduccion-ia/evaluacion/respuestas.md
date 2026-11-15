# Respuestas — Módulo 04

1. Pensar como humano, actuar como humano, pensar racionalmente, actuar racionalmente. AIMA adopta el agente racional: es más general que la lógica y matemáticamente definible.
2. Elige la acción que maximiza el desempeño esperado dada la información disponible. No: racional ≠ omnisciente; maximiza lo *esperado*, no el resultado real.
3. Un interrogador conversa por texto con humano y máquina; si no distingue, la máquina "pasa". Objeciones: habitación china (sin comprensión), antropocentrismo, se puede engañar con trucos (ELIZA).
4. Modelo de neurona umbral; redes de ellas computan cualquier función lógica.
5. Taller de verano que acuñó "IA": McCarthy, Minsky, Shannon, Rochester, Newell, Simon.
6. Probó limitaciones del perceptrón de una capa (XOR, conectividad) y desalentó el financiamiento de redes neuronales.
7. Programas con reglas de expertos humanos + motor de inferencia. Decayeron por fragilidad, mantenimiento costoso y cuello de botella de adquisición de conocimiento.
8. Deep Blue: búsqueda α-β con función de evaluación hecha a mano y hardware especial. AlphaGo: MCTS guiado por redes de política y valor aprendidas con RL. Se pasó de conocimiento codificado a aprendido.
9. Un sistema de símbolos físicos tiene los medios necesarios y suficientes para la acción inteligente general (Newell & Simon, 1976).
10. Simbólico: reglas explícitas, aprendizaje limitado, muy explicable. Conexionista: pesos distribuidos, aprende de datos con gradiente, poco explicable. Evolutivo: población de soluciones, aprende por selección, explicabilidad media.
11. Combina redes neuronales con razonamiento simbólico; p. ej. AlphaGeometry, LLM que genera código verificado por un intérprete, LLM + solver.
12. P: clics, tiempo de visualización, satisfacción; E: usuarios, catálogo; A: lista de recomendaciones; S: historial, calificaciones, contexto.
13. Parcialmente observable, estocástico, secuencial, estático, discreto, multiagente (competitivo), conocido.
14. Puede entrar en ciclos infinitos porque no recuerda lo ya visto; necesita estado o aleatorización.
15. Metas: binario (logra o no). Utilidad: grado de preferencia entre estados, permite compromisos y riesgo.
16. Filosofía (razonamiento, mente), matemáticas (lógica, probabilidad), economía (decisión, utilidad), neurociencia (neuronas), psicología (cognición), control (retroalimentación), lingüística (gramáticas).
17. Los métodos generales que aprovechan el cómputo (búsqueda y aprendizaje) superan a largo plazo al conocimiento humano codificado. Crítica abierta: costos energéticos, datos, estructura inductiva sí ayuda.
18. Ejemplos: agentes autónomos (acciones no deseadas), multimodalidad (deepfakes), IA en dispositivo (eficiencia vs. capacidad), modelos fundacionales (concentración de poder).
19. XOR no es linealmente separable y un perceptrón traza una sola frontera lineal. Se resolvió con capas ocultas entrenadas por backpropagation.
