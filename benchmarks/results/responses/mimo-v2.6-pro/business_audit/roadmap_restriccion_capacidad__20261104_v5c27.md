# MiMo V2.6 Pro — business_audit/roadmap_restriccion_capacidad

- model_id: `xiaomi/mimo-v2.6-pro`
- success: True  | final: 7.02 | quality: 8.0
- latency_total: 80.761s | tokens_per_second: 29.9
- input_tokens: 275 | output_tokens: 2415

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

## Primero el dato que lo decide: tu capacidad real

**8 semanas × 5 días × 4h = 160h** de construcción en todo el trimestre.

Contra eso:

| Iniciativa | Horas estimadas | % de tu trimestre | ¿Cabe? |
|---|---|---|---|
| A) Reescribir plataforma | ~520h (3 meses full-time) | **325%** | ❌ Imposible |
| B) Arreglar alta | ~20h (1 semana) | 12% | ✅ |
| C) Panel de métricas | ~60h (3 semanas) | 37% | ❌ Bloqueada por A |
| D) 10 videos | ~40h (2 semanas) | 25% | ✅ |

**A no entra ni aunque borraras las otras tres.** Y C depende de A, así que hereda su imposibilidad. Eso no es una decisión difícil: es aritmética.

---

## El orden del trimestre

### 1. B — Arreglar el flujo de alta (Semana 1, 20h)
Razones, en orden:
- **Es 12% de tu trimestre y desbloquea ingresos ahora.** Arreglar una fuga del 60% es el apalancamiento más barato que tienes.
- **No arreglarlo invalida a D.** El contenido manda tráfico a un embudo que pierde 6 de cada 10 personas en el paso 2. Estarías pagando tráfico para filtrarlo por el desagüe.
- Es reversible y medible: instrumenta el paso 2 **antes** de tocarlo, así tienes línea base. Si el "60%" es intuición y no dato, ese es tu primer paso (2-3h).

> ⚠️ Tu estimación de 1 semana es optimista: incluye deploy, QA, edge cases de pago/verificación y las 2-3 roturas que aparecerán. Bloquea la semana entera y no prometas nada más.

### 2. D — Contenido (Semanas 3-4, ~40h)
- **Recórtalo a 6-8 videos.** 10 videos en 2 semanas a 4h/día son 8h por video con guion, grabación, edición y publicación. Es el tipo de estimación que se rompe el día 5. Menos piezas, mejor hechas, publicadas con constancia.
- Ventaja: es el único trabajo de estas cuatro que **sigue rindiendo sin ti** (distribución acumulativa).

### 3. Iterar sobre el embudo con datos reales (Semanas 5-6, 40h)
Ahora sí tienes datos post-B: ¿sigue perdiendo gente en otros pasos? ¿En cuáles? Ahí está tu siguiente palanca. Convierte los siguientes 4-5 pasos del alta en tu propio backlog priorizado por tamaño de fuga.

### 4. C-lite o retención (Semana 7, 20h)
Si el valor de C es retención/churn, **redescríbelo desacoplado de A**: 3-4 métricas en solo lectura sobre el stack actual, en 1 semana, no un panel completo en 3. Es "suficiente para retener", no "bonito".

### 5. Buffer explícito (Semana 8, 20h)
No lo llenes. Como fundador solo, el soporte tiene picos, algo se rompe y las estimaciones se desvían. 20h de colchón es lo que evita que el trimestre se caiga.

---

## Qué hago con A

**No se descarta para siempre: se descompone.** El error no es querer mejorar la plataforma, es comprarlo como un bloque de 520h con payoff futuro mientras el trimestre actual produce cero.

Versión correcta: **refactor incremental de 30h máximo** dirigido solo al módulo que hoy más te frena (el que hace que cada feature te cueste el doble). Sin "reescritura", sin cambio de framework. Si de verdad el framework te está matando, te darás cuenta en el trimestre siguiente con más datos y más ingresos — y con 4h/día, un cambio de framework probablemente necesite que antes contrates o automatices ese soporte de 2h.

## Resumen de una línea

**B (semana 1) → D recortado a 6-8 videos (semanas 3-4) → iterar embudo con datos (5-6) → C-lite opcional (7) → buffer (8).** A queda fuera del trimestre; C muere tal como está definida.

La pregunta que te deja este trimestre no es "cómo construyo más", es "cómo recupero esas 2h de soporte" — porque cada hora que liberes ahí vale más que cualquier iniciativa de esta lista.