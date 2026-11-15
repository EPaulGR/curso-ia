"""Ejercicio 06 — Planificación clásica con STRIPS (AIMA cap. 11).

Estado = frozenset de hechos (cadenas). Una acción tiene precondiciones, lista de
agregados y lista de borrados:
    aplicable(s, a)  ⇔  pre(a) ⊆ s
    resultado(s, a)  =  (s − borrar(a)) ∪ agregar(a)
Meta = conjunto de hechos que deben ser ciertos.

Implementa:
- planificar_bfs: búsqueda hacia adelante en anchura (plan más corto).
- h_ignorar_borrados: heurística = nº de pasos del plan relajado (ignorando listas de
  borrado) calculado en capas: cuántas capas hacen falta para alcanzar la meta.
- planificar_astar con esa heurística.
- acciones_bloques: genera las acciones del mundo de bloques.
"""
import heapq
from collections import deque, namedtuple

Accion = namedtuple("Accion", "nombre pre agregar borrar")


def aplicable(s, a):
    """True si las precondiciones de a están en s."""
    return a.pre <= s


def resultado(s, a):
    """Estado sucesor."""
    return (s - a.borrar) | a.agregar


def planificar_bfs(inicial, meta, acciones):
    """Lista de nombres de acciones del plan más corto, o None."""
    inicial = frozenset(inicial)
    meta = frozenset(meta)
    cola, visto = deque([(inicial, [])]), {inicial}
    while cola:
        s, plan = cola.popleft()
        if meta <= s:
            return plan
        for a in acciones:
            if aplicable(s, a):
                t = resultado(s, a)
                if t not in visto:
                    visto.add(t)
                    cola.append((t, plan + [a.nombre]))
    return None


def h_ignorar_borrados(s, meta, acciones):
    """Número de capas de expansión relajada hasta cubrir la meta (inf si imposible)."""
    alcanzado, capas = set(s), 0
    while not meta <= alcanzado:
        nuevo = set(alcanzado)
        for a in acciones:
            if a.pre <= alcanzado:
                nuevo |= a.agregar
        if nuevo == alcanzado:
            return float("inf")
        alcanzado, capas = nuevo, capas + 1
    return capas


def planificar_astar(inicial, meta, acciones):
    """A* con h_ignorar_borrados (costo 1 por acción). Devuelve (plan, nodos_expandidos)."""
    inicial, meta = frozenset(inicial), frozenset(meta)
    frontera = [(h_ignorar_borrados(inicial, meta, acciones), 0, 0, inicial, [])]
    g_mejor, cont, expandidos = {inicial: 0}, 1, 0
    while frontera:
        _, g, _, s, plan = heapq.heappop(frontera)
        if meta <= s:
            return plan, expandidos
        expandidos += 1
        for a in acciones:
            if aplicable(s, a):
                t = resultado(s, a)
                if g + 1 < g_mejor.get(t, float("inf")):
                    g_mejor[t] = g + 1
                    heapq.heappush(frontera, (g + 1 + h_ignorar_borrados(t, meta, acciones), g + 1, cont, t, plan + [a.nombre]))
                    cont += 1
    return None, expandidos


def acciones_bloques(bloques):
    """Acciones del mundo de bloques con hechos 'sobre(x,y)', 'sobre(x,mesa)', 'libre(x)':
    mover(x, desde, hacia) para x bloque, desde/hacia ∈ bloques ∪ {'mesa'}, todos distintos.
    pre = {sobre(x,desde), libre(x)} ∪ {libre(hacia) si hacia ≠ mesa}
    agregar = {sobre(x,hacia)} ∪ {libre(desde) si desde ≠ mesa}
    borrar = {sobre(x,desde)} ∪ {libre(hacia) si hacia ≠ mesa}"""
    acs = []
    lugares = list(bloques) + ["mesa"]
    for x in bloques:
        for d in lugares:
            for h in lugares:
                if len({x, d, h}) < 3:
                    continue
                pre = {f"sobre({x},{d})", f"libre({x})"} | ({f"libre({h})"} if h != "mesa" else set())
                ag = {f"sobre({x},{h})"} | ({f"libre({d})"} if d != "mesa" else set())
                bo = {f"sobre({x},{d})"} | ({f"libre({h})"} if h != "mesa" else set())
                acs.append(Accion(f"mover({x},{d},{h})", frozenset(pre), frozenset(ag), frozenset(bo)))
    return acs
