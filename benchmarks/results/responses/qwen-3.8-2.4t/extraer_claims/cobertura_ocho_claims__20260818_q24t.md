# Qwen 3.8 2.4T (A95B) — extraer_claims/cobertura_ocho_claims

- model_id: `qwen/qwen3.8-2.4t-a95b`
- success: True  | final: 8.37 | quality: 10.0
- latency_total: 22.947s | tokens_per_second: 89.2
- input_tokens: 317 | output_tokens: 2048

## Entrada exacta (lo que recibió el modelo)

**system:**

Extraé de la nota TODOS los datos verificables: cifras, fechas, nombres de empresas con su acción, y afirmaciones factuales que un verificador podría contrastar contra una fuente.

Devolvé SOLO un JSON:
{"claims": [{"texto": "<el dato, en una frase>", "tipo": "cifra|fecha|evento|cita"}]}

Reglas:
- NO extraigas opiniones, adjetivos ni proyecciones sin cifra.
- NO inventes: si no está en el texto, no va.
- Una cifra usada como EJEMPLO o comparación general no es un hecho de la nota.
- Respetá las negaciones: «no cerró» no es «cerró».

**user:**

Nordvia cerró una ronda semilla de US$ 4,2 millones el 14 de agosto de 2026, liderada por Aurora Ventures. La empresa, fundada en 2024 en Montevideo, emplea a 50 personas y opera en 3 países. Su facturación anual llegó a € 1,8 millones en 2025. Según su CEO, Marta Iribarne, la compañía abrirá oficinas en Chile durante el primer trimestre de 2027.


## Respuesta completa

We need to extract all verifiable data from the note: figures, dates, company names with their action, and factual claims that a verifier could check against a source.

The text: "Nordvia cerró una ronda semilla de US$ 4,2 millones el 14 de agosto de 2026, liderada por Aurora Ventures. La empresa, fundada en 2024 en Montevideo, emplea a 50 personas y opera en 3 países. Su facturación anual llegó a € 1,8 millones en 2025. Según su CEO, Marta Iribarne, la compañía abrirá oficinas en Chile durante el primer trimestre de 2027."

We need to output only JSON: {"claims": [{"texto": "<the data, in one sentence>", "tipo": "cifra|fecha|evento|cita"}]}

Rules:
- Do not extract opinions, adjectives, or projections without figures.
- Do not invent: if not in text, don't include.
- A figure used as example or general comparison is not a fact of the note.
- Respect negations: "no cerró" is not "cerró".

We need to classify each claim as cifra, fecha, evento, or cita.

Let's identify verifiable facts:

1. Nordvia cerró una ronda semilla de US$ 4,2 millones el 14 de agosto de 2026, liderada por Aurora Ventures.
This contains: event (closing seed round), amount US$4.2 million, date August 14, 2026, led by Aurora Ventures. We can break into claims:
- Nordvia closed a seed round of US$4.2 million. (evento/cifra? The amount is cifra, the closing is evento. But each claim should be one sentence. We can extract separate claims: "Nordvia cerró una ronda semilla de US$ 4,2 millones" tipo evento or cifra? The instruction says extract all verifiable data: figures, dates, company names with action, factual claims. We need to assign tipo. Probably:
  - "Nordvia cerró una ronda semilla de US$ 4,2 millones." could be evento (or cifra? It includes cifra). But we need to extract figures separately? The output expects claims with texto. We can make each atomic verifiable fact. For example:
    * "Nordvia cerró una ronda semilla." evento
    * "La ronda semilla de Nordvia fue de US$ 4,2 millones." cifra
    * "La ronda semilla de Nordvia se cerró el 14 de agosto de 2026." fecha
    * "La ronda semilla de Nordvia fue liderada por Aurora Ventures." evento (company action)
But the instruction says "empresas con su acción" so company names with action. We can extract as events.

Maybe better to keep as factual sentences from the text. The tipo categories: cifra, fecha, evento, cita.

- US$4.2 million is a cifra.
- August 14, 2026 is a fecha.
- Founded in 2024 is fecha.
- in Montevideo is evento? location fact.
- employs 50 people: cifra.
- operates in 3 countries: cifra.
- annual revenue reached €1.8 million in 2025: cifra and fecha? "€1.8 million" cifra, "2025" fecha. But the claim "Su facturación anual llegó a € 1,8 millones en 2025." includes both. We can split or keep as one? The instruction says extract all verifiable data: figures, dates, names... We can have multiple claims. Each claim should be one sentence. It's okay to have a claim with both figure and date, but tipo must be one. We need to choose the primary type? Probably extract atomic facts: "La facturación anual de Nordvia fue de € 1,8 millones en 2025." could be cifra or fecha? It includes both. Maybe better to split: "La facturación anual de Nordvia llegó a € 1,8 millones." cifra; "La facturación anual de Nordvia correspondió a 2025." fecha? But that's awkward. Alternatively, we can extract each distinct figure/date as separate claims with context. The instruction says "todos los datos verificables: cifras, fechas, nombres de empresas con su acción, y afirmaciones factuales". So we can list:
- Nordvia cerró una ronda semilla. (evento)
- El monto de la ronda semilla de Nordvia fue de US$ 4,2 millones. (cifra)
- La ronda semilla de Nordvia se cerró el 14 de agosto de 2026. (fecha)
- Aurora Ventures lideró la ronda semilla de Nordvia. (evento)
- Nordvia fue fundada en 2024. (fecha)
- Nordvia fue fundada en Montevideo. (evento)
- Nordvia emplea a 50 personas. (cifra)
- Nordvia opera en 3 países. (cifra)
- La facturación anual de Nordvia fue de € 1,8 millones en 2025. (cifra? or evento) But includes date. Could split: "La facturación anual de Nordvia alcanzó € 1,8 millones." cifra; "La facturación anual de Nordvia correspondió al año 2025." fecha. But maybe it's acceptable to have one claim with tipo cifra because the figure is main, and date is also verifiable. However, we need to extract all dates too. We can also add "2025" as fecha in a separate claim: "La facturación anual de € 1,8 millones de Nordvia correspondió a 2025." fecha.
- Marta Iribarne es CEO de Nordvia. (evento/cita? It's a factual claim, maybe evento)
- According to CEO, Marta Iribarne, the company will open offices in Chile during Q1 2027. This is a projection with date and location. The rule says "NO extraigas opiniones, adjetivos ni proyecciones sin cifra." This is a projection with a date and location. It says "proyecciones sin cifra" meaning don't extract projections without figures. This has a date (Q1 2027) and location, but it's a future plan. Is it verifiable? It's a statement attributed to CEO. The instruction says extract "citas"? tipo includes "cita". So maybe we should extract the attribution: "Según su CEO, Marta Iribarne, la compañía abrirá oficinas en Chile durante el primer trimestre de 2027." But it's a projection. The rule says no projections without figure. This has a date, which is a figure? Fecha. It might be extractable as a cita (quote/claim) because it's attributed. But we must be careful: "proyecciones sin cifra" not allowed. This projection has a fecha (primer trimestre de 2027) and a location (Chile). It might be considered a factual claim about a plan, verifiable against source. The tipo could be "cita" because it's according to CEO. Or "evento" future? But we should extract verifiable data: the statement itself is a claim. The instruction says "afirmaciones factuales que un verificador podría contrastar contra una fuente." The statement that the CEO said that is verifiable. The future opening is not yet factual, but the plan/announcement is. Given tipo includes "cita", likely we should extract attributed statements. But the rule says no projections without figure. This has a date, so maybe it's okay. However, "abrirá oficinas" is a future event, not a current fact. But it's a claim about intention. We can extract as cita: "Marta Iribarne, CEO de Nordvia, afirmó que la compañía abrirá oficinas en Chile durante el primer trimestre de 2027." That includes fecha. But is it a projection with cifra? It has fecha. The rule says no projections without cifra, implying projections with cifra might be extracted? It says "NO extraigas opiniones, adjetivos ni proyecciones sin cifra." So projections with cifra might be allowed? But it's still a projection. However, the date is verifiable as part of the statement. I think we should extract it as a cita, because it's attributed and includes a date. But we must ensure not to treat future as fact. The texto should reflect that it's a statement: "Según su CEO, Marta Iribarne, Nordvia abrirá oficinas en Chile durante el primer trimestre de 2027." tipo cita. Or maybe extract the CEO name and role as evento, and the statement as cita.

Let's list all possible claims:

1. Nordvia cerró una ronda semilla. (evento)
2. La ronda semilla de Nordvia fue de US$ 4,2 millones. (cifra)
3. La ronda semilla de Nordvia se cerró el 14 de agosto de 2026. (fecha)
4. Aurora Ventures lideró la ronda semilla de Nordvia. (evento)
5. Nordvia fue fundada en 2024. (fecha)
6. Nordvia fue fundada en Montevideo. (evento)
7. Nord