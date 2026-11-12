#!/usr/bin/env python3
"""Las cifras que la comunidad ya midió, mapeadas a nuestras `key`, con fecha y licencia.

POR QUÉ EXISTE (3-nov-2026, corte-v5 2.1)
-----------------------------------------
Regla de Cristian: *«usemos benchmarks públicos verificados por la comunidad. No cualquiera que
encontremos»*. `FUENTES-EXTERNAS.md` dice cuáles entran y por qué; este script las trae. Su
primer trabajo es un número: cuántos de los rankeados tienen dato comunitario. Ese número
decide el tamaño del conjunto base (tarea 2.3), y lo decide Cristian con el número delante.

LAS TRES FUENTES, AL 3-NOV-2026
-------------------------------
  Terminal-Bench 2.0   SE INGESTA. Dataset Apache-2.0 en Hugging Face, un `result.json` por
                       job con la recompensa de cada intento, mínimo 5 intentos por tarea.
  Toolathlon-Verified  NO se ingesta: ni el repo ni el dataset declaran licencia (y el
                       dataset pide login). Se enlaza. Issues abiertos sin respuesta: #87, #97.
  SWE-bench Pro        NO se ingesta: la tabla pública se arma con JavaScript y el repo (MIT)
                       solo trae trayectorias de 9 modelos de 2025, no los resultados. Se enlaza.

CÓMO SE LEE TERMINAL-BENCH (DECISIONES.md, 3-nov-2026)
------------------------------------------------------
Terminal-Bench puntúa pares AGENTE + MODELO. La cifra principal de un modelo es la del agente
de referencia del harness (Terminus); la del mejor agente va aparte y con el nombre del
agente. Nunca se promedian agentes ni versiones. La cifra de un envío es aciertos sobre el
total de intentos del job (89 tareas × k): un intento sin resultado cuenta como fallo, igual
que la media que publica el propio job.

Un envío con varios modelos (un agente que los combina) no se le atribuye a ninguno.

EL MAPEO ES EXPLÍCITO
---------------------
Nombre del envío → `key` de `models.py`, en `MAPA`, a mano y revisable. Nunca por `name`
(DECISIONES, 17-sep: el `name` colapsa variantes). Lo que no está en el mapa se lista como
«sin mapear» en vez de adivinarse.

Uso:
    python benchmarks/fuentes_externas.py               # offline, sobre la última foto
    python benchmarks/fuentes_externas.py --actualizar  # baja una foto nueva (red)
    python benchmarks/fuentes_externas.py --json        # la cobertura como JSON
"""

import argparse
import json
import re
import sys
from collections import Counter
import time
import urllib.request
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FOTOS = ROOT / "externos" / "fotos"
MODELS_JSON = ROOT / "sitio" / "legado" / "data" / "models.json"

TB_REPO = "harborframework/terminal-bench-2-leaderboard"
TB_VERSION = "2.0"
TB_RAIZ = f"submissions/terminal-bench/{TB_VERSION}"
TB_API = f"https://huggingface.co/api/datasets/{TB_REPO}/tree/main/"
TB_RAW = f"https://huggingface.co/datasets/{TB_REPO}/raw/main/"
TB_LICENCIA = "apache-2.0"
# El agente de referencia del harness. En los envíos aparece como «Terminus 2».
AGENTE_REFERENCIA = "Terminus 2"

NO_INGESTADAS = {
    "Toolathlon-Verified": {
        "url": "https://toolathlon.xyz/",
        "motivo": "sin licencia declarada en el repo ni en el dataset (que además pide login)",
        "issues": ["https://github.com/hkust-nlp/Toolathlon/issues/87",
                   "https://github.com/hkust-nlp/Toolathlon/issues/97"],
    },
    "SWE-bench Pro público": {
        "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public",
        "motivo": "la tabla se arma con JavaScript; el repo solo trae trayectorias de 9 modelos de 2025",
    },
}

# `model_name` del metadata.yaml del envío (en minúsculas) → `key` de models.py.
# Revisado a mano el 3-nov-2026 contra los ids de OpenRouter. Lo que no está, no se adivina.
MAPA = {
    "claude-opus-4-6": "claude-opus-4.6",
    "claude-opus-4.6": "claude-opus-4.6",
    "claude-opus-4-7": "claude-opus-4.7",
    "claude-opus-4.7": "claude-opus-4.7",
    "claude-sonnet-4-6": "claude-sonnet-4.6",
    "claude-sonnet-4.6": "claude-sonnet-4.6",
    "glm-5": "or-glm5",
    # Ojo: en models.py la key `or-deepseek-v3` es el id `deepseek/deepseek-v3.2`, y la key
    # `deepseek-v3` es `deepseek/deepseek-chat`. Se mapea por el id, que es lo que se midió.
    "deepseek-v3.2": "or-deepseek-v3",
    "kimi-k2.5": "or-kimi-k2.5",
    "minimax-m2.5": "or-minimax-m2.5",
    "minimax-m2.7": "minimax-m2.7",
    "gpt-5.5": "gpt-5.5",
    "gpt-5.4": "gpt-5.4",
    "gemini-3.1-pro-preview": "gemini-3.1-pro",
    "grok-4.20-0309-reasoning": "grok-4.20",
    "qwen3.6-35b-a3b": "qwen3.6-35b",
    "gpt-oss-20b": "or-gpt-oss-20b",
    # Los mismos modelos, escritos de otra forma por otros envíos.
    "anthropic/claude-opus-4-7": "claude-opus-4.7",
    "claude-4.6-opus": "claude-opus-4.6",
    "minimax/minimax-m2.7": "minimax-m2.7",
    "qwen/qwen3.6-35b-a3b": "qwen3.6-35b",
    # Qwen3 Coder 480B A35B servido en fp8: el mismo modelo que `qwen/qwen3-coder` de OpenRouter.
    "qwen/qwen3-coder-480b-a35b-instruct-fp8": "qwen3-coder",
    # Variante de la API directa de MiniMax; está en el catálogo, no en el ranking.
    "minimax-m2.7-highspeed": "minimax-m2.7-highspeed",
}
# Sin mapear A PROPÓSITO (no están en nuestro catálogo al 3-nov-2026): claude-4.5-sonnet,
# claude-opus-4-5, gemini-3-flash-preview, gemini-3-pro-preview, glm-4.7, gpt-5-nano,
# gpt-5.1-codex-mini, gpt-5.2, gpt-5.2-codex, gpt-5.3-codex, gpt-oss-20b-rl (un fine-tune de
# AfterQuery), qwen/qwen3.5-9b, ucsb-surfi/termigen-32b. Y `multiple`, que no es un modelo.


# ── red: solo con --actualizar ─────────────────────────────────────────────────
def _get(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "ai-benchmarks-alternativos/fuentes_externas"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def _arbol(ruta: str) -> list[dict]:
    return json.loads(_get(TB_API + ruta))


def _metadata(texto: str) -> dict:
    import yaml
    return yaml.safe_load(texto) or {}


def _aciertos_e_intentos(res: dict) -> tuple[int, int]:
    """Los dos formatos de `result.json` de job que hay en el dataset al 3-nov-2026.

    El de Harbor (`stats.evals.*.reward_stats`) y uno con `result.trial_pass_count`. Un
    tercero levanta excepción y el envío queda sin cifra: no se adivina.
    """
    if "stats" in res:
        a = sum(len((e.get("reward_stats") or {}).get("reward", {}).get("1.0", []))
                for e in res["stats"]["evals"].values())
        return a, res.get("n_total_trials") or res["stats"]["n_trials"]
    r = res.get("result") or {}
    if "trial_pass_count" in r and "total_trials" in r:
        return int(r["trial_pass_count"]), int(r["total_trials"])
    raise ValueError(f"formato de result.json desconocido: {sorted(res)[:8]}")


def bajar_terminal_bench() -> dict:
    filas = []
    for env in _arbol(TB_RAIZ):
        if env["type"] != "directory":
            continue
        nombre = env["path"].rsplit("/", 1)[-1]
        try:
            meta = _metadata(_get(TB_RAW + env["path"] + "/metadata.yaml").decode())
        except Exception as e:  # noqa: BLE001
            filas.append({"envio": nombre, "error": f"metadata.yaml ilegible: {type(e).__name__}"})
            continue
        aciertos = total = 0
        jobs, ilegibles = [], []
        for job in _arbol(env["path"]):
            if job["type"] != "directory":
                continue
            nombre_job = job["path"].rsplit("/", 1)[-1]
            try:
                res = json.loads(_get(TB_RAW + job["path"] + "/result.json"))
                a, n = _aciertos_e_intentos(res)
            except Exception as e:  # noqa: BLE001
                ilegibles.append(f"{nombre_job}: {type(e).__name__}: {e}"[:200])
                continue
            aciertos, total = aciertos + a, total + n
            jobs.append({"job": nombre_job, "aciertos": a, "intentos": n})
            time.sleep(0.1)
        filas.append({
            "envio": nombre,
            "agente": meta.get("agent_display_name"),
            "agente_url": meta.get("agent_url"),
            "modelos": [{"model_name": m.get("model_name"), "provider": m.get("model_provider"),
                         "display": m.get("model_display_name")} for m in meta.get("models") or []],
            "jobs": jobs,
            "aciertos": aciertos,
            "intentos": total,
            # Con un job ilegible la cifra sería de una parte del envío: no se publica.
            "cifra": round(aciertos / total, 4) if total and not ilegibles else None,
            "jobs_ilegibles": ilegibles,
        })
        time.sleep(0.1)
    info = json.loads(_get(f"https://huggingface.co/api/datasets/{TB_REPO}"))
    return {
        "fuente": "Terminal-Bench",
        "version": TB_VERSION,
        "url": f"https://huggingface.co/datasets/{TB_REPO}",
        "licencia": TB_LICENCIA,
        "consultado": date.today().isoformat(),
        "dataset_modificado": info.get("lastModified"),
        "agente_referencia": AGENTE_REFERENCIA,
        "metrica": "aciertos / intentos totales del job (89 tareas × k); un intento sin resultado es fallo",
        "envios": filas,
    }


# ── offline: lo que corre siempre ──────────────────────────────────────────────
def ultima_foto(prefijo: str) -> Path | None:
    fotos = sorted(FOTOS.glob(f"{prefijo}-*.json"))
    return fotos[-1] if fotos else None


# ── misma versión exacta (DECISIONES, 3-nov-2026) ───────────────────────────
# La banda externa se muestra solo si la fuente midió la MISMA versión del modelo que está
# en el índice. El `MAPA` dice a qué key apunta un nombre; esta regla dice si ese nombre es
# la versión que medimos o un pariente: otro snapshot (`grok-4.20-0309-reasoning` contra
# `x-ai/grok-4.20`), otro modo o otra cuantización (`…-fp8` contra `qwen/qwen3-coder`).
# Se compara el multiconjunto de tokens del nombre sin el proveedor: el orden y el
# separador no importan (`claude-4.6-opus` = `anthropic/claude-opus-4-6`), un token de más
# o de menos sí.
def _tokens(nombre: str) -> Counter:
    return Counter(x for x in re.split(r"[-._:\s]+", nombre.lower().split("/")[-1]) if x)


def misma_version(model_name: str, model_id: str) -> bool:
    return _tokens(model_name) == _tokens(model_id)


def _ids() -> dict[str, str]:
    """key → id de `models.py`, la fuente del id que medimos."""
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    from benchmarks.models import MODELS, OLLAMA_MODELS
    return {k: c["id"] for k, c in {**OLLAMA_MODELS, **MODELS}.items()}


def cifras_por_key(foto: dict, mapa: dict = MAPA,
                   ids: dict | None = None) -> tuple[dict, list[str], list[dict]]:
    """key → {referencia, mejor} desde una foto de Terminal-Bench; los modelos sin mapear; y
    los envíos mapeados que midieron OTRA versión del modelo, que no se muestran.

    `referencia` es la cifra del agente de referencia (o None si nadie lo corrió con él);
    `mejor` es la mejor cifra con cualquier agente, con su nombre. Nunca un promedio.
    Una key del `MAPA` sin id en `ids` levanta KeyError: sin id no se puede verificar la versión.
    """
    ids = _ids() if ids is None else ids
    por_key, sin_mapear, otra_version = {}, set(), []
    for f in foto["envios"]:
        if f.get("cifra") is None or len(f.get("modelos") or []) != 1:
            continue  # un envío con varios modelos no se le atribuye a ninguno
        mn = str(f["modelos"][0]["model_name"]).lower()
        key = mapa.get(mn)
        if key is None:
            sin_mapear.add(mn)
            continue
        if not misma_version(mn, ids[key]):
            otra_version.append({"envio": f["envio"], "model_name": mn, "key": key, "id": ids[key]})
            continue
        dato = {"cifra": f["cifra"], "agente": f["agente"], "envio": f["envio"],
                "intentos": f["intentos"]}
        e = por_key.setdefault(key, {"referencia": None, "mejor": None})
        if f["agente"] == foto["agente_referencia"]:
            if e["referencia"] is None or dato["cifra"] > e["referencia"]["cifra"]:
                e["referencia"] = dato
        if e["mejor"] is None or dato["cifra"] > e["mejor"]["cifra"]:
            e["mejor"] = dato
    return por_key, sorted(sin_mapear), otra_version


def cobertura(foto: dict, rankeados: list[dict], mapa: dict = MAPA) -> dict:
    keys = {m["key"] for m in rankeados}
    desconocidas = sorted(set(mapa.values()) - {m["key"] for m in rankeados} - _todas_las_keys())
    if desconocidas:
        raise ValueError(f"MAPA apunta a keys que no existen en models.json: {desconocidas}")
    por_key, sin_mapear, otra = cifras_por_key(foto, mapa)
    con_ref = sorted(k for k, v in por_key.items() if k in keys and v["referencia"])
    con_alguno = sorted(k for k, v in por_key.items() if k in keys)
    return {
        "fuente": foto["fuente"], "version": foto["version"], "consultado": foto["consultado"],
        "rankeados": len(keys),
        "con_agente_referencia": con_ref,
        "con_algun_agente": con_alguno,
        "fuera_del_ranking": sorted(k for k in por_key if k not in keys),
        "sin_mapear": sin_mapear,
        "otra_version": sorted({(o["model_name"], o["key"]) for o in otra}),
        "envios_multimodelo": [f["envio"] for f in foto["envios"] if len(f.get("modelos") or []) > 1],
    }


# ── Conjunto base (corte-v5 2.3) ────────────────────────────────────────────────
#
# Conjunto base = rankeados vigentes en `models.py` (sin `retired`, `unavailable` ni
# `pendiente_proveedor`) menos los que el último ping de `check_endpoints.py --ranked
# --guardar` dio MUERTOS. Las fuentes externas no lo recortan (DECISIONES, 3-nov-2026).
# El ping se guarda fechado en `externos/endpoints/` para que el número se recalcule sin red
# y sin volver a gastar. INTERMITENTE, SIN CREDENCIAL o ERROR no sacan a nadie: el modelo
# existe y un mal momento no es un retiro; se listan para que se vean.
ENDPOINTS = ROOT / "externos" / "endpoints"
NO_VIGENTE = ("retired", "unavailable", "pendiente_proveedor")


def ultimo_ping() -> Path | None:
    pings = sorted(ENDPOINTS.glob("endpoints-*.json"))
    return pings[-1] if pings else None


def resultados_efectivos(ping: dict) -> dict:
    """El estado vigente de cada key: el del ping completo, pisado por cada reverificación
    (`check_endpoints.py --keys … --guardar`) en orden de fecha. Cada resultado lleva la
    fecha en que se observó, para que el conteo diga de cuándo es cada dato."""
    res = {k: {**v, "fecha": ping["fecha"]} for k, v in ping["resultados"].items()}
    for rev in sorted(ping.get("reverificaciones", []), key=lambda r: r["fecha"]):
        for k, v in rev["resultados"].items():
            res[k] = {**v, "fecha": rev["fecha"]}
    return res


def conjunto_base(rankeados: list[str], catalogo: dict, ping: dict) -> dict:
    """Las keys del conjunto base, las que quedan fuera con su motivo, las que el ping no
    cubrió y las que respondieron con algo distinto de VIVO sin estar MUERTAS."""
    res = resultados_efectivos(ping)
    base, fuera = [], {}
    for k in sorted(set(rankeados)):
        cfg = catalogo[k]  # una key rankeada sin config en models.py es un error, no un cero
        motivo = next((f for f in NO_VIGENTE if cfg.get(f)), None)
        if motivo is None and res.get(k, {}).get("estado") == "MUERTO":
            motivo = f"MUERTO en el ping del {res[k]['fecha']}: {res[k].get('detalle', '')}"
        if motivo:
            fuera[k] = motivo
        else:
            base.append(k)
    return {
        "ping": ping["fecha"],
        "reverificado": max((r["fecha"] for r in ping.get("reverificaciones", [])), default=None),
        "rankeados": len(set(rankeados)),
        "base": base,
        "fuera": fuera,
        "sin_ping": [k for k in base if k not in res],
        "no_vivos": {k: res[k]["estado"] for k in base
                     if k in res and res[k]["estado"] != "VIVO"},
    }


def conjunto_base_actual() -> dict | None:
    """El conjunto base con los datos del repo: models.json (rankeados), models.py y el
    último ping guardado. None si todavía no hay ping."""
    ruta = ultimo_ping()
    if ruta is None:
        return None
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    from benchmarks.models import MODELS, OLLAMA_MODELS
    rankeados = [m["key"] for m in json.loads(MODELS_JSON.read_text())["models"]
                 if m.get("ranked")]
    return conjunto_base(rankeados, {**OLLAMA_MODELS, **MODELS}, json.loads(ruta.read_text()))


def _todas_las_keys() -> set[str]:
    return {m["key"] for m in json.loads(MODELS_JSON.read_text())["models"]}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--actualizar", action="store_true", help="baja una foto nueva (usa la red)")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    if a.actualizar:
        foto = bajar_terminal_bench()
        FOTOS.mkdir(parents=True, exist_ok=True)
        destino = FOTOS / f"terminal-bench-{TB_VERSION}-{foto['consultado']}.json"
        destino.write_text(json.dumps(foto, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print(f"  ✅ foto guardada: {destino.relative_to(ROOT)} · {len(foto['envios'])} envíos")

    ruta = ultima_foto(f"terminal-bench-{TB_VERSION}")
    if ruta is None:
        print("  ❌ no hay foto de Terminal-Bench: correr con --actualizar")
        return 1
    foto = json.loads(ruta.read_text())
    rankeados = [m for m in json.loads(MODELS_JSON.read_text())["models"] if m.get("ranked")]
    c = cobertura(foto, rankeados)
    cb = conjunto_base_actual()
    if a.json:
        print(json.dumps({**c, "conjunto_base": cb}, ensure_ascii=False, indent=1))
        return 0

    print(f"\nFuentes externas · foto {ruta.name}\n")
    print(f"  Terminal-Bench {c['version']} (consultado {c['consultado']}, licencia {foto['licencia']})")
    print(f"    con el agente de referencia ({foto['agente_referencia']}): "
          f"{len(c['con_agente_referencia'])} de {c['rankeados']} rankeados")
    print(f"    con algún agente:                               "
          f"{len(c['con_algun_agente'])} de {c['rankeados']} rankeados")
    if c["fuera_del_ranking"]:
        print(f"    mapeados pero no rankeados: {', '.join(c['fuera_del_ranking'])}")
    print(f"    sin mapear ({len(c['sin_mapear'])}): {', '.join(c['sin_mapear'])}")
    if c["otra_version"]:
        print("    otra versión del modelo, no se muestra: "
              + ", ".join(f"{mn} ≠ {k}" for mn, k in c["otra_version"]))
    print(f"    envíos con varios modelos, sin atribuir: {len(c['envios_multimodelo'])}")
    for nombre, info in NO_INGESTADAS.items():
        print(f"  {nombre}: no se ingesta — {info['motivo']}")
    if cb is None:
        print("\n  ⚠️  sin ping guardado: correr check_endpoints.py --ranked --guardar")
        return 0
    print(f"\n  Conjunto base: {len(cb['base'])} de {cb['rankeados']} rankeados "
          f"(models.py + ping del {cb['ping']}"
          + (f", reverificado el {cb['reverificado']}" if cb.get("reverificado") else "") + ")")
    for k, motivo in cb["fuera"].items():
        print(f"    fuera: {k} — {motivo}")
    if cb["no_vivos"]:
        print("    no respondieron VIVO, siguen dentro: "
              + ", ".join(f"{k} ({e})" for k, e in cb["no_vivos"].items()))
    if cb["sin_ping"]:
        print(f"    sin ping (rankeados después del {cb['ping']}): {', '.join(cb['sin_ping'])}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
