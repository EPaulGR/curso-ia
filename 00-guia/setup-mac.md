# Configuración del entorno en Mac (Apple Silicon)

## 1. Herramientas base
```bash
xcode-select --install
```
```bash
brew install uv git
```

## 2. Entorno del curso
Desde la carpeta `curso-ia`:
```bash
uv venv --python 3.13
```
```bash
source .venv/bin/activate
```
```bash
uv pip install -r 00-guia/requirements.txt
```
> Se usa Python 3.13: PyTorch 2.15 (oct 2026) soporta 3.11–3.13 en macOS y MLX pide ≥ 3.10. Aún no hay ruedas de PyTorch para 3.15 en Mac y el 3.14 del sistema no es el recomendado para el curso. Evita mezclar con el Python del sistema.

## 3. Verifica la GPU de Apple (MPS) y MLX
```bash
python -c "import torch; print('MPS:', torch.backends.mps.is_available())"
```
```bash
python -c "import mlx.core as mx; a = mx.random.normal((1000,1000)); print((a@a).sum())"
```

Patrón estándar en todo el curso:
```python
import torch
device = "mps" if torch.backends.mps.is_available() else "cpu"
model.to(device)
```
Si una operación no está implementada en MPS: `export PYTORCH_ENABLE_MPS_FALLBACK=1`.

## 4. LLMs locales
```bash
brew install ollama
```
```bash
ollama run llama3.2
```
Con MLX:
```bash
python -m mlx_lm.generate --model mlx-community/Llama-3.2-3B-Instruct-4bit --prompt "Explica A*"
```

## 5. Jupyter y editor
```bash
jupyter lab
```
Recomendado: VS Code o Cursor con extensiones Python y Jupyter.

## 6. Planeando la Mac Studio M5 Ultra
- **La memoria unificada es el recurso clave**: determina el tamaño de modelo que puedes cargar. Regla aproximada: parámetros × bytes por parámetro (fp16 = 2 B, 4-bit ≈ 0.5 B) + ~20 % de sobrecarga. Un modelo de 70B en 4-bit ≈ 40 GB.
- Con 128 GB+ podrás: fine-tuning LoRA de modelos 7–30B con MLX, inferencia de 70B+ cuantizados, entrenar modelos propios pequeños (≤ 1B) desde cero.
- Limitaciones vs. NVIDIA: menos ancho de cómputo bruto para entrenamiento a gran escala y algunas librerías solo-CUDA. Para eso, alquila GPU por horas (Lambda, RunPod, Modal) solo en experimentos puntuales del módulo 18/23.
- Mientras llega: todo el curso hasta el módulo 17 corre bien en cualquier Mac M1+ con 16 GB.

## 7. Correr los tests
```bash
pytest modulo-05-busqueda
```
```bash
SOLUCIONES=1 pytest
```
