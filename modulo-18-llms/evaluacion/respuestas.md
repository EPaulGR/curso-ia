# Respuestas — Módulo 18

1. exp de la entropía cruzada promedio por token; es el "número efectivo de opciones" entre las que el modelo duda.
2. 256 bytes cubren cualquier texto sin tokens desconocidos (UNK) y el vocabulario base es pequeño.
3. Dificultad para deletrear/contar letras; aritmética inconsistente; más tokens (y costo) en idiomas no ingleses; espacios iniciales que cambian el token.
4. ≈ 20 × 7B = 140B tokens.
5. 6·N·D = 6 · 7e9 · 1.4e11 ≈ 5.9e21 FLOPs.
6. Reduce el tamaño del KV cache (y el ancho de banda) compartiendo K/V entre grupos de cabezas; pérdida de calidad mínima.
7. Un router activa solo k expertos por token: los parámetros activos son una fracción; todos deben estar en memoria.
8. (b) greedy.
9. Top-p elige un número variable de tokens según la confianza; top-k fija k aunque la distribución esté muy concentrada o muy plana.
10. Para que ΔW = BA = 0 al inicio y el modelo arranque idéntico al preentrenado.
11. r·(d_in + d_out) = 8 · 8192 = 65,536.
12. Base congelada en 4-bit (NF4) + adaptadores LoRA en bf16; la memoria de pesos cae ~4× y los gradientes solo se calculan para los adaptadores.
13. RLHF: modelo de recompensa + RL (PPO) con penalización KL, complejo e inestable. DPO: pérdida de clasificación directa sobre pares preferido/rechazado, sin RL ni modelo de recompensa.
14. Las proyecciones K y V de cada token previo en cada capa; se agrega un vector por token nuevo.
15. Por cada token generado se deben leer todos los pesos de memoria; con batch 1 la intensidad aritmética es baja.
16. Pesos 35 GB; KV: 2·80·8192·(8192·8/64)·2 B ≈ 2.7 GB; total ×1.2 ≈ 45 GB.
17. Los valores atípicos afectan solo a su grupo; el error de cuantización baja mucho.
18. Abierta: p. ej. un MoE o un 70B en 4–6 bits con mlx-lm, dejando margen para KV cache y el SO; justificar con la calculadora.
