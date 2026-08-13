#!/usr/bin/env python3
"""Corre la tarea de cotización N veces contra varios modelos y verifica cada corrida.

Reporta pass^k: en cuántas de las k corridas el modelo sacó puntaje perfecto. Para un
agente eso importa más que el promedio — uno que acierta 7 de 10 veces es inservible
desatendido.
"""
import json, os, subprocess, sys, urllib.request
from pathlib import Path
from dotenv import load_dotenv

AQUI = Path(__file__).resolve().parent
load_dotenv(AQUI.parent.parent / ".env")
KEY = os.getenv("OPENROUTER_API_KEY")

CONSIGNA = "Cotizá el encargo del cliente."

def prompt() -> str:
    e = AQUI / "entorno"
    return (f"Sos el asistente de una consultora. Tenés estos archivos:\n\n"
            f"=== tarifario.csv ===\n{(e/'tarifario.csv').read_text()}\n"
            f"=== reglas.md ===\n{(e/'reglas.md').read_text()}\n"
            f"=== encargo.md ===\n{(e/'encargo.md').read_text()}\n"
            f"=== TAREA ===\n{CONSIGNA}")

def llamar(modelo: str, p: str) -> str:
    # 64.000 de techo de salida. `max_tokens` es un TECHO, no un cargo: solo se paga lo
    # que el modelo genera. Limitarlo no ahorraba nada y sí producía respuestas vacías —
    # los thinking models consumen el presupuesto razonando y devuelven content="".
    #
    # Cristian, 13-ago: "ese problema no estará en un agente real que usará el máximo
    # contexto disponible del modelo; manejemos un máximo de 64k, que sería un Hermes
    # con contexto pequeño". Correcto: la restricción era del script, no del caso de uso.
    body = {"model": modelo, "messages": [{"role": "user", "content": p}],
            "max_tokens": 64000, "temperature": 0.7}
    req = urllib.request.Request(
        "https://openrouter.ai/api/v1/chat/completions",
        data=json.dumps(body).encode(),
        headers={"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"})
    d = json.load(urllib.request.urlopen(req, timeout=600))
    ch = d["choices"][0]
    u = d.get("usage") or {}
    det = u.get("completion_tokens_details") or {}
    # Se guarda POR QUÉ terminó y cuánto razonó: sin esto no se distingue "se truncó"
    # de "falló de verdad", y las dos se ven igual en el puntaje.
    return (ch["message"].get("content") or "", {
        "finish_reason": ch.get("finish_reason"),
        "out_tokens": u.get("completion_tokens"),
        "reasoning_tokens": det.get("reasoning_tokens"),
    })

def puntuar(texto: str) -> dict:
    tmp = AQUI / ".tmp_resp.txt"
    tmp.write_text(texto, encoding="utf-8")
    out = subprocess.run([sys.executable, str(AQUI / "verificar.py"), str(tmp)],
                         capture_output=True, text=True).stdout
    tmp.unlink(missing_ok=True)
    for linea in out.splitlines()[::-1]:
        if linea.startswith("{"):
            return json.loads(linea)
    return {"puntos": 0}

# Un archivo de resultados POR MODELO: así N procesos corren en paralelo sin pisarse.
# La Regla 0 del RUNBOOK lo dice desde julio —"modelos cloud, NUNCA secuencial: el cuello
# es la latencia de red, no la CPU"— y lo escribí secuencial igual. 60 corridas en fila
# son ~75 min; en paralelo, ~12.
if __name__ == "__main__":
    modelos = sys.argv[1:-1] or ["openai/gpt-5.6-luna"]
    k = int(sys.argv[-1]) if sys.argv[-1].isdigit() else 3
    p = prompt()
    salida = AQUI / f"res_{modelos[0].replace('/', '_')}.json"
    todo = json.loads(salida.read_text()) if salida.exists() else {}
    for m in modelos:
        corridas = todo.get(m, [])
        for i in range(len(corridas), k):
            try:
                texto, meta = llamar(m, p)
                r = {**puntuar(texto), **meta, "chars": len(texto)}
            except Exception as e:
                r = {"puntos": None, "error": str(e)[:90]}
            corridas.append(r)
            todo[m] = corridas
            salida.write_text(json.dumps(todo, ensure_ascii=False, indent=1))
            pts = r.get("puntos")
            print(f"  {m:<34} run {i+1}/{k}: {pts if pts is not None else 'ERROR'}/17", flush=True)
