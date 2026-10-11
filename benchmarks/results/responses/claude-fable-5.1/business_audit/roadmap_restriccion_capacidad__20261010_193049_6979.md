# Claude Fable 5.1 — business_audit/roadmap_restriccion_capacidad

- model_id: `anthropic/claude-fable-5.1`
- success: True  | final: 8.02 | quality: 10.0
- latency_total: 26.461s | tokens_per_second: 58.2
- input_tokens: 420 | output_tokens: 1539

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

## Primero, la capacidad real

4h/día × 5 días × 8 semanas = **~160 horas de construcción en todo el trimestre**. Eso es lo que hay. No "3 meses a tiempo completo", no "una semana" en abstracto.

Y tus estimaciones casi seguro están en semanas de 40h. Con 20h/semana reales, **cada estimación se duplica**:

| Iniciativa | Esfuerzo estimado | Esfuerzo real para ti | ¿Cabe en 160h? |
|---|---|---|---|
| A) Reescritura | ~480h | ~24 semanas | No. Ni de cerca. |
| B) Flujo de alta | ~40h | ~2 semanas | Sí |
| C) Panel métricas | ~120h | ~6 semanas | Bloqueada por A → no existe este trimestre |
| D) 10 videos | ~80h | ~4 semanas | Sí |

## El trimestre

**Semanas 1–2: B. Solo B.**
Pierdes al 60% en el paso 2. Cada día que no lo arreglas, el 60% de todo lo que entra se va por el desagüe. Es la mejor relación impacto/hora de la lista por un margen enorme. Nada compite.

**Semana 3: medir B.**
No empieces lo siguiente sin saber si el arreglo funcionó. Si el 60% bajó a 30%, perfecto. Si no, iteras aquí antes de irte a otra cosa.

**Semanas 3–7: D.**
Caben los 10 videos con holgura. Si el tiempo aprieta, 6 videos buenos valen más que 10 a medias. Bonus: ahora que el alta no gotea, el tráfico que generen los videos sí convierte.

**Semana 8: colchón.**
Soporte que explotó, bugs del alta, lo que sea. Si no lo usas, haces más videos. Nunca planifiques el 100%.

## Lo que NO haces

**A) La reescritura.** Con tu capacidad son 6 meses, no 3. Durante esos 6 meses no mejoras nada que vea el cliente. Es un proyecto que una persona sola con soporte a cuestas no puede ejecutar sin que el negocio se detenga. Si el problema real es "voy lento", la respuesta es: aislar el módulo más doloroso y migrar solo eso, o esperar a tener ingresos para que alguien más lo haga. La reescritura total vuelve a la mesa cuando tengas un segundo par de manos.

**C) El panel.** Está bloqueado por algo que no va a pasar. Pero te lanzo una pregunta: ¿**de verdad** depende de A? Si hay una versión fea del panel en el stack actual (una tabla, un export CSV, un Metabase incrustado), eso es candidato para el trimestre siguiente. Cuestiona la dependencia antes de aceptarla.

## Una cosa más

Esas 2h/día de soporte: pregúntate cuánto viene de gente confundida en el alta. Si B está bien hecho, puede que recuperes media hora al día. Eso solo ya justifica que vaya primero.

**Resumen: B → medir → D → colchón. A y C no existen este trimestre.**