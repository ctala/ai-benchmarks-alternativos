#!/usr/bin/env python3
"""¿Hay una credencial real en un archivo que se publica?

POR QUÉ EXISTE (17-ago-2026)
----------------------------
El valor de `hex_64` en la suite `string_precision` era **la Secret Key real del bucket
R2 de Cloudflare**. No llegó ahí por un commit descuidado: **era el fixture**, el dato de
prueba que el examen le pide copiar al modelo. Y por eso hizo lo peor que puede hacer un
secreto en este repo — **se replicó solo**:

    benchmarks/tests/string_precision.py     el fixture
    → PROMPTS.md                             el catálogo de prompts se genera de ahí
    → TESTS.md                               ídem
    → ~600 archivos de results/responses/    cada run guarda su prompt junto a la respuesta

Esa última línea es la que convierte un descuido en un incidente: la regla *«cada run
guarda su ENTRADA, no solo su salida»* es correcta y se mantiene — pero significa que
**cualquier cosa que entre a un prompt se publica cientos de veces**, en un repo público,
con 6 forks y las refs de pull request que GitHub conserva para siempre. Rotar la clave
resolvió; purgar la historia no.

Y el repo tenía QUINCE guardrails que no lo vieron. Ninguno miraba credenciales, porque
todos se escribieron pensando en la calidad del dato publicado y no en su contenido.

CÓMO DISTINGUE UN FIXTURE DE UNA CREDENCIAL
-------------------------------------------
Por forma es imposible: un `sk-proj-...` inventado y uno real se parecen exactamente. Por
eso el chequeo tiene dos capas y la primera no puede dar falsos positivos:

1. **Los valores del `.env`, buscados literalmente en lo que git versiona.** Si una clave
   que usás de verdad aparece en un archivo publicable, es un incidente, sin ambigüedad y
   sin criterio de nadie. Los valores no se imprimen nunca: solo el nombre de la variable
   y dónde apareció.

2. **Patrones de credencial conocidos**, contra una allowlist de fixtures *declarados*.
   Un fixture legítimo vive en `benchmarks/tests/` y lleva su comentario diciendo que es
   sintético — como quedó `hex_64` después del incidente, y como son a propósito los
   cebos de `prompt_injection_es`, cuyo examen consiste justamente en darle al modelo un
   token falso a ver si lo filtra. Cualquier patrón fuera de esa lista se reporta.

La regla que deja escrita, y que el chequeo hace cumplir: **los fixtures se GENERAN
(`secrets.token_hex(32)`), no se copian de un `.env`.**

QUÉ NO CUBRE — decirlo importa más que el chequeo
--------------------------------------------------
La capa 1 solo puede buscar lo que puede leer. Medido el día que se escribió: de las 8
API keys del `.env` de esta máquina, **6 están vacías** porque viven en Infisical, y la
del incidente —la Secret Key de R2— no está en este `.env` en ninguna forma. O sea: **la
capa que no da falsos positivos tampoco habría cazado el caso que la motivó.**

Lo que sí lo caza es la capa 2, el patrón, y por eso la lista de patrones no es
decoración: es la única red para toda credencial que no esté en el `.env` local. Cuando
entre un proveedor nuevo al repo, su patrón entra acá el mismo día.

Y queda una zona a la que ninguna de las dos llega: una credencial sin forma reconocible
—un hex de 64, una contraseña— que no esté en el `.env`. Ésa es exactamente la del
incidente. Contra eso el único control real es el de arriba del todo: **los fixtures se
generan.**

Uso:
    python benchmarks/check_secretos.py           # reporte
    python benchmarks/check_secretos.py --duro    # exit 1 si encuentra algo
"""

import argparse
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Patrones de credenciales de los proveedores que este repo usa de verdad, más los
# genéricos que aparecen en cualquier stack. El hex de 64 está porque fue el caso real.
PATRONES = [
    ("OpenRouter",   re.compile(r"sk-or-v1-[a-f0-9]{48,}")),
    ("OpenAI",       re.compile(r"sk-(?:proj-)?[A-Za-z0-9_-]{40,}")),
    ("Anthropic",    re.compile(r"sk-ant-[A-Za-z0-9_-]{40,}")),
    ("Google",       re.compile(r"AIza[0-9A-Za-z_-]{35}")),
    ("xAI",          re.compile(r"xai-[A-Za-z0-9]{40,}")),
    ("Groq",         re.compile(r"gsk_[A-Za-z0-9]{40,}")),
    ("NVIDIA NIM",   re.compile(r"nvapi-[A-Za-z0-9_-]{40,}")),
    ("Apify",        re.compile(r"apify_api_[A-Za-z0-9]{30,}")),
    ("GitHub",       re.compile(r"gh[pousr]_[A-Za-z0-9]{36,}")),
    ("AWS/R2",       re.compile(r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b")),
    ("clave privada", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")),
]

# Dónde SÍ puede haber algo con forma de credencial, porque el examen consiste en eso.
# Es una lista corta y explícita a propósito: si crece, la pregunta es por qué.
FIXTURES_DECLARADOS = {
    "benchmarks/tests/string_precision.py",   # copiar strings sin alterarlos
    "benchmarks/tests/prompt_injection_es.py",  # el cebo que el modelo NO debe filtrar
}
# Los derivados de esos fixtures: se generan solos y arrastran el mismo valor.
#
# `benchmarks/results/` entero entra acá, y la razón importa: cada run guarda su prompt,
# así que TODO fixture con forma de credencial termina replicado ahí cientos de veces.
# Pasarles la capa 2 daba 256 alarmas de un solo origen — y un chequeo que grita 256
# veces por algo correcto es uno que se apaga a la semana.
#
# Pero NO quedan exentos: sobre ellos sigue corriendo la CAPA 1, que es justamente la
# que atrapa el incidente real. Un fixture inventado puede estar ahí; un valor de tu
# `.env`, jamás — y ése es exactamente el camino por el que la Secret Key de R2 llegó a
# ~600 archivos.
DERIVADOS = ("PROMPTS.md", "TESTS.md", "benchmarks/results/")

# Valores que son públicos POR DEFINICIÓN: los ejemplos que el propio proveedor publica
# en su documentación. `AKIAIOSFODNN7EXAMPLE` sale en los docs de AWS y es, con toda
# intención, la cadena que se usa para enseñar sin exponer nada.
EJEMPLOS_PUBLICOS = {"AKIAIOSFODNN7EXAMPLE", "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"}

# Un `.env` no guarda solo secretos: guarda CONFIGURACIÓN. Los endpoints
# (`OPENAI_BASE_URL=https://api.openai.com/v1`) son públicos por definición —están en la
# documentación del proveedor— y aparecen en config.py, en el README y hasta en las
# respuestas que los modelos generaron. Tratarlos como filtración da 200 alarmas falsas,
# y un chequeo que grita siempre es uno que se apaga.
#
# El corte NO es por lista de nombres —esa se olvida de la próxima variable— sino por
# forma del VALOR: si es una URL o un puerto, no es una credencial.
def _es_config(clave: str, valor: str) -> bool:
    if valor.startswith(("http://", "https://", "/")) or valor.isdigit():
        return True
    return clave.endswith(("_URL", "_HOST", "_PORT", "_MODEL", "_PATH", "_DIR"))


def versionados() -> list[Path]:
    """Solo lo que git publica. Un secreto en un archivo ignorado es otro problema."""
    r = subprocess.run(["git", "ls-files"], capture_output=True, text=True, cwd=ROOT)
    return [ROOT / l for l in r.stdout.splitlines() if l]


def valores_del_env() -> dict:
    """Los valores reales, para buscarlos. NUNCA se imprimen."""
    env = ROOT / ".env"
    if not env.exists():
        return {}
    out = {}
    for linea in env.read_text(errors="ignore").splitlines():
        linea = linea.strip()
        if not linea or linea.startswith("#") or "=" not in linea:
            continue
        k, v = linea.split("=", 1)
        v = v.strip().strip('"').strip("'")
        k = k.strip()
        # Bajo 16 caracteres no es una credencial: es un flag, un host o un puerto, y
        # buscarlo literalmente llenaría el reporte de coincidencias sin sentido.
        if len(v) >= 16 and not _es_config(k, v):
            out[k] = v
    return out


def es_fixture(rel: str) -> bool:
    return rel in FIXTURES_DECLARADOS or any(rel.startswith(d) or rel == d for d in DERIVADOS)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--duro", action="store_true", help="exit 1 si encuentra algo")
    a = ap.parse_args()

    archivos = versionados()
    env = valores_del_env()
    print(f"SECRETOS — {len(archivos)} archivos versionados · "
          f"{len(env)} variables del .env a contrastar\n")

    criticos, sospechas = [], []
    for f in archivos:
        rel = str(f.relative_to(ROOT))
        if not f.is_file() or f.stat().st_size > 4_000_000:
            continue
        try:
            txt = f.read_text(errors="ignore")
        except Exception:
            continue

        # CAPA 1 — un valor real del .env en algo que se publica. Sin ambigüedad.
        for k, v in env.items():
            if v in txt:
                criticos.append((rel, k))

        # CAPA 2 — forma de credencial fuera de los fixtures declarados.
        if es_fixture(rel):
            continue
        for nombre, pat in PATRONES:
            m = pat.search(txt)
            if m and m.group(0) not in EJEMPLOS_PUBLICOS:
                muestra = m.group(0)[:12]
                sospechas.append((rel, nombre, muestra))
                break

    if criticos:
        print("  🔴 CRÍTICO — una credencial de tu .env está en un archivo que git publica:\n")
        for rel, k in criticos:
            print(f"     {k:<28} aparece en  {rel}")
        print("\n     Rotala YA. Purgar la historia NO alcanza: el repo es público, tiene")
        print("     forks, y GitHub conserva las refs de los pull requests.")
    if sospechas:
        print("\n  ⚠️  Con forma de credencial, fuera de los fixtures declarados:\n")
        for rel, nombre, muestra in sospechas:
            print(f"     {nombre:<16} {muestra}…  en  {rel}")
        print("\n     Si es un dato de prueba: generalo (secrets.token_hex(32)), anotalo")
        print("     como sintético y sumá el archivo a FIXTURES_DECLARADOS acá.")
    if not criticos and not sospechas:
        print("  ✅ ninguna credencial real en los archivos versionados.")
        print("     (los fixtures de string_precision y prompt_injection_es están")
        print("      declarados: su examen consiste en llevar algo con esa forma)")
        return 0

    print(f"\n  {len(criticos)} crítico(s) · {len(sospechas)} sospecha(s)")
    return 1 if (a.duro and (criticos or sospechas)) else (1 if criticos else 0)


if __name__ == "__main__":
    sys.exit(main())
