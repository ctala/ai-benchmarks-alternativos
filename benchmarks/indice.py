#!/usr/bin/env python3
"""La nota de calidad del índice: 75 % examen + 25 % Harbor, con su margen de error.

POR QUÉ (DECISIONES, 9-nov-2026, Cristian)
------------------------------------------
El examen separa poco a los rankeados (desviación 0,27 entre 70) y las 4 tareas reales de
agente en Harbor separan mucho (1,87). Una nota que no las ve ordena por la parte que menos
distingue. Desde v6.0.0 la nota pública (`score_calidad`) las incluye con un peso fijo.

UNA SOLA DEFINICIÓN
-------------------
El peso vive acá y en ningún otro lado. El export calcula la nota y la publica; la
calculadora y las páginas la leen de `models.json`. Lo hace cumplir `check_indice_calidad`:
un segundo lugar que combine examen y Harbor es una segunda definición que se va a
desincronizar.

EL MARGEN (método B, elegido por Cristian el 9-nov)
---------------------------------------------------
El error del examen es el de siempre (1,96 × desviación / √n sobre los runs). El de Harbor
sale de un bootstrap: se remuestrean con reposición los intentos de cada tarea (las tareas
son fijas: todos rinden las mismas 4) y se recalcula la nota. Con 3 intentos, un modelo que
saca lo mismo en los tres tendría error cero, y «nunca falló en 3» no prueba que no falle:
por eso la varianza de cada tarea se encoge hacia la varianza agrupada de esa tarea en todos
los modelos, con peso K0 = 1 frente a los k = 3 intentos propios (Bayes empírico). Los dos
errores se combinan como independientes:

    margen = 1,96 × √((0,75 · se_examen)² + (0,25 · se_harbor)²)

Pesa poco a propósito: la varianza de Harbor entra multiplicada por 0,25² = 0,0625. En la
simulación del 9-nov el grupo de cabeza dio 18 de 68 con este método y sin el encogimiento.
"""

from __future__ import annotations

import random
import statistics as st

# El peso de Harbor dentro de la nota de calidad. Una sola constante (Cristian, 9-nov).
PESO_HARBOR_EN_CALIDAD = 0.25

# La nota de Harbor 0-10: la misma fórmula de `score_agentico` sin tool calling. El piso
# pesa porque para trabajo desatendido «a veces falla» y «no falla» no son lo mismo.
PESO_MEDIA_HARBOR = 0.6
PESO_PISO_HARBOR = 0.4

# CHECKS QUE NO CUENTAN EN LA NOTA HASTA QUE SU TAREA SE CORRIJA (DECISIONES, 9-nov-2026).
# Regla de Cristian: un check cuya trampa el agente no puede conocer por lo que ve (el
# enunciado y los archivos de /app) no cuenta. El reward de un intento se recalcula sobre
# los checks que quedan, desde el `ctrf.json` del verificador. La corrección de la tarea va
# a corte-v5-1 como medición; cuando la tarea corregida esté medida, el check vuelve.
CHECKS_SIN_CONTAR: dict[str, dict[str, str]] = {
    "harbor-facturacion": {
        "test_no_factura_la_linea_duplicada":
            "ninguna regla dice qué hacer con un registro dudoso y el CSV no permite "
            "distinguir un duplicado de dos sesiones; cobrar y dejar constancia sacaba cero",
        "test_total_correcto":
            "depende del duplicado: el mismo error contaba dos veces",
        "test_escala_lo_que_requiere_decision_humana":
            "el enunciado no pide dejar constancia, y en la práctica solo busca «CL-0355»",
    },
}


def reward_sin_checks(tarea: str, tests: dict[str, str]) -> float | None:
    """Reward 0-1 de un intento desde el estado de cada check (`{nombre: "passed"|…}`),
    sin los de `CHECKS_SIN_CONTAR`. None si no queda ningún check que contar."""
    fuera = CHECKS_SIN_CONTAR.get(tarea, {})
    cuentan = [s for n, s in tests.items() if n not in fuera]
    if not cuentan:
        return None
    return round(sum(s == "passed" for s in cuentan) / len(cuentan), 4)


BOOT_REPLICAS = 4000
BOOT_SEMILLA = 20261109
K0_ENCOGIMIENTO = 1


def nota_harbor(tareas: dict) -> float | None:
    """Nota 0-10 de Harbor desde `{tarea: {"media", "piso"} | {"rewards"}}`. None sin tareas."""
    medias, pisos = [], []
    for f in (tareas or {}).values():
        r = f.get("rewards")
        if r:
            medias.append(sum(r) / len(r))
            pisos.append(min(r))
        elif f.get("media") is not None:
            medias.append(f["media"])
            pisos.append(f.get("piso") if f.get("piso") is not None else 0.0)
    if not medias:
        return None
    return 10 * (PESO_MEDIA_HARBOR * sum(medias) / len(medias) + PESO_PISO_HARBOR * min(pisos))


def _nota_de_listas(listas: list[list[float]]) -> float:
    medias = [sum(r) / len(r) for r in listas]
    return 10 * (PESO_MEDIA_HARBOR * sum(medias) / len(medias)
                 + PESO_PISO_HARBOR * min(min(r) for r in listas))


def varianza_agrupada(modelos_tareas: list[dict]) -> dict[str, float]:
    """Varianza media de los intentos de cada tarea, sobre todos los modelos que la rindieron."""
    por_tarea: dict[str, list[float]] = {}
    for tareas in modelos_tareas:
        for t, f in (tareas or {}).items():
            r = f.get("rewards") or []
            if len(r) >= 2:
                por_tarea.setdefault(t, []).append(st.pvariance(r))
    return {t: st.mean(v) for t, v in por_tarea.items()}


def se_harbor(tareas: dict, var_pool: dict[str, float], replicas: int = BOOT_REPLICAS,
              semilla: int = BOOT_SEMILLA) -> float | None:
    """Error estándar de la nota de Harbor (bootstrap estratificado, varianza encogida)."""
    nombres = sorted(t for t, f in (tareas or {}).items() if f.get("rewards"))
    if not nombres:
        return None
    listas = [list(tareas[t]["rewards"]) for t in nombres]
    extra = []
    for t, r in zip(nombres, listas):
        k = len(r)
        s_obs = st.pvariance(r) if k >= 2 else 0.0
        s2 = (k * s_obs + K0_ENCOGIMIENTO * var_pool.get(t, 0.0)) / (k + K0_ENCOGIMIENTO)
        extra.append(max(0.0, s2 - s_obs) ** 0.5)
    rng = random.Random(semilla)
    vals = []
    for _ in range(replicas):
        res = []
        for r, e in zip(listas, extra):
            s = [rng.choice(r) for _ in r]
            if e > 0:
                s = [min(1.0, max(0.0, x + rng.gauss(0, e))) for x in s]
            res.append(s)
        vals.append(_nota_de_listas(res))
    return st.pstdev(vals)


def calidad(examen: float | None, ci95_examen: float | None,
            harbor: float | None, se_h: float | None) -> tuple[float | None, float | None]:
    """(nota, margen al 95 %). Sin examen o sin Harbor no hay nota: no se inventa la mitad."""
    if examen is None or harbor is None:
        return None, None
    w = PESO_HARBOR_EN_CALIDAD
    nota = (1 - w) * examen + w * harbor
    se_e = (ci95_examen or 0.0) / 1.96
    margen = 1.96 * (((1 - w) * se_e) ** 2 + (w * (se_h or 0.0)) ** 2) ** 0.5
    return nota, margen


# ── Tier de precio (9-nov-2026) ──────────────────────────────────────────────────
# `cloud_nim`, `cloud_ollama` y `cloud` son RUTAS (por dónde se sirve), no precios, y la
# calculadora los mostraba en la columna Tier al lado de `cheap` y `premium`. Si el tier
# declarado es una ruta, el tier publicado se deriva del precio mezclado (3 de entrada por
# 1 de salida, USD por millón) con los umbrales que mejor reproducen los tiers declarados a
# mano (133 de 159); la ruta se publica aparte.
def es_ruta(tier: str | None) -> bool:
    """`cloud`, `cloud_nim`, `cloud_ollama`…: dicen por dónde se sirve, no cuánto cuesta."""
    return bool(tier) and str(tier).startswith("cloud")


UMBRALES_TIER = ((0.25, "ultra_cheap"), (2.0, "cheap"), (6.0, "medium"))


def tier_de_precio(tier_declarado: str | None, cost_input: float | None,
                   cost_output: float | None) -> str:
    if not es_ruta(tier_declarado):
        return tier_declarado or "?"
    if cost_input is None or cost_output is None:
        return "?"
    mezcla = (3 * cost_input + cost_output) / 4
    for tope, nombre in UMBRALES_TIER:
        if mezcla <= tope:
            return nombre
    return "premium"
