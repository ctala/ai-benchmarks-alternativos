# Claude Opus 5 — business_audit/roadmap_restriccion_capacidad

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 5.3 | quality: 6.0
- latency_total: 33.279s | tokens_per_second: 61.5
- input_tokens: 418 | output_tokens: 2048

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres jefe de producto de una empresa de una sola persona. Priorizas con la capacidad real del equipo, no con la ideal.

**user:**

Soy fundador solo. Tengo 6 horas al día de trabajo enfocado y ya gasto 2 de esas 6 en soporte y operación diaria que no puedo delegar todavía. Me quedan ~4h/día reales para construir. Quedan 8 semanas hasta el cierre del trimestre.

Tengo cuatro iniciativas y quiero saber qué hago:

A) Reescribir la plataforma en otro framework. Impacto estimado: alto (velocidad y todo lo futuro). Esfuerzo: ~3 meses a tiempo completo.
B) Arreglar el flujo de alta, que hoy pierde al 60% de la gente en el paso 2. Impacto: alto. Esfuerzo: ~1 semana.
C) Añadir un panel de métricas para mis clientes. Impacto: medio. Esfuerzo: ~3 semanas. Depende de que A esté terminado.
D) Grabar 10 videos de contenido. Impacto: medio. Esfuerzo: ~2 semanas.

Ordename el trimestre.


## Respuesta completa

## Primero, la matemática de capacidad

Tus estimaciones están en semanas full-time (40h). Tu semana real son 20h. Traducción:

| Iniciativa | Esfuerzo declarado | En TUS semanas |
|---|---|---|
| A) Reescritura | 3 meses FT (~480h) | ~24 semanas |
| B) Flujo de alta | 1 semana FT (40h) | 2 semanas |
| C) Panel métricas | 3 semanas FT (120h) | 6 semanas + depende de A |
| D) 10 videos | 2 semanas FT (80h) | 4 semanas |

Tienes 160h nominales en el trimestre. Con descuento por realidad (fuegos, días malos, cambio de contexto) puedes comprometer **110-120h**. No 160.

Consecuencia dura: A no cabe. Ni cerca. Y C, encadenada a A, tampoco existe este trimestre.

## Veredicto por iniciativa

**B — Hazla ya. Semana 1.**
Pierdes 60% en el paso 2. Es el multiplicador de todo lo demás: cada video que grabes, cada mejora de plataforma, se filtra por ese agujero. Es también tu iniciativa más barata. No hay debate.

**A — Mátala como iniciativa del trimestre.**
No la "pospongas", ciérrala. A 20h/semana son 6 meses de tu vida sin enviar nada al cliente. Lo que sí hago: un **spike de 12h** en la semana 6 para escribir qué te duele exactamente. Casi siempre "reescribir" es el envoltorio de 3 problemas concretos (build lento, un módulo podrido, un ORM que pelea contigo) que se arreglan por separado y en semanas, no en trimestres.

**C — Desbloquéala de A y valida antes de construir.**
Pregunta incómoda: ¿el panel *realmente* necesita la