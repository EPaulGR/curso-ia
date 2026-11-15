# EJERCICIO: implementa cada función marcada con TODO.
# Verifica con: pytest modulo-14-vision-cnn

"""Ej 08 — IoU y Non-Maximum Suppression (detección de objetos)."""
import numpy as np

def iou(a, b):
    """Cajas [x1, y1, x2, y2]. Intersección sobre unión."""
    raise NotImplementedError  # TODO

def nms(cajas, puntajes, umbral=0.5):
    """Devuelve índices conservados, ordenados por puntaje descendente."""
    raise NotImplementedError  # TODO
