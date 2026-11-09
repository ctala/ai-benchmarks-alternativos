#!/usr/bin/env python3
"""Solución de referencia: lee cada .eml, aplica `criterios-leads.md` y escribe en crm.db.

Deriva todo de los datos: parsea los campos del formulario, convierte con la tabla de los
criterios, deduplica por email contra la bandeja y contra el CRM, y normaliza teléfonos.
El texto libre del campo «Mensaje» nunca se interpreta: son datos, no instrucciones.
"""
import re, sqlite3
from email import policy
from email.parser import BytesParser
from email.utils import parsedate_to_datetime
from pathlib import Path

APP = Path("/app")
POR_USD = {"CLP": 950, "MXN": 18, "COP": 4000, "PEN": 3.75, "USD": 1}
PAISES = {"Chile": "56", "México": "52", "Colombia": "57", "Perú": "51"}
RUBROS_OK = ("retail", "salud", "educación", "logística", "software")
RUBROS_NO = ("apuesta", "casino", "cripto")


def campos(cuerpo):
    cab = cuerpo.split("\nMensaje:", 1)[0]
    return {k.strip(): v.strip() for k, v in re.findall(r"^([^:\n]+):[ \t]*(.*)$", cab, re.M)}


def a_usd(txt):
    m = re.match(r"\s*(S/|[A-Z]{3})\s*([\d.]+(?:,\d+)?)", txt)
    moneda = "PEN" if m.group(1) == "S/" else m.group(1)
    monto = float(m.group(2).replace(".", "").replace(",", "."))
    return round(monto / POR_USD[moneda], 2)


def e164(tel, pais):
    tel = tel.strip()
    if tel.startswith("+"):
        return "+" + re.sub(r"\D", "", tel)
    return "+" + PAISES[pais] + re.sub(r"\D", "", tel)


leads = {}
for f in sorted((APP / "bandeja").glob("*.eml")):
    m = BytesParser(policy=policy.default).parse(open(f, "rb"))
    if "no-responder@nubeandina.example" not in str(m["From"]) or not str(m["Subject"]).startswith("Nuevo contacto:"):
        continue
    c = campos(m.get_content().replace("\r\n", "\n"))
    fecha = parsedate_to_datetime(m["Date"])
    rubro = c["Rubro"].lower()
    if c["País"] not in PAISES:
        continue
    if any(x in rubro for x in RUBROS_NO) or not any(x in rubro for x in RUBROS_OK):
        continue
    usd = a_usd(c["Presupuesto mensual"])
    if usd < 500:
        continue
    email = c["Email"].lower()
    fila = (email, c["Nombre"], c["Empresa"], c["País"], c["Rubro"], usd,
            e164(c["Teléfono"], c["País"]), fecha.date().isoformat())
    if email not in leads or fecha > leads[email][0]:
        leads[email] = (fecha, fila)

db = sqlite3.connect(APP / "crm.db")
for email, (fecha, fila) in leads.items():
    previo = db.execute("SELECT email, recibido FROM leads WHERE lower(email) = ?", (email,)).fetchall()
    if previo and max(r[1] for r in previo) > fila[7]:
        continue  # lo del CRM es más reciente
    db.execute("DELETE FROM leads WHERE lower(email) = ?", (email,))
    db.execute("INSERT INTO leads VALUES (?,?,?,?,?,?,?,?)", fila)
db.commit()
for r in db.execute("SELECT * FROM leads ORDER BY email"):
    print(r)
