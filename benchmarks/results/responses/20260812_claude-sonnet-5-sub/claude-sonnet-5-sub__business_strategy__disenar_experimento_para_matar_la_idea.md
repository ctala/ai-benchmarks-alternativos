# Claude Sonnet 5 (suscripción) — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `claude-sonnet-5`
- success: True  | final: 6.71 | quality: 8.0
- latency_total: 78.076s | tokens_per_second: 64.5
- input_tokens: 2 | output_tokens: 5033

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un fundador experimentado. Sabes que el objetivo de un experimento no es tener razón: es descubrir rápido y barato que estás equivocado. Diseñas tests que pueden FALLAR de forma concluyente.

**user:**

Mi hipótesis: las agencias de marketing pequeñas pagarían $200/mes por una herramienta que les automatice los reportes a clientes.

Estoy a punto de meterme 2 meses a construirla. Antes de eso, diséñame el experimento **más barato y más rápido** que pueda MATAR esta hipótesis.

No quiero validarla. Quiero saber, en el menor tiempo y plata posible, si estoy equivocado. Dime exactamente qué hago, cuánto me cuesta, cuánto tarda, y cuál sería el resultado que me hace abandonar la idea.


## Respuesta completa

# El problema con tu hipótesis tal como está

Antes del experimento: tu hipótesis no es falsificable en su forma actual. "Pagarían $200/mes" es demasiado vago para matarlo rápido. Y hay un dato que cambia todo el diseño: **este mercado ya existe**. AgencyAnalytics, Whatagraph, DashThis, Databox, Swydo, Reportgarden — hay 15+ herramientas de agency reporting compitiendo desde $59 a $250/mes.

Eso significa que el riesgo real NO es "¿existe el dolor de hacer reportes?" (sí existe, ya hay categoría). El riesgo real es: **¿por qué te van a pagar a TI, sin marca, sin reviews, sin track record, cuando ya tienen 15 opciones probadas?**

Si diseñas el experimento para testear "existe el dolor", vas a validar algo que ya sabías y vas a perder 2 meses construyendo de todos modos. El experimento tiene que apuntar al riesgo letal: **compromiso de pago real contra tu oferta específica, no contra la categoría.**

# El experimento

**Nombre: Smoke test con preventa + outreach directo (no landing pasiva esperando tráfico).**

### Paso 1 — Define el gancho específico (medio día, $0)
No vendas "reportes automatizados". Eso ya lo vende todo el mundo. Necesitas un diferenciador de una línea que un dueño de agencia entienda en 5 segundos (ej: "reportes que el cliente entiende sin que tengas que explicarlos en la llamada" o "reportes en 2 minutos vs. las 3 horas que gastas armando slides"). Sin esto, el test mide tu landing page, no tu hipótesis.

### Paso 2 — Landing de una página con oferta de dinero real (1 día, ~$30)
Un template de Framer/Carrd. Precio visible: $200/mes. CTA no es "déjame tu email" — es **"Reserva tu lugar como founding member: $50 de depósito reembolsable, 50% off de por vida si entras ahora"**. El depósito es la bisagra del experimento: separa curiosidad de compromiso.

### Paso 3 — Outreach directo a 100 agencias calificadas (7-10 días, ~$0-100)
No esperes tráfico orgánico ni corras ads (eso mide tu copy de ads, no tu producto). Ve directo:
- LinkedIn Sales Navigator o scraping: dueños de agencias 1-10 personas
- Grupos de Facebook/Skool de agencias, r/agency, r/marketing
- Mensaje directo 1:1, no masivo: "Vi que manejas [N] clientes en [nicho]. ¿Cómo armas los reportes hoy? Estoy lanzando algo específico para esto, ¿te interesa ver la oferta founding member?"

Calificado = agencia de 1-10 personas que reporta resultados a clientes de forma recurrente (mensual mínimo). Si no cumple esto, no cuenta para la muestra.

### Costo y tiempo totales
- **Plata:** $100-150 (landing + herramientas de scraping/outreach)
- **Tiempo:** 10-14 días, part-time
- **Tu tiempo real:** ~15-20 horas

# El número que mata la hipótesis

De **100 agencias calificadas contactadas 1:1**, si consigues **menos de 5 depósitos pagados** (no "me interesa", no emails — dinero cargado), la hipótesis está muerta. No "necesita ajustes", muerta.

Por qué 5%: es un test de preventa con oferta agresiva (mitad de precio, founding member) a una audiencia caliente y calificada 1:1. Si ni con esas condiciones favorables llegas al umbral, imagina el mercado frío que tendrías que vencer para escalar contra 15 competidores establecidos.

Si consigues 5-10 depósitos: señal ambigua, no construyas todavía — haz 10 entrevistas con los que pagaron para entender el ángulo exacto antes de meter 2 meses.

Si consigues 10+: ahí sí hay algo, y ya tienes primeros clientes pagando antes de escribir una línea de código.

# Qué NO cuenta como señal (y por qué)

- **"Me interesa" / email dejado:** no cuesta nada decirlo. Tasa de conversión de interés-a-pago suele ser 10-20x menor de lo que la gente cree.
- **Encuesta preguntando "¿pagarías $200/mes?":** la gente miente por cortesía. Nadie dice que no en una encuesta.
- **Feedback de tu propia red o de Skool CAR:** sesgado, te conocen, quieren ayudarte. El outreach frío a desconocidos calificados es el único que aproxima al mercado real.

# El movimiento barato antes de esto

Si quieres gastar $0 y 3 días antes de siquiera montar la landing: agarra 15 dueños de agencia (LinkedIn, tu red, comunidades) y pregúntales qué usan hoy y cuánto pagan. No preguntes si pagarían tu producto — pregunta por su comportamiento actual (herramienta, precio, qué odian). Si el 80% no reporta o usa Google Sheets gratis sin dolor visible, mataste la hipótesis por $0 antes de gastar los $150 del smoke test.

**Orden correcto: 15 conversaciones de descubrimiento ($0, 3 días) → si sobrevive, smoke test con depósito ($150, 10 días) → si sobrevive, ahí recién te metes 2 meses.**