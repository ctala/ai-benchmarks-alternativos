# Inkling Small — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `thinkingmachines/inkling-small`
- success: True  | final: 7.3 | quality: 8.0
- latency_total: 23.331s | tokens_per_second: 181.6
- input_tokens: 174 | output_tokens: 4238

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un fundador experimentado. Sabes que el objetivo de un experimento no es tener razón: es descubrir rápido y barato que estás equivocado. Diseñas tests que pueden FALLAR de forma concluyente.

**user:**

Mi hipótesis: las agencias de marketing pequeñas pagarían $200/mes por una herramienta que les automatice los reportes a clientes.

Estoy a punto de meterme 2 meses a construirla. Antes de eso, diséñame el experimento **más barato y más rápido** que pueda MATAR esta hipótesis.

No quiero validarla. Quiero saber, en el menor tiempo y plata posible, si estoy equivocado. Dime exactamente qué hago, cuánto me cuesta, cuánto tarda, y cuál sería el resultado que me hace abandonar la idea.


## Respuesta completa

Tu objetivo no es que te digan “me suena interesante”. Es que saquen la tarjeta **antes de que existas**. Si no lo hacen, no hay producto que construir.

Aquí está el experimento más barato y más rápido para **matar** tu hipótesis. No valida. Falsifica.

---

### El experimento: “Concierge Pre-Venta con Cobro Real” (Wizard of Oz)

No construyas nada. No hagas landing page bonita. No hagas encuesta. **Vendes manualmente un servicio que luego podría ser software**, cobras $200/mes real, y mides cuántos cierran en 10 días.

**La lógica:** Si una agencia pequeña no paga $200/mes por un reporte manual hecho por ti (que resuelve su dolor hoy), **no pagará $200/mes por una herramienta que aún no existe**.

---

### Qué haces paso a paso (exacto)

**Paso 1 – Define el objetivo de matar (1 día, $0)**
Busca **20 agencias pequeñas** que cumplan:
- 2 a 10 empleados.
- Tienen clientes externos (no solo su marca).
- No sean amigos ni conocidos (para que el “sí” sea real).

Dónde encontrarlas sin pagar: LinkedIn (búsqueda gratuita por “marketing agency” + “founder” + ciudad), directorios de Clutch.co filtrando por tamaño, grupos de Facebook/Slack de marketing.

**Paso 2 – Redacta la oferta (30 minutos, $0)**
No digas “¿te gustaría automatizar?”. Di esto exacto en DM/email:

> *“Hola [Nombre], vi que [Agencia] maneja cuentas para clientes externos. Una pregunta rápida: ¿cuánto tiempo te toma armar los reportes mensuales para cada cliente? Estoy lanzando un servicio (y luego una herramienta) para entregar reportes automáticos a tus clientes por **$200/mes**. Por ahora lo hago manual para asegurar calidad: te entrego el primero este mes sin que armes nada. Si no te convence, te devuelvo el dinero. ¿Te apunto para este mes o prefieres que no te moleste?”*

**Paso 3 – Envía a 20 (3 días, $0)**
Envía 7 mensajes al día, manuales. No uses mailchimp. Si no responden en 48h, un recordatorio cortísimo.

**Paso 4 – Cierra con pago real (7 días, $0)**
Si dicen “sí, me interesa”, no digas “te mando más info”. Di:
> *“Perfecto. Te paso el enlace de pago (Stripe/PayPal/transferencia) por $200 para este mes. Una vez que entra, te pido los accesos y te entrego el primer reporte el día 5.”*

Si no te pasan la tarjeta/transferencia en 3 días, **no es un “sí”**. Es un “quizás” que mata tu hipótesis.

**Paso 5 – Entrega manual si pagan (opcional, 2 horas, $0)**
Si alguien paga, armas el reporte con Google Sheets / Data Studio / Canva / Notion manualmente. Esto no es para validar la tecnología; es para no ser estafa y ver si realmente usan el servicio. Pero **no necesitas hacer esto para matar la idea**; es solo ética si cierran.

---

### Costos y tiempo exactos

| Concepto | Costo | Tiempo |
|---|---|---|
| Buscar 20 agencias | $0 (LinkedIn/Clutch manual) | 1 día |
| Mensajes de contacto | $0 | 3 días |
| Cobro (Stripe/transferencia) | $0 a $10 (Stripe cobra ~3%) | 7 días |
| Landing page (opcional, no necesaria) | $0 (Notion/Google Sites) | 0 días |
| Entrega manual (solo si pagan) | $0 (tú o un VA barato) | 2 horas |
| **Total** | **$0 – $30** | **10 días máximos** |

---

### El resultado que te hace abandonar (Kill Criteria)

**Matas la hipótesis inmediatamente si:**
- **0 o 1 de 20 agencias te paga** dentro de los 10 días.
- Te dicen “ya lo hago con Sheets/Looker” o “no es tan urgente”.
- Te dicen “me suena bien” pero no te pasan el pago.

**¿Por qué es concluyente?**
No estás midiendo “interés” (que siempre es alto). Estás midiendo **disposición a pagar real** por un dolor que hoy resuelven gratis o con 2 horas de trabajo. Si a $200/mes nadie saca la tarjeta, el problema no es lo suficientemente agudo para una herramienta pagada de $200. No necesitas 2 meses de desarrollo para saberlo.

**Nota crucial:** Si alguien paga, **no te emocione y no empieces a construir software**. Sigue entregando manualmente por 2 meses. Si solo 1 o 2 pagan, tu modelo es un servicio, no un SaaS escalable a $200/mes.

---

### Lo que NO debes hacer (porque te hace perder tiempo)

- No hagas una encuesta “¿te gustaría una herramienta de reportes?”. Eso valida tu sesgo.
- No construyas un MVP funcional.
- No hagas una landing page con “pre-orden” sin cobro real; es fácil que alguien deje su email sin intención de pagar.
- No bajes el precio a $50 “para validar”. Si el problema es real, $200 es un precio razonable para una agencia; si no pagan a $200, no es que el precio esté mal, es que **el valor percibido no está ahí**.

**Tu tarea hoy:** Escribe el mensaje de 3 líneas, busca 20 nombres, envía hoy. En 10 días sabes si estás equivocado. Si estás equivocado, abandonas antes de escribir una sola línea de código. Eso es descubrir barato y rápido.