"""Ejercicio 02 — Redes bayesianas e inferencia exacta por enumeración (AIMA 13.2–13.3).

Red con variables booleanas como dict:
    red = {"variables": [...orden topológico...],
           "padres":    {var: [padres]},
           "cpt":       {var: {tupla_valores_padres: P(var=True | padres)}}}
Semántica: P(x1,…,xn) = Π_i P(xi | padres(Xi)).
Enumeración: P(X | e) = α Σ_y P(X, e, y).
"""


def red_alarma():
    """DADO: red de la alarma de Pearl (AIMA fig. 13.2): Robo, Sismo → Alarma → Juan, Maria."""
    return {
        "variables": ["Robo", "Sismo", "Alarma", "Juan", "Maria"],
        "padres": {"Robo": [], "Sismo": [], "Alarma": ["Robo", "Sismo"], "Juan": ["Alarma"], "Maria": ["Alarma"]},
        "cpt": {
            "Robo": {(): 0.001}, "Sismo": {(): 0.002},
            "Alarma": {(True, True): 0.95, (True, False): 0.94, (False, True): 0.29, (False, False): 0.001},
            "Juan": {(True,): 0.90, (False,): 0.05},
            "Maria": {(True,): 0.70, (False,): 0.01},
        },
    }


def prob_condicional(red, var, valor, asignacion):
    """P(var = valor | padres) con los valores de los padres tomados de `asignacion`."""
    p = red["cpt"][var][tuple(asignacion[x] for x in red["padres"][var])]
    return p if valor else 1 - p


def prob_conjunta(red, asignacion):
    """P de una asignación completa."""
    r = 1.0
    for v in red["variables"]:
        r *= prob_condicional(red, v, asignacion[v], asignacion)
    return r


def enumeracion(red, X, evidencia):
    """Distribución {True: p, False: p} de P(X | evidencia) por ENUMERATION-ASK."""
    def enum_todo(vars_, e):
        if not vars_:
            return 1.0
        y, resto = vars_[0], vars_[1:]
        if y in e:
            return prob_condicional(red, y, e[y], e) * enum_todo(resto, e)
        return sum(prob_condicional(red, y, v, e) * enum_todo(resto, {**e, y: v}) for v in (True, False))

    q = {x: enum_todo(red["variables"], {**evidencia, X: x}) for x in (True, False)}
    s = q[True] + q[False]
    return {k: v / s for k, v in q.items()}
