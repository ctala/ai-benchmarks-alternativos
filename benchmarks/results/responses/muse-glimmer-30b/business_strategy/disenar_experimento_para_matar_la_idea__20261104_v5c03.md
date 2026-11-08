# Muse Glimmer 30B — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `meta/muse-glimmer-30b`
- success: True  | final: 7.4 | quality: 8.0
- latency_total: 16.883s | tokens_per_second: 119.8
- input_tokens: 181 | output_tokens: 2023

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un fundador experimentado. Sabes que el objetivo de un experimento no es tener razón: es descubrir rápido y barato que estás equivocado. Diseñas tests que pueden FALLAR de forma concluyente.

**user:**

Mi hipótesis: las agencias de marketing pequeñas pagarían $200/mes por una herramienta que les automatice los reportes a clientes.

Estoy a punto de meterme 2 meses a construirla. Antes de eso, diséñame el experimento **más barato y más rápido** que pueda MATAR esta hipótesis.

No quiero validarla. Quiero saber, en el menor tiempo y plata posible, si estoy equivocado. Dime exactamente qué hago, cuánto me cuesta, cuánto tarda, y cuál sería el resultado que me hace abandonar la idea.


## Respuesta completa

Tu hipótesis muere si no consigues dinero real en 5 días. No entrevistas, no likes. Pago o interés de pago real.

Aquí está el experimento de falsación más barato:

### Experimento: Fake Door + Pre-venta con depósito

**Objetivo:** Probar si agencias pequeñas están dispuestas a sacar la tarjeta por $200/mes por automatizar reportes.

**Hipótesis a matar:** "Pagarían $200/mes"

**Criterio de muerte:** 0 pagos y <10% de interés real tras 100 agencias calificadas contactadas en 72h.

### Qué haces exactamente

**Día 1 - 3 horas de setup**

1. **ICP concreto:** Agencias de marketing de 3-15 personas en LATAM/ES, que gestionen 10+ clientes y usen Meta Ads / Google Ads. No freelancers.
2. **Landing de humo:** Carrd / Framer gratis. 1 pantalla.
    Headline: "Reportes de clientes de Meta Ads y Google Ads en 1 clic. Se envían solos cada lunes."
    3 bullets: Conecta cuentas, plantilla editable, se envía por email/Slack a cliente.
    Precio: $200/mes. CTA: "Reserva tu acceso anticipado - $149 el primer mes".
    Botón lleva a Stripe Payment Link con pago de $49 de depósito reembolsable. Texto: "Depósito para acceso prioritario. Te devolvemos el dinero si no te gusta en 7 días."
3. **Demo falsa:** 1 video de 60s con Loom grabando un prototipo en Figma. Muestra login, conexión a Meta, reporte PDF generado. No hay backend real.
4. **Lista:** 100 agencias calificadas. Sácalas de LinkedIn, Instagram, Clutch, Facebook Groups "Agencias de Marketing". Necesitas nombre, email/IG/LinkedIn del dueño.

**Día 2-4 - Outreach**

Script DM/Email corto y sin vender:

> Hola [Nombre], vi que gestionan [X] cuentas en [plataforma]. Estoy lanzando una herramienta que automatiza los reportes mensuales a clientes para agencias como la tuya. Se conecta a Meta/Google y envía el PDF por email cada lunes.
> 
> Es $200/mes. Estoy dando acceso anticipado a 10 agencias por $149 el primer mes.
> 
> ¿Te interesa ver el demo de 60s y reservar plaza? Te dejo el link: [landing]

No hables de features. Pregunta por el pago.

Canal: 50 DMs de Instagram/LinkedIn + 50 emails con Instantly/Mailerlite gratis. 0$ en ads. Si quieres acelerar, $30 en ads a audiencia de dueños de agencias.

**Día 5 - Lectura**

### Coste y tiempo

* Tiempo: 1 día de setup + 3 días de outreach = 4 días hábiles.
* Dinero: Carrd $0 gratis / $19 año, dominio opcional. Stripe 0%. Total real: $0 - $30.

### Resultado que te hace abandonar YA

Mata la hipótesis si se cumple **cualquiera** de estos:

1. **Hard kill:** 0 depósitos/pagos tras 100 contactos cualificados. Si nadie saca la tarjeta, no hay mercado.
2. **Kill de precio:** >60% de respuestas dicen "caro", "lo hacemos con Data Studio/Notion gratis" o "ya tenemos a alguien que lo hace".
3. **Kill de interés:** <10% hace clic al demo y <5% pide info de precio. Es decir, 100 contactos -> <10 clics a landing.

Si consigues 3+ depósitos de $49 en 72h, la hipótesis sobrevive y puedes pasar a un concierge manual. Si no, no construyas nada.

Regla brutal: Si no hay dinero, no hay problema real. Los reportes son un dolor, pero no un dolor que paguen $200/mes.

¿Quieres que te escriba el copy exacto de la landing y el script de DM para copiar/pegar?