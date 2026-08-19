# Seed 2.0 Code — ocr_extraction/handwritten_notes_extraction

- model_id: `bytedance-seed/seed-2.0-code`
- success: True  | final: 8.51 | quality: 10.0
- latency_total: 35.822s | tokens_per_second: 57.2
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


El usuario quiere que procese el OCR de la reunión y lo ponga en JSON según el esquema. Primero, voy paso a paso:

1. Texto corregido: Arreglar los errores de OCR: Reunlon → Reunión, equlpo → equipo, prod (abreviatura de producción, dejar como está o clarificar? Wait, el OCR tenía errores como 0 por o: Lanzamient0 → Lanzamiento, abr → abril, may → mayo, modul0 → módulo, webho0ks → webhooks, baj0 → bajo, actualzr → actualizar, prep → preparar, JDs (mantener, es Job Descriptions), falt0 → faltó. También fechas: 14/04/26 → wait, año? El OCR puso 26? Wait no, mirar el original: "14/04/26" — quizás es 2024? Porque las fechas posteriores son 16/04, 21/04, 23/04, 5 de mayo (no año, pero se infiere 2024). Wait, pero el OCR tiene 14/04/26 — tal vez es un error de OCR, 14/04/24? Wait no, revisar el texto original del usuario: el OCR es "14/04/26". Pero las fechas cercanas son abril 21, 16, 23, mayo 5. Quizás 26 es error de OCR por 24? Wait, o tal vez el usuario escribió 24 pero OCR lo leyó como 26. Wait, pero mejor: primero corregir errores obvios de caracteres:

- Reunlon → Reunión
- equlpo → equipo
- Lanzamient0 → Lanzamiento
- falt0 → faltó
- modul0 → módulo
- webho0ks → webhooks
- baj0 → bajo
- actualzr → actualizar
- prep → preparar
- p/ → para (o dejar como abreviatura? Pero el texto limpio debe ser legible, pero abreviaturas válidas como p/ se pueden mantener? Wait, no, el usuario dice corregir errores de OCR, no necesariamente expandir abreviaturas, pero errores de caracteres sí.

Ahora, fecha_reunion: el OCR dice 14/04/26, pero las fechas posteriores son abril 16, 21, 23, mayo 5. Es muy probable que sea un error de OCR: 14/04/24 (año 2024) en lugar de 26, porque 26 sería futuro si las demás son 24. O tal vez el OCR leyó mal el último dígito. Vamos a marcarla como 14/04/2024? Wait, pero el usuario puso "14/04/26" — tal vez es 14/04/2024, ya que 26 no tiene sentido con las fechas cercanas. Sí, porque el action item de Seba es para miercoles 16/04, que es dos días después del 14, así que 14/04/2024 es correcto, el 26 es error de OCR.

Asistentes: el OCR dice Asist: JP, MaJo, Seba, Cami. Ausentes: faltó Nico.

Action items: hay que estructurar cada uno:
- Seba: fix webhook bug para miércoles 16/04/2024 (agregar año por coherencia)
- MaJo: actualizar roadmap en Notion (no tiene fecha límite? Wait, el OCR no dice, así que dejar vacío?
- Cami: preparar demo para cliente Falabella para 23/04/2024
- JP: publicar JDs (Job Descriptions) en LinkedIn + GetOnBrd. También, el texto dice "JP hace JD p/ lunes" — wait, en la sección 3: Contratar 2 devs sr +1 QA: "JP hace JD p/ lunes" — ¿eso es un action item también? Wait, mirar el texto original:

El texto reconocido tiene:
3) Contratar 2 devs sr + 1 QA
   - presup aprob: $8M CLP/mes x 3 pax
   - JP hace JD p/ lunes

Y luego Action items explícitos:
- Seba: fix webhook bug p/ mierc 16/04
- MaJo: actualzr roadmap en Notion
- Cami: prep demo p/ cliente Falabella (23/04)
- JP: publicar JDs en LinkedIn + GetOnBrd

Wait, "JP hace JD p/ lunes" — ¿es parte de los action items? Porque el lunes es el 21/04, ya que la próxima reunión es lun 21/04 10am. Sí, porque el 14 es viernes? Wait no, 14/04/2024: ¿qué día es? Wait, no importa, el texto dice "JP hace JD p/ lunes" y la próxima reunión es lun 21/04, así que fecha límite 21/04/2024.

Así que los action items son:
1. Responsable: Seba, Tarea: Corregir bug crítico en API de webhooks, Fecha límite: 16/04/2024
2. Responsable: MaJo, Tarea: Actualizar roadmap en Notion, Fecha límite: (no especificada, dejar vacío?)
3. Responsable: Cami, Tarea: Preparar demo para cliente Falabella, Fecha límite: 23/04/2024
4. Responsable: JP, Tarea: Elaborar Job Descriptions (JDs) para contrataciones, Fecha límite: 21/04/2024
5. Responsable: JP, Tarea: Publicar JDs en LinkedIn + GetOnBrd, Fecha límite: (no especificada? Wait, el texto no dice, pero tal vez después de hacerlos el lunes? Pero mejor ceñirse al texto.)

Ahora fechas clave (timeline):
- 14/04/2024: Reunión del equipo de producción
- 16/04/2024: Fecha límite para corrección de bug de webhooks (Seba)
- 21/04/2024: Próxima reunión (10am) + Fecha límite para elaborar JDs (JP)
- 23/04/2024: Fecha límite para preparar demo de Falabella (Cami)
- 05/05/2024: Nueva fecha de lanzamiento v2.0 (movida del 28/04)
- 28/04/2024: Fecha original de lanzamiento v2.0 (cancelada/movida)

Decisiones: Hay que extraer las decisiones tomadas en la reunión:
1. Mover el lanzamiento de la versión 2.0 del 28 de abril al 5 de mayo
2. Aprobar presupuesto de $8M CLP mensual por 3 personas para contratación de 2 desarrolladores senior y 1 QA
3. Programar próxima reunión para el lunes 21 de abril a las 10am
4. Asignar el bug crítico de webhooks a Seba

Ahora, el texto corregido: Hay que arreglar todos los errores de OCR (0 por o, letras mal escritas, etc.):

Original errores:
- Reunlon → Reunión
- equlpo → equipo
- Lanzamient0 → Lanzamiento
- falt0 → faltó
- modul0 → módulo
- webho0ks → webhooks
- baj0 → bajo
- actualzr → actualizar
- prep → preparar
- 14/04/26 → 14/04/2024 (por coherencia con fechas cercanas, 26 es error OCR)
- mierc → miércoles
- lun → lunes
- p/ → para (se puede dejar como abreviatura o expandir, mejor expandir para claridad, pero si es abreviatura válida, pero el texto limpio debe ser correcto)

Así que el texto corregido quedaría:
"Reunión equipo producción - 14/04/2024
Asistentes: JP, MaJo, Seba, Cami (faltó Nico)

1) Lanzamiento v2.0 - mover del 2