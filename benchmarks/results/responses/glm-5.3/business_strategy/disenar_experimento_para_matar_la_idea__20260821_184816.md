# GLM 5.3 — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `z-ai/glm-5.3`
- success: True  | final: 6.72 | quality: 8.0
- latency_total: 175.077s | tokens_per_second: 60.0
- input_tokens: 194 | output_tokens: 10513

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un fundador experimentado. Sabes que el objetivo de un experimento no es tener razón: es descubrir rápido y barato que estás equivocado. Diseñas tests que pueden FALLAR de forma concluyente.

**user:**

Mi hipótesis: las agencias de marketing pequeñas pagarían $200/mes por una herramienta que les automatice los reportes a clientes.

Estoy a punto de meterme 2 meses a construirla. Antes de eso, diséñame el experimento **más barato y más rápido** que pueda MATAR esta hipótesis.

No quiero validarla. Quiero saber, en el menor tiempo y plata posible, si estoy equivocado. Dime exactamente qué hago, cuánto me cuesta, cuánto tarda, y cuál sería el resultado que me hace abandonar la idea.


## Respuesta completa

# El experimento: vende el resultado a mano, cobra antes de construir

**La lógica primero.** Para que un test pueda matar, la hipótesis necesita su *mejor* oportunidad de sobrevivir. Así que no vendas software: vende el resultado hecho por ti. "Tus reportes de clientes, con tu marca, entregados cada mes, $200". Un humano entregándolo es la versión **máxima** de tu producto: sin setup, sin curva de aprendizaje. Si ni esa versión se vende a $200, la versión software —que exige configuración— tampoco. Muerte sin apelación.

Lo que **no** es el test: landing page + ads (resultado ambiguo: no distingues idea mala de copy malo), entrevistas solas (la gente miente sobre disposición a pagar), o preguntar "¿pagarías $200 por esto?" (basura).

---

### Paso 0 — 1 hora, $0
Mira los precios de AgencyAnalytics, Swydo, Databox, Whatagraph. La mayoría entra por debajo de $200, y tu competidor real es **Looker Studio gratis + un asistente**. Esto no mata nada por sí solo, pero afila el criterio: tu test tiene que demostrar que gente que ya tiene opciones más baratas paga tu premium.

### Días 1-2 — ICP y lista
"Agencia pequeña" no es un ICP. Define: 2-15 personas, ≥5 clientes con reporte recurrente, decide el dueño. Arma una lista de 150-200 (Clutch, LinkedIn, directorios, comunidades de agencias).

### Días 3-10 — Outreach con oferta real
15-20 contactos diarios, personalizados:

> "Hola [Nombre], vi que [Agencia] maneja cuentas de [Meta/Google Ads]. ¿Quién arma los reportes mensuales para tus clientes y cuánto les toma? Estoy lanzando un servicio para agencias chicas: reportes de clientes automáticos, con tu marca, sin que nadie toque una hoja de cálculo. $200/mes. Estoy tomando solo 5 agencias fundadoras. Si el tema te pica, ¿15 min esta semana?"

En la llamada, **tres preguntas de comportamiento antes de pitchear**:
1. ¿Cómo arman los reportes hoy? ¿Quién y cuántas horas?
2. ¿Qué han probado para quitárselo de encima? (Si no intentaron nada, el dolor es cosmético.)
3. ¿Cuánto les cuesta hoy? (Horas × sueldo, o lo que pagan a VA/herramienta.)

Luego la oferta y, **el mismo día, el link de pago**. No "te mando una propuesta": link de Stripe.

**La oferta exacta:** $200/mes, reportes white-label, hasta 10 reportes/mes, "5 agencias fundadoras, precio congelado para siempre", sin permanencia. Tú entregas con Looker Studio + sudor. Cap en 5 clientes.

---

### Criterios de muerte — escríbelos HOY, con fecha, y mándaselos a alguien

Dentro de dos semanas vas a querer renegociarlos. No podrás.

Con mínimo 20-25 conversaciones con decisor:

- **Muere el problema** si menos de la mitad confirma ≥2 horas/semana en reportes o ya paga por resolverlo (VA, herramienta, freelancer).
- **Muere la hipótesis** si menos de 3 de ~25 pagan o firman compromiso con fecha de inicio (<12%).
- **Zona gris** (3-4 pagos): un solo cambio — segmento u oferta — una semana más, misma vara. No dos cambios, no un mes más.
- **Señal fuerte** (≥5 pagos, ~20%): y aun así **no construyas todavía**. Entrega manual un mes, aprende el flujo real, y construyes con una spec escrita por clientes pagando.
- **Muerte por precio**: si solo cierran a $99, tu hipótesis de $200 murió. Y a $99 con agencias chicas, revisa el math del negocio antes de celebrar.

**Qué cuenta como pago:** dinero movido o contrato firmado con fecha y monto. "Me interesa, mándame info" = no. "Lo consulto con mi socio" = no. Un sí sin pago es un no con modales.

**Si no llegas a 15-20 conversaciones tras 200 contactos:** no es muerte automática del producto, pero sí bandera roja seria. Si no puedes hablar con 20 dueños de agencia sobre un dolor que dicen tener, venderles software a $200/mes va a ser peor.

---

### Costo y tiempo
- **Dinero:** $0-50 (LinkedIn, Gmail, Meet, Stripe y Looker Studio son gratis; opcional un dominio + Carrd).
- **Tiempo:** 10-14 días laborables.

Estás intercambiando 2 semanas y $0 por 2 meses de build + 6 de iteración a ciegas.

Un detalle de veteranos: si el test muere después de que alguien pagó, entrega lo pagado y reembolsa el resto. No quemes el mercado al que quizás vuelvas con otra cosa.

---

El peor resultado posible no es que la hipótesis muera — es que sobreviva por casualidad y te coma 8 meses descubriéndolo en producción. Este test no puede darte eso: te da pagos con nombre y apellido, o un no con razones concretas. Ambos te hacen más rico de lo que estás hoy.