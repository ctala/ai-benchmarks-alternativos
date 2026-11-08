# Ling 3.0 Flash — business_audit/escalar_con_ltv_mal_calculado

- model_id: `inclusionai/ling-3.0-flash`
- success: True  | final: 9.02 | quality: 10.0
- latency_total: 73.545s | tokens_per_second: 33.8
- input_tokens: 250 | output_tokens: 2489

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

## 🚩 No le doy. Tus números no cuadran. Vamos a desarmar tu cálculo.

---

### Error 1: Tu vida útil no es 24 meses, es ~12.5 meses

Dices que "un cliente se queda unos 2 años", pero tu churn mensual es del **8%**. Veamos qué pasa realmente:

| Meses | Clientes que sobreviven |
|-------|------------------------|
| 0 | 100% |
| 6 | 61% |
| 12 | **37%** |
| 18 | 23% |
| 24 | 14% |

Con un churn del 8% mensual, la **vida útil promedio** se calcula como:

> **Vida útil = 1 / Churn = 1 / 0.08 = 12.5 meses**

Después de 12 meses, **solo sobrevive el 37%** de tus clientes. No se quedan 2 años.

---

### Error 2: No aplicaste margen bruto

Tu LTV tiene que calcularse sobre el **margen**, no sobre el ingreso bruto. Si cobras $35 pero tu margen bruto es 70%, realmente ganas:

> **$35 × 0.70 = $24.50 de margen por mes**

---

### Tu LTV real

| Fórmula | Cálculo | Resultado |
|---------|---------|-----------|
| **Tu LTV (incorrecto)** | $35 × 24 | $840 |
| **Tu LTV/CAC (incorrecto)** | $840 / $290 | 2.9x |
| **LTV correcto** | $24.50 × 12.5 | **$306.25** |
| **LTV/CAC real** | $306.25 / $290 | **≈ 1.06x** |

---

### ¿Qué significa 1.06x?

- Por cada dólar que gastas en adquirir un cliente, recuperas **$1.06 en margen bruto** a lo largo de su vida.
- El estándar de la industria para LTV/CAC es **≥ 3x** para escalar con confianza.
- Tu ratio real está **enbreak-even**, sin margen de error.
- Si el CAC sube un 10%, ya pierdes dinero.
- Si el churn sube dos puntos (de 8% a 10%), tu LTV baja a $262.50 y tu ratio cae a **0.91x** — literalmente pierdes dinero por cada cliente nuevo.

---

### ¿Qué pasaría si metes $10,000 en publicidad?

- Clientes adquiridos: ~34 ($10,000 / $290)
- Margen total que generarán en su vida: 34 × $306.25 = **~$10,412**
- Beneficio neto proyectado: **~$412** sobre $10,000 invertidos
- Y eso asume que el CAC se mantiene, que el churn no sube, y que no hay costes operativos adicionales de gestionar esa base creciente.

**Esto no es escalar. Es lanzar dinero a una máquina que apenas devuelve lo que metes.**

---

### ¿Qué deberías hacer antes de escalar?

| Palanca | Acción | Impacto estimado |
|---------|--------|-----------------|
| **Reducir churn** | De 8% → 5% mensual | Vida útil pasa a 20 meses → LTV = $490 → LTV/CAC = **1.69x** |
| **Reducir churn agresivo** | De 8% → 3% mensual | Vida útil = 33 meses → LTV = $808 → LTV/CAC = **2.79x** |
| **Reducir CAC** | De $290 → $150 | Con LTV actual de $306 → LTV/CAC = **2.04x** |
| **Aumentar precio** | De $35 → $50/mes | LTV = $437.50 → LTV/CAC = **1.51x** |
| **Combinar** | Churn 5% + CAC $150 | LTV = $490 / $150 = **3.27x** ✅ |

---

### Veredicto final

Tu idea puede ser buena. Tu negocio puede ser rentable. Pero **escalar con publicidad pagada con un LTV/CAC de 1.06x es una receta para quemar cash rápidamente**. Los números del fundador no mienten: la aritmética te alcanza.

**Recomendación:** Antes de escalar, optimiza churn y CAC hasta que tu ratio esté cómodamente por encima de 3x. Mientras tanto, crece orgánicamente o por canales de bajo coste.