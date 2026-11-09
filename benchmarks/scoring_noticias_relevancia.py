"""Scorer de la suite `noticias_relevancia`: decisión binaria PASA / NO_PASA, nota 10 o 0.

El modelo debe responder `{"decision": "PASA"|"NO_PASA", "motivo": "..."}`. El scorer es
tolerante con la FORMA (bloque ```json, texto alrededor, traza <think>, mayúsculas, «NO PASA»
con espacio o guion) y estricto con el FONDO: sin una decisión parseable la nota es 0, nunca
una media plausible. El `motivo` no se puntúa.

Si la respuesta trae varios JSON con decisión (un borrador y una respuesta final, típico de
los modelos que razonan en voz alta), manda el ÚLTIMO.
"""

import json
import re

_VALIDAS = {"PASA", "NO_PASA"}

_THINK = re.compile(r"<think>.*?</think>", re.DOTALL | re.IGNORECASE)
_FENCE = re.compile(r"```(?:json)?\s*(.*?)```", re.DOTALL | re.IGNORECASE)
_DECISION_SUELTA = re.compile(r'["\']?decision["\']?\s*:\s*["\']([^"\']+)["\']', re.IGNORECASE)


def _normalizar(valor):
    if not isinstance(valor, str):
        return None
    v = re.sub(r"[\s\-]+", "_", valor.strip().upper())
    return v if v in _VALIDAS else None


def _objetos_json(texto):
    """Devuelve, en orden de aparición, todo objeto JSON decodificable dentro del texto."""
    dec = json.JSONDecoder()
    objetos, i = [], 0
    while True:
        i = texto.find("{", i)
        if i < 0:
            return objetos
        try:
            obj, fin = dec.raw_decode(texto, i)
        except ValueError:
            i += 1
            continue
        if isinstance(obj, dict):
            objetos.append(obj)
        i = fin


def _decision_de(obj):
    for k, v in obj.items():
        if isinstance(k, str) and k.strip().lower() == "decision":
            return _normalizar(v)
    return None


def extraer_decision(response):
    """La decisión normalizada ('PASA' / 'NO_PASA') o None si no hay ninguna parseable."""
    if not isinstance(response, str) or not response.strip():
        return None
    texto = _THINK.sub("", response)

    candidatos = []
    for bloque in _FENCE.findall(texto):
        candidatos += _objetos_json(bloque)
    candidatos += _objetos_json(texto)
    decisiones = [d for d in (_decision_de(o) for o in candidatos) if d]
    if decisiones:
        # Los fences se recorren primero y luego el texto completo (que los incluye), así que
        # el último elemento es siempre el último JSON del texto.
        return decisiones[-1]

    # JSON roto (comilla de más, coma final): se rescata la clave `decision` si está escrita.
    sueltas = [d for d in (_normalizar(m) for m in _DECISION_SUELTA.findall(texto)) if d]
    return sueltas[-1] if sueltas else None


def score_noticias_relevancia(response, expected):
    """10.0 si la decisión coincide con `expected['decision']`, 0.0 en cualquier otro caso."""
    esperada = _normalizar((expected or {}).get("decision"))
    if esperada is None:
        raise ValueError(f"expected_answer sin decisión válida: {expected!r}")
    return 10.0 if extraer_decision(response) == esperada else 0.0
