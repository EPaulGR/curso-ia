"""Ejercicio 09 — Simulador de batching estático vs continuo.

solicitudes: lista de (paso_llegada, tokens_a_generar). En cada paso de tiempo el
servidor genera 1 token para cada solicitud activa del batch (máx `max_batch`).

- modo "estatico": solo se forma un batch nuevo cuando el actual terminó por
  completo (las cortas esperan a las largas).
- modo "continuo": al inicio de cada paso se rellenan los huecos libres con
  solicitudes que ya llegaron (orden FIFO).

simular(solicitudes, max_batch, modo) -> {"pasos": total de pasos hasta terminar
todo, "latencia_media": media de (paso_fin - llegada), "utilizacion": tokens
generados / (pasos * max_batch)}.
Una solicitud que termina en el paso t (0-indexado) tiene paso_fin = t + 1.
"""


def simular(solicitudes, max_batch, modo):
    raise NotImplementedError  # TODO
