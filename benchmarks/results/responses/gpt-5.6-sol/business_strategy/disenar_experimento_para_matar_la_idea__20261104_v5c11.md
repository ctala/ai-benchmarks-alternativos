# GPT-5.6 Sol — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `openai/gpt-5.6-sol`
- success: True  | final: 6.83 | quality: 8.0
- latency_total: 34.082s | tokens_per_second: 79.0
- input_tokens: 167 | output_tokens: 2694

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un fundador experimentado. Sabes que el objetivo de un experimento no es tener razón: es descubrir rápido y barato que estás equivocado. Diseñas tests que pueden FALLAR de forma concluyente.

**user:**

Mi hipótesis: las agencias de marketing pequeñas pagarían $200/mes por una herramienta que les automatice los reportes a clientes.

Estoy a punto de meterme 2 meses a construirla. Antes de eso, diséñame el experimento **más barato y más rápido** que pueda MATAR esta hipótesis.

No quiero validarla. Quiero saber, en el menor tiempo y plata posible, si estoy equivocado. Dime exactamente qué hago, cuánto me cuesta, cuánto tarda, y cuál sería el resultado que me hace abandonar la idea.


## Respuesta completa

## Hipótesis falsable

Tu hipótesis actual es demasiado vaga. La convertiría en:

> “Al menos el 10% de las agencias de marketing de 2–20 empleados, con 5 o más clientes recurrentes y que hoy preparan reportes mensuales manualmente, pagará $200/mes para automatizarlos.”

No medirás interés, encuestas ni reuniones. **Solo pagos reales.**

## Experimento: vender antes de construir

Ofrece un piloto de pago que inicialmente cumplirás de forma manual. El cliente compra el resultado; no necesitas construir el software para comprobar disposición a pagar.

### Oferta exacta

> Reportes mensuales white-label para hasta 10 clientes, usando GA4, Google Ads y Meta Ads. Incluye plantilla con tu marca, actualización automática y envío programado.  
> **Precio: $200/mes, cobrado hoy. Sin contrato; cancelable mensualmente. Primer reporte en 7 días.**

Sé transparente: es un piloto y parte del proceso puede ser manual durante las primeras semanas. No ofrezcas descuento ni prueba gratis. Puedes garantizar devolución si no entregas el primer reporte.

---

## Qué hacer

### Día 1: prepara solo tres cosas

1. **Un reporte de muestra**
   - Hazlo en Canva, Google Slides o Looker Studio.
   - Usa datos ficticios.
   - Tiempo máximo: 2 horas.

2. **Un video de 90 segundos**
   - Muestra el reporte.
   - Explica que conecta las fuentes, aplica branding y programa el envío.
   - No necesitas prototipo interactivo.

3. **Un enlace de pago**
   - Stripe Payment Link por una suscripción real de $200/mes.
   - La tarjeta se cobra inmediatamente.
   - Nada de “reserva tu plaza” sin pago.

No construyas una web completa. Un documento de Notion o una página gratuita es suficiente.

### Días 2–5: haz 30 ofertas reales

Crea primero una lista cerrada de agencias para evitar escoger solo a quienes parezcan receptivos.

Deben cumplir:

- 2–20 empleados.
- 5 o más clientes recurrentes.
- Envían reportes mensualmente.
- Usan al menos dos de estas fuentes: GA4, Google Ads o Meta Ads.
- Hablas con el dueño o con quien puede autorizar una compra de $200.

Contacta por teléfono, LinkedIn y email. Tu objetivo no son 30 mensajes enviados, sino **30 conversaciones con decisores cualificados en las que presentes precio y pidas el pago**.

Guion:

> “Estoy probando un servicio para agencias que genera y envía reportes white-label para hasta 10 clientes. Incluye GA4, Google Ads y Meta, cuesta $200 al mes y el primer reporte se entrega en 7 días. Estoy aceptando cinco agencias para el piloto. Si esto te resuelve el problema, ¿lo contratarías hoy? Puedo enviarte ahora el enlace de pago.”

Si responde “me interesa”, contesta:

> “Perfecto. Para contar como participante del piloto necesito activar la suscripción de $200. ¿Te envío el enlace?”

No cuentes como venta:

- “Me interesa”.
- “Hablemos más adelante”.
- Una carta de intención.
- Una prueba gratuita.
- Una reunión agendada.
- Alguien que pagaría solo por $50.
- Alguien que exige funciones personalizadas antes de pagar.

Cuenta únicamente:

1. Pago de $200 realizado.
2. Inicio del onboarding o entrega de accesos dentro de 48 horas.

---

## Coste y duración

| Concepto | Coste |
|---|---:|
| Canva, Notion, Loom y Calendly gratuitos | $0 |
| Stripe | $0 por adelantado; comisión solo si vendes |
| Listado manual desde Google Maps/LinkedIn | $0 |
| Dominio, opcional | $10–15 |
| **Total** | **$0–30** |

Tiempo:

- Preparación: 3–4 horas.
- Crear lista y contactar: 8–12 horas.
- Conversaciones: 5–8 horas.
- **Duración total: 4–7 días.**

## Resultado que mata la hipótesis

> **Si 0 de 30 decisores cualificados paga $200 después de recibir una oferta clara, abandona la idea en su forma actual.**

Con 0 pagos de 30, el límite superior aproximado de la tasa de compra es 9,5% con un 95% de confianza. Eso contradice la hipótesis operacionalizada de que al menos un 10% compraría.

Interpretación adicional:

- **0/30:** mata la hipótesis; no construyas.
- **1–2/30:** evidencia débil; tampoco justifica dos meses de desarrollo. Solo continúa si consigues más pagos con otra muestra, sin cambiar precio ni añadir personalización.
- **3+/30:** no prueba todavía que haya un negocio escalable, pero sí justifica cumplir manualmente durante un mes y observar retención.
- **Pagos seguidos de negativa a dar accesos:** no cuentan; probablemente compraron por impulso o cortesía.

La regla fundamental: **no cambies la oferta a mitad del experimento**. Si bajas el precio, añades servicios a medida o aceptas promesas en vez de dinero, ya no estás probando la hipótesis de $200/mes.