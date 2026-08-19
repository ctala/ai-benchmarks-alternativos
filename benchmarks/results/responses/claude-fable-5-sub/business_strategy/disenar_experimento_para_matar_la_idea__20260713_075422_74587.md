# Claude Fable 5 (suscripción) — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `claude-fable-5`
- success: True  | final: 6.48 | quality: 8.0
- latency_total: 63.837s | tokens_per_second: 51.5
- input_tokens: 2 | output_tokens: 3289

## Respuesta completa

Bien planteado. La mayoría diseña experimentos para confirmarse. Vamos a hacer lo contrario.

Primero, tu hipótesis tal como está es infalsificable ("pagarían" no se puede medir). La reescribo en algo que puede morir:

> **"De 30 agencias de 2-10 personas contactadas en frío, al menos 3 me pagan dinero real por adelantado en 14 días, antes de que exista el producto."**

Si eso no pasa, abandonas. Ahora el experimento, en 3 fases con kill-switch en cada una:

---

## Fase 0 — Chequeo de realidad (2 horas, $0)

Googlea "agency client reporting tool". Vas a encontrar AgencyAnalytics ($79/mes), Swydo, DashThis, Whatagraph, y Looker Studio **gratis**.

**Pregunta kill:** ¿puedes escribir en UNA frase por qué una agencia pagaría $200 a un desconocido en vez de $79 a un incumbente con 10 años de mercado?

- No puedes escribirla → **muerta aquí**. Te ahorraste 2 meses en 2 horas.
- Puedes (ej: "los incumbentes conectan datos, yo entrego el reporte redactado y enviado, cero trabajo humano") → sigue a Fase 1.

---

## Fase 1 — 15 conversaciones sobre el pasado, no el futuro (5 días, $0)

Contacta 40-50 dueños de agencias por LinkedIn (mensaje corto, sin pitch: "estoy investigando cómo las agencias manejan reportes a clientes, ¿me regalas 15 min?"). Con ~30% de respuesta tienes tus 15 llamadas.

**Prohibido preguntar:** "¿pagarías $200 por X?" — todo el mundo dice que sí y luego nadie paga.

**Preguntas obligatorias (comportamiento pasado):**
1. ¿Cuántas horas gastaste el mes pasado en reportes? ¿Quién las gastó y cuánto le pagas por hora?
2. ¿Qué has **intentado ya** para resolverlo? ¿Qué pagas hoy?
3. ¿Cuándo fue la última vez que perdiste un cliente o una venta por este tema?

**Kill criteria Fase 1:** si menos de 5 de 15 gastan >4 horas/mes en esto **Y** ya intentaron o pagaron por resolverlo → **muerta**. Un dolor por el que nadie ha movido un dedo no es un dolor de $200/mes, es una molestia de $0.

---

## Fase 2 — Pre-venta con dinero real (7-10 días, ~$100)

A los que mostraron dolor real en Fase 1 (y a 10-15 más del mismo perfil), les mandas una **oferta concreta**, no una encuesta:

> "Te automatizo los reportes de tus clientes. $200/mes. Primer reporte entregado en 7 días. Si no te sirve, te devuelvo el 100%."

Con un payment link de Stripe. Dinero por adelantado o mínimo tarjeta ingresada.

Truco clave: **no necesitas producto para cumplir**. Los primeros 3-5 clientes los atiendes en modo concierge — tú armas los reportes a mano con Looker Studio + plantillas. Aprendes el workflow real ANTES de escribir una línea de código, y validas el precio con la única moneda que no miente.

**Kill criteria Fase 2 (el importante):**

| Resultado en 10 propuestas | Veredicto |
|---|---|
| 0-1 pagan | **Muerta. Abandonas.** No importa cuántos dijeron "me encanta". |
| 2 pagan | Zona gris. Cambia segmento o precio UNA vez y repite. Segundo fallo = muerta. |
| 3+ pagan | Recién ahora te ganaste el derecho a construir. Y ya tienes clientes fundadores pagando. |

---

## Presupuesto total

- **Tiempo:** 12-14 días, ~2-3 horas diarias.
- **Plata:** <$150 (LinkedIn Sales Nav en trial gratis, Stripe gratis, quizás $99 si el trial se acaba).
- **Vs. tu plan actual:** 2 meses de tu vida construyendo a ciegas.

Una advertencia final: la señal de muerte más peligrosa es la que suena bien. **"Buenísima idea, avísame cuando lo lances" = no.** Solo cuenta tarjeta ingresada, transferencia hecha, o alguien que te da acceso a sus cuentas de clientes hoy. Todo lo demás es cortesía.

Si a los 14 días tienes menos de 3 pagos, la hipótesis está muerta y te costó $150 descubrirlo. Eso es un experimento exitoso — aunque la idea no lo sea.