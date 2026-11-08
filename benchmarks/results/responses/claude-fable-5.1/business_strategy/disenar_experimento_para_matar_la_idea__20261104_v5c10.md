# Claude Fable 5.1 — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `anthropic/claude-fable-5.1`
- success: True  | final: 6.49 | quality: 8.0
- latency_total: 52.002s | tokens_per_second: 59.1
- input_tokens: 291 | output_tokens: 3074

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un fundador experimentado. Sabes que el objetivo de un experimento no es tener razón: es descubrir rápido y barato que estás equivocado. Diseñas tests que pueden FALLAR de forma concluyente.

**user:**

Mi hipótesis: las agencias de marketing pequeñas pagarían $200/mes por una herramienta que les automatice los reportes a clientes.

Estoy a punto de meterme 2 meses a construirla. Antes de eso, diséñame el experimento **más barato y más rápido** que pueda MATAR esta hipótesis.

No quiero validarla. Quiero saber, en el menor tiempo y plata posible, si estoy equivocado. Dime exactamente qué hago, cuánto me cuesta, cuánto tarda, y cuál sería el resultado que me hace abandonar la idea.


## Respuesta completa

Primero, lo que de verdad estás apostando. Tu hipótesis son tres apuestas encadenadas y basta con que una falle:

1. Las agencias pequeñas sienten el reporting como un dolor real (no como una molestia tolerable).
2. Ese dolor vale **$200/mes** para ellas (no $50, no $0).
3. Están dispuestas a cambiar lo que hacen hoy por una herramienta nueva.

El experimento más barato no es construir nada. Es **intentar cobrar**.

---

## Paso 0 — Chequeo de 1 hora (puede matarla antes de empezar)

Abre AgencyAnalytics, DashThis, Swydo, Whatagraph, Looker Studio (gratis). Anota precios.

Spoiler: hay herramientas de reporting para agencias desde ~$40–$150/mes, y Looker Studio es gratis. Pregúntate honestamente: **¿qué hace que una agencia pequeña pague $200 por la tuya en vez de $59 por la que ya existe?** Si no puedes escribir esa respuesta en una frase que una agencia reconocería como su problema, la hipótesis ya está muerta. No hace falta seguir.

Si tienes esa frase, sigue.

---

## El experimento: pre-venta concierge

**Costo:** $0–100 (dominio, Stripe, quizá un trial de Sales Navigator o Apollo).
**Tiempo:** 10 días hábiles, máximo 2 semanas.
**Qué construyes:** nada. Cero código.

### Día 1–2: lista de 50 agencias
Agencias de 2–10 personas. Fuentes: Clutch, Google Maps ("agencia marketing digital" + ciudad), LinkedIn, grupos de Facebook/Slack de agencias. Ideal: que tengan 5+ clientes, porque con 2 clientes el reporting no duele.

### Día 2–8: 15 conversaciones de 20 minutos
Mensaje de contacto (LinkedIn o email, no vendas todavía):

> "Estoy hablando con dueños de agencias pequeñas sobre cómo hacen los reportes mensuales a clientes. ¿Me regalas 20 min esta semana? No vendo nada todavía, estoy investigando."

Tasa esperada: 50 contactos → 15 llamadas. Si no llegas a 10 llamadas en una semana, ya tienes una señal: el tema no les importa lo suficiente ni para hablar.

En la llamada, **prohibido preguntar "¿pagarías $200?"**. Todos dicen que sí. Preguntas esto:

- ¿Cómo hiciste el último reporte a un cliente? Cuéntamelo paso a paso.
- ¿Cuántas horas al mes se van en eso, de quién?
- ¿Qué has probado para resolverlo? ¿Qué pagas hoy por eso?
- ¿Qué fue lo último que te hizo decir "esto tiene que cambiar"?
- Si mañana desaparece el problema, ¿qué es lo primero que harías con ese tiempo?

### Último tercio de cada llamada: la oferta
Si (y solo si) el dolor apareció solo, sin que lo sugieras:

> "Te propongo algo concreto. Yo te entrego los reportes de todos tus clientes cada mes, con tu marca, a partir del próximo lunes. $200/mes. Para empezar te cobro el primer mes ahora, $200, y si el primer reporte no te sirve te devuelvo todo. ¿Te mando el link de pago?"

Lo haces **tú a mano** con Looker Studio y Google Sheets. Es el "concierge": vendes el resultado, no la herramienta. Si pagan por el resultado manual, pagarán por el automatizado. Si no pagan ni por el resultado hecho, ninguna herramienta lo salva.

Mandas link de Stripe **en la llamada o inmediatamente después**. No "te lo pienso y te aviso". Esa frase es un no.

---

## Criterio de muerte (decídelo hoy, antes de la primera llamada)

Abandona la idea si ocurre **cualquiera** de estas:

| Señal | Umbral de muerte |
|---|---|
| Pagos reales | Menos de **3 de 15** pagan $200 (o al menos un depósito de $100) |
| Dolor | Menos de 5 de 15 dedican **más de 4 horas/mes** al reporting |
| Prioridad | Al preguntar "¿qué te quita el sueño?", el reporting no aparece espontáneamente en el top 3 de al menos 5 |
| Alternativas | La mayoría ya paga una herramienta de $50–150 y dice que "funciona bien" |
| Precio | Los que sí pagarían negocian a $50–80 — eso dice que el valor percibido es un tercio de tu hipótesis |

Tres pagos de quince es un **20%** de conversión en frío, con oferta manual y sin producto. Si no llegas ni ahí con gente que acaba de contarte su dolor en voz alta, no vas a llegar con un SaaS que tiene que descubrirte, confiar en ti y configurarse solo.

---

## Lo que NO cuenta como validación (para que no te engañes)

- "Me encantaría, avísame cuando esté listo." → No.
- "Sí, pagaría $200, suena bien." → No. Solo cuenta el link de Stripe cobrado.
- "Es un dolor enorme" pero dedican 1 hora al mes. → No. Es una queja, no un dolor.
- 2 pagos y "varios interesados". → No. Definiste 3. No muevas el umbral después.
- Un amigo que tiene agencia y te paga. → No cuenta en los 15.

---

## Si sobrevive

Tendrás 3+ clientes pagando, una lista de qué tienen que incluir los reportes exactamente (porque los hiciste a mano), y sabrás qué integraciones importan de verdad (Meta Ads, Google Ads, GA4… o algo que no esperabas). Ahí construyes 2 meses **con ingresos y con spec real**, no con una hipótesis.

Costo total del experimento: ~$50 y dos semanas. Costo de saltártelo: dos meses y, probablemente, descubrir lo mismo en el lanzamiento.