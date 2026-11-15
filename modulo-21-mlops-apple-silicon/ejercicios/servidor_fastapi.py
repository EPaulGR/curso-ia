"""Ejemplo: exponer ServicioModelo con FastAPI.  uv pip install fastapi uvicorn
Ejecuta:  uvicorn servidor_fastapi:app --reload   (desde soluciones/)
"""
from fastapi import FastAPI, HTTPException
from ej03_servicio import ServicioModelo

servicio = ServicioModelo(lambda xs: [sum(x) for x in xs], version="0.1.0")
app = FastAPI(title="Servicio de modelo")


@app.get("/salud")
def salud():
    return servicio.salud()


@app.post("/predecir")
def predecir(payload: dict):
    try:
        return servicio.predecir(payload)
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
