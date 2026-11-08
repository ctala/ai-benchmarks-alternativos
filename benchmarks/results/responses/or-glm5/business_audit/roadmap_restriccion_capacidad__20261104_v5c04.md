# GLM 5 — business_audit/roadmap_restriccion_capacidad

- model_id: `z-ai/glm-5`
- success: True  | final: 7.11 | quality: 8.0
- latency_total: 30.154s | tokens_per_second: 49.3
- input_tokens: 263 | output_tokens: 1487

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

# Priorización del trimestre — capacidad real

## La matemática primero

Tienes 4h/día × 40 días laborables = **160h reales de construcción** en el trimestre. Eso equivale a **4 semanas a tiempo completo**, no 8. Cualquier plan que asuma más es ficción.

## Lo que no entra

**A no entra este trimestre.** Necesita ~480h. Tienes 160h. Ni siquiera se acerca. Y si la empiezas, dejas la plataforma en estado híbrido durante meses, que es peor que no tocarla. Además **C depende de A**, así que C también queda fuera automáticamente.

No es que A no sea importante. Es que es matemáticamente imposible con la capacidad actual. Priorizar no es decidir qué es valioso. Es decidir qué cabe.

## El trimestre

| Semanas | Iniciativa | Por qué |
|---------|-----------|---------|
| 1–2 | **B — Arreglar flujo de alta** | Pierdes 60% de usuarios hoy. Cada semana que esperas es dinero quemado. Es corto, de alto impacto y no tiene dependencias. Sin discusión. |
| 3–6 | **D — 10 videos de contenido** | Impacto medio, sin dependencias, cabe en el tiempo restante. Genera activación, SEO y credibilidad mientras no puedes construir features grandes. |
| 7–8 | **Margen** | Imprevistos, soporte escalado, o pre-diseño de A en papel. No código. |

## Lo que haces con A

No la tocas este trimestre. Pero haces dos cosas concretas:

1. **Diseño y planificación en las semanas 7–8**, sin escribir código. Arquitectura, migración de datos, plan por fases. Para que cuando decidas empezar, no pierdas tiempo decidiendo.
2. **Decisión explícita el próximo trimestre**: o buscas delegar parte del soporte/operación para liberar más horas de construcción, o A seguirá siendo imposible. La reescritura no se resuelve con priorización. Se resuelve con capacidad.

## Lo que no haces

- No empiezas A "a ver hasta dónde llego". Medio framework migrado es deuda técnica activa.
- No construyes C sobre la plataforma actual sabiendo que la vas a reescribir. Es trabajo tirado.
- No metes nada nuevo en el backlog hasta que B esté en producción.

**El trimestre queda en: B + D. Eso es todo lo que cabe. Y está bien.**