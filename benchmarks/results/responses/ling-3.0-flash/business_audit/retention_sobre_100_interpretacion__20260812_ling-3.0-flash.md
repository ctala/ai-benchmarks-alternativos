# Ling 3.0 Flash — business_audit/retention_sobre_100_interpretacion

- model_id: `inclusionai/ling-3.0-flash`
- success: True  | final: 9.55 | quality: 10.0
- latency_total: 4.873s | tokens_per_second: 316.0
- input_tokens: 165 | output_tokens: 1540
- judge_score: 5.0 | justificación: 

## Respuesta completa

No, ninguna de las dos conclusiones es correcta. Y la segunda es, de hecho, la más peligrosa de las dos.

---

## Qué mide realmente el 114%

Ese número es **Net Revenue Retention (NRR)**, no Retención de Clientes. Mide si los clientes que *ya estaban* te generan más o menos dinero que el mes pasado. Incluye:

- Lo que se quedó (ingresos de los clientes que no se fueron)
- Lo que subieron (upsell, cross-sell, upgrades de plan)
- Menos lo que se fue (churn)

Un NRR del 114% significa que por cada $100 que tenías con tu base existente, ahora tienes $114. Esa expansión compensa y supera las pérdidas.

---

## Qué NO te dice el 114%

### 1. La retención de clientes no es 114%
Pasaste de 40 a 36 clientes de pago. Eso es **90% de retención de clientes**, no 114%. Se fueron 4 personas. El 114% es un promedio ponderado por ingresos, así que si los que se fueron estaban en planes bajos y los que subieron en planes altos, el balance de dinero se ve bien aunque la base de clientes se esté erosionando.

### 2. Sí se te está yendo gente
Tasa de churn mensual: **10%** (4 de 40). En SaaS, un churn mensual sostenido del 10% es alto. A ese ritmo, en un año pierdes la mayoría de tu base si no la renuevas constantemente.

### 3. El 114% puede esconder una bomba de tiempo
Tu NRR actual depende de que la expansión siga compensando las pérdidas. Si:
- Los upgrades fueron puntuales (ej: alguien pagó 6 meses por adelantado)
- Los nuevos planes tienen descuentos de lanzamiento que caducan
- El mercado se enfría y la gente deja de querer subir de plan

...ese 114% puede convertirse en un 85% o un 70% de la noche a la mañana.

---

## La lectura correcta de tu panel

| Métrica | Valor | Qué significa |
|---|---|---|
| **NRR (Net Revenue Retention)** | 114% | Tu base existente genera más dinero que antes |
| **Retención de clientes** | 90% | Perdiste el 10% de tus clientes este mes |
| **Churn mensual** | 10% | Alto. Necesitas investigar por qué se van |

---

## Qué deberías hacer

- **No dejar de preocuparte por el churn.** El churn es una de las métricas más importantes de un SaaS, y el 10% mensual merece investigación urgente: ¿se van de un segmento? ¿Hay un patrón en quién cancela? ¿El producto cumple la promesa para todos los perfiles?
- **No redirigir todo el esfuerzo a captación nueva.** Si gastas en adquisición mientras pierdes clientes existentes, estás corriendo en una rueda. Cada cliente nuevo cuesta entre 5x y 25x retener uno existente.
- **Separar las métricas en el panel.** Mide NRR y retención de clientes como indicadores distintos. Uno te dice si la economía funciona; el otro te dice si el negocio es sostenible.

El 114% es una buena noticia, pero solo cuenta la mitad de la historia. La otra mitad —los 4 clientes que se fueron— te está diciendo algo que el panel no te está mostrando claramente.