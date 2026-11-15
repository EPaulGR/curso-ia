# Quiz — Módulo 18

1. ¿Qué mide la perplejidad y cómo se relaciona con la entropía cruzada?
2. En BPE, ¿por qué se parte de bytes y no de caracteres Unicode?
3. Menciona dos fenómenos causados por la tokenización.
4. Según Chinchilla, ¿cuántos tokens son óptimos para entrenar un modelo de 7B parámetros?
5. ¿Cuántos FLOPs aproximados requiere entrenar ese modelo con esos tokens?
6. ¿Qué problema resuelve GQA y a qué costo?
7. Explica cómo un MoE puede tener 400B parámetros pero el costo de cómputo de uno de ~17B.
8. Opción múltiple: con temperatura → 0, el muestreo equivale a: (a) uniforme (b) greedy (c) top-p con p=1.
9. ¿Por qué top-p se adapta mejor que top-k a distribuciones con colas distintas?
10. ¿Por qué B se inicializa en ceros en LoRA?
11. Calcula los parámetros entrenables de LoRA con r=8 en una matriz de 4096×4096.
12. ¿Qué es QLoRA y qué lo hace posible en hardware modesto?
13. Diferencias entre RLHF con PPO y DPO.
14. ¿Qué guarda el KV cache y por qué su memoria crece linealmente con el contexto?
15. ¿Por qué la inferencia de LLMs está limitada por ancho de banda de memoria y no por FLOPs?
16. Estima la memoria para inferencia de un modelo de 70B a 4 bits con contexto 8k (80 capas, d=8192, GQA 8/64 cabezas).
17. ¿Qué ventaja tiene la cuantización por grupos frente a una sola escala por tensor?
18. Pregunta abierta: ¿qué modelo y configuración elegirías para un asistente local en una Mac con 192 GB? Justifica.
