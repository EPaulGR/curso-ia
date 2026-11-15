"""Ejercicio 01 — Mini Model Context Protocol (MCP) en Python puro.

MCP es un protocolo JSON-RPC 2.0 con el que un cliente (la app del LLM) descubre
y llama herramientas expuestas por un servidor. Implementa:

- ServidorMCP.manejar(linea): recibe UNA línea JSON y devuelve la respuesta como
  str JSON (o None si era una notificación, es decir, sin "id").
  Métodos: "initialize", "notifications/initialized", "tools/list", "tools/call".
  Errores JSON-RPC: -32700 (JSON inválido), -32601 (método no existe),
  -32602 (parámetros inválidos: herramienta desconocida).
  Si faltan argumentos requeridos (según inputSchema["required"]) o la
  herramienta lanza excepción, responde un resultado con "isError": True.
- ClienteMCP: envuelve una función `enviar(str) -> str` (el transporte) y ofrece
  inicializar(), listar_herramientas() y llamar(nombre, argumentos).
"""
import json
import sys

VERSION_PROTOCOLO = "2025-06-18"


class ServidorMCP:
    def __init__(self, nombre="mini-mcp"):
        self.nombre = nombre
        self.herramientas = {}  # nombre -> (descripcion, schema, funcion)

    def herramienta(self, nombre, descripcion, schema):
        """Decorador DADO para registrar herramientas."""
        def deco(fn):
            self.herramientas[nombre] = (descripcion, schema, fn)
            return fn
        return deco

    def manejar(self, linea):
        raise NotImplementedError  # TODO

    def _error(self, id_, codigo, mensaje):
        return json.dumps({"jsonrpc": "2.0", "id": id_, "error": {"code": codigo, "message": mensaje}})


def servir_stdio(servidor):
    """DADO: bucle de transporte stdio (una línea JSON por mensaje)."""
    for linea in sys.stdin:
        resp = servidor.manejar(linea)
        if resp is not None:
            print(resp, flush=True)


class ClienteMCP:
    def __init__(self, enviar):
        self.enviar = enviar
        self._id = 0

    def _peticion(self, metodo, params=None):
        self._id += 1
        resp = json.loads(self.enviar(json.dumps(
            {"jsonrpc": "2.0", "id": self._id, "method": metodo, "params": params or {}})))
        if "error" in resp:
            raise RuntimeError(resp["error"]["message"])
        return resp["result"]

    def inicializar(self):
        raise NotImplementedError  # TODO

    def listar_herramientas(self):
        raise NotImplementedError  # TODO

    def llamar(self, nombre, argumentos):
        raise NotImplementedError  # TODO
