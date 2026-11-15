import numpy as np
import pytest


def test_tracking(cargar, tmp_path):
    m = cargar("ej01_tracking")
    r = m.Rastreador(tmp_path)
    a = r.iniciar("a", {"lr": 0.1}); b = r.iniciar("b", {"lr": 0.01})
    assert a != b and (tmp_path / a / "params.json").exists()
    for p, v in enumerate([1.0, 0.5]):
        r.log_metrica(a, "loss", v, p)
    for p, v in enumerate([0.2, 0.8]):
        r.log_metrica(b, "loss", v, p)
    assert r.historial(a, "loss") == [(0, 1.0), (1, 0.5)]
    assert r.mejor_run("loss") == a


def test_benchmark(cargar):
    m = cargar("ej02_benchmark")
    llamadas = []
    res = m.medir(lambda: llamadas.append(1), 5, 2, sincronizar=lambda: None)
    assert len(llamadas) == 7 and res["min"] <= res["mediana"] <= res["p95"]
    assert np.isclose(m.gflops_matmul(1000, 1.0), 2)
    assert np.isclose(m.ancho_banda_gbs(8e9, 2), 4)


def test_servicio(cargar):
    m = cargar("ej03_servicio")
    s = m.ServicioModelo(lambda xs: [sum(x) for x in xs], "1.0", max_lote=2)
    r = s.predecir({"instancias": [[1, 2], [3, 4]]})
    assert r["predicciones"] == [3, 7] and r["version"] == "1.0"
    for bad in [{}, {"instancias": []}, {"instancias": [[1], [1, 2]]},
                {"instancias": [[1]] * 3}, {"instancias": [["a"]]}]:
        with pytest.raises(ValueError):
            s.predecir(bad)
    assert s.salud()["peticiones"] == 1


def test_drift(cargar):
    m = cargar("ej04_drift")
    rng = np.random.default_rng(0)
    ref = rng.normal(size=5000)
    assert m.alerta(m.psi(ref, rng.normal(size=5000))) == "estable"
    assert m.alerta(m.psi(ref, rng.normal(1, 1, 5000))) == "severo"
    assert m.ks_estadistico(ref, ref) == 0
    assert m.ks_estadistico(ref, ref + 3) > 0.8
    assert m.alerta(0.15) == "moderado"


def test_dispositivo(cargar):
    m = cargar("ej05_dispositivo")
    assert m.elegir_dispositivo("cpu") == "cpu"
    assert m.elegir_dispositivo() in ("cpu", "mps")
    assert m.tamano_modelo_mb(1e6, "float16") == 2
    assert m.plan_despliegue(7e9, 64) == "float16"
    assert m.plan_despliegue(70e9, 64) == "int4"
    assert m.plan_despliegue(400e9, 64) is None


def test_registro(cargar):
    m = cargar("ej06_registro")
    r = m.RegistroModelos()
    for v in ["1.9.0", "1.10.0"]:
        r.registrar("clf", v, {"acc": 0.9})
    assert r.ultima_version("clf") == "1.10.0"
    r.promover("clf", "1.9.0", "produccion"); r.promover("clf", "1.10.0", "produccion")
    assert r.en_etapa("clf", "produccion") == "1.10.0"
    assert r.modelos["clf"]["1.9.0"]["etapa"] == "archivado"
    with pytest.raises(KeyError):
        r.promover("clf", "9.9.9", "staging")
    frac = np.mean([m.enrutar_canario(i, 10) for i in range(5000)])
    assert 0.07 < frac < 0.13 and m.enrutar_canario(42, 10) == m.enrutar_canario(42, 10)
