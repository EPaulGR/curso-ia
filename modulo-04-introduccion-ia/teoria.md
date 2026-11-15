# Teoría — Introducción a la IA

## 1. ¿Qué es la IA? Cuatro enfoques (Russell & Norvig)
| | Humano | Racional |
|---|---|---|
| **Pensar** | Modelado cognitivo | Leyes del pensamiento (lógica) |
| **Actuar** | Test de Turing | **Agente racional** (enfoque del libro) |

Un **agente racional** elige la acción que maximiza la medida de desempeño esperada, dada la secuencia de percepciones y su conocimiento.

## 2. Antecedentes
- **Lógica:** Aristóteles (silogismos), Boole (1854, álgebra), Frege (lógica de predicados).
- **Computabilidad:** Turing (1936) máquina universal; problema de la parada; Church.
- **Neuronas formales:** McCulloch & Pitts (1943) demostraron que redes de neuronas umbral computan cualquier función lógica.
- **Cibernética:** Wiener (1948), retroalimentación y control.
- **Turing (1950):** "¿Pueden pensar las máquinas?" → juego de imitación.

## 3. Historia resumida
| Año | Hito | Paradigma |
|---|---|---|
| 1956 | Taller de Dartmouth: nace el término "Inteligencia Artificial" | — |
| 1956–59 | Logic Theorist, General Problem Solver (Newell & Simon) | Simbólico |
| 1958 | Perceptrón (Rosenblatt) | Conexionista |
| 1966 | ELIZA (Weizenbaum) | Simbólico |
| 1969 | *Perceptrons* (Minsky & Papert): un perceptrón no resuelve XOR | — |
| 1970s | Primer invierno; Holland y algoritmos genéticos (1975) | Evolutivo |
| 1980s | Sistemas expertos (MYCIN, XCON); Prolog; boom comercial | Simbólico |
| 1986 | Backpropagation (Rumelhart, Hinton, Williams) | Conexionista |
| 1987–93 | Segundo invierno (caída de máquinas Lisp) | — |
| 1988 | Redes bayesianas (Pearl) | Probabilístico |
| 1997 | Deep Blue vence a Kasparov (búsqueda α-β) | Búsqueda |
| 2012 | AlexNet gana ImageNet en GPU | Deep learning |
| 2016 | AlphaGo: MCTS + redes + RL | Híbrido |
| 2017 | *Attention Is All You Need* (Transformer) | Conexionista |
| 2020 | GPT-3; AlphaFold 2 | |
| 2022 | ChatGPT (RLHF) | |
| 2024–26 | Modelos de razonamiento, agentes con herramientas, IA en el dispositivo | |

## 4. Paradigmas
### 4.1 Simbólico (GOFAI)
Hipótesis del sistema de símbolos físicos (Newell & Simon): manipular símbolos es necesario y suficiente para la inteligencia. Herramientas: lógica, reglas, búsqueda, planificación. **Fortalezas:** explicable, preciso. **Debilidades:** frágil, cuello de botella de adquisición de conocimiento, mal con percepción.

### 4.2 Conexionista
Conocimiento distribuido en pesos de redes neuronales aprendidos de datos. **Fortalezas:** percepción, lenguaje, escalado con datos/cómputo. **Debilidades:** opacidad, alucinaciones, hambre de datos.

### 4.3 Evolutivo
Inspirado en Darwin: población, selección, cruza, mutación (Holland, Rechenberg, Koza). Optimización sin gradiente; se estudia en el módulo 07.

### 4.4 Otros enfoques
- **Probabilístico/bayesiano:** incertidumbre explícita (Pearl).
- **Conductual/encarnado:** Brooks (1986), arquitectura de subsunción; inteligencia sin representación.
- **Neurosimbólico / híbrido:** AlphaGo, LLM + herramientas + verificadores.
- **Inteligencia de enjambre:** ACO, PSO.

## 5. Agentes y entornos
**PEAS:** *Performance, Environment, Actuators, Sensors.* Ejemplo taxi autónomo: P = seguridad, rapidez, legalidad, confort; E = calles, tráfico, peatones; A = volante, acelerador, freno; S = cámaras, LIDAR, GPS.

Propiedades de entornos: totalmente/parcialmente observable · determinista/estocástico · episódico/secuencial · estático/dinámico · discreto/continuo · uno/multiagente · conocido/desconocido.

Tipos de agente:
1. **Reactivo simple:** reglas condición–acción sobre la percepción actual.
2. **Basado en modelo:** mantiene estado interno del mundo.
3. **Basado en metas:** busca/planifica para alcanzar metas (módulos 05–08).
4. **Basado en utilidad:** maximiza utilidad esperada.
5. **Que aprende:** elemento de desempeño + crítico + elemento de aprendizaje + generador de problemas.

## 6. Debates clave
- Habitación china (Searle, 1980): ¿sintaxis basta para semántica?
- IA débil vs fuerte vs AGI.
- *The Bitter Lesson* (Sutton): los métodos generales que escalan con cómputo (búsqueda y aprendizaje) terminan ganando a los que codifican conocimiento humano.
