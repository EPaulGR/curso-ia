"""Configuración común de pytest para todo el curso.

Los tests de cada módulo cargan tu código desde `ejercicios/`.
Para validar contra las soluciones de referencia:  SOLUCIONES=1 pytest
"""
import importlib.util
import os
from pathlib import Path

import pytest


def _cargar(test_file: str, nombre: str):
    carpeta = "soluciones" if os.environ.get("SOLUCIONES") == "1" else "ejercicios"
    ruta = Path(test_file).resolve().parent.parent / carpeta / f"{nombre}.py"
    spec = importlib.util.spec_from_file_location(f"{carpeta}_{nombre}_{abs(hash(ruta))}", ruta)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


@pytest.fixture
def cargar(request):
    """Uso en un test:  m = cargar("ej01_bfs");  m.bfs(...)"""
    return lambda nombre: _cargar(str(request.path), nombre)
