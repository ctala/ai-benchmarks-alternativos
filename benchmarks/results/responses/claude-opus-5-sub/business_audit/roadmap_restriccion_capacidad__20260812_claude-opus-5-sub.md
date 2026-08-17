# Claude Opus 5 (suscripción) — business_audit/roadmap_restriccion_capacidad

- model_id: `claude-opus-5`
- success: True  | final: 6.61 | quality: 8.0
- latency_total: 65.812s | tokens_per_second: 50.9
- input_tokens: 2 | output_tokens: 3351

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

## Primero, la matemática

Tus 8 semanas son **160h nominales** (4h × 5 días × 8). Descontando enfermedad, imprevistos y días que se van en nada, tu capacidad real de construcción es **~120-130h**.

Y hay un detalle que hunde la mitad de los planes de founder solo: cuando estimas "1 semana", estás estimando **1 semana a tiempo completo (40h)**. A 4h/día eso son **2 semanas de calendario**. Traducido:

| | Tu estimación | Horas reales | Semanas a tu ritmo |
|---|---|---|---|
| A) Reescribir | 3 meses full time | ~480h | **24 semanas** |
| B) Flujo de alta | 1 semana | ~40h | 2 (3 con margen) |
| C) Panel métricas | 3 semanas | ~120h | 6 — y bloqueada por A |
| D) 10 videos | 2 semanas | ~80h | 4 |

## Dos se caen solas

**A no es "baja prioridad", es imposible.** Necesita 3× el trimestre que tienes. Si la empiezas, llegas a la semana 8 con una plataforma a medio migrar, la vieja sin mantener y cero cosas entregadas. Es el peor resultado posible de los cinco escenarios.

**C se cae por dependencia.** Depende de A, A no ocurre, C no ocurre. No la discutas más este trimestre.

Te quedan B y D. Y eso está bien: es exactamente lo que cabe.

## El orden: B antes que D, y no es por ROI

B primero porque **D alimenta el embudo que B repara**. Grabar 10 videos para mandar tráfico a una puerta que pierde 60% en el paso 2 es pagar por gente que no entra. Arreglar el paso 2 multiplica el retorno de todo lo que hagas después — este trimestre y los siguientes.

Segundo motivo, menos obvio: parte de tus 2h/día de soporte probablemente **nace de ese paso 2**. Gente atascada que te escribe. Si B funciona, no solo conviertes más: recuperas capacidad. Es la única iniciativa de las cuatro que puede devolverte horas.

## Las 8 semanas

**Semana 1 — Diagnóstico, no construcción (16h)**
No asumas que sabes por qué se cae el 60%. Instrumenta el paso 2, mira grabaciones de sesión, habla con 5 personas que abandonaron. Timebox duro: 4 días. Es posible que el arreglo real sean 2 días de código y no una semana; también es posible que sean tres problemas distintos. Mejor saberlo antes.

**Semanas 2-3 — Construir y lanzar B (32h)**
Envío a producción con medición. No pases a otra cosa sin el número antes/después.

**Semana 4 — Segunda pasada de B + soporte (16h)**
Los embudos casi nunca se arreglan en un intento. Reserva esta semana para la iteración 2 sobre lo que la data mostró. Si B salió limpio a la primera, usa la semana en atacar tu top-3 de tickets de soporte recurrentes.

**Semanas 5-8 — D, recortado (56h)**
No 10 videos. **6 videos**, grabados en 2 sesiones de bloque, edición ligera. Diez videos mediocres publicados con prisa valen menos que seis decentes, y el recorte te da el colchón para cuando la semana 4 se desborde (se va a desbordar).

Total comprometido: ~120h. Sin héroes.

## Qué haces con A

No la ignores: conviértela en una decisión con fecha. Antes del cierre del trimestre, escribe en una página **qué problema concreto y medible resuelve la reescritura** — qué pantalla tarda cuántos segundos, qué feature no puedes construir y cuánto dinero cuesta eso.

Si no logras escribirlo con números, no era una prioridad, era incomodidad con el código. Y si sí lo logras, casi seguro descubres que el 80% del dolor está en 2 o 3 puntos concretos que puedes atacar con 2 semanas de trabajo quirúrgico el próximo trimestre — no con 6 meses de reescritura que, a tu ritmo real, terminarías en un año.

## La línea de corte

Al cierre tienes que poder decir: *"el paso 2 pasó de perder 60% a perder X%"*. Ese es el trimestre. Los videos son el bonus.

Si en la semana 4 B no se movió, **cancela D** y sigue con B. Un embudo que convierte es un activo permanente; 6 videos son 6 videos.