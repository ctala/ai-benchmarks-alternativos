#!/usr/bin/env python3
"""
Bandas de empate estadistico: convierte un ranking en una DECISION.

EL PROBLEMA QUE RESUELVE
------------------------
El ranking ordena por score con dos decimales y eso finge una precision que la
medicion no tiene. Los numeros, medidos sobre este mismo benchmark:

  - std de la calidad ENTRE modelos (la senal)      ~0.60
  - dispersion de la calidad DENTRO de un modelo    ~1.70

Con esa relacion, la diferencia entre el #1 y el #4 del ranking es, casi
siempre, ruido con decimales. De hecho **9 de los top-12 empatan
estadisticamente** en calidad: sus intervalos de confianza al 95% se solapan.

Publicar "8.47 vs 8.44" como si fueran distintos no ayuda a decidir: induce a
pagar de mas por una diferencia que no existe.

QUE HACE
--------
Agrupa en una misma BANDA a los modelos cuya calidad es indistinguible (IC95
solapado con el mejor). **Dentro de la banda, ordena por COSTO** — porque si la
calidad empata, la decision es de precio. Ese es el hallazgo entero:

    9 modelos empatan en calidad. El mas barato sale $19/mes; el mas caro, $780.
    41x de diferencia por 0.09 puntos de calidad, que estan dentro del ruido.

Uso:
    from benchmarks.bands import quality_bands, verdict
"""

from __future__ import annotations


def _q(m: dict, pillar: str | None):
    """(calidad, margen_error) del modelo — global o dentro de un pilar."""
    if pillar:
        d = (m.get("dims_by_pillar") or {}).get(pillar) or {}
        return d.get("quality_avg"), d.get("quality_ci95")
    return m.get("quality_avg"), m.get("quality_ci95")


def _indistinguishable(a: dict, b: dict, pillar: str | None) -> bool:
    """True si NO hay evidencia de que a sea mejor que b (test de diferencia de medias).

    Comparar si los IC95 individuales se solapan es el test equivocado: es
    demasiado laxo y encadenaba bandas de 80+ modelos. El correcto compara la
    DIFERENCIA de las medias contra su propio error:

        se_dif = sqrt(se_a^2 + se_b^2);  distinguibles si |mu_a - mu_b| > 1.96 * se_dif

    (se = ci95 / 1.96)
    """
    mua, cia = _q(a, pillar)
    mub, cib = _q(b, pillar)
    if mua is None or mub is None:
        return False
    delta = abs(mua - mub)
    # Guardia absoluta: por mucho que el test estadistico "no distinga", una
    # diferencia grande de calidad no se declara empate. Evita que un lider mal
    # medido arrastre a medio catalogo a su banda.
    if delta > MAX_BAND_DELTA:
        return False
    sea = (cia or 0.0) / 1.96
    seb = (cib or 0.0) / 1.96
    se_dif = (sea ** 2 + seb ** 2) ** 0.5
    if se_dif == 0:
        return delta < 1e-9
    return delta <= 1.96 * se_dif


def quality_bands(models: list[dict], pillar: str | None = None) -> list[list[dict]]:
    """Agrupa modelos en bandas de calidad estadisticamente indistinguible.

    Se toma el mejor no asignado como lider; entran a su banda los que NO son
    distinguibles de EL. Dentro de la banda se ordena por COSTO ascendente,
    porque si la calidad empata la decision es de precio.

    Devuelve [[banda A...], [banda B...], ...] ordenadas por calidad.
    """
    pool = [m for m in models if _q(m, pillar)[0] is not None]
    pool.sort(key=lambda m: -_q(m, pillar)[0])

    bands: list[list[dict]] = []
    used: set[int] = set()

    for m in pool:
        if id(m) in used:
            continue
        band = [m]
        used.add(id(m))
        for other in pool:
            if id(other) in used:
                continue
            if _indistinguishable(m, other, pillar):
                band.append(other)
                used.add(id(other))
        band.sort(key=lambda x: (x.get("cost_per_1k_calls_usd") is None,
                                 x.get("cost_per_1k_calls_usd") or 0))
        bands.append(band)

    return bands


# Si la banda de empate cubre mas que esto del pool, el resultado honesto NO es
# "estos N son igual de buenos, elegi el mas barato" sino "el benchmark no separa
# a estos modelos". Paso de verdad: en Coding la banda cubria 56 de 98 = 57% del
# catalogo, y el veredicto igual recomendaba Mistral Nemo "para programar". Un
# empate que abarca medio catalogo es la confesion de que el instrumento no
# discrimina — y hay que decirlo, no venderlo como recomendacion.
MAX_BAND_SHARE = 0.20

# Ademas del test estadistico, distancia absoluta maxima para entrar a la banda.
# Sin esto, un lider mal medido (IC ancho por ruido) se "empata" con medio mundo:
# cuanto PEOR medido el lider, mas gente empata con el. Perverso.
MAX_BAND_DELTA = 0.30


def price_note(m: dict) -> str | None:
    """Precio por suscripcion, si el modelo tiene una.

    Sin esto publicabamos dos precios para el mismo modelo: el veredicto decia
    "Claude Fable 5 ~$234/mes" (costo API) mientras la calculadora mostraba
    "Sub $20/mes" leyendo el campo `subscriptions` del MISMO json. 11x de
    diferencia, en dos paginas que se enlazan entre si.
    """
    subs = m.get("subscriptions") or []
    for s in subs:
        p = s.get("price_month_usd")
        if p:
            return f"${p:,.0f}/mes con {s.get('name', 'suscripción')} (sin acceso API)"
    return None


def is_local(m: dict) -> bool:
    """Modelo que corre en hardware propio (Spark/Ollama), no via API.

    Importa para la recomendacion: el mas barato de una banda suele ser un local
    con costo ~0, pero recomendarselo a alguien que no tiene una DGX Spark no es
    una recomendacion, es una trampa. El local se ofrece como opcion APARTE.
    """
    tier = (m.get("tier") or "").lower()
    prov = (m.get("provider") or "").lower()
    return tier == "local" or any(k in prov for k in ("local", "ollama", "diffusion", "llama_server"))


def verdict(models: list[dict], pillar: str | None = None, calls_per_month: int = 3000) -> dict:
    """La recomendacion concreta. Lo que el sitio nunca decia.

    - best     = el mas barato ACCESIBLE POR API dentro de la banda de calidad top.
    - priciest = el mas caro de esa misma banda -> el contraste que duele: pagas
                 N veces mas por una diferencia de calidad que esta dentro del ruido.
    - local    = la mejor opcion si tenes hardware propio (aparte, no mezclada).
    - open     = la mejor open-source por API.
    """
    pool = list(models)
    bands = quality_bands(pool, pillar)
    if not bands:
        return {}
    top = bands[0]

    def month(m):
        c = m.get("cost_per_1k_calls_usd")
        return round(c * calls_per_month / 1000, 2) if c is not None else None

    def card(m):
        return {"name": m["name"], "quality": _q(m, pillar)[0],
                "cost_month": month(m), "id": m.get("id"),
                "sub": price_note(m)}   # el precio de suscripcion, si lo tiene

    # El LIDER de la banda: el de mas calidad. Es el #1 de la tabla de la pagina,
    # que ordena por capacidad. Nombrarlo explicitamente evita que el veredicto
    # parezca contradecir a su propia tabla (paso: la tabla coronaba a uno y el
    # veredicto recomendaba a otro, sin explicar por que).
    leader = max(top, key=lambda m: _q(m, pillar)[0] or 0)

    api = [m for m in top if not is_local(m)]
    if not api:
        api = top

    best = api[0]                                    # banda ya ordenada por costo
    priciest = api[-1]
    openm = next((m for m in api if m.get("open_source")), None)
    localm = next((m for m in top if is_local(m)), None)

    share = len(top) / len(pool) if pool else 0

    out = {
        "band_size": len(top),
        "pool_size": len(pool),
        "band_share": round(share, 3),
        # Si el empate cubre mas de MAX_BAND_SHARE del catalogo, no hay recomendacion
        # honesta por calidad: el instrumento no separa. Se dice, no se disimula.
        "inconclusive": share > MAX_BAND_SHARE,
        "calls_per_month": calls_per_month,
        "leader": card(leader),
        "best": card(best),
    }
    if priciest is not best:
        out["priciest"] = {
            **card(priciest),
            # Lo que estas pagando de mas por una diferencia dentro del ruido.
            "extra_month": round((month(priciest) or 0) - (month(best) or 0), 2),
            "quality_gap": round((_q(priciest, pillar)[0] or 0) - (_q(best, pillar)[0] or 0), 2),
            "times": (round((month(priciest) or 0) / (month(best) or 1), 1)
                      if (month(best) or 0) > 0 else None),
        }
    if openm is not None and openm is not best:
        out["open"] = card(openm)
    if localm is not None:
        out["local"] = card(localm)
    return out
