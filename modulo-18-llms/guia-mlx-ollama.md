# Práctica guiada: fine-tuning LoRA con MLX y servir con Ollama

> Requiere `uv pip install mlx-lm` y ~16 GB de RAM para un modelo de 1–3B en 4-bit.

## 1. Probar un modelo base
```bash
python -m mlx_lm.generate --model mlx-community/Llama-3.2-1B-Instruct-4bit --prompt "¿Qué es A*?" --max-tokens 200
```

## 2. Preparar datos
Crea `datos/train.jsonl` y `datos/valid.jsonl`, una línea por ejemplo:
```json
{"messages": [{"role": "user", "content": "Explica la poda alfa-beta"}, {"role": "assistant", "content": "..."}]}
```
Meta: 200–1000 ejemplos de tu propio dominio (por ejemplo, preguntas y respuestas de los módulos 04–07 de este curso).

## 3. Entrenar LoRA
```bash
python -m mlx_lm.lora --model mlx-community/Llama-3.2-1B-Instruct-4bit --train --data datos --iters 600 --batch-size 4 --num-layers 16
```
Observa la pérdida de validación; si sube mientras la de entrenamiento baja, hay sobreajuste.

## 4. Evaluar y fusionar
```bash
python -m mlx_lm.generate --model mlx-community/Llama-3.2-1B-Instruct-4bit --adapter-path adapters --prompt "Explica la poda alfa-beta"
```
```bash
python -m mlx_lm.fuse --model mlx-community/Llama-3.2-1B-Instruct-4bit --adapter-path adapters --save-path modelo-fusionado
```

## 5. Llevarlo a Ollama
Exporta a GGUF (con `--export-gguf` si tu versión de mlx-lm lo soporta, o con el script `convert_hf_to_gguf.py` de llama.cpp) y crea un `Modelfile`:
```
FROM ./modelo.gguf
PARAMETER temperature 0.3
```
```bash
ollama create mi-tutor-ia -f Modelfile
```
```bash
ollama run mi-tutor-ia
```

## 6. Escalar en la M5 Ultra
Repite con modelos de 8B, 14B y 32B. Mide tokens/s y memoria (Monitor de Actividad o `mx.get_peak_memory()`), y compáralo con tu calculadora del ejercicio 5.
