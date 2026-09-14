# Muse Spark 1.3 — business_audit/roadmap_restriccion_capacidad

- model_id: `meta/muse-spark-1.3`
- success: True  | final: 8.56 | quality: 10.0
- latency_total: 17.466s | tokens_per_second: 143.5
- input_tokens: 264 | output_tokens: 2506

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

Como jefe de producto de un equipo de 1, no te ordeno por lo que más ilusión hace. Te ordeno por lo que cabe en tu capacidad **real**.

Y tu capacidad real no son 8 semanas. Es esto:

**4h/día x 5 días x 8 semanas = 160h para construir.**
Eso son ~4 semanas a tiempo completo. No 8.

Con 160h, el trimestre ya está decidido por matemáticas:

### El orden es: B -> D -> NADA MÁS. A y C aparcadas.

**1. B primero, semanas 1-2: Arreglar el alta**
Es lo único alto impacto + cabe en tu capacidad.
Ese 60% que pierdes en el paso 2 es un agujero en el cubo. Todo lo demás que hagas pierde el 60% de su valor mientras eso siga roto.

Esfuerzo "~1 semana" normalmente significa 1 semana full-time = 40h. Para ti son 2 semanas de calendario. Es perfecto para empezar.

Definición de hecho: no "mejorar el flujo", sino pasar de 40% que pasa el paso 2 a X%. Mídelo antes y después.

**2. D segundo, semanas 3-6: 10 videos de contenido**
Impacto medio, pero independiente y cabe.
Esfuerzo "~2 semanas" full-time = 80h = 4 semanas para ti. Grábalos en lote, no uno por uno. 1 semana guion, 1 semana grabar, 2 semanas editar/publicar.

Importante el orden: **D tiene que ir DESPUÉS de B.** No tiene sentido echar tráfico (videos) a un funnel roto. Arreglas la fuga y luego abres el grifo. Así D rinde el doble.

**3. Semanas 7-8: Colchón. No las llenes.**
Te quedan 40h libres de tus 160h [40h B + 80h D = 120h]. Déjalas para iterar B, picos de soporte, bugs y vender. Si planificas al 100% con 2h/día ya comprometidas en soporte, el primer imprevisto te rompe el trimestre.

### Por qué NO a A y C este trimestre

**A) Reescribir la plataforma: NO, aunque tenga impacto alto.**
Necesita ~3 meses a tiempo completo = ~480h. Tú tienes 160h. Ni siquiera dejando soporte podrías. A tu ritmo real necesitarías ~24 semanas de calendario, 6 meses.

Es la trampa clásica: te deja 8 semanas sin entregar nada a clientes mientras sigues perdiendo el 60% del alta. Te mata el trimestre.

Lo que sí haz: timebox de 10% para anotar los 3 dolores que más te frenan de A y poner parches pequeños de <4h. Nada de rewrite.

**C) Panel de métricas: NO, está bloqueado.**
Impacto medio + depende de A. Como A es imposible este trimestre, C vale 0 este trimestre. No importa lo bueno que sea.

Sustituto barato: en la semana 7 entrevista a 5 clientes y mándales un reporte manual por email. Validarás si de verdad lo quieren sin construir nada.

### Tu trimestre en una línea

> Semanas 1-2: tapas la fuga (B). Semanas 3-6: atraes (D). Semanas 7-8: mides y respiras. A y C no se tocan hasta enero.

Si intentas hacer las 4, entregas cero. Si haces B+D, terminas el trimestre con más activación y con pipeline de contenido funcionando.

¿Empezamos definiendo el lunes qué significa exactamente "arreglar el paso 2"?