#!/usr/bin/env python3
"""Línea base de Search Console por tipo de página del registro. (12-nov-2026, motor-sitio 2.6)

POR QUÉ EXISTE
--------------
El corte cambia el motor de 204 URLs de un golpe. Para saber a las 4 y a las 8 semanas si ganó o
perdió tráfico, y en qué tipo de página, hace falta la foto de antes, congelada en el repo y por
tipo (ficha, comparación, ranking, landing, variantes, home, proveedores, redirect). Sin la foto,
la comparación se hace contra el recuerdo. No se atribuye nada antes de las 4 semanas (DECISIONES,
«SEO del motor», 11-nov-2026).

QUÉ GUARDA (`--out <dir>`)
  linea-base-gsc-<fecha>.json  totales del subdominio, agregados por tipo, cada URL con su tipo, la
                               serie diaria y el estado de indexación de cada URL destino.
  linea-base-gsc-<fecha>.md    las tablas por tipo, para leerlas sin abrir el JSON.

El 12-nov la serie diaria mostró que el subdominio pasó de ~100 impresiones al día a cero desde
el 16-ago-2026, y la inspección de URL dice «Crawled - currently not indexed» en la home y en las
comparaciones. Con eso, clics e impresiones de 90 días miden sobre todo la cola de agosto: el
estado de indexación por tipo es la parte de la línea base que sirve para comparar.

La posición por tipo es la media de las posiciones de sus URLs ponderada por impresiones, que es
como Search Console agrega. Una URL que Search Console reporta y el registro no declara (un query
string, `/data/models.json`, una URL vieja) va a «fuera del registro»: no se descarta.

La misma corrida, con otra `--fin`, sirve para la comparación de las 4 y las 8 semanas.

Uso (desde el repo padre, el secreto solo de su carpeta):
    sh scripts/infisical-run.sh --path /cloud/google/nyx -- \\
        python3 benchmarks/benchmarks/linea_base_gsc.py --out benchmarks/seo
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from collections import defaultdict
from datetime import date, timedelta
from pathlib import Path
from urllib.parse import urlsplit

sys.path.insert(0, str(Path(__file__).resolve().parent))

SITE = "sc-domain:cristiantala.com"
HOST = "benchmarks.cristiantala.com"


def cliente():
    from google.oauth2 import service_account
    from googleapiclient.discovery import build
    info = json.loads(os.environ["GOOGLE_SERVICE_ACCOUNT_NYX_JSON"])
    creds = service_account.Credentials.from_service_account_info(
        info, scopes=["https://www.googleapis.com/auth/webmasters.readonly"])
    return build("searchconsole", "v1", credentials=creds, cache_discovery=False)


def consulta(gsc, cuerpo: dict) -> list[dict]:
    return gsc.searchanalytics().query(siteUrl=SITE, body=cuerpo).execute().get("rows", [])


def tipo_de(url_completa: str, tipos: dict[str, str]) -> tuple[str, str]:
    p = urlsplit(url_completa)
    ruta = p.path or "/"
    if p.query or p.fragment:
        return ruta + (f"?{p.query}" if p.query else ""), "fuera del registro"
    if not ruta.endswith("/") and "." not in ruta.rsplit("/", 1)[-1]:
        ruta += "/"
    return ruta, tipos.get(ruta, "fuera del registro")


def inspeccionar(gsc, urls: list[str]) -> dict[str, dict]:
    """Estado de indexación de cada URL (URL Inspection API; cuota de 2.000 al día)."""
    out = {}
    for u in urls:
        try:
            r = gsc.urlInspection().index().inspect(body={"inspectionUrl": f"https://{HOST}{u}",
                                                          "siteUrl": SITE}).execute()
            i = r.get("inspectionResult", {}).get("indexStatusResult", {})
            out[u] = {"cobertura": i.get("coverageState"), "veredicto": i.get("verdict"),
                      "ultimo_rastreo": (i.get("lastCrawlTime") or "")[:10] or None}
        except Exception as e:  # una URL que falla no tumba la línea base: queda anotada
            out[u] = {"cobertura": f"error: {type(e).__name__}", "veredicto": None, "ultimo_rastreo": None}
    return out


def agregar(filas: list[dict]) -> dict:
    """Clics, impresiones, CTR y posición ponderada por impresiones de un conjunto de URLs."""
    c = sum(f["clics"] for f in filas)
    i = sum(f["impresiones"] for f in filas)
    pos = sum(f["posicion"] * f["impresiones"] for f in filas) / i if i else None
    return {"urls_con_datos": len(filas), "clics": c, "impresiones": i,
            "ctr": round(c / i, 4) if i else None, "posicion": round(pos, 1) if pos else None}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--fin", default=None, help="último día (AAAA-MM-DD); por defecto hoy - 2 (el retraso de GSC)")
    ap.add_argument("--dias", type=int, default=90)
    ap.add_argument("--sin-inspeccion", action="store_true", help="no inspecciona cada URL")
    a = ap.parse_args()
    import registro_paginas as rp

    fin = date.fromisoformat(a.fin) if a.fin else date.today() - timedelta(days=2)
    inicio = fin - timedelta(days=a.dias - 1)
    regs = rp.paginas()
    tipos = {e["url"]: e["tipo"] for e in regs}
    filtro = [{"filters": [{"dimension": "page", "operator": "contains", "expression": HOST}]}]
    gsc = cliente()

    base = {"startDate": inicio.isoformat(), "endDate": fin.isoformat(), "dimensionFilterGroups": filtro}
    tot = consulta(gsc, base)
    filas = consulta(gsc, {**base, "dimensions": ["page"], "rowLimit": 25000})

    diario = consulta(gsc, {"startDate": (fin - timedelta(days=179)).isoformat(), "endDate": fin.isoformat(),
                            "dimensions": ["date"], "dimensionFilterGroups": filtro, "dataState": "all"})
    serie = [{"fecha": r["keys"][0], "clics": int(r["clicks"]), "impresiones": int(r["impressions"])}
             for r in diario]
    destinos = [e["url"] for e in regs if not e["redirect_a"]]
    insp = {} if a.sin_inspeccion else inspeccionar(gsc, destinos)
    indexacion = defaultdict(lambda: defaultdict(int))
    for e in regs:
        if e["url"] in insp:
            indexacion[e["tipo"]][insp[e["url"]]["cobertura"]] += 1

    urls = []
    for r in filas:
        ruta, tipo = tipo_de(r["keys"][0], tipos)
        urls.append({"url": ruta, "tipo": tipo, "clics": int(r["clicks"]),
                     "impresiones": int(r["impressions"]), "posicion": round(r["position"], 1)})
    urls.sort(key=lambda f: (-f["clics"], -f["impresiones"], f["url"]))
    por_tipo = defaultdict(list)
    for f in urls:
        por_tipo[f["tipo"]].append(f)
    declaradas = defaultdict(int)
    for e in regs:
        declaradas[e["tipo"]] += 1
    tabla = {t: {"urls_declaradas": declaradas.get(t, 0), **agregar(por_tipo.get(t, []))}
             for t in sorted(set(declaradas) | set(por_tipo))}

    t0 = tot[0] if tot else {}
    out = {
        "generado": date.today().isoformat(), "propiedad": SITE, "host": HOST,
        "ventana": {"inicio": inicio.isoformat(), "fin": fin.isoformat(), "dias": a.dias},
        "total_subdominio": {"clics": int(t0.get("clicks", 0)), "impresiones": int(t0.get("impressions", 0)),
                             "ctr": round(t0.get("ctr", 0), 4), "posicion": round(t0.get("position", 0), 1)},
        "nota": "total_subdominio es el agregado por propiedad; la suma por URL puede diferir (Search Console "
                "agrega distinto por página). La posición por tipo está ponderada por impresiones.",
        "por_tipo": tabla, "urls": urls,
        "serie_diaria_180d": serie,
        "indexacion_por_tipo": {t: dict(v) for t, v in sorted(indexacion.items())},
        "inspeccion": insp,
    }
    a.out.mkdir(parents=True, exist_ok=True)
    nombre = f"linea-base-gsc-{date.today().isoformat()}"
    (a.out / f"{nombre}.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    ts = out["total_subdominio"]
    lin = [f"# Línea base de Search Console antes del corte del motor ({date.today().isoformat()})", "",
           f"Propiedad `{SITE}`, solo `{HOST}`. Ventana: {inicio.isoformat()} a {fin.isoformat()} ({a.dias} días).",
           f"Generado con `benchmarks/linea_base_gsc.py`; el detalle por URL está en `{nombre}.json`.", "",
           f"**Total del subdominio:** {ts['clics']} clics, {ts['impresiones']} impresiones, "
           f"CTR {ts['ctr'] * 100:.2f} %".replace(".", ",") + f", posición media {str(ts['posicion']).replace('.', ',')}.", "",
           "| Tipo | URLs declaradas | URLs con datos | Clics | Impresiones | CTR | Posición |",
           "|---|---:|---:|---:|---:|---:|---:|"]
    for t, v in sorted(tabla.items(), key=lambda kv: (-kv[1]["impresiones"], kv[0])):
        ctr = f"{v['ctr'] * 100:.2f} %".replace(".", ",") if v["ctr"] is not None else "—"
        lin.append(f"| {t} | {v['urls_declaradas']} | {v['urls_con_datos']} | {v['clics']} | "
                   f"{v['impresiones']} | {ctr} | {str(v['posicion']).replace('.', ',') if v['posicion'] is not None else '—'} |")
    if insp:
        estados = sorted({c for v in indexacion.values() for c in v})
        lin += ["", f"**Indexación de las {len(insp)} URLs destino** (URL Inspection API, {date.today().isoformat()}):", "",
                "| Tipo | " + " | ".join(estados) + " |", "|---|" + "---:|" * len(estados)]
        for t, v in sorted(indexacion.items()):
            lin.append(f"| {t} | " + " | ".join(str(v.get(c, 0)) for c in estados) + " |")
    dias_con = [d for d in serie if d["impresiones"]]
    if dias_con:
        ult = dias_con[-1]
        lin += ["", f"**Serie diaria (180 días):** {len(dias_con)} días con impresiones; el último, {ult['fecha']} "
                f"({ult['impresiones']} impresiones). El detalle está en el JSON."]
    lin += ["", "La posición por tipo está ponderada por impresiones. La suma por URL puede no coincidir "
            "con el total del subdominio: Search Console agrega distinto por página y por propiedad.",
            "", "Revisiones: a las 4 y a las 8 semanas del corte, con la misma ventana de 90 días "
            "(`--fin` el día de la revisión menos 2). No se atribuye nada antes de las 4 semanas.", ""]
    (a.out / f"{nombre}.md").write_text("\n".join(lin), encoding="utf-8")
    print("\n".join(lin))
    return 0


if __name__ == "__main__":
    sys.exit(main())
