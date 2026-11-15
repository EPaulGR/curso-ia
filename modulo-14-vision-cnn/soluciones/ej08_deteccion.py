"""Ej 08 — IoU y Non-Maximum Suppression (detección de objetos)."""
import numpy as np


def iou(a, b):
    """Cajas [x1, y1, x2, y2]. Intersección sobre unión."""
    ix = max(0, min(a[2], b[2]) - max(a[0], b[0]))
    iy = max(0, min(a[3], b[3]) - max(a[1], b[1]))
    inter = ix * iy
    area = lambda c: (c[2] - c[0]) * (c[3] - c[1])
    return inter / (area(a) + area(b) - inter)


def nms(cajas, puntajes, umbral=0.5):
    """Devuelve índices conservados, ordenados por puntaje descendente."""
    orden = list(np.argsort(puntajes)[::-1])
    keep = []
    while orden:
        i = orden.pop(0)
        keep.append(int(i))
        orden = [j for j in orden if iou(cajas[i], cajas[j]) <= umbral]
    return keep
