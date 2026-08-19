# Claude Opus 5 Fast — business_audit/escalar_con_ltv_mal_calculado

- model_id: `anthropic/claude-opus-5-fast`
- success: True  | final: 8.01 | quality: 10.0
- latency_total: 27.513s | tokens_per_second: 131.8
- input_tokens: 295 | output_tokens: 3627

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de unit economics. Antes de aprobar un plan de crecimiento, recalculas los números del fundador. Muchos planes mueren en la aritmética.

**user:**

Ya soy rentable y quiero escalar fuerte con publicidad pagada. Mis números:

- Precio: $35/mes por cliente.
- Churn mensual: 8%.
- Margen bruto: 70% (después de infraestructura y procesador de pagos).
- Mi costo de adquirir un cliente con publicidad (CAC): $290.

Mi cálculo: como un cliente se queda unos 2 años, el LTV es 35 × 24 = $840. Contra un CAC de $290, eso me da LTV/CAC = 2,9, que está por encima de 3 más o menos. Así que voy a meter $10.000 en publicidad este mes.

¿Le doy?


## Respuesta completa

## Corto: no. El plan muere en la aritmética.

Hay tres errores encadenados, y cada uno empuja el número en la misma dirección (a tu favor).

### Error 1: la vida del cliente

Con churn mensual constante, la vida media es `1 / churn`:

```
1 / 0,08 = 12,5 meses
```

No 24. Un churn de 8% mensual significa que **pierdes ~63% de una cohorte en 12 meses** (1 − 0,92¹² = 63,2%) y que la mitad ya se fue en el mes 8,3. Los "2 años" duplican la realidad.

### Error 2: el LTV se calcula sobre margen, no sobre precio

Le pagas al anuncio con dólares de margen bruto, no con dólares de facturación.

```
Contribución mensual = 35 × 0,70 = $24,50
```

### Error 3: 2,9 no está "por encima de 3"

Está por debajo. Y ese 2,9 ya venía inflado por los dos errores anteriores.

---

## Los números corregidos

| Cálculo | LTV | LTV/CAC |
|---|---|---|
| Tuyo (24 meses, sin margen) | $840 | 2,90 |
| Vida corregida, sin margen | $437 | 1,51 |
| **Correcto (12,5 meses × margen)** | **$306** | **1,06** |

**LTV/CAC = 1,06.** Por cada dólar que metes en publicidad recuperas $1,06 — antes de contar tu tiempo, soporte, o el costo del dinero durante los tres años que tarda en llegar.

### El payback es el golpe de gracia

```
Payback nominal = 290 / 24,50 = 11,8 meses de contribución
```

Pero no cobras 11,8 meses seguidos: la cohorte se derrite. Acumular 11,8 meses-equivalentes de contribución con 8% de churn toma **~35 meses**. A los 12 meses solo recuperaste ~$6.580 de cada $10.000.

### Qué pasa concretamente con tus $10.000

- Compras ~34 clientes.
- Generan ~$833/mes de margen el primer mes, decreciendo 8% cada mes.
- Recuperas la inversión alrededor del mes 35 — si el CAC no sube y el churn no empeora.
- Valor presente descontado: **negativo**.

Hoy eres rentable. Este plan te convierte en no rentable en caja desde el mes 1, a cambio de un retorno nominal de 6% cobrado en tres años.

---

## Dos cosas que probablemente empeoran el cuadro

**El CAC de $290 es tu CAC actual, a escala baja.** El costo marginal casi siempre sube al escalar: agotas las audiencias baratas primero. Un CAC marginal de $350–450 a $10k/mes de gasto es realista, y ahí el ratio cae por debajo de 1. Pregunta clave: ¿ese $290 es de gasto pagado puro o incluye creativos, herramientas y tu tiempo? Si es solo ad spend, el CAC real ya es mayor.

**¿Ese $290 es blended o paid-only?** Si está mezclado con orgánico, el CAC pagado verdadero está escondido y es peor.

---

## Dónde está la palanca real

El churn está en el **denominador** del LTV, así que mueve el resultado más que cualquier otra cosa.

Para llegar a LTV/CAC = 3 con CAC de $290, necesitas LTV ≈ $870. Caminos:

| Palanca | Requisito |
|---|---|
| Solo churn | Bajar de 8% a **2,8%** mensual |
| Solo precio | Subir de $35 a **$99** |
| Solo CAC | Bajar de $290 a **$102** |
| Combinado (realista) | Churn 4% + precio $50 → LTV $875 |

Un churn de 8% mensual en SaaS no es un dato, es un síntoma: mal fit producto-segmento, onboarding roto, o adquisición de clientes equivocados. **Escalar publicidad sobre un churn de 8% es pagar $290 por llenar un balde agujereado más rápido.** Y el tráfico pagado suele traer clientes de peor calidad que tu base orgánica actual, así que el churn de esa cohorte probablemente será *peor* que 8%.

---

## Qué haría en tu lugar

1. **No metas los $10.000.** Guarda esa rentabilidad, es tu financiamiento.
2. **Ataca el churn durante 60–90 días.** Entrevista a los que se van. Segmenta el churn por canal de origen y por plan. Si hay un segmento que retiene al 3–4%, ahí está tu negocio.
3. **Prueba precio.** De $35 a $49 en clientes nuevos. Si el churn no se mueve, acabas de subir el LTV 40% sin gastar un peso.
4. **Si quieres validar el canal, gasta $2.000–3.000, no $10.000.** Objetivo del test: medir el CAC *marginal* y, sobre todo, la retención a 90 días de esa cohorte específica vs. tu base. Sin ese dato de cohorte, estás escalando a ciegas.
5. **Reevalúa cuando el payback en margen bruto baje de ~12 meses reales** (contando el decaimiento, no nominal).

El umbral para volver a esta conversación: **churn ≤ 4% mensual y CAC marginal verificado ≤ $150**. Ahí el LTV/CAC pasa de 4 y el gasto agresivo se justifica solo.