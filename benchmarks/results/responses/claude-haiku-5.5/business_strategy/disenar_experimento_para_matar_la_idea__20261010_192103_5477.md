# Claude Haiku 5.5 — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 7.51 | quality: 8.0
- latency_total: 20.956s | tokens_per_second: 167.7
- input_tokens: 291 | output_tokens: 3515

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un fundador experimentado. Sabes que el objetivo de un experimento no es tener razón: es descubrir rápido y barato que estás equivocado. Diseñas tests que pueden FALLAR de forma concluyente.

**user:**

Mi hipótesis: las agencias de marketing pequeñas pagarían $200/mes por una herramienta que les automatice los reportes a clientes.

Estoy a punto de meterme 2 meses a construirla. Antes de eso, diséñame el experimento **más barato y más rápido** que pueda MATAR esta hipótesis.

No quiero validarla. Quiero saber, en el menor tiempo y plata posible, si estoy equivocado. Dime exactamente qué hago, cuánto me cuesta, cuánto tarda, y cuál sería el resultado que me hace abandonar la idea.


## Respuesta completa

# Experimento de falsificación: pre-venta a agencias antes de construir

Tu hipótesis tiene tres partes que pueden fallar por separado:

1. **Dolor:** las agencias pierden tiempo real con reportes.
2. **Solución:** esperan que la automatización sea la respuesta.
3. **Precio:** pagarían $200/mes, con tarjeta, no solo "sí, me interesa".

El experimento ataca la parte 3 directamente, porque es la que más te puede matar y la más barata de probar.

---

## Paso 1: Define la muerte antes de empezar

Escríbelo ahora, antes de hablar con nadie:

- **Muere la hipótesis si:** de **60 agencias calificadas** contactadas, **menos de 3** pagan una pre-orden real (o firman un piloto pagado) en **14 días**.
- **Muere o se reprecia si:** la mayoría de los que responden dicen que pagarían **menos de $100/mes** o que ya usan algo gratis (Looker Studio, Sheets) y no ven el problema.
- **Gana (provisionalmente) si:** ≥ 5 pagos reales de 60 contactos, o ≥ 10% de quienes agendan llamada pagan.

Son umbrales pensados para matar. Con muestras chicas no se "prueba" nada, pero sí puedes descartar algo barato.

---

## Paso 2: Lista de 60 agencias calificadas (2 días, $0)

Criterios de calificación, todos obligatorios:
- Entre 2 y 15 empleados.
- Reportan resultados mensuales a clientes (lo ves en su web o en un post).
- Tienen al menos 5 clientes activos.
- Son de habla hispana, o del país donde planeas lanzar.

Úsalo en LinkedIn Sales Navigator (o búsqueda manual) y anota en una hoja: nombre, dueño, cuántos clientes, qué herramientas mencionan.

**Dato útil:** si ya pagan por un tool de reportes (AgencyAnalytics, Whatagraph, DashThis), eso prueba que hay dolor y disposición a pagar. Pero también significa que compites. Anótalo como señal aparte.

---

## Paso 3: Mensaje + landing de pre-orden (2 días, ~$20)

**Landing de una página** (Carrd, Framer o Notion publicado), con:
- Problema: "Tu equipo pasa X horas al mes armando reportes para clientes."
- Solución en una línea.
- Precio: **$200/mes**, sin trial gratis.
- Botón: **"Reservar mi lugar con pre-orden"**, que cobra un **depósito reembolsable de $1 o $20** vía Stripe o Payment Link. Pagar algo, aunque sea $1, separa al interesado del curioso.

**Mensaje de contacto** (LinkedIn o email, corto):

> Hola [nombre], vi que [agencia] maneja reportes para [X] clientes. Estoy validando una herramienta que automatiza esos reportes. Antes de construirla, quiero saber si tendría sentido para ustedes. ¿Tienes 15 minutos esta semana? Si te interesa, hay un link para reservar lugar con pre-orden reembolsable.

---

## Paso 4: Las 15 minutos que realmente importan

Para quien responda, haz estas preguntas **antes** de mostrar nada:

1. "¿Cuántas horas al mes gasta tu equipo en reportes?" *(si dicen "poco" o "no sé", es mala señal)*
2. "¿Qué herramienta usan hoy y cuánto pagan?"
3. "Si esto existiera hoy, ¿lo pagarías? ¿Cuánto?" *(anota el número que dicen, no el que quieres oír)*
4. "¿Quién en tu agencia decide la compra y cuánto tardaría?"

Si al final de la llamada no te dan su tarjeta o una pre-orden, **no cuenta como venta**. Un "me parece interesante, avísame" es un no.

---

## Paso 5: Costo y tiempo

| Concepto | Costo | Tiempo |
|---|---|---|
| Lista de prospectos (Sales Navigator, opcional) | ~$0 a $100 | 2 días |
| Landing + Stripe | ~$20 | 1 día |
| Outreach (manual o herramienta tipo Lemlist) | ~$0 a $50 | 14 días |
| Llamadas | $0 | ~5 horas |
| **Total** | **≈ $20 a $170** | **≈ 3 semanas, tu tiempo** |

Si quieres agregar tráfico pagado para llegar a más gente, pon $200 en anuncios de LinkedIn. Pero no es necesario para este test.

---

## Paso 6: Experimento de confirmación (solo si pasas el paso 5)

Antes de programar nada, ofrece a los 3 a 5 que pagaron un **servicio manual**: tú generas sus reportes con plantillas de Looker Studio y un script o Sheets por $200/mes durante 2 meses.

- Si no puedes entregarlo a mano con calidad, el software tampoco lo resolverá.
- Si al mes 2 no renuevan, la hipótesis de retención muere, aunque la de compra haya vivido.

Esto te cuesta 2 semanas más y evita los 2 meses de construcción a ciegas.

---

## Resumen de la decisión

- **Abandona la idea** si en 14 días tienes menos de 3 pre-órdenes de 60 contactos calificados, o si el precio que dicen está por debajo de $100.
- **Reprecia y repite** si el dolor es real pero el precio no encaja.
- **Avanza** solo si pagan, no si aplauden.

Lo más probable es que el resultado sea ambiguo, con 2 o 3 pagos. En ese caso, no construyas todavía: sube a 150 contactos o cambia el segmento (agencias de nicho específico, por ejemplo e-commerce) y repite el mismo test. Si no logras pagos en ningún segmento, ya tienes tu respuesta, y te costó menos de $200 y tres semanas, no dos meses de código.