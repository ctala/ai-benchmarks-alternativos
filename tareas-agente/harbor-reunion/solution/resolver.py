#!/usr/bin/env python3
"""Solución de referencia: DERIVA el tablero actualizado desde los dos archivos (R8).

No es un JSON precomputado a propósito: si mañana se cambia una tarea del tablero base,
esto se recalcula en vez de quedar mudo. Las decisiones de la reunión sí están
codificadas acá —son el "criterio humano" que la tarea mide— pero parten del tablero
real, no de una copia congelada.
"""
import json
from pathlib import Path

APP = Path("/app") if Path("/app/tablero.json").exists() else Path(__file__).parent.parent / "environment"

tablero = json.loads((APP / "tablero.json").read_text(encoding="utf-8"))
por_id = {t["id"]: dict(t) for t in tablero["tareas"]}

# ── Lo que se decidió en la reunión ──────────────────────────────────────────

# T-01 · «listo» pero falta el correo de confirmación → SIGUE abierta,
#        y pasa a ser lo primero de la semana.
por_id["T-01"]["estado"] = "en_curso"
por_id["T-01"]["prioridad"] = "alta"
por_id["T-01"]["nota"] = ("El pago funciona. Falta el correo de confirmación al cliente: "
                          "sin eso no se cierra. Acordado como lo primero de la semana.")

# T-02 · el precio se menciona como 12.000 y se CORRIGE a 14.000. Queda cerrado.
por_id["T-02"]["estado"] = "hecho"
por_id["T-02"]["nota"] = "Plan mensual definido en 14.000 (se corrigió el 12.000 inicial)."

# T-03 · seguro: NO se decide hoy, falta la diferencia de precio. Lo toma Marcela
#        (ojo: «Diego Rojas» es el corredor, no el socio).
por_id["T-03"]["estado"] = "pendiente"
por_id["T-03"]["responsable"] = "Marcela"
por_id["T-03"]["nota"] = ("Dos opciones del corredor. Se decide cuando esté la diferencia "
                          "de precio entre la cobertura amplia y la básica.")

# T-04 · se confirma que queda en baja, sin cambios (no se contrata hasta tener ingresos).
por_id["T-04"]["nota"] = ("Sin cambios: no se contrata al tercer técnico hasta tener "
                          "ingresos.")

# T-05 · la ficha de servicio SUBE a alta. No se duplica: la «condiciones del servicio»
#        que se menciona es esta misma.
por_id["T-05"]["prioridad"] = "alta"
por_id["T-05"]["nota"] = ("Sube a alta: sin la ficha firmada no se puede atender al "
                          "primer cliente. Es la misma que 'condiciones del servicio'.")

# T-06 · hecha, no se toca.

# ── Lo ÚNICO nuevo que se acordó anotar ─────────────────────────────────────
# La app se propuso y se DESCARTÓ explícitamente → no entra.
siguiente = f"T-{max(int(i.split('-')[1]) for i in por_id) + 1:02d}"
por_id[siguiente] = {
    "id": siguiente,
    "titulo": "Definir qué se hace ante una falla no prevista en la bici",
    "estado": "pendiente",
    "prioridad": "media",
    "responsable": "Marcela",
    # Sin respuesta: la reunión NO la definió. Inventarla es el fallo que la tarea caza.
    "nota": ("Pendiente de definir. Opciones mencionadas sin resolver: cobrar aparte, "
             "incluir, o avisar y esperar. No se tomó decisión en la reunión."),
}

salida = {
    "proyecto": tablero["proyecto"],
    "socios": tablero["socios"],
    "actualizado": "2026-08-14",
    "tareas": list(por_id.values()),
}
Path("/app/tablero_actualizado.json" if Path("/app").exists()
     else Path(__file__).parent / "tablero_actualizado.json").write_text(
    json.dumps(salida, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(f"tablero actualizado: {len(salida['tareas'])} tareas")
