#!/usr/bin/env python3
"""Verifica que el effort de razonamiento salga de la regla, no de un string fijo.

POR QUÉ EXISTE (14-sep-2026)
----------------------------
Del 2 al 14-sep se mandó `effort: medium` a todo thinking model por OpenRouter. Nadie lo
contrastó con lo que cada modelo declara soportar, y en 10 de los rankeados `medium` no
era un nivel válido: GLM 5.3 reportaba 0 tokens de razonamiento contra 619 de su default.
La regla era razonable; faltaba el instrumento. La vigente —el examen es el default de
cada modelo, y se sabe cuál es— está en `effort.py`.

QUÉ VERIFICA
------------
E1. Todo modelo del catálogo que va por OpenRouter está en la foto (o en sus ausentes).
    Uno nuevo sin foto rendiría sin que el run sepa en qué modo lo hizo.
E2. Todo `reasoning_effort` declarado en un test es un nivel que existe. Y que el
    detector haya leído tests: un E2 que no encuentra ninguno está ciego, no en verde.
E3. Sobre CADA modelo de la foto y CADA nivel:
      · sin pedido no se manda nada, y la etiqueta registra el default declarado;
      · un pedido nunca manda un effort fuera de `supported_efforts`;
      · nunca se le enciende el razonamiento a un modelo con `default_enabled: false`.
E4. (aviso) la foto tiene más de 45 días: el default de un proveedor pudo cambiar.
    Se confirma con `python benchmarks/effort.py --vivo`.
E5. Ningún archivo que lee el export trae runs con effort PEDIDO. Un experimento es otro
    examen: si cae en `results/benchmark_*.json`, el export lo promedia con el índice. Así
    entraron a lo publicado 27 runs con `medium` forzado (piloto del 2-sep), y el 4-sep
    quedaron 92 más esperando la próxima regeneración. El export además los descarta.
E6. Ningún `benchmark_*.json` con nombre de experimento (exp, piloto…). Los runs viejos
    no tienen etiqueta de effort y E5 no los ve: el nombre es la única huella que dejan.
E7. La foto tiene los parámetros que declara cada modelo. Sin ellos `effort.declara()`
    devuelve None, el adapter vuelve a mandar `max_tokens` a quien no lo acepta, y los
    tests con herramientas dan 404: así perdió Sakana Namazu 81 runs y el ranking.

E8. El examen de v5 (thinking por peldaño, DECISIONES 4-nov-2026), un caso por clase:
      · interruptor → el apagado manda `{effort: none}` si declara el nivel, si no
        `{enabled: false}`, y la etiqueta empieza con `apagado:`;
      · siempre piensa → no se manda nada y la etiqueta dice `siempre_piensa:default:X`;
      · apagado por defecto y sin razonamiento → no se manda nada.
    Y el pedido por suite: apagado en TODO peldaño 1-2, nada en 3-4 ni fuera del índice.
    Si alguna clase no aparece en la foto, el detector está ciego y es rojo.

E9. Todo RANKEADO tiene su nivel de razonamiento declarado: los de OpenRouter en la foto,
    los demás en `reasoning_directo.json` con la fuente citada (corte-v5 6.2). Sin eso la
    línea «medido en» de su ficha diría «default» a secas.

E5 y E6 cazan contaminación por PRESENCIA: tiene número, tiene forma válida y pasa
`validate.py`. Los detectores de ausencia del repo no la iban a ver.

Uso:  python benchmarks/check_effort.py
"""
import importlib.util
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "benchmarks"))

from benchmarks import effort  # noqa: E402

DIAS_AVISO = 45
MIN_TESTS = 100   # hay más de 200; bajo esto el detector no está leyendo lo que cree


def e1_cobertura(foto: dict, catalogo: dict) -> list[str]:
    conocidos = set(foto.get("modelos", {})) | set(foto.get("ausentes", []))
    return [f"E1 {k} ({c['id']}) no está en la foto — correr `effort.py --actualizar`"
            for k, c in sorted(catalogo.items())
            if c.get("id") and c.get("provider", "openrouter") == "openrouter"
            and not c.get("retired") and c["id"] not in conocidos]


def _tests_declarados() -> list[tuple[str, dict]]:
    out = []
    for py in sorted((ROOT / "benchmarks" / "tests").glob("*.py")):
        if py.name.startswith("_"):
            continue
        spec = importlib.util.spec_from_file_location(f"_check_effort_{py.stem}", py)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        for v in vars(mod).values():
            if isinstance(v, list):
                out += [(py.stem, t) for t in v
                        if isinstance(t, dict) and "name" in t
                        and ("messages" in t or "reasoning_effort" in t)]
    return out


def e2_niveles(tests: list[tuple[str, dict]]) -> list[str]:
    if len(tests) < MIN_TESTS:
        return [f"E2 sólo leyó {len(tests)} tests (se esperan ≥{MIN_TESTS}): el detector "
                "está ciego, no en verde"]
    return [f"E2 {archivo}/{t['name']}: reasoning_effort={t['reasoning_effort']!r} no es "
            f"un nivel ({', '.join(effort.NIVELES)})"
            for archivo, t in tests
            if t.get("reasoning_effort") is not None
            and str(t["reasoning_effort"]).strip().lower() not in effort.NIVELES]


def e3_resolver(foto: dict) -> list[str]:
    out = []
    for mid, rz in sorted(foto.get("modelos", {}).items()):
        rz = rz or {}
        niveles = rz.get("supported_efforts") or []

        ef, etiqueta = effort.resolver(mid, None, foto=foto)
        if ef is not None:
            out.append(f"E3 {mid}: sin pedido manda {ef!r} — el examen es el default, "
                       "no se manda nada")
        default = rz.get("default_effort")
        if (niveles and rz.get("default_enabled") is not False and default
                and etiqueta != f"default:{default}"):
            out.append(f"E3 {mid}: la etiqueta {etiqueta!r} no registra el default "
                       f"declarado {default!r}")

        for pedido in effort.NIVELES:
            ef, _ = effort.resolver(mid, pedido, foto=foto)
            if ef is None:
                continue
            if ef not in niveles:
                out.append(f"E3 {mid}: pedido={pedido!r} manda {ef!r}, fuera de {niveles}")
            elif rz.get("default_enabled") is False:
                out.append(f"E3 {mid}: le enciende el razonamiento (default_enabled=false)")
    return out


# E6: el nombre después de `benchmark_` delata un experimento. `validacion_…` no entra: es
# la validación de una suite nueva, medida en el default.
EXPERIMENTO_EN_NOMBRE = re.compile(r"(^|_)(exp|piloto|experimento|prueba)(_|\.)", re.I)
# E5: se busca en el texto crudo, sin parsear: son ~640 archivos y ~80 MB, y el QA rápido
# no puede tardar lo que tarda cargarlos todos.
EFFORT_PEDIDO = re.compile(rb'"reasoning_effort"\s*:\s*"pedido:')


def e5_e6_indice_limpio() -> list[str]:
    out = []
    for f in sorted((ROOT / "benchmarks" / "results").glob("benchmark_*.json")):
        if EXPERIMENTO_EN_NOMBRE.search(f.name[len("benchmark_"):]):
            out.append(f"E6 {f.name}: nombre de experimento en la carpeta que lee el export "
                       "— moverlo a results/_experimentos/")
        if EFFORT_PEDIDO.search(f.read_bytes()):
            out.append(f"E5 {f.name}: trae runs con effort pedido, o sea otro examen — "
                       "moverlo a results/_experimentos/")
    return out


def e7_parametros(foto: dict) -> list[str]:
    params = foto.get("parametros")
    if params is None:
        return ["E7 la foto no tiene `parametros`: el adapter no sabe qué modelo no declara "
                "max_tokens y los tests con herramientas vuelven a dar 404 — correr "
                "`effort.py --actualizar`"]
    return [f"E7 {mid}: la foto no tiene sus parámetros declarados"
            for mid in sorted(foto.get("modelos", {})) if mid not in params]


def e8_examen_v5(foto: dict) -> list[str]:
    from benchmarks.suites import PELDANO, SUITES
    out, vistas = [], set()
    for mid, rz in sorted(foto.get("modelos", {}).items()):
        cls = effort.clase(mid, foto=foto)
        vistas.add(cls)
        ef, et = effort.resolver(mid, effort.APAGADO, foto=foto)
        niveles = (rz or {}).get("supported_efforts") or []
        if cls == "interruptor" and effort.sin_apagado_en_endpoint(mid):
            # 7-nov-2026 · el endpoint declarado no acepta apagar (Mistral Large 4.0 en
            # mistral/zdr, `sin_apagado` en proveedores_declarados.json): se mide como
            # siempre_piensa, al default, y la etiqueta tiene que decirlo.
            if ef is not None or not et.startswith("siempre_piensa:default:"):
                out.append(f"E8 {mid} (interruptor, endpoint sin apagado): manda {ef!r} con "
                           f"etiqueta {et!r}; se esperaba None y `siempre_piensa:default:…`")
        elif cls == "interruptor":
            esperado = {"effort": "none"} if "none" in niveles else {"enabled": False}
            if ef != esperado or not et.startswith("apagado:"):
                out.append(f"E8 {mid} (interruptor): apagar manda {ef!r} con etiqueta "
                           f"{et!r}; se esperaba {esperado!r} y `apagado:…`")
        elif ef is not None:
            out.append(f"E8 {mid} ({cls}): el apagado le manda {ef!r} — solo se apaga a "
                       f"quien tiene interruptor")
        elif cls == "siempre_piensa" and not et.startswith("siempre_piensa:default:"):
            out.append(f"E8 {mid}: siempre piensa y la etiqueta {et!r} no lo dice")
    for falta in sorted({"interruptor", "siempre_piensa", "apagado_por_defecto",
                         "sin_razonamiento"} - vistas):
        out.append(f"E8 ninguna entrada de la foto es `{falta}`: el detector está ciego")
    for suite in SUITES:
        p = PELDANO.get(suite)
        quiere = effort.APAGADO if p is not None and p <= 2 else None
        if effort.pedido_por_suite(suite) != quiere:
            out.append(f"E8 `{suite}` (peldaño {p}): el examen pide "
                       f"{effort.pedido_por_suite(suite)!r}, debía pedir {quiere!r}")
    return out


def e9_rankeados_con_nivel(catalogo: dict) -> list[str]:
    import json
    mj = ROOT / "sitio" / "legado" / "data" / "models.json"
    rank = [m["key"] for m in json.loads(mj.read_text())["models"] if m.get("ranked")]
    if not rank:
        return ["E9 models.json no trae rankeados: el detector está ciego"]
    out = []
    for k in rank:
        c = catalogo.get(k)
        if not c:
            continue
        prov = c.get("provider", "openrouter")
        prov = "openrouter" if prov == "openrouter" else "directo"
        nivel = effort.nivel_declarado(c["id"], prov)
        if nivel == "no_registrado":
            print(f"  ⚠ E9 {k}: ausente de OpenRouter el día de la foto — nivel «no registrado»")
        if nivel is None:
            fuente = "la foto de OpenRouter" if prov == "openrouter" else "reasoning_directo.json"
            out.append(f"E9 {k} ({c['id']}) está rankeado y no tiene nivel declarado en {fuente}")
    return out


def main() -> int:
    foto = effort.cargar_foto()
    if not foto.get("modelos"):
        print("❌ E0 no hay foto de effort (benchmarks/reasoning_openrouter.json) — "
              "correr `python benchmarks/effort.py --actualizar`")
        return 1

    from benchmarks.models import MODELS
    tests = _tests_declarados()
    fallos = (e1_cobertura(foto, MODELS) + e2_niveles(tests) + e3_resolver(foto)
              + e5_e6_indice_limpio() + e7_parametros(foto) + e8_examen_v5(foto)
              + e9_rankeados_con_nivel(MODELS))

    tomada = foto.get("tomada")
    if tomada and (date.today() - date.fromisoformat(tomada)).days > DIAS_AVISO:
        print(f"  ⚠ E4 la foto es del {tomada}: confirmar con `effort.py --vivo` antes de un lote")

    for f in fallos:
        print(f"  ❌ {f}")
    if fallos:
        print(f"❌ {len(fallos)} problema(s) con el effort de razonamiento")
        return 1

    con = sum(1 for v in foto["modelos"].values() if v and v.get("supported_efforts"))
    print(f"✅ effort: foto del {tomada} · {len(foto['modelos'])} modelos ({con} con niveles "
          f"declarados) · {len(tests)} tests leídos · E1-E3, E5-E9 en verde")
    return 0


if __name__ == "__main__":
    sys.exit(main())
