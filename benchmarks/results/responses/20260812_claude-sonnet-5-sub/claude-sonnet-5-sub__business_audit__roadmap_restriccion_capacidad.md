# Claude Sonnet 5 (suscripción) — business_audit/roadmap_restriccion_capacidad

- model_id: `claude-sonnet-5`
- success: True  | final: 8.15 | quality: 10.0
- latency_total: 59.556s | tokens_per_second: 66.9
- input_tokens: 2 | output_tokens: 3986

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

## Capacidad real del trimestre

8 semanas × 5 días × 4h/día = **160h**. Esa es la cancha, no las 6h nominales.

Los esfuerzos que diste están en "tiempo completo" (8h/día). Convertidos a tu ritmo real de 4h/día:

| Iniciativa | Esfuerzo (FT) | Horas | A 4h/día real |
|---|---|---|---|
| B — arreglar alta | 1 semana | 40h | **2 semanas** |
| D — 10 videos | 2 semanas | 80h | **4 semanas** |
| C — panel métricas | 3 semanas | 120h | 6 semanas (bloqueada) |
| A — reescritura | 3 meses | ~480h | **24-26 semanas (~6 meses)** |

A sola es 3x tu trimestre completo. No es una opción este trimestre, es una decisión de otro trimestre.

## Orden

**1. B (semana 1-2).** Alto impacto, bajo esfuerzo, ROI inmediato y medible. Cada día que no lo arreglas sigues perdiendo el 60% de la gente que ya te costó traer — es la pérdida más cara del negocio ahora mismo, y es la más barata de arreglar. Esto no se discute, se hace primero.

**2. D (semana 3-6).** Tiene sentido secuencial: mandar contenido/tráfico a un embudo que pierde 6 de cada 10 personas en el paso 2 es quemar audiencia. Arreglado B, D empieza a convertir de verdad.

**3. Semana 7-8 = buffer, no A.** Con B+D usas 6 de las 8 semanas. No llenes el 100%: los founders solos subestiman esfuerzo sistemáticamente y ya tienes soporte diario comiéndote 2h que puede crecer. Ese colchón es realista, no perezoso.

Si insistes en tocar A, usa como máximo esas 2 semanas de buffer como **spike de descubrimiento**, no como ejecución: ¿la reescritura completa es necesaria o hay un camino incremental (migrar módulo por módulo, strangler pattern) que no te obliga a bloquear 6 meses y a C entero? Output esperado: un plan y un scope, no código en producción.

## Qué NO hacer

- **No arrancar A esta cabeza.** Empezarla sin poder terminarla en el trimestre te deja con dos sistemas a medio mantener y cero ROI entregado. Es el error clásico de fundador solo: la reescritura se siente como "lo importante" porque es grande, pero no mueve ningún número este trimestre.
- **C queda descartada para este trimestre**, no por prioridad baja sino por dependencia dura de A. No la pongas en el plan, ponla en el próximo trimestre condicionada a que A avance.

## La pregunta que vale la pena hacerte

A promete "velocidad para todo lo futuro" — pero el cuello de botella medible que tienes hoy es B: 60% de fuga en el paso 2. Antes de comprometer medio año a una reescritura, vale confirmar que A no es una forma elegante de evitar el trabajo menos glamoroso (B) que es el que realmente mueve el negocio ahora.