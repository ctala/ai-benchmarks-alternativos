# Kimi K2.7 Code — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `moonshotai/kimi-k2.7-code`
- success: True  | final: 6.89 | quality: 8.0
- latency_total: 112.138s | tokens_per_second: 51.3
- input_tokens: 222 | output_tokens: 5755

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un fundador experimentado. Sabes que el objetivo de un experimento no es tener razón: es descubrir rápido y barato que estás equivocado. Diseñas tests que pueden FALLAR de forma concluyente.

**user:**

Mi hipótesis: las agencias de marketing pequeñas pagarían $200/mes por una herramienta que les automatice los reportes a clientes.

Estoy a punto de meterme 2 meses a construirla. Antes de eso, diséñame el experimento **más barato y más rápido** que pueda MATAR esta hipótesis.

No quiero validarla. Quiero saber, en el menor tiempo y plata posible, si estoy equivocado. Dime exactamente qué hago, cuánto me cuesta, cuánto tarda, y cuál sería el resultado que me hace abandonar la idea.


## Respuesta completa

No construyas nada todavía. El experimento más barato y rápido para **matar** tu hipótesis es un **Concierge Prepaid / Wizard of Oz**: les vendes el *resultado* (reportes automáticos entregados) como si ya existiera el software, pero tú lo produces manualmente.

Si no logras que agencias reales paguen \$200 antes de que exista el producto, no hay mercado. Punto.

---

## 1. Qué vas a construir (2-3 horas, casi gratis)

Una fachada creíble, nada de código:

- **Landing simple** en Carrd, Notion o Webflow gratuito. Título: *“Reportes mensuales para clientes de agencias, hechos automáticamente. \$200/mes.”*
- **Una demo falsa** hecha en Figma o Google Slides, grabada en Loom (3-5 min). Muestra el “dashboard” y un ejemplo de reporte PDF/Email saliendo solo.
- **Página de pago** con Stripe Link, PayPal o Mercado Pago: \$200 por el primer mes, pago adelantado.
- **Calendly gratuito** para agendar demos de 15 min.
- **Dominio barato** si quieres verse profesional: ~\$12/año.

Total inicial: **\$0-15**.

---

## 2. A quién le vas a vender

Define exactamente a quién contactas. No a “agencias”, sino a:

- Agencias de marketing digital de **2 a 20 personas**.
- Que tengan **más de 5 clientes activos**.
- Que hoy **envíen reportes mensuales manualmente** (Google Sheets, PowerPoint, Looker Studio a mano, etc.).
- Que el contacto sea **quien decide** (founder, director de operaciones o account manager senior).

Si no califica, no cuenta.

---

## 3. Dónde encontrarlas (sin pagar ads)

- LinkedIn: búsqueda por “Founder + marketing agency” filtrando por tamaño.
- Directorios de agencias: Clutch, Sortlist, Google Maps en tu ciudad/región.
- Comunidades: grupos de Facebook/Slack/Discord de agencias de marketing.
- Apollo.io o Hunter.io (plan gratuito) para encontrar emails.

Tu objetivo: armar una lista de **30 agencias calificadas**.

---

## 4. Qué les vas a decir (copia y pega, ajusta)

**Email/LinkedIn:**

> Asunto: ¿Sigues armando reportes a mano cada mes?
>
> Hola [Nombre],
>
> Vi [nombre agencia] y me imagino que cada mes alguien de tu equipo pierde horas armando reportes para clientes.
>
> Estoy probando un servicio que entrega reportes mensuales automáticos por \$200/mes. Por ahora lo estoy operando de forma *concierge* (manual por detrás) para validar que el resultado valga la pena, pero tú lo recibes como si fuera automático.
>
> Si te interesa, armo una demo de 15 min esta semana. El primer mes se paga adelantado (\$200). Si no te ahorra tiempo, te devuelvo el dinero.
>
> ¿Tienes 15 min el martes o miércoles?
>
> [Tu nombre]

**Importante:** no digas “estoy pensando en construir”. Dices que ya tienes el servicio y vendes pago adelantado.

---

## 5. Qué haces en la demo (15 min)

1. Pregunta cuántos clientes reportean, cuánto tiempo les toma y quién lo hace.
2. Muestra la demo falsa en Loom/Figma.
3. Cierra directo: **“¿Te anotas? El primer mes son \$200, pagás ahora y empezamos esta semana.”**

Si dudan, pregunta: *“¿Qué te frena a pagar hoy?”*

- Si dicen “falta tal integración” o “quiero otra métrica” → es objeción de producto, no mata la idea.
- Si dicen “no tenemos presupuesto”, “no es prioridad”, “ya lo resolvemos gratis con Google Sheets/Looker” → **eso mata**.

---

## 6. Resultado que te hace abandonar

Tu métrica es **una sola: pago real de \$200 adelantado**.

Tras contactar a **30 agencias calificadas** con **dos follow-ups** cada una:

- **0 pagos** = mata la idea. No hay mercado dispuesto a pagar \$200/mes por esto.
- **1-2 pagos** = señal débil. Probablemente también mates, a menos que los que pagaron sean muy similares y haya un patrón claro.
- **3-5 pagos o más** = la idea sobrevive y pasas a la siguiente etapa.

**Regla de muerte temprana:** si después de 30 contactos no logras ni siquiera **5 demos agendadas**, también mata. Significa que ni siquiera les interesa lo suficiente como para escucharte.

---

## 7. Cuánto tarda y cuánto cuesta

| Ítem | Tiempo | Costo |
|------|--------|-------|
| Landing + demo falsa + pago | 2-3 horas | \$0-15 |
| Armar lista de 30 agencias | 2-3 horas | \$0 |
| Outbound (email/LinkedIn + follow-ups) | 4-6 horas | \$0 |
| Demos y cierre | 3-5 horas | \$0 |
| **Total** | **\~3-5 días de trabajo esparcido en 7-10 días hábiles** | **\$0-15** |

Si nadie paga, **no entregas nada** y no pierdes más tiempo.

Si alguien paga, produces el reporte manualmente ese primer mes usando Google Sheets, Looker Studio, Canva o contratando a un freelancer por hora. Eso te cuesta tiempo, pero **solo si ya validaste que alguien paga**.

---

## 8. Por qué esto mata mejor que una encuesta

- **No importa si dicen que les “interesa”.** La gente miente en encuestas. El pago no.
- **No importa si les gusta la idea.** Importa si sacan la tarjeta.
- **No gastaste 2 meses programando.** Gastaste una semana y \$15.

---

## Resumen de tu plan

1. Construye fachada en un día.
2. Contacta 30 agencias calificadas.
3. Vende \$200/mes con pago adelantado.
4. Si logras **0 pagos** (o no logras 5 demos), **abandona la idea**.
5. Si logras **3-5 pagos**, sigue: cumple manualmente un mes y luego decidirás si construyes el software.

Tu objetivo no es tener razón. Es descubrir lo más rápido posible que estás equivocado. Si en 10 días y \$15 nadie paga, lo estás. Y eso te ahorró 2 meses de código.