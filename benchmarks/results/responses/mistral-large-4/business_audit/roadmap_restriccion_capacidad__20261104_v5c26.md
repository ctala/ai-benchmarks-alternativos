# Mistral Large 4.0 — business_audit/roadmap_restriccion_capacidad

- model_id: `mistralai/mistral-large-4-0`
- success: True  | final: 7.12 | quality: 8.0
- latency_total: 57.239s | tokens_per_second: 50.1
- input_tokens: 248 | output_tokens: 2867

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

Primero el ancla numérica, porque todo lo demás depende de ella:

**Tu capacidad real este trimestre: 8 semanas × 5 días × 4h = ~160 horas de construcción.** Las otras 2h/día de soporte a veces se desbordan, así que reserva buffer.

Ahora el dictamen por iniciativa:

**A) Reescritura: NO entra este trimestre. Ni a medias.**
"3 meses a tiempo completo" son ~480h. Tú tienes 160h. Incluso si lo hicieras en 4h/día, te llevaría 6 meses. Y aquí está la trampa del fundador solo: **una reescritura incompleta no da ningún valor**. Al final del trimestre seguirías con la plataforma vieja en producción y 160h tiradas. La regla con poca gente es: no reescribas, refactoriza por módulos (strangler fig) en el trimestre siguiente si de verdad duele. Este trimestre, A = 0 horas en producción. Como mucho, 1 semana de diseño/especificación técnica para ejecutarlo bien después.

**C) Panel de métricas: bloqueado por A, así que tal como está definido no entra.** Salvo que aceptes desacoplarlo: hacerlo sobre tu stack actual o con una herramienta externa embebida (Metabase, PostHog, etc.) sin esperar a A. Si lo haces así, sí cabe (~60h).

**B) Fuga del 60% en el paso 2: esto es dinero que se te escapa HOY.** 1 semana (20h) con impacto alto es el mejor ROI por hora de toda la lista. Va primero, sin discusión.

**D) 10 videos: entra.** 2 semanas (40h), impacto medio, y además es evergreen: cuanto antes los publiques, antes empiezan a trabajar. Y con el onboarding arreglado, ese tráfico nuevo no se fugará.

## El orden del trimestre

| Semanas | Iniciativa | Horas | Objetivo medible |
|---|---|---|---|
| **1** | **B** — arreglar paso 2 del alta | 20h | Pasar de 40% a ≥70% de supervivencia en el paso 2 |
| **2–3** | **D** — 10 videos publicados | 40h | 10 videos en vivo, no perfectos |
| **4–6** | **C-lite** — métricas básicas sobre stack actual o herramienta externa (si no, salta a la fila de abajo) | 60h | Cliente ve sus métricas sin escribirte a ti |
| **7–8** | **Buffer + palanca de soporte** | 40h | Reducir tus 2h/día de soporte (macros, FAQ, automatizaciones) y documentar el plan de A para el Q+1 |

**Total comprometido: 160h justas, con las últimas 2 semanas como colchón** (que en la práctica se comerán los imprevistos de soporte).

## Dos decisiones que cambian el juego

1. **Ataca esas 2h de soporte.** Si consigues bajarlas a 1h/día, ganas **40h extra en el trimestre**: eso es medio C o medio D gratis. Automatiza respuestas recurrentes, crea una FAQ pública, usa macros. Es la única forma de "contratar" sin contratar.

2. **No empieces A "un poquito".** Cero código de reescritura en producción este trimestre. Si el framework actual te duele, saca un módulo pequeño (el que más duela) y pruébalo aparte; si funciona, sigue el Q que viene. Si no, no has roto nada.

**Resumen ejecutivo:** Semana 1 para la hemorragia (B), semanas 2–3 para llenar el embudo (D), semanas 4–6 para retener lo que ya tienes (C-lite), semanas 7–8 para recuperar tiempo futuro (menos soporte) y preparar bien A. A se queda para el trimestre siguiente, hecho por fases, no en big bang.