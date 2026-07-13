# Claude Opus 4.8 (suscripción) — business_audit/churn_mezcla_free_y_pago

- model_id: `claude-opus-4-8`
- success: True  | final: 5.93 | quality: 7.2
- latency_total: 56.218s | tokens_per_second: 49.8
- input_tokens: 4 | output_tokens: 2802

## Respuesta completa

## Corto: el 31% no es tu churn. Es el churn de gente que nunca te pagó.

Tu panel está sumando dos poblaciones distintas y reportando el promedio como si fuera una sola cosa. Separémoslas:

| Población | Base inicio | Bajas | Churn real |
|---|---|---|---|
| Free | 178 | 60 | **33.7%** |
| Pago | 22 | 2 | **9.1%** |
| Blended (lo que reporta el panel) | 200 | 62 | 31% |

El 89% de tu base es free. Por eso el "churn de la plataforma" es, matemáticamente, casi el churn del plan gratuito con otro nombre. El número de pago —el único que toca tu caja— ni siquiera mueve la aguja del promedio.

## Y ahora la parte que te va a bajar la adrenalina

Tienes **2 bajas sobre 22 pagos**. Eso no es una señal, es ruido.

Si tu churn real fuera exactamente el 5% que creías, esperarías ~1.1 bajas al mes. La probabilidad de ver 2 o más bajas *aunque nada haya cambiado* es de ~30%. Es decir: 1 de cada 3 meses "malos" son simple azar.

El intervalo de confianza de 2/22 va aproximadamente de **2.5% a 28%**. Con esa muestra no puedes distinguir un churn de 5% de uno de 15%. No tienes evidencia de que algo se rompió. Tampoco tienes evidencia de que estés en 5%. Tienes una muestra demasiado chica para afirmar cualquiera de las dos cosas.

**Gravedad real: baja para revenue, media-alta para tu instrumentación.** El problema no es el churn. El problema es que tu panel te mintió y casi tomas una decisión de pánico con eso.

## Lo que sí falta y no me diste

1. **Churn de ingresos (gross MRR churn).** ¿Cuánto MRR se fue con esos 2 vs. tu MRR total? Si uno era tu cuenta más grande, tu churn de revenue puede ser 20%+ aunque el churn de logos sea 9%. Si eran los dos más chicos, es 3%. Son historias opuestas y ahora mismo no sabes cuál vives.
2. **¿Qué significa "baja" en el plan free?** ¿Cancelaron activamente o el sistema los marcó por inactividad? Si es lo segundo, no es churn: es que nunca activaron.
3. **Fecha de registro de esos 60.** Si la mayoría se registró hace <30 días y nunca completaron la acción core, no tienes un problema de retención sino de **activación/onboarding**. Es otro problema, con otro dueño y otra solución.

## Plan

**Esta semana**
- Mata la métrica "churn" del panel. Reemplázala por tres: `churn_free`, `churn_paid_logos`, `churn_mrr_bruto`. Que nunca más se promedien.
- Calcula el MRR churn de este mes. Es el número que define si esto es una anécdota o un incendio.
- Segmenta los 60 free entre "activó y se fue" vs "nunca activó". Es la línea que separa problema de retención de problema de onboarding.

**Próximas 2 semanas**
- Llama a los 2 que se fueron. Con n=22, cada cliente es el 4.5% de tu negocio; una llamada te da más información que el panel completo.
- Arma una tabla de cohortes de pago por mes de alta, con 3-6 meses hacia atrás. Recién ahí vas a poder decir si tu churn es 5% o 12%. Un mes suelto no lo puede responder.

**Lo que NO hagas ahora**
- No rediseñes el producto, no bajes precios, no lances una campaña de "win-back" y no dispares descuentos de retención. Cualquiera de esas cosas basada en 2 datos es tirar dinero contra el ruido.

## La conclusión incómoda

Tu problema no es un churn del 31%. Es que 178 de 200 usuarios están en free y solo 22 pagan. El cuello no es retención: es conversión free→paid. Ese 33.7% de churn gratuito te está diciendo que la gente entra, no encuentra el valor y se va antes de llegar a la caja.

Ese es el número al que le tengo que ver miedo. No al del panel.