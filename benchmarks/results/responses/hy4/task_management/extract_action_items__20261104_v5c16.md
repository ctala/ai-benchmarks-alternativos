# Tencent Hy4 — task_management/extract_action_items

- model_id: `tencent/hy4`
- success: True  | final: 8.71 | quality: 9.6
- latency_total: 7.563s | tokens_per_second: 77.1
- input_tokens: 232 | output_tokens: 583
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando una estructura organizada y prioridades basadas en dependencias.

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un asistente que organiza notas de reunion.

**user:**

Aqui estan las notas de la reunion de hoy:

Reunion de equipo - 11 abril 2026
Asistentes: Maria (PM), Carlos (Dev), Ana (Diseno), Pedro (QA)

- Maria comento que el deadline del proyecto Alpha es el 30 de abril
- Carlos necesita terminar el API de pagos antes del 20 de abril
- Ana va a entregar los mockups del dashboard el lunes 14
- Pedro dijo que faltan escribir tests para el modulo de autenticacion, lo hara esta semana
- Maria pidio a Carlos que documente los endpoints antes del viernes 18
- Se acordo hacer daily standups a las 9:30 AM empezando manana

Extrae todos los action items con: responsable, tarea, fecha limite, y prioridad sugerida. Formatea como tabla.


## Respuesta completa

Aquí tienes los **action items** extraídos y organizados. He añadido una **prioridad sugerida** basada en dependencias técnicas y cercanía al deadline final (30 abril):

| Responsable | Tarea | Fecha límite | Prioridad sugerida | Motivo / Dependencia |
|---|---|---|---|---|
| Ana | Entregar los mockups del dashboard | Lun, 14 abr 2026 | 🔴 Alta | Bloquea diseño/implementación del frontend; es el entregable más próximo |
| Carlos | Documentar los endpoints del API | Vie, 18 abr 2026 | 🔴 Alta | Pedido explícito por PM; necesario para QA e integración antes del API final |
| Carlos | Terminar el API de pagos | Dom, 20 abr 2026 | 🔴 Alta | Hito crítico previo al cierre del proyecto (30 abr) |
| Pedro | Escribir tests del módulo de autenticación | Esta semana (hasta vie, 18 abr 2026*) | 🟠 Media-Alta | Debe estar listo antes de que Carlos cierre integración; se alinea con documentación |
| Maria | Coordinar / habilitar los daily standups (9:30 AM) | Dom, 12 abr 2026 (inicio) | 🟠 Media | Ritual de seguimiento; arranca mañana y sostiene el cumplimiento del resto |
| Equipo (todos) | Asistir a los daily standups a las 9:30 AM | Desde dom, 12 abr 2026 (diario) | 🟡 Media | Acuerdo de equipo, recurrente hasta el 30 abr |

\* *Nota:* Pedro dijo "esta semana". Considerando que la reunión fue sábado 11 abril, se interpreta como **viernes 18 abril** para alinearlo con la documentación de Carlos y evitar ambigüedad. Si tu semana laboral empieza el lunes, sería **vie 17 abril**; dime cuál prefieres y lo ajusto.

**Resumen de dependencias**
```
Ana (14) ──► Carlos (18 doc / 20 API) ──► Pedro (tests) ──► Maria (30 abr)
                    ▲
              Daily 9:30 (desde 12) ── seguimiento transversal
```

¿Quieres que lo exporte también en formato Markdown para tu tablero (Jira/Trello/Notion) o que añada una columna de **estado** (Pendiente / En curso)?