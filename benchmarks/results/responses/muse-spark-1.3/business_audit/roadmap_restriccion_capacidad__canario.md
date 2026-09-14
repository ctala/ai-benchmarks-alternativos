# Muse Spark 1.3 — business_audit/roadmap_restriccion_capacidad

- model_id: `meta/muse-spark-1.3`
- success: True  | final: 8.54 | quality: 10.0
- latency_total: 20.275s | tokens_per_second: 134.6
- input_tokens: 264 | output_tokens: 2729

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

Como tu jefe de producto de equipo de 1, no te voy a planificar con el equipo ideal. Te planifico con tu capacidad real.

Hagamos la matemática que duele:

**Tu capacidad real no son 8 semanas. Son 4.**
6h/día - 2h de soporte/operación = **4h/día para construir**
4h x 5 días x 8 semanas = 160h = **4 semanas a tiempo completo**

**Tu demanda es de 18 semanas:**
B: 1 sem + D: 2 sem + C: 3 sem + A: 12 sem (3 meses) = 18 semanas full-time

Tienes 4 y quieres hacer 18. Solo puedes hacer el 22%. Hay que cortar.

Este es tu orden para el trimestre:

### 1. HACER AHORA: B) Arreglar el alta. Semanas 1-2
Es tu único P0.

Pierdes al 60% en el paso 2. Eso significa que todo lo demás está roto por defecto. ¿Para qué quieres grabar videos (D) para llevar gente a un embudo que tira a 6 de cada 10? ¿Para qué quieres un panel (C) si no tienes usuarios activados que lo miren?

A tu ritmo, 1 semana full-time = 2 semanas calendario para ti (10 días x 4h = 40h). Hazlo en WIP=1, nada más en paralelo.

Éxito = bajar ese 60% a <35%. Mídelo antes y después. Si no lo bajas, no avanzas.

### 2. HACER RECORTADO: D) Videos. Semanas 3-6
Pero NO 10 videos. A tu ritmo 2 semanas full-time = 4 semanas calendario. No te quedan 4 semanas limpias.

Haz versión founder-solo: 3 videos, no 10. Y que sean los 3 que ataquen la objeción que descubriste en el paso 2 de B. Así B + D se refuerzan.

El resto de los 7 los aparcas para el Q siguiente si estos 3 convierten.

Semanas 7-8: no las planifiques. Son tu colchón. Eres solo, el soporte sube, hay bugs, te enfermas. Ese colchón es para iterar B, responder, y hacer discovery sin construir.

### 3. NO HACER: A) Rewrite y C) Panel

**A es una trampa.** 3 meses a tiempo completo = para ti, a 4h/día, son **6 meses calendario.** Si lo empiezas ahora, terminas el trimestre con: rewrite a la mitad, alta todavía perdiendo 60%, 0 valor entregado, y sin poder desplegar nada por el riesgo de migración. Un solo fundador nunca empieza un rewrite con el funnel roto.

Lo que sí haces con A: Congelarlo. Anota el dolor, pon un límite: máximo 30 min/semana en contener deuda técnica, nada de refactors grandes.

**C se cae sola.** Impacto medio, esfuerzo 3 semanas full-time (= 6 semanas para ti, no las tienes) Y depende de que A esté terminado. Como A es imposible este trimestre, C es automáticamente imposible. No es un No, es un No-puedo-físicamente.

Si clientes piden métricas, finge el producto: mándales 1 reporte manual por email/semana a 3 clientes. Validas demanda con 2h, no con 120h.

**Resumen de jefe de producto:**

Sem 1-2: Solo B. Arreglar fuga.
Sem 3-6: Solo D-lite. 3 videos que tapan la fuga.
Sem 7-8: Buffer + medir. Nada nuevo.

Regla de solo: 1 proyecto a la vez, 2h de soporte por bloques (no repartidas), planifica al 70% porque la operación siempre se expande.

¿Quieres que partamos B en bloques de 4h para que lo puedas ejecutar esta semana sin tocar soporte?