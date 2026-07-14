# Claude Sonnet 4.6 (ultimo Anthropic) — business_audit/retention_sobre_100_interpretacion

- model_id: `anthropic/claude-sonnet-4-6`
- success: True  | final: 6.86 | quality: 8.0
- latency_total: 16.27s | tokens_per_second: 42.6
- input_tokens: 170 | output_tokens: 693
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente útil, proporcionando una comprensión completa de la métrica NRR y sus implicaciones para la retención de clientes.

## Respuesta completa

## Tu lectura es incorrecta en un punto crítico

Vamos por partes, porque estás mezclando dos métricas distintas.

---

### Qué mide realmente el 114%

Ese número es **Net Revenue Retention (NRR)** o Retención Neta de Ingresos. Mide si los ingresos de tu cohorte existente crecen o decrecen, combinando tres factores:

- Ingresos perdidos por cancelaciones (churn)
- Ingresos perdidos por downgrades
- Ingresos ganados por upgrades y expansión

El 114% significa que **los upgrades compensan con creces las cancelaciones en términos de dinero**. Es una métrica excelente.

---

### El problema con tu conclusión

Tu contexto lo deja claro: **pasaste de 40 a 36 clientes**. Eso es un **10% de churn de clientes** en un mes, lo cual es alto.

Lo que ocurre es que los upgrades de los que se quedaron generan más ingresos que los que se fueron, por eso el NRR sale positivo. Pero los clientes sí se están yendo.

| Lo que mide el 114% | Lo que NO mide |
|---|---|
| Salud de ingresos de clientes existentes | Cuántos clientes abandonan |
| Expansión por upgrades | Por qué se van los que se van |
| Compensación neta en euros | Si el patrón de fuga es sostenible |

---

### Por qué sería un error dejar de mirar el churn

**Primero**, perder 4 clientes al mes sobre una base de 40 es una tasa que, sostenida, vacía tu base en menos de un año aunque el NRR sea positivo.

**Segundo**, el NRR alto puede estar enmascarando una dependencia peligrosa: si tus upgrades vienen de pocos clientes grandes, la concentración de riesgo aumenta.

**Tercero**, los clientes que se van te dicen algo sobre tu producto o tu mercado que los que se quedan y expanden no te dicen.

---

### Qué deberías hacer

Celebra el NRR, es una señal real de valor. Pero investiga el churn de clientes en paralelo:

- ¿Quiénes son los 4 que se fueron?
- ¿Tienen algo en común: tamaño, sector, tiempo como clientes, plan contratado?
- ¿Se fueron antes de tener oportunidad de hacer upgrade o justo después?

Un NRR del 114% con churn del 10% mensual no es un negocio tranquilo. Es un negocio que corre para quedarse en el mismo sitio.