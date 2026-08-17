# Claude Opus 4.8 (suscripción) — business_audit/escalar_con_ltv_mal_calculado

- model_id: `claude-opus-4-8`
- success: True  | final: 6.88 | quality: 8.4
- latency_total: 61.922s | tokens_per_second: 56.3
- input_tokens: 4 | output_tokens: 3488

## Respuesta completa

## No. La aritmética no da.

Hay tres errores encadenados y cada uno infla el resultado.

---

### Error 1: la vida del cliente

Con 8% de churn mensual, la vida promedio no son 24 meses. Es:

**1 / 0,08 = 12,5 meses**

Los 24 meses salieron de la intuición, no del churn. Verifícalo: con 8% mensual, al cabo de 12 meses te queda el **37%** de la cohorte (0,92¹²). A los 24 meses te queda el **13,5%**. La afirmación "se quedan unos 2 años" describe a 1 de cada 7 clientes, no al promedio.

### Error 2: LTV con revenue, no con margen

El LTV se calcula sobre **margen bruto**, no sobre precio de lista. Le pagaste a la infra y al procesador; ese dinero no es tuyo.

### Error 3: 2,9 no está "por encima de 3"

Está por debajo. Detalle menor comparado con lo anterior, pero es la clase de redondeo que aparece justo cuando uno quiere que el número funcione.

---

## Los números reales

| Concepto | Tu cálculo | Real |
|---|---|---|
| Vida del cliente | 24 meses | **12,5 meses** |
| Margen mensual/cliente | $35 | **$24,50** (35 × 0,70) |
| LTV | $840 | **$306** |
| CAC | $290 | $290 |
| **LTV/CAC** | **2,9** | **1,06** |
| **Payback** | — | **11,8 meses** |

**LTV/CAC = 1,06.** No es un negocio que escala con paid: es un negocio que recupera el CAC justo cuando el cliente se va. Recuperas $290 en 11,8 meses y el cliente promedio muere a los 12,5. Te quedas con $16 de margen por cliente. Eso no es crecimiento, es una transferencia de tu caja a Meta con un paso intermedio.

---

## Qué pasa si igual metes los $10.000

- Compras ~34 clientes.
- Generan ~$10.560 de margen bruto... **repartidos a lo largo de 12 meses**.
- Pagas los $10.000 hoy. Recuperas en un año. Ganas ~$560.
- Y eso asumiendo que el CAC se queda en $290. **No se queda.** El CAC de $290 es a tu volumen actual. Escalar 10x el gasto casi siempre lo sube 20-50% (agotas la audiencia barata). A CAC $350, tu LTV/CAC baja a **0,87**: pierdes dinero con cada cliente.

Estás siendo rentable *a pesar* del paid, no gracias a él. Escalar lo que no funciona solo lo rompe más rápido.

---

## Dos preguntas antes de seguir

1. **¿Ese CAC es por cliente PAGO o por registro?** Si estás midiendo un evento de alta gratuita y luego hay conversión free→paid, el CAC real es el que muestra tu dashboard dividido por la tasa de conversión. Con 20% de conversión free→paid, tu CAC real no es $290: es $1.450. Verifícalo antes que nada.
2. **¿El CAC está cargado completo?** Ad spend + creativos + herramientas + tu tiempo. Si solo es ad spend, el número real es más alto.

---

## Qué tendría que ser cierto para que dé

Dejando el CAC fijo en $290, para llegar a LTV/CAC = 3 necesitas:

**Churn ≤ 2,8% mensual.** (Hoy: 8%.)

O, dejando el churn fijo en 8%, necesitas:

**CAC ≤ $102.** (Hoy: $290.)

Cualquiera de los dos. No hay tercera salida en esta ecuación.

**El churn es la palanca dominante.** No es un problema de ads: es que el producto no retiene. Bajar el churn de 8% a 4% duplica la vida del cliente y te lleva a LTV/CAC = 2,1 sin tocar un dólar de publicidad. A 3% llegas a 2,8. Ninguna optimización de creativos te va a dar ese multiplicador.

---

## Qué haría con los $10.000

1. **No los metas en paid.** Todavía.
2. **Analiza la cohorte de churn por mes de vida.** El 8% promedio casi nunca es plano: normalmente es 15-20% en los meses 1-3 y luego se aplana. Si tu problema es onboarding, se arregla; si es abandono a los 8 meses, es problema de valor y es más caro.
3. **Empuja el plan anual con prepago.** Cobrar $249 por adelantado no solo mejora el churn estructural (el que paga anual no cancela en el mes 3): elimina el agujero de capital de trabajo. En vez de financiar 12 meses de payback, cobras hoy.
4. **Si igual quieres testear paid, hazlo con $1.500 y tracking de cohorte**, no con $10.000 a ciegas. Mide free→paid y retención a 60 días de esos clientes específicos. Los clientes de paid frío suelen retener peor que los orgánicos, lo que empeora todavía más el número.

Cuando el churn esté en 3-4% y el CAC bajo $150, vuelves y escalas. Ahí el motor sí funciona y los $10.000 se convierten en $30.000. Hoy se convierten en $10.560 dentro de un año.