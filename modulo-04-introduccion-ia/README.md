# Módulo 04 — Introducción a la Inteligencia Artificial

**Duración:** 3 semanas (25–30 h) · **Fase 1 · Unidad 1 del programa BUAP CCOS 258**

## Objetivos
- Explicar qué es la IA desde sus cuatro enfoques (pensar/actuar × humano/racional).
- Conocer la historia: desde Turing y Dartmouth hasta los LLMs, incluyendo los "inviernos".
- Distinguir los paradigmas simbólico, conexionista, evolutivo y otros (probabilístico, conductual, híbrido/neurosimbólico).
- Modelar problemas con el marco de **agentes inteligentes** y entornos (PEAS).

## Temario (alineado a la Unidad 1 BUAP)
1.1 Antecedentes de la IA: lógica (Aristóteles, Boole, Frege), computabilidad (Turing, Church), cibernética (Wiener), McCulloch–Pitts.
1.2 Conceptos básicos: inteligencia, racionalidad, agente, entorno, test de Turing, IA débil/fuerte/general.
1.3 Pasado y presente: Dartmouth 1956, Logic Theorist, GPS, ELIZA, perceptrón (1958) y crítica de Minsky–Papert (1969), sistemas expertos (MYCIN, DENDRAL), inviernos de la IA, backprop (1986), Deep Blue (1997), ImageNet/AlexNet (2012), AlphaGo (2016), Transformer (2017), GPT/ChatGPT (2018–2022), modelos de razonamiento y agentes (2024–2026).
1.4 Relación con otras disciplinas: filosofía, matemáticas, economía (teoría de decisiones), neurociencia, psicología cognitiva, ingeniería de control, lingüística.
1.5 Áreas de aplicación: visión, PLN, robótica, salud, finanzas, juegos, ciencia (AlphaFold).
1.6 Tendencias: modelos fundacionales, multimodalidad, agentes, IA en el dispositivo (Apple Silicon), eficiencia, regulación (EU AI Act).
1.7 Paradigmas: 1.7.1 simbólico · 1.7.2 conexionista · 1.7.3 evolutivo · 1.7.4 otros (bayesiano, conductual/Brooks, neurosimbólico).
Extra: agentes (reactivo simple, basado en modelo, en metas, en utilidad, que aprende); entornos (observable, determinista, episódico, estático, discreto, multiagente).

## Lecturas
- Russell & Norvig, *AIMA* 4ª ed. — **Cap. 1** (completo) y **Cap. 2** (agentes inteligentes).
- Boden, *Inteligencia artificial* (2018) — completo (lectura corta en español).
- Rich, Knight & Nair — Cap. 1.
- Nilsson — Cap. 1.
- Eiben & Smith — Cap. 1 (paradigma evolutivo).
- Turing, A. (1950). *Computing Machinery and Intelligence*. Mind. 🆓
- McCarthy et al. (1955). *Propuesta de Dartmouth*. 🆓
- Sutton, R. (2019). *The Bitter Lesson* (ensayo corto). 🆓

## Ejercicios (ligeros; el peso está en la lectura y el ensayo)
| Archivo | Tema |
|---|---|
| ej01_peas.py | clasificar entornos y describir PEAS |
| ej02_agente_reactivo.py | aspiradora de Russell & Norvig |
| ej03_agente_modelo.py | agente con estado interno |
| ej04_eliza.py | chatbot simbólico por reglas (1966) |
| ej05_perceptron_rosenblatt.py | perceptrón de 1958 y el problema XOR |
| ej06_evolutivo_minimo.py | algoritmo evolutivo (1+1)-ES / OneMax |

## Evaluación
- Tests (20 %), quiz (30 %), **ensayo** (30 %, ver proyecto), línea de tiempo (20 %). Aprobación ≥ 8/10.
