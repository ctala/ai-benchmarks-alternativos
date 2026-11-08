# Muse Spark 1.3 — business_audit/roadmap_restriccion_capacidad

- model_id: `meta/muse-spark-1.3`
- success: True  | final: 8.57 | quality: 10.0
- latency_total: 18.781s | tokens_per_second: 125.7
- input_tokens: 265 | output_tokens: 2361

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

Como jefe de producto de un equipo de 1, no te ordeno por impacto ideal. Te ordeno por **capacidad real.**

Tu capacidad real no es 8 semanas. Es esto:

4h/día x 5 días x 8 semanas = **160h para construir = 4 semanas a tiempo completo.**

Tus 4 iniciativas suman ~18 semanas a tiempo completo. No caben. Hay que matar 2.

Aquí va el trimestre:

### TL;DR: Haz B, luego D. NO hagas A ni C este trimestre.

**1. B PRIMERO - Arreglar el alta (Semanas 1-2)**
Alto impacto / ~1 semana full-time = ~2 semanas para ti.

Es lo único no negociable. Pierdes al 60% en el paso 2. Todo lo demás que hagas - contenido, métricas, rewrite - pierde el 60% de su valor si no arreglas esa fuga primero.

Hazlo en modo quirúrgico: solo paso 2, mide conversión antes/después, no rediseñes todo el onboarding.

**2. D SEGUNDO - 10 videos (Semanas 3-6)**
Impacto medio / ~2 semanas full-time = ~4 semanas para ti.

Es lo segundo porque sí cabe en tu capacidad, no tiene dependencias, y te trae usuarios al flujo que acabas de arreglar en B. Lotea: guion una semana, graba todo junto, edita simple.

Con B + D ya usas ~6 semanas calendario. Te quedan 2 semanas.

**3. Esas 2 semanas restantes NO son libres. Son tu colchón.**
Eres solo. Soporte se expande, las estimaciones mienten, B necesitará una iteración. Reserva semanas 7-8 para: medir B, arreglar bugs, y deuda técnica pequeña.

### Lo que MATAMOS explícitamente:

**A - Rewrite: NO.** Es la trampa clásica.
3 meses a tiempo completo = **~6 meses a tu ritmo de 4h/día.** Te come 3 trimestres, no 1. Cero valor entregado en 8 semanas y paras todo lo demás. Si te pica, dedica 4h *una sola vez* a listar qué te duele del framework actual y arregla solo ese dolor, sin rewrite.

**C - Panel de métricas: NO.** No es por impacto, es por dependencia.
Depende de que A esté terminado. Como A es imposible este trimestre, C está automáticamente bloqueada. Hacerla sin A sería tirar 3 semanas.

**Orden final:**
Semana 1-2: B y medir
Semana 3-6: D
Semana 7-8: Buffer + iterar B + operar

Entregas en 8 semanas: más activación + más adquisición. Eso es un buen trimestre para una sola persona.