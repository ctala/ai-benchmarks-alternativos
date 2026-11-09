#!/usr/bin/env python3
"""Solución de referencia: diagnostica cada ticket leyendo la evidencia de `/app` y aplica
el arreglo que dicta `README-operacion.md`. Los valores del arreglo se DERIVAN de las
fuentes de verdad, no vienen escritos acá.
"""
import csv, json, re
from datetime import datetime
from pathlib import Path

A = Path("/app")
log = (A / "n8n/ejecuciones.log").read_text(encoding="utf-8")
diag = []

# INC-1 · boletín en verde sin campaña: el filtro dejó 0 items. ¿Contra qué compara?
estado = json.loads((A / "estado/boletin.json").read_text())
campanas = json.loads((A / "listmonk/campanas.json").read_text())
enviadas = [c for c in campanas if c["tipo"] == "boletin" and c["status"] == "finished"]
real = max(enviadas, key=lambda c: datetime.fromisoformat(c["sent_at"]))["sent_at"]
assert "Filtrar nuevos(0)" in log
if datetime.fromisoformat(estado["ultimo_envio"]) > datetime.fromisoformat(real):
    estado["ultimo_envio"] = real
    (A / "estado/boletin.json").write_text(json.dumps(estado, ensure_ascii=False, indent=2) + "\n")
    diag.append({"ticket": "INC-1", "causa": "estado_con_fecha_futura", "archivo": "estado/boletin.json",
                 "arreglo": f"ultimo_envio = {real} (sent_at del último boletín finished)"})

# INC-2 · 535 tras el PUT del 4-nov con el cuerpo del GET: password enmascarado.
settings = json.loads((A / "listmonk/settings.json").read_text())
smtp_env = dict(l.split("=", 1) for l in (A / "secretos/smtp.env").read_text().splitlines()
                if "=" in l and not l.startswith("#"))
for s in settings["smtp"]:
    if re.fullmatch(r"[•*]+", s["password"]) and s["username"] == smtp_env["SMTP_USER"]:
        s["password"] = smtp_env["SMTP_PASSWORD"]
        diag.append({"ticket": "INC-2", "causa": "password_enmascarado", "archivo": "listmonk/settings.json",
                     "arreglo": "smtp[].password con el valor vigente de secretos/smtp.env"})
(A / "listmonk/settings.json").write_text(json.dumps(settings, ensure_ascii=False, indent=2) + "\n")

# INC-3 · se envía y no se registra: el CREATE falla porque `version` no acepta una versión aprobada.
esquema = json.loads((A / "nocodb/drip_estado.schema.json").read_text())
aprobadas = {r["version"] for r in csv.DictReader(open(A / "datos/drip_copy.csv", encoding="utf-8"))}
for col in esquema["columnas"]:
    if col["nombre"] == "version":
        faltan = sorted(aprobadas - set(col["opciones"]))
        col["opciones"] += faltan
(A / "nocodb/drip_estado.schema.json").write_text(json.dumps(esquema, ensure_ascii=False, indent=2) + "\n")
diag.append({"ticket": "INC-3", "causa": "opcion_select_faltante", "archivo": "nocodb/drip_estado.schema.json",
             "arreglo": f"se agregan a `version` las opciones {faltan}"})

(A / "diagnostico.json").write_text(json.dumps({"incidentes": diag}, ensure_ascii=False, indent=2) + "\n")
print(json.dumps(diag, ensure_ascii=False, indent=2))
