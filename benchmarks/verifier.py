#!/usr/bin/env python3
"""
LLM como VERIFICADOR de afirmaciones, no como juez de calidad.

EL ERROR QUE CORRIGE
--------------------
El benchmark usaba un LLM para responder *"¿está bien hecha esta auditoría?"*. Esa
pregunta es subjetiva, y los LLM la contestan que sí. Probamos seis jueces sin conflicto
de interés, de 14B a 671B (benchmarks/judge_bakeoff.py): **todos** le ponen la nota máxima
a casi todo, incluidas las respuestas que no vieron el error aritmético plantado. phi-4:
100% de techo, correlación 0.00 con la verdad objetiva. Cogito 671B: idéntico. No es un
problema de tamaño — una respuesta bien escrita que se equivoca **parece** excelente.

La alternativa era el matcher de keywords del rúbrico (`_score_reasoning`): busca que
≥60% de las palabras de cada insight aparezcan en el texto. No satura, pero castiga los
sinónimos — un modelo que dice lo correcto con otras palabras reprueba. Ya nos pasó: la
suite `persistencia` se descartó porque el string-matching leyó "no es viable" (que
descartaba una opción inferior) como una rendición.

Ninguna de las dos sirve. Pero el problema no era el LLM: era **la pregunta**.

    ✗  "¿Está bien hecha esta auditoría?"          → subjetivo  → 5/5 siempre
    ✓  "¿Esta respuesta afirma que los costos       → verificable → sí / no
        reales suman 9.150 y no 7.400?"

A la segunda, un LLM chico contesta bien. Es lectura comprensiva, no crítica literaria.
Y arregla las dos fallas a la vez: no satura (no está opinando) y entiende sinónimos
(no está haciendo grep).

CÓMO PUNTÚA
-----------
Por cada `key_insight` del test se pregunta una sola cosa, verificable, y se responde
SÍ/NO. El score es la fracción de insights que la respuesta realmente contiene.

    score = 10 * (insights afirmados / insights esperados)

Ese número no es una opinión sobre el estilo. Es cuántas de las cosas que había que ver,
el modelo vio.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))

# El verificador no necesita ser grande: está leyendo, no juzgando. phi-4 sirve, es
# barato, y Microsoft no tiene modelos en el benchmark (cero auto-preferencia).
VERIFIER_MODEL = "microsoft/phi-4"

PROMPT = """Sos un verificador. Tu única tarea es decir si un texto AFIRMA una idea concreta.

TEXTO A REVISAR:
---
{respuesta}
---

IDEA A BUSCAR:
"{insight}"

¿El texto afirma esa idea? Puede decirlo con otras palabras — lo que importa es el
contenido, no la redacción literal. No evalúes si el texto es bueno, ni si está bien
escrito, ni si estás de acuerdo. Solo si AFIRMA esa idea.

Respondé SOLO con JSON: {{"afirma": true}} o {{"afirma": false}}"""


class Verifier:
    def __init__(self, api_key: str, model: str = VERIFIER_MODEL,
                 base_url: str = "https://openrouter.ai/api/v1"):
        from openai import OpenAI
        self.model = model
        self.client = OpenAI(api_key=api_key, base_url=base_url)

    def afirma(self, respuesta: str, insight: str) -> bool | None:
        """¿El texto afirma esta idea? None si el verificador falla."""
        try:
            r = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user",
                           "content": PROMPT.format(respuesta=respuesta[:6000], insight=insight)}],
                temperature=0,
                max_tokens=20,
            )
            txt = (r.choices[0].message.content or "").strip()
            m = txt[txt.find("{"): txt.rfind("}") + 1]
            return bool(json.loads(m).get("afirma"))
        except Exception:  # noqa: BLE001
            return None

    def score(self, respuesta: str, key_insights: list[str]) -> float:
        """0-10 = qué fracción de lo que había que ver, el modelo vio."""
        if not key_insights:
            return -1.0
        vistos = 0
        validos = 0
        for i in key_insights:
            r = self.afirma(respuesta, i)
            if r is None:
                continue
            validos += 1
            vistos += int(r)
        if not validos:
            return -1.0
        return 10.0 * vistos / validos
