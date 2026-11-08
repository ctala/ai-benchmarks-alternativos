# DeepSeek V4.1 Flash — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `deepseek/deepseek-v4.1-flash`
- success: True  | final: 7.31 | quality: 8.0
- latency_total: 80.812s | tokens_per_second: 101.3
- input_tokens: 218 | output_tokens: 8190

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un fundador experimentado. Sabes que el objetivo de un experimento no es tener razón: es descubrir rápido y barato que estás equivocado. Diseñas tests que pueden FALLAR de forma concluyente.

**user:**

Mi hipótesis: las agencias de marketing pequeñas pagarían $200/mes por una herramienta que les automatice los reportes a clientes.

Estoy a punto de meterme 2 meses a construirla. Antes de eso, diséñame el experimento **más barato y más rápido** que pueda MATAR esta hipótesis.

No quiero validarla. Quiero saber, en el menor tiempo y plata posible, si estoy equivocado. Dime exactamente qué hago, cuánto me cuesta, cuánto tarda, y cuál sería el resultado que me hace abandonar la idea.


## Respuesta completa

## El único test que la mata en 10 días y <$150: **pre-venta pagada**

No landing page con waitlist. No encuestas. No "customer discovery". No ads. Todo eso te da opiniones, y las opiniones no matan hipótesis.

Tu hipótesis tiene 4 supuestos metidos en una frase: (1) existen agencias pequeñas alcanzables, (2) el reporting les duele lo suficiente, (3) pagan $200/mes por eso, (4) lo pagan a una *herramienta* y no a un humano. El test de abajo los pone a los cuatro contra la pared con **un solo número: ¿se movió dinero antes de que exista el producto?**

Si nadie te paga $200 por algo que todavía no construiste, no lo vas a construir en 2 meses para que tampoco te paguen.

---

## Paso 0 — Definí el ICP en una frase (30 min)

"Pequeña agencia" es demasiado vago y te va a dar un falso negativo. Escribí esto y no lo cambies a mitad del test:

> Dueño u ops lead · 2–15 empleados · 5–40 clientes activos con retainer · hace reporting mensual de performance (GA4/Google Ads/Meta/SEO) como parte del retainer · hoy lo hace a mano en Sheets/Looker Studio.

**Excluí explícitamente:** solopreneurs con <5 clientes (no pagan $200), agencias con un rol dedicado a BI, agencias de un solo canal con dashboard nativo, y agencias de 50+ empleados (ciclo de venta enterprise).

Si el ICP no te da 150 nombres, el problema ya es de distribución y la idea está muerta igual.

---

## El experimento: 10 días hábiles

| Día | Qué hacés | Horas |
|---|---|---|
| 1 | Armar lista de 150 agencias del ICP (Clutch, Google Maps, LinkedIn, comunidades de agency owners). Nombre + canal de contacto. | 8 |
| 2 | Armar la oferta: mockup clickeable en Figma/Canva del flujo exacto (conectar datos → PDF branded → enviar al cliente) + Loom de 3 min mostrando el antes/después con un cliente ficticio. | 6 |
| 3–9 | Outreach personalizado, 20/día. Dos pasos (abajo). Agendar demos. | 15 |
| 3–10 | Hacer las demos (30 min). Al final de cada una: pedir la tarjeta. En vivo. | 8 |
| 10 | Contar. Decidir. | 1 |

**Costo cash total: ~$15–150.** Dominio + Stripe (~$15). Loom, Figma, Canva, Notion: gratis. Sales Navigator: trial gratis (o $99 un mes). Nada más.

---

## El guion (importante: no preguntes "¿pagarías?")

**Mensaje 1 (DM LinkedIn o email):**
> "Hola [Nombre] — estoy investigando cómo las agencias chicas manejan el reporting mensual a clientes. Pregunta rápida: ¿cuántas horas por mes se les va armando reportes y con qué lo hacen? Te comparto lo que estoy construyendo a cambio — demo de 3 min, sin pitch."

**Mensaje 2 (cuando responde, o a los 2 días):**
> "Justo ese es el problema que estoy atacando. Acá va el Loom de 3 min: [link]. Conecta GA4/Ads/Meta y genera el reporte branded solo. Estoy onboardeando 5 agencias fundadoras este mes a **$200/mes**. Si entrás esta semana: yo hago tu próximo reporte a mano mientras termino el producto, y te devuelvo todo si no te ahorra tiempo. ¿Te lo armo con [Cliente X]?"

Link de pago en el segundo mensaje. No en el quinto.

---

## La oferta (tiene que ser buena, o el test no vale)

- **Precio: $200/mes. Cobralo de verdad.** No lo bajes a $50 "para validar" — estás matando la hipótesis de $200, no la de $50.
- **Risk reversal:** "hasta que el producto esté listo, te hago el reporte a mano yo". Esto convierte la pre-venta en algo ético y creíble, y además te da el test de servicio gratis.
- **Urgencia real:** cohorte fundador de 5, con fecha de cierre.

---

## Qué cuenta como "pagó"

✅ Cargo en la tarjeta, depósito reembolsable, o acuerdo firmado con tarjeta en archivo y fecha de cobro.
❌ "Me interesa", "mandame más info", "seguro lo compraría", "avisame cuando esté".

**Un solo "sí" verbal no es dato. Es cortesía.**

---

## El resultado que te hace abandonar (escribilo ANTES de empezar)

**Criterio primario — matá la hipótesis si:**
> Después de **150 contactos calificados** y **≥12 demos mostradas** con la oferta de $200, **menos de 3 pagan**.

Por qué 3/12: si 1 de cada 4 dueños de agencia, viendo el demo y con descuento fundador + garantía + entrega manual, no pone $200 para ahorrarse horas al mes, el dolor es tibio o el precio está mal. Y si no conseguís 12 demos de 150 contactos dirigidos, el problema es que no podés alcanzar el segmento barato — eso también mata el negocio, aunque el producto sea bueno.

**Criterios secundarios (cualquiera solo alcanza para abandonar):**
- **<12 demos de 150 contactos** → distribución rota. Matalo.
- **La objeción dominante es "ya lo resolvemos en <30 min/mes" o "los clientes ni leen los reportes"** → el dolor no es agudo. Matalo.
- **Hay interés pero solo a <$75/mes** → la hipótesis de $200 está muerta (el producto puede vivir en otro precio, pero *tu hipótesis* no).
- **Solo convierten agencias de 20+ empleados o 50+ clientes** → "agencias pequeñas" es el segmento equivocado. Matalo.

**Abandonar = no empezar los 2 meses de build.**

---

## Si sobrevive (3–5 pagos)

Eso no es validación: es permiso para un build *chico*, no de 2 meses. Construí el MVP mínimo con esos clientes pagando, entregales el reporte a mano mientras construís, y seguí vendiendo. El dinero en la cuenta es el único andamio que vale.

---

## Si querés un segundo tiro, más duro (opcional, +1 semana, $0)

Antes del pre-sale, o en paralelo: posteá en 5 comunidades donde viven agency owners (Online Geniuses, r/marketingagency, grupos de Facebook de agencias) ofreciendo: *"Te tomo el reporting mensual de clientes, primer reporte gratis, después $200/mes."* Si ni siquiera el **done-for-you** (que vale más que la herramienta) genera interés, la herramienta a $200 está muerta con certeza. Tratalo como evidencia de apoyo, no como conclusión: los posts en comunidades tienen alcance errático.

---

## Lo que NO hagas (es donde se cae el 90% de los founders)

- ❌ Landing page + $100 de ads: tráfico frío, muestra chica, 3 semanas, cero señal de precio.
- ❌ Encuesta "¿pagarías $200?": todos mienten.
- ❌ Entrevistas de discovery: sirven para afinar el pitch y el ICP, no para falsificar el precio. Cualquiera dice "qué bueno" en una llamada.
- ❌ Prototipo más allá de un mockup clickeable + Loom.

**El experimento cuesta ~$100 y 10 días. El error que estás por cometer cuesta 2 meses de tu vida.** La asimetría es obvia: corré el test, pre-commiteá el criterio de muerte por escrito hoy, y dejá que la realidad te diga que estás equivocado barato.