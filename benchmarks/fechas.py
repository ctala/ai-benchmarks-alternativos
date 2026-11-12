#!/usr/bin/env python3
"""Las fechas que publica el sitio salen del dato, nunca fijas. (11-nov-2026, motor-sitio 2.4)

Dos piezas:

1. **El año de un título sale de la fecha de la medición.** «Mejor LLM para programar (2026)»
   estaba escrito así en la config: el 1-ene-2027 la página seguiría diciendo 2026 sin que nadie
   midiera nada, o diría 2027 sin medir nada nuevo. La config lleva `{anio}` y se resuelve con
   `models.json → medido_hasta` (la última ejecución contada de un rankeado). Una ficha usa la
   de su modelo (`medido_en.hasta`).

2. **`dateModified` y `lastmod` solo cambian con el contenido** (`fechar_dist`, abajo). Antes se
   movían a hoy en cada regeneración: 135 páginas amanecían «actualizadas» por un commit que no
   les cambió una palabra. Google aprende a no creerle a un `lastmod` así.
"""
from __future__ import annotations

import hashlib
import json
import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MODELS = ROOT / "sitio" / "legado" / "data" / "models.json"
REGISTRO = ROOT / "sitio" / "fechas_contenido.json"

MESES = ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto",
         "septiembre", "octubre", "noviembre", "diciembre")


# ── 1. El año de los títulos ──────────────────────────────────────────────────

def medido_hasta(d: dict | None = None) -> str:
    d = d if d is not None else json.loads(MODELS.read_text(encoding="utf-8"))
    f = d.get("medido_hasta")
    if not f:
        raise SystemExit("models.json no trae `medido_hasta`: corre export_for_pages.py")
    return f


def anio(d: dict | None = None) -> str:
    return medido_hasta(d)[:4]


def titular(texto: str, d: dict | None = None) -> str:
    """Resuelve `{anio}` en un texto de configuración."""
    return texto.replace("{anio}", anio(d)) if "{anio}" in texto else texto


def resolver_config(cfgs: list[dict], claves=("title", "h1", "lead")) -> list[dict]:
    """Cada `{anio}` de las claves dadas, resuelto en el lugar. Si models.json no existe todavía
    (un checkout vacío), se deja el marcador: el guardrail de títulos lo marca en rojo."""
    if not MODELS.exists():
        return cfgs
    d = json.loads(MODELS.read_text(encoding="utf-8"))
    for c in cfgs:
        for k in claves:
            if isinstance(c.get(k), str):
                c[k] = titular(c[k], d)
    return cfgs


# ── 2. dateModified y lastmod solo con cambio de contenido ───────────────────

FECHA_MOD = re.compile(r'("dateModified":\s*")(\d{4}-\d{2}-\d{2})(")')
# Las dos formas visibles de la fecha de modificación: «Última actualización: D» (rankings,
# comparaciones, landings) y «· actualizado D» (fichas). «medido el D» no: es contenido.
ULTIMA = re.compile(r"((?:Última actualización:|·\s*actualizado)\s*)(\d{4}-\d{2}-\d{2})")
MARCA = "AAAA-MM-DD"


def huella(html: str) -> str:
    """La huella del contenido de una página: su texto visible y su JSON-LD, sin la fecha de
    modificación, sin la cabecera, el pie ni las referencias a CSS y JS. Cambiar el estilo o la
    navegación no cambia la huella; cambiar una frase, una cifra o una fila, sí. Función pura."""
    h = FECHA_MOD.sub(lambda m: m.group(1) + MARCA + m.group(3), html)
    h = ULTIMA.sub(lambda m: m.group(1) + MARCA, h)
    jsonld = "".join(re.findall(r'<script type="application/ld\+json">(.*?)</script>', h, re.S))
    cuerpo = re.search(r"<main\b[^>]*>(.*)</main>", h, re.S)
    cuerpo = cuerpo.group(1) if cuerpo else re.sub(r"<head\b.*?</head>", " ", h, flags=re.S)
    cuerpo = re.sub(r"<(script|style)\b[^>]*>.*?</\1>", " ", cuerpo, flags=re.S | re.I)
    cuerpo = re.sub(r"<(header|footer|nav)\b[^>]*>.*?</\1>", " ", cuerpo, flags=re.S | re.I)
    texto = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", cuerpo)).strip()
    return hashlib.sha256((texto + "\n" + re.sub(r"\s+", " ", jsonld)).encode("utf-8")).hexdigest()[:16]


def fecha_de(url: str, html: str, registro: dict, hoy: str) -> tuple[str, bool]:
    """(fecha de modificación, ¿cambió el registro?). Si la huella es la registrada, la fecha
    registrada; si no, hoy. Función pura."""
    h = huella(html)
    e = registro.get(url)
    if e and e.get("huella") == h:
        return e["modificada"], False
    registro[url] = {"huella": h, "modificada": hoy}
    return hoy, True


def fechar(html: str, fecha: str) -> str:
    """Escribe la fecha de modificación en el JSON-LD y en «Última actualización»."""
    html = FECHA_MOD.sub(lambda m: m.group(1) + fecha + m.group(3), html)
    return ULTIMA.sub(lambda m: m.group(1) + fecha, html)


def leer_registro(ruta: Path = REGISTRO) -> dict:
    return json.loads(ruta.read_text(encoding="utf-8")) if ruta.exists() else {}


def escribir_registro(reg: dict, ruta: Path = REGISTRO) -> None:
    ruta.write_text(json.dumps(dict(sorted(reg.items())), ensure_ascii=False, indent=1) + "\n",
                    encoding="utf-8")


def hoy() -> str:
    return date.today().isoformat()
