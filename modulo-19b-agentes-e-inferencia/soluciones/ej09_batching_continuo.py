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
    pendientes = sorted(enumerate(solicitudes), key=lambda x: (x[1][0], x[0]))
    restantes = {i: n for i, (_, n) in enumerate(solicitudes)}
    activas, fin, t, tokens = [], {}, 0, 0
    while len(fin) < len(solicitudes):
        puede_admitir = modo == "continuo" or not activas
        if puede_admitir:
            while pendientes and len(activas) < max_batch and pendientes[0][1][0] <= t:
                activas.append(pendientes.pop(0)[0])
        for i in activas:
            restantes[i] -= 1
            tokens += 1
        for i in [i for i in activas if restantes[i] == 0]:
            fin[i] = t + 1
            activas.remove(i)
        t += 1
    lat = sum(fin[i] - solicitudes[i][0] for i in fin) / len(fin)
    return {"pasos": t, "latencia_media": lat, "utilizacion": tokens / (t * max_batch)}
