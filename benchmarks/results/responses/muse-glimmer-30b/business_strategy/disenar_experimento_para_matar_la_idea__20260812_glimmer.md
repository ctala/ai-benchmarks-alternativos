# Muse Glimmer 30B — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `meta/muse-glimmer-30b`
- success: True  | final: 7.39 | quality: 8.0
- latency_total: 19.29s | tokens_per_second: 112.1
- input_tokens: 181 | output_tokens: 2162
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil para un emprendedor, proporcionando un plan detallado y práctico para validar la hipótesis.

## Respuesta completa

Tu hipótesis a matar es: **Agencias pequeñas pagan $200/mes por automatización de reportes.**

No necesitas validar interés. Necesitas probar disposición a pagar real. El experimento más barato para matarla es una puerta falsa con pago real.

### Experimento: Pre-venta con demo falsa en 7 días

**Objetivo:** Conseguir 0 pagos reales. Si no pagan, la hipótesis muere.

**Métrica de muerte:** Menos de 3 agencias que paguen $200/mes o dejen tarjeta en Stripe después de ver la demo. O <2% de conversión de visita a pago con 500 visitas.

Si eso pasa, abandonas. No construyas nada.

#### Qué haces exactamente

**Día 1-2: Setup 3 horas**
1. **ICP:** Agencias de marketing de 2 a 10 personas, 5-20 clientes activos, usan Meta Ads / Google Ads / GA4. Foco en LATAM/España.
2. **Página de venta falsa:** Carrd $19/año + dominio opcional. 1 página con:
   * Headline: "Reportes de clientes automatizados en 1 clic. Sin Data Studio."
   * 3 screenshots mockeados en Figma de un dashboard con logo de cliente.
   * Video demo de 60s con Loom grabando la pantalla de Figma como si fuera la app.
   * Precio: $200/mes, facturación mensual. Botón "Activar prueba 7 días".
3. **Pago real:** Stripe Payment Link con $1 de prueba que requiere tarjeta válida. O mejor, $200 con trial de 7 días y cancelación inmediata. El pago es la prueba.

**Día 3-7: Tráfico barato**
Opción A - Ads $100:
* Meta Ads $10/día x 7 días. Audiencia: Intereses "Agencia de marketing digital", "Social Media Manager", cargo: Dueño/CEO, países AR/MX/CO/ES. Landing a la página.

Opción B - Gratis y más rápido:
* 150 mensajes directos personalizados en LinkedIn/Instagram a dueños de agencias. No spam.

Script DM:
"Hola [Nombre], vi que manejas [X] clientes. Estoy probando una herramienta que automatiza el reporte mensual de Meta/Google/GA4 y lo envía al cliente por email/WhatsApp sin tocar nada. Serían $200/mes. ¿Te interesa ver el demo de 60s y reservar un acceso?"

Si dice sí, le mandas el link a la landing con pago.

#### Costo y tiempo

* Carrd: $19
* Stripe: $0
* Ads: $70-100
* Tu tiempo: 4 horas setup + 30 min/día monitorear

**Total: $89 - $119. 7 días.**

#### Resultado que te hace abandonar

Mata la hipótesis SI:
* 0 pagos reales en 7 días con 500 visitas mínimo.
* <3 agencias aceptan dejar tarjeta tras ver el demo.
* >80% de las respuestas son objeción de precio: "caro", "ya lo hacemos gratis con Data Studio/Sheets".
* Tasa de conversión visita -> pago < 0.5%.

Si pasa eso, no es problema de producto, es problema de disposición a pagar. No construyas.

Si consigues 3+ pagos, ahí sí tienes señal para construir un concierge manual primero, no la app.

No necesitas más.