#!/usr/bin/env python3
"""
Chequeo de salud de los endpoints: qué modelos del catálogo siguen vivos.

POR QUE EXISTE
--------------
El 13-jul-2026, a mitad de un backfill de ~$44, descubrimos que 5 modelos del ranking
YA NO EXISTÍAN. Los 10 tests fallaban con "deprecated" o "No endpoints found". Uno de
ellos, **Devstral Small, estaba #5 del ranking**: alguien podía leer "#5, $0.48 cada
1.000 llamadas", integrarlo, y estrellarse contra un endpoint que no está.

Nos enteramos **tarde y caro**: porque el lote se estrelló, no porque lo comprobáramos.

Este script lo comprueba **antes**, por centavos: manda un ping mínimo (1 token) a cada
modelo y clasifica la respuesta.

MUERTO vs CAÍDO — la distinción que importa
-------------------------------------------
No es lo mismo un modelo retirado que uno con un mal día. Marcar como muerto a alguien
que solo tuvo un timeout sería tan malo como lo contrario.

  MUERTO      → el proveedor lo retiró. Error explícito y permanente:
                "deprecated", "No endpoints found", "not a valid model ID", 404.
                → propone `retired: True`.

  INTERMITENTE→ 429 (rate limit), 5xx, timeout. El modelo existe, el momento es malo.
                → NO se toca. Se reporta para reintentar.

  SIN CREDENCIAL → 401/403. No es culpa del modelo: falta la key de ese provider.
                → se avisa aparte, no se retira nada.

Uso:
    python benchmarks/check_endpoints.py                 # solo reporta
    python benchmarks/check_endpoints.py --ranked        # solo los que están en el ranking
    python benchmarks/check_endpoints.py --fix           # además parchea models.py
"""
import argparse
import json
import sys
import time
from pathlib import Path

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))

# ⚠️ Este import NO es decorativo: `benchmarks/config.py` es el ÚNICO módulo del repo que
# corre `load_dotenv()`. Sin él, el `.env` nunca se lee, `build_providers()` no encuentra
# ninguna credencial y ESTE SCRIPT REPORTA "SIN CREDENCIAL" EN TODOS LOS MODELOS — es decir,
# no puede detectar un solo muerto y termina en verde.
#
# Fallo real (11-ago-2026): corriendo dentro de `regenerate_all.py` dio SIN CREDENCIAL en los
# 70 rankeados. El pipeline no vio ningún MUERTO y publicó sin avisar nada. El guardrail que
# existe porque Devstral Small estuvo #5 con el endpoint apagado llevaba tiempo ciego.
# Si alguna vez hay que quitar este import, mover el `load_dotenv()` primero.
import benchmarks.config  # noqa: E402,F401  ← carga el .env. NO borrar (ver arriba)
from benchmarks.models import MODELS, OLLAMA_MODELS  # noqa: E402
from providers.registry import MissingCredential, build_providers, provider_for  # noqa: E402

MODELS_PY = ROOT / "benchmarks" / "models.py"
MODELS_JSON = ROOT / "docs" / "data" / "models.json"

# Errores que significan "el proveedor lo retiró". Permanentes, no se reintentan.
DEAD_MARKERS = (
    "deprecated",
    "no endpoints found",
    "not a valid model",
    "model_not_found",
    "does not exist",
    "no longer available",
    "has been removed",
    "decommissioned",   # la palabra que usa Groq
    "has been shut down",
    # 12-ago-2026 · Devstral 2 (`mistralai/devstral-2512`), RANKEADO con 136 runs, devolvía
    # 404 con este texto y caía al bucket genérico "ERROR" — o sea, se publicaba igual.
    # El mensaje de OpenRouter además se contradice: dice "migrá al slug pago:
    # mistralai/devstral-2512", que es EXACTAMENTE el slug que se estaba llamando. No hay
    # a dónde migrar. Confirmado por dos vías independientes: cero ids `devstral` en el
    # catálogo público, y la cuenta sana (mistral-large-2512 responde 200 con la misma key).
    "period has ended",
    "please migrate to",
)
# Errores del momento. El modelo existe; el intento fue malo.
TRANSIENT_MARKERS = ("rate limit", "429", "timeout", "timed out", "502", "503", "504", "overloaded")
# Falta la key de ese provider. No es problema del modelo.
AUTH_MARKERS = ("401", "403", "invalid api key", "unauthorized", "no auth credentials")
# Self-hosted en TU hardware (Spark, llama-server, Ollama local) que no responde.
# El modelo EXISTE y funcionaría con la máquina encendida. No es un endpoint retirado:
# marcarlo como muerto sería el mismo falso positivo que casi nos hace borrar a Llama
# 3.1 8B (que estaba vivo) por una credencial faltante.
LOCAL_DOWN_MARKERS = ("connection error", "connection refused", "max retries",
                      "failed to establish", "name or service not known", "no route to host")
PROVIDERS_LOCALES = ("llama_server", "llama_server_think", "ollama", "diffusion_cli")


def classify(err: str, provider: str = "") -> str:
    e = (err or "").lower()
    # Primero lo local: tu Spark apagado no es un modelo retirado.
    if provider in PROVIDERS_LOCALES and any(m in e for m in LOCAL_DOWN_MARKERS):
        return "APAGADO"
    if any(m in e for m in DEAD_MARKERS):
        return "MUERTO"
    if any(m in e for m in AUTH_MARKERS):
        return "SIN CREDENCIAL"
    if any(m in e for m in TRANSIENT_MARKERS):
        return "INTERMITENTE"
    return "ERROR"


def ping(cfg: dict, P: dict) -> tuple[str, str]:
    """Manda 1 token al modelo por EL MISMO CAMINO que usa el runner.

    Usar otro camino sería inútil: podría decir VIVO lo que el runner no logra llamar.
    """
    try:
        provider = provider_for(cfg, P)
    except MissingCredential as e:
        return "SIN CREDENCIAL", str(e)
    try:
        r = provider.chat(
            model=cfg["id"],
            messages=[{"role": "user", "content": "Di: ok"}],
            # 16, no 1. GPT-4.1 rechaza `max_output_tokens=1` con un 400 — y ese 400 se
            # lee igual que el de un modelo muerto. Un chequeo de salud que usa un valor
            # que algunos proveedores no aceptan inventa cadáveres. (13-jul-2026: me pasó.)
            max_tokens=16,
            temperature=0,
            timeout=30,
        )
        if getattr(r, "error", None):
            return classify(str(r.error)), str(r.error)[:110]
        return "VIVO", ""
    except Exception as e:  # noqa: BLE001
        return classify(str(e)), str(e)[:110]


def patch_models_py(dead: dict) -> int:
    """Añade `retired: True` a los modelos muertos, con la causa y la fecha."""
    import re
    t = MODELS_PY.read_text()
    today = time.strftime("%Y-%m-%d")
    n = 0
    for key, why in dead.items():
        m = re.search(rf'("{re.escape(key)}"\s*:\s*\{{)', t)
        if not m:
            print(f"     ⚠️  no encontré la clave «{key}» en models.py")
            continue
        if "retired" in t[m.end(): m.end() + 400]:
            continue
        # Campos ESTRUCTURADOS, no un comentario. Hasta el 12-ago-2026 la causa y la fecha
        # se escribían como `# texto (fecha)`: ningún generador podía leerlas, así que el
        # sitio no mostraba nada y la sección "Retirados" de MODELOS.md no podía decir ni
        # cuándo ni por qué. Peor: mezclaba los que sacó el proveedor con los que sacamos
        # nosotros (Phi-4 estaba listado bajo "el proveedor ya no los sirve" siendo que es
        # el juez del benchmark). Con campos, eso lo resuelve el generador.
        campos = (f'\n        "retired": True,'
                  f'\n        "retired_at": "{today}",'
                  f'\n        "retired_reason": "{why[:150]}",'
                  f'\n        "retired_kind": "provider",')
        t = t[:m.end()] + campos + t[m.end():]
        n += 1
    if n:
        MODELS_PY.write_text(t)
    return n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ranked", action="store_true", help="Solo los que están en el ranking")
    ap.add_argument("--fix", action="store_true", help="Parchea models.py con retired: True")
    ap.add_argument("--recheck-retired", action="store_true",
                    help="Al revés: pinguea SOLO los retirados y avisa si alguno revivió")
    args = ap.parse_args()

    catalog = {**MODELS, **OLLAMA_MODELS}

    only = None
    if args.ranked:
        if not MODELS_JSON.exists():
            sys.exit("Falta models.json — corré export_for_pages.py primero")
        d = json.loads(MODELS_JSON.read_text())
        only = {m["name"] for m in d["models"] if m.get("ranked")}

    if args.recheck_retired:
        # El retiro NO es una puerta de una sola vía, y esto lo descubrimos tarde.
        # `stepfun/step-3.5-flash` y `qwen/qwen-2.5-72b-instruct` se retiraron el
        # 14-jul-2026 con razón —ningún proveedor los servía— y el 12-ago-2026 volvían a
        # responder 200 (SiliconFlow y DeepInfra los recogieron). Como el chequeo normal
        # EXCLUYE a los retirados, un modelo que revive queda muerto para siempre en
        # nuestros datos: el error espejo de publicar uno muerto, y más difícil de ver
        # porque nada falla. Este modo existe para que eso se detecte solo.
        targets = {k: v for k, v in catalog.items() if v.get("retired")}
    else:
        targets = {
            k: v for k, v in catalog.items()
            if not v.get("retired") and (only is None or v.get("name") in only)
        }
    P = build_providers(include_ollama=True)
    print(f"Chequeando {len(targets)} endpoints (ping de 1 token cada uno)…\n")

    buckets = {"VIVO": [], "MUERTO": [], "INTERMITENTE": [], "SIN CREDENCIAL": [],
               "APAGADO": [], "ERROR": []}
    dead_reasons = {}

    for i, (k, cfg) in enumerate(targets.items(), 1):
        estado, detalle = ping(cfg, P)
        buckets[estado].append((k, cfg.get("name"), detalle))
        if estado == "MUERTO":
            prov = cfg.get("provider", "openrouter")
            dead_reasons[k] = f"{prov}: {detalle[:60]}"
        icon = {"VIVO": "·", "MUERTO": "💀", "INTERMITENTE": "…", "SIN CREDENCIAL": "🔑",
                "APAGADO": "🔌", "ERROR": "?"}[estado]
        print(f"  [{i:>3}/{len(targets)}] {icon} {cfg.get('name','')[:34]:<36} {estado}")

    print("\n" + "=" * 70)
    print(f"  VIVOS:          {len(buckets['VIVO'])}")
    print(f"  MUERTOS:        {len(buckets['MUERTO'])}   ← el proveedor los retiró")
    print(f"  INTERMITENTES:  {len(buckets['INTERMITENTE'])}   ← existen, reintentar")
    print(f"  SIN CREDENCIAL: {len(buckets['SIN CREDENCIAL'])}   ← falta la key del provider")
    print(f"  APAGADOS:       {len(buckets['APAGADO'])}   ← self-hosted tuyo, la máquina no responde")
    print(f"  OTROS ERRORES:  {len(buckets['ERROR'])}")

    if buckets["MUERTO"]:
        print("\n  💀 MUERTOS — no pueden aparecer como recomendación:")
        for k, name, det in buckets["MUERTO"]:
            print(f"       {name[:34]:<36} ({k})")
            print(f"         └ {det}")

    if buckets["INTERMITENTE"]:
        print("\n  … INTERMITENTES — NO se retiran; el modelo existe:")
        for k, name, det in buckets["INTERMITENTE"]:
            print(f"       {name[:34]:<36} {det[:44]}")

    if args.recheck_retired:
        # En este modo la noticia es al revés: un retirado que responde REVIVIÓ.
        if buckets["VIVO"]:
            print("\n  🔄 RESUCITADOS — están marcados retirados y HOY responden:")
            for k, name, _ in buckets["VIVO"]:
                cfg = catalog[k]
                print(f"       {name[:34]:<36} ({k})  retirado el {cfg.get('retired_at','?')}")
                print(f"         └ causa registrada: {cfg.get('retired_reason','—')}")
            print("\n     Volver a activarlos es una DECISIÓN, no un automatismo: quitar")
            print("     `retired` los devuelve al catálogo y puede reincorporarlos al")
            print("     ranking. Verificá con un ping de contenido real antes de tocar.")
        else:
            print("\n  ✓ Ningún retirado revivió.")
        return 0

    if args.fix and dead_reasons:
        n = patch_models_py(dead_reasons)
        print(f"\n  ✅ models.py parcheado: {n} modelo(s) marcados como retirados.")
        print("     Corré `regenerate_all.py` para sacarlos del ranking.")
    elif dead_reasons:
        print("\n  (corré con --fix para marcarlos como retirados en models.py)")

    return 1 if buckets["MUERTO"] else 0


if __name__ == "__main__":
    sys.exit(main())
