# Grok 4.7 — business_audit/roadmap_restriccion_capacidad

- model_id: `x-ai/grok-4.7`
- success: True  | final: 8.22 | quality: 10.0
- latency_total: 40.015s | tokens_per_second: 43.7
- input_tokens: 1479 | output_tokens: 1747

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

Haz B. No empieces A. C queda fuera. D solo si B ya movió el número.

Capacidad real: 4 h/día × 5 días × 8 semanas ≈ **160 h**. Un “mes a tiempo completo” son unas 160 h. A son ~3 meses a tiempo completo, o sea **~480 h**: tres veces el trimestre, y un rewrite casi nunca entra en la estimación. En 8 semanas no lo terminas. Un rewrite a medias no da velocidad; solo te deja sin producto nuevo y con el alta rota.

**Orden del trimestre**

1. **B, semanas 1–2.** Es el único ítem de impacto alto que cabe y no depende de nadie. Pierdes al 60 % en el paso 2: cada hora de contenido o de rewrite sigue empujando gente a un embudo roto. Trata “1 semana” como ~40 h, o sea unas 2 semanas de calendario a 4 h/día. Define el éxito antes de tocar código (por ejemplo, paso 2 completado del 40 % a ≥70 %) y mídelo al terminar. Si no se mueve, iteras B, no abres otra iniciativa.

2. **D, semanas 3–6, y solo entonces.** Impacto medio, ~80 h, cabe. Tiene sentido después de B: si no, los 10 vídeos alimentan el mismo agujero. Si al cerrar B el cuello ya no es el alta sino que no entra nadie, súbela; si el alta sigue rota, no grabes.

3. **Semanas 7–8: colchón.** Bugs del alta, picos de soporte y una decisión escrita sobre A. No es tiempo para “empezar el rewrite un poco”.

**Fuera**

- **A.** No este trimestre. Aunque la estimación fuera exacta, ocuparía todo y no entregarías nada usable. Un spike de unos días para anotar por qué el framework actual duele puede vivir en el colchón; la reescritura, no.
- **C.** Depende de A terminado, y A no termina. Además, 3 semanas a tiempo completo son ~6 semanas tuyas: con B no cabe sin colchón. Un panel para clientes no arregla el 60 % que ni llega a ser cliente.

Regla para no reabrir el debate a mitad de trimestre: no se empieza nada que no quepa entero en las horas que quedan, y no se escala adquisición mientras el paso 2 siga comiéndose a la mayoría.