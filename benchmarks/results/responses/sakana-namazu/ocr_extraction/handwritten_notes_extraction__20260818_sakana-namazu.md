# Sakana Namazu — ocr_extraction/handwritten_notes_extraction

- model_id: `sakana/sakana-namazu`
- success: True  | final: 8.68 | quality: 10.0
- latency_total: 6.687s | tokens_per_second: 306.3
- input_tokens: 485 | output_tokens: 2048

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

El usuario quiere que interprete notas manuscritas con errores de OCR, las corrija, extraiga action items, fechas y las presente en un formato JSON específico.

Primero, analicemos el texto OCR con errores:

"Reunlon equlpo prod - 14/04/26"
-> "Reunión equipo prod" o "Reunión equipo producto" (probablemente "equipo producto" o "equipo prod"). Fecha: 14/04/26 (probablemente 2026 o 14/04/2026, pero dado el contexto podría ser 2026 o simplemente 14/04/26. En el contexto de notas manuscritas, "26" probablemente es el año. Asumiré 14/04/2026 o mantener 14/04/26.

"Asist: JP, MaJo, Seba, Cami (falt0 Nico)"
-> Asistentes: JP, MaJo, Seba, Cami. Ausentes: Nico.

"1) Lanzamient0 v2.0 - mover de abr 28 a may 5"
-> Lanzamiento v2.0 - mover de abr 28 a may 5. Decisión: mover fecha de lanzamiento.

"   - falta QA en modul0 pagos"
-> falta QA en módulo pagos.

"   - bug crit en API webho0ks (Seba lo toma)"
-> bug crítico en API webhooks (Seba lo toma).

"2) Metricas Q1:"
-> Métricas Q1:

"   - MRR 52.1k (+15% vs Q4)"
-> MRR 52.1k (+15% vs Q4)

"   - churn baj0 a 3.1% (obj era 3.5%)"
-> churn bajó a 3.1% (objetivo era 3.5%)

"   - NPS subio a 51 (re bueno!!)"
-> NPS subió a 51 (re bueno!!)

"3) Contratar 2 devs sr + 1 QA"
-> Contratar 2 devs senior + 1 QA

"   - presup aprob: $8M CLP/mes x 3 pax"
-> presupuesto aprobado: $8M CLP/mes por 3 personas

"   - JP hace JD p/ lunes"
-> JP hace JD (Job Description) para lunes. El lunes más cercano sería 21/04 según punto 4, o podría ser lunes 14/04 (mismo día de la reunión) pero no tiene sentido. Probablemente se refiere al lunes siguiente: 21/04.

"4) Prox reunion: lun 21/04 10am"
-> Próxima reunión: lun 21/04 10am

"Action items:"
-> Action items:

"- Seba: fix webhook bug p/ mierc 16/04"
-> Seba: fix webhook bug para miércoles 16/04

"- MaJo: actualzr roadmap en Notion"
-> MaJo: actualizar roadmap en Notion. Sin fecha límite explícita, pero podría ser para la próxima reunión (21/04) o podría no tener fecha. En el texto no dice fecha. Dejaré sin fecha o inferir null/empty. Pero el esquema JSON requiere fecha_limite. Podría ser null o "".

"- Cami: prep demo p/ cliente Falabella (23/04)"
-> Cami: preparar demo para cliente Falabella (23/04). Fecha límite: 23/04.

"- JP: publicar JDs en LinkedIn + GetOnBrd"
-> JP: publicar JDs en LinkedIn + GetOnBrd. Sin fecha explícita, pero el punto 3 dice "JP hace JD p/ lunes" (21/04). Así que fecha límite probable: 21/04.

Ahora, fechas clave:
- 14/04/26 (o 2026): fecha de la reunión (asumo 14/04/2026)
- 16/04: fix webhook bug (Seba)
- 21/04: próxima reunión 10am, y JP publica JDs
- 23/04: demo cliente Falabella
- 28/04 (abr 28): fecha original lanzamiento v2.0
- 05/05 (may 5): nueva fecha lanzamiento v2.0

Decisiones:
- Mover lanzamiento v2.0 del 28/04 al 05/05
- Falta QA en módulo pagos
- Bug crítico en API webhooks asignado a Seba
- Contratar 2 devs senior + 1 QA
- Presupuesto aprobado: $8M CLP/mes por 3 personas
- JP hace JD para lunes

Sobre el JSON:
- "texto_corregido": texto limpio, con acentos y formato.
- "fecha_reunion": "14/04/2026" o "14/04/26". Voy a usar "14/04/2026" para ser más explícito, aunque podría ser 2026. También podría ser 14/04/2026. O simplemente 14/04/26. Voy a usar 2026.
- "asistentes": ["JP", "MaJo", "Seba", "Cami"]
- "ausentes": ["Nico"]
- "action_items": lista con objetos.
  * Seba: fix webhook bug, fecha_limite: "16/04/2026" (o 16/04/26)
  * MaJo: actualizar roadmap en Notion, fecha_limite: null o "" o "21/04/2026" (próxima reunión). Como no se especifica, podría ser null o "21/04/2026". Voy a poner "21/04/2026" dado que es la próxima reunión y es común que los action items sean para esa fecha. Pero el texto no dice. Para ser preciso, podría dejarlo como "" o inferir 21/04/2026. Creo que lo más honesto es poner null o "" pero el esquema dice string. Puedo poner "No especificada" o "21/04/2026". Mejor "No especificada" para MaJo y JP? Pero luego dice "JP hace JD p/ lunes" en el punto 3, que es 21/04. Así que JP tiene fecha 21/04. MaJo no tiene fecha explícita. Voy a poner "" para MaJo o "21/04/2026" si asumimos que es para la próxima reunión. Voy a poner null como string? No, el esquema sugiere string. Puedo poner "Pendiente" o dejar vacío. Voy a optar por poner "21/04/2026" para MaJo asumiendo próxima reunión, pero anotaré que es inferido? No, el JSON no debe tener comentarios. Mejor poner "" (string vacío) o "No especificada". Voy a usar "" para ser neutral.
  
  Espera, en el punto 3 dice "JP hace JD p/ lunes", y el lunes sería 21/04 (próxima reunión es lun 21/04). Así que el action item de JP tiene fecha límite 21/04/2026.
  
  Cami: 23/04/2026.
  
  Seba: 16/04/2026.

- "fechas_clave": lista de eventos.
  * 14/04/2026: Reunión equipo
  * 16/04/2026: Entrega fix webhook bug (Seba)
  * 21/04/2026: Próxima reunión + publicación JDs (JP)
  * 23/04/2026: Demo cliente Falabella
  * 28/04/2026: Fecha original lanzamiento v2.0 (movida)
  * 05/05/2026: Nueva fecha lanzamiento v2.0

- "decisiones": lista de strings.
  * "Mover fecha de lanzamiento v2.0 del 28 de abril al 5 de mayo debido a falta de QA en módulo de pagos y bug crítico en API de webhooks"
  * "Aprobar presupuesto de $8M CLP/mes para contratar 2 desarrolladores senior y 1 QA"
  * "Asignar a Seba la corrección del bug crítico en API de webhooks"
  * "JP responsable de crear las Job Descriptions (JD) para las nuevas vacantes"

Voy a preparar el texto corregido. Debe ser limpio, con buena redacción.

Texto corregido