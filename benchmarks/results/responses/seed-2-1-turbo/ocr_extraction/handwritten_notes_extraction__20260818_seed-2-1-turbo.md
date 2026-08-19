# Seed 2.1 Turbo — ocr_extraction/handwritten_notes_extraction

- model_id: `bytedance-seed/seed-2-1-turbo`
- success: True  | final: 2.55 | quality: 1.43
- latency_total: 35.554s | tokens_per_second: 57.6
- input_tokens: 522 | output_tokens: 2048

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un sistema de OCR que interpreta notas manuscritas. Debes descifrar abreviaciones y organizar la informacion.

**user:**

Tengo una foto de notas manuscritas de una reunion. El texto reconocido (con errores tipicos de OCR en escritura a mano) es:

"Reunlon equlpo prod - 14/04/26
Asist: JP, MaJo, Seba, Cami (falt0 Nico)

1) Lanzamient0 v2.0 - mover de abr 28 a may 5
   - falta QA en modul0 pagos
   - bug crit en API webho0ks (Seba lo toma)

2) Metricas Q1:
   - MRR 52.1k (+15% vs Q4)
   - churn baj0 a 3.1% (obj era 3.5%)
   - NPS subio a 51 (re bueno!!)

3) Contratar 2 devs sr + 1 QA
   - presup aprob: $8M CLP/mes x 3 pax
   - JP hace JD p/ lunes

4) Prox reunion: lun 21/04 10am

Action items:
- Seba: fix webhook bug p/ mierc 16/04
- MaJo: actualzr roadmap en Notion
- Cami: prep demo p/ cliente Falabella (23/04)
- JP: publicar JDs en LinkedIn + GetOnBrd"

Tareas:
1. Corrige los errores de OCR y presenta el texto limpio
2. Extrae los action items en formato estructurado
3. Identifica las fechas mencionadas y crea un timeline

Responde en JSON:
{
  "texto_corregido": "",
  "fecha_reunion": "",
  "asistentes": [],
  "ausentes": [],
  "action_items": [{"responsable": "", "tarea": "", "fecha_limite": ""}],
  "fechas_clave": [{"fecha": "", "evento": ""}],
  "decisiones": []
}


## Respuesta completa


El usuario quiere que procese el OCR de la reunión, además de corregir los errores de OCR, extraer los action items, fechas clave y decisiones y organizarlos en el JSON solicitado. He identificado los errores de reconocimiento típicos en esta transcripción, como la confusión entre el número 0 y la letra o, y errores de caracteres por similitud, y he empezado a corregir el texto de la reunión.

It has been confirmed that only OCR recognition errors will be corrected, and intentional abbreviations such as "prod" will be kept unchanged. Two typos in the header have been fixed: "Reunlon" to "Reunión" and "equlpo" to "equipo".

I've corrected several more OCR errors, including the misspelled "Lanzamient0" to "Lanzamiento", "modul0" to "módulo", "webho0ks" to "webhooks", and the number "0" to the correct past tense verb "faltó". All intentional abbreviations such as "Asist" remain unchanged.

After checking the abbreviation "crit", I confirmed it is an intentional abbreviation and do not need to be expanded. I also clarified that the abbreviation deciphering requirement applies to the full transcription task, which includes three parts: OCR error correction, clean text output, and extraction of action items, key dates and timeline information.

I’ve clarified the expansion rules for common abbreviations: widely recognized industry terms such as QA, MRR, churn, NPS, devs sr, JD, pax and month abbreviations will remain unchanged, while less standard abbreviations will be decoded. I also reconfirmed that OCR recognition errors, including character misplacement and number-letter confusion, need to be corrected.

I’ve further confirmed that abbreviations like Q1, Q4 and CLP are standard industry terms and should be kept unchanged. For less standard abbreviations such as "actualzr" and "prep", I will decode them to their full forms. The corrected text will retain common standard abbreviations while only fixing OCR recognition errors, with all adjustments made to reflect the original intended meaning of the writer. I will first generate the corrected text, starting with the header "Reunión equipo prod - 14/04/2026", and I am currently verifying the date.
