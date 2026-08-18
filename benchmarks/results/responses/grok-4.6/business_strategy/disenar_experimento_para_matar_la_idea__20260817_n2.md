# Grok 4.6 — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `x-ai/grok-4.6`
- success: True  | final: 6.9 | quality: 8.0
- latency_total: 40.829s | tokens_per_second: 72.6
- input_tokens: 373 | output_tokens: 2965

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un fundador experimentado. Sabes que el objetivo de un experimento no es tener razón: es descubrir rápido y barato que estás equivocado. Diseñas tests que pueden FALLAR de forma concluyente.

**user:**

Mi hipótesis: las agencias de marketing pequeñas pagarían $200/mes por una herramienta que les automatice los reportes a clientes.

Estoy a punto de meterme 2 meses a construirla. Antes de eso, diséñame el experimento **más barato y más rápido** que pueda MATAR esta hipótesis.

No quiero validarla. Quiero saber, en el menor tiempo y plata posible, si estoy equivocado. Dime exactamente qué hago, cuánto me cuesta, cuánto tarda, y cuál sería el resultado que me hace abandonar la idea.


## Respuesta completa

**Experimento: pre-venta fría a 25 dueños de agencias (sin producto, sin landing elaborada).**

Esto mata la hipótesis de “pagarían $200/mes” de forma concluyente porque exige dinero o un compromiso que duele, no opiniones.

### Qué haces exactamente (en este orden)
1. En 90 minutos arma esto:
   - Un one-pager feo en Google Docs o Notion (gratis): problema (“pasas 8-15 h/mes armando reportes para clientes”), solución en 4 viñetas (conecta Ads + Analytics + Meta, genera PDF/PPT automático, se envía solo), precio $200/mes, “lanzamiento en 8 semanas, early access”.
   - Un enlace de pago Stripe Payment Link (o Mercado Pago) de $200 “Founding spot — Automated Client Reports. Reembolso completo si no entrego en 60 días”.
   - Un mensaje de 4 líneas para LinkedIn/email.

2. Encuentra 25 dueños/decision-makers de agencias pequeñas (1-15 personas). Búscalo en LinkedIn (“marketing agency owner” + ciudad o “agencia de marketing” + “dueño”), Clutch, o grupos de Facebook. Anota nombre + agencia. (1-2 horas).

3. Mándales el mensaje personalizado + el one-pager + el link de pago. Ejemplo de mensaje:
   “Vi que [agencia] maneja clientes de performance. Estoy sacando una herramienta que automatiza los reportes mensuales (Ads + Analytics + creativos). $200/mes. Si te sirve, el primer mes lo cobro ahora y te dejo como founding (o te devuelvo si no lo entrego). ¿Lo ves o prefieres que te muestre en 10 min?”

4. Haz follow-up una sola vez a las 48 h a los que no contestaron. A los que contesten “interesante”, pide el pago o una llamada de 15 min donde cierras el pago.

No construyas nada más. No hagas demos reales. No ofrezcas “te lo hago manual”. El único yes que cuenta es dinero o tarjeta.

### Costo y tiempo
- Costo: $0 (Stripe/Mercado Pago no cobra hasta que alguien pague; LinkedIn/email gratis).
- Tiempo total: 4-5 horas de trabajo + 4-5 días de espera de respuestas. Empiezas hoy, tienes el veredicto el viernes.

### Resultado que te hace abandonar la idea (criterio de muerte)
Si después de contactar a 25 dueños:
- 0 personas pagan los $200, **y**
- menos de 3 agendan la llamada **y** en esas llamadas nadie dice “te paso la tarjeta ahora” o “mándame la factura”,

la hipótesis está muerta. Las agencias pequeñas no pagan $200/mes por esto (el dolor no es tan fuerte, ya lo resuelven con AgencyAnalytics/DashThis/Excel + pasante, o $200 es demasiado). No construyas.

Si alguien paga, tienes señal real y puedes decidir si sigues. Si solo hay “me interesa, avísame cuando esté listo”, también está muerta: eso no es pago.

Hazlo esta semana. No empieces a codear.