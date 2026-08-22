# GLM 5.3 — business_audit/roadmap_restriccion_capacidad

- model_id: `z-ai/glm-5.3`
- success: True  | final: 6.8 | quality: 8.0
- latency_total: 104.922s | tokens_per_second: 66.1
- input_tokens: 263 | output_tokens: 6931

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

4h/día × 5 días × 8 semanas = **~160 horas de construcción** este trimestre. Todo lo demás se decide contra ese número.

## El veredicto por iniciativa

**A — Fuera de este trimestre. No es priorización, es aritmética.** "3 meses a tiempo completo" son 360–480h según cómo lo cuentes. Necesitas 2–3× tu trimestre entero, y las rewrites siempre se exceden (cuenta 1.5× de buffer). Además, mientras reescribes sigues manteniendo la plataforma vieja con tus 2h diarias de ops. Empezarla "en los huecos" es el peor escenario: dos plataformas, cero shipped. Decisión: próximo trimestre, y re-escópala como migración incremental (un módulo por sprint, sin dejar de shippear) en vez de rewrite de golpe.

**C — Bloqueada por A, queda diferida automáticamente.** No la construyas sobre el stack actual: es trabajo desechable si A ocurre. Si hay clientes pidiendo métricas ya, mándales un reporte semanal a mano (2h) mientras tanto.

**B — Primera. Semana 1.** El mejor ratio impacto/hora de la lista: impacto alto por ~20h. Y desbloquea todo lo demás — el contenido y cualquier adquisición futura caen en un funnel que hoy pierde al 60%. Instrumenta cada paso *antes* de tocar nada, para medir el antes/después.

**D — Segunda. Semanas 2–4.** El contenido tiene retorno retardado, así que mitad de trimestre es el último momento responsable para empezarlo. Y así aterriza sobre un funnel arreglado, no roto. Aviso: 10 videos en 2 semanas es agresivo para un fundador solo con ops encima; 6–8 bien hechos es un resultado válido. Dale criterio de corte: si en 2 semanas no genera señal, paras.

## El trimestre, semana a semana

- **Semana 1:** B (20h). Ship + medir.
- **Semana 2:** iterar B con datos (10–15h) + arrancar D.
- **Semanas 3–4:** D (40h).
- **Semana 5:** spike de A, timeboxed a 20h con hard stop. Migra una porción real (un endpoint, un módulo) al framework nuevo y mide tu velocidad real. Esto convierte el "3 meses estimados" en un plan con datos para el próximo trimestre. Si prefieres no tocar A aún, usa la semana en B v2.
- **Semanas 6–8:** iterar lo shipped + **la quinta iniciativa que no listaste: tus 2h/día de ops**. Son 120h este trimestre — tu partida individual más grande, más que D. Ataca los 3 mayores generadores de tickets (docs, self-serve, arreglos de producto). Cada hora que bajes de ahí es una hora de build que ganas todos los días, para siempre.

Son ~95h comprometidas de 160. El resto no es holgura vacía: es donde el plan absorbe la realidad.

## Dos avisos

1. **Si B funciona, entran más usuarios → más soporte → menos de tus 4h.** Por eso las semanas 6–8 tienen aire a propósito.
2. **No arranques A "un poco por semana".** Una rewrite al 40% a cierre de trimestre es peor que no haberla empezado.

Cierre del trimestre realista: funnel arreglado y medido, contenido en marcha, la apuesta grande de-riesgada con datos, y cero plataformas a medias.