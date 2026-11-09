#!/usr/bin/env python3
"""Solución de referencia: cada respuesta se LEE del proyecto, ninguna viene escrita acá.

Si cambia `.python-version`, el pin de ruff, el `.env.local`, la carpeta de reportes o la
última migración, la solución sigue siendo correcta.
"""
import re, subprocess, sys
from importlib import metadata
from pathlib import Path

P = Path("/app/proyecto")

# 1 · versiones que fija el proyecto (README: `.python-version` manda; ruff en requirements-dev)
python = (P / ".python-version").read_text().strip()
ruff = re.search(r"^ruff==(\S+)", (P / "requirements-dev.txt").read_text(), re.M).group(1)
dep = (P / "config/deploy.toml").read_text()
dep = re.sub(r'^python = ".*"', f'python = "{python}"', dep, flags=re.M)
dep = re.sub(r'^ruff = ".*"', f'ruff = "{ruff}"', dep, flags=re.M)
(P / "config/deploy.toml").write_text(dep)

# 2 · la dependencia que falta: la dice el error real, no la costumbre
r = subprocess.run([sys.executable, str(P / "scripts/sincronizar.py"), "--simular"],
                   capture_output=True, text=True)
falta = re.search(r"No module named '([^'.]+)", r.stderr)
if falta:
    modulo = falta.group(1)
    # nombre de import → nombre de distribución (los que difieren)
    dist = {"dateutil": "python-dateutil", "yaml": "PyYAML", "bs4": "beautifulsoup4",
            "PIL": "Pillow", "dotenv": "python-dotenv"}.get(modulo, modulo)
    subprocess.run([sys.executable, "-m", "pip", "install", "-q", dist], check=True)
    version = metadata.version(dist)
    req = (P / "requirements.txt").read_text().rstrip("\n").splitlines()
    req.append(f"{dist}=={version}")
    (P / "requirements.txt").write_text("\n".join(req) + "\n")
subprocess.run([sys.executable, str(P / "scripts/sincronizar.py"), "--simular"], check=True)

# 3 · el reporte, con la convención que muestran los meses anteriores
previo = sorted((P / "reportes").glob("*/*.csv"))[-1]          # reportes/2026-09/ventas-2026-09.csv
mes_previo = previo.parent.name
mes = "2026-10"
destino = P / "reportes" / mes / previo.name.replace(mes_previo, mes)
subprocess.run([sys.executable, str(P / "scripts/exportar.py"), "--mes", mes,
                "--salida", str(destino)], check=True)

# 4 · la base del entorno: .env, y .env.local manda sobre .env (README)
env = {}
for nombre in (".env", ".env.local"):
    f = P / nombre
    if f.exists():
        for linea in f.read_text().splitlines():
            if "=" in linea and not linea.lstrip().startswith("#"):
                k, v = linea.split("=", 1)
                env[k.strip()] = v.strip()
(P / "config/app.toml").write_text(
    f'[db]\nhost = "{env["DB_HOST"]}"\nport = {int(env["DB_PORT"])}\nnombre = "{env["DB_NAME"]}"\n')

# 5 · la migración: siguiente número, mismo ancho, mismo estilo de nombre
mig = sorted((P / "db/migraciones").glob("*.sql"))
ultimo = mig[-1].name.split("_", 1)[0]
sig = str(int(ultimo) + 1).zfill(len(ultimo))
(P / "db/migraciones" / f"{sig}_crear_boletas.sql").write_text(
    "CREATE TABLE boletas (\n    id SERIAL PRIMARY KEY,\n    folio TEXT NOT NULL,\n"
    "    fecha DATE NOT NULL,\n    monto_clp INTEGER NOT NULL\n);\n")
print("listo")
