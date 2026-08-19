# Grok 4.20 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `x-ai/grok-4.20`
- success: True  | final: 8.01 | quality: 8.4
- latency_total: 4.409s | tokens_per_second: 124.5
- input_tokens: 363 | output_tokens: 549

## Respuesta completa

**No. No le des. Tu plan tiene un problema grave de aritmética.**

Vamos a recalcularlo correctamente (con los números reales que me diste):

### 1. Cálculo correcto del LTV

- Precio: $35/mes
- Churn mensual: **8%** → Retention mensual = 92%
- Life expectancy (meses) = 1 / 0.08 = **12.5 meses** (no 24)
- LTV bruto (sin margen) = 35 × 12.5 = **$437.5**
- LTV neto (con 70% margen bruto) = 437.5 × 0.7 = **$306.25**

### 2. Ratios reales

| Métrica              | Tu cálculo | Cálculo correcto |
|----------------------|------------|------------------|
| LTV (neto)           | $840       | **$306**         |
| LTV/CAC              | 2.9x       | **1.06x**        |
| Payback period       | ~8 meses   | **12.4 meses**   |

### 3. Conclusión clara

**Estás perdiendo dinero con cada cliente que adquieres vía paid.**

- Pagas $290 para adquirir un cliente
- Generas solo ~$306 de margen bruto a lo largo de toda su vida
- Tu payback es de más de 12 meses (demasiado lento para paid ads)

### Regla rápida que uso como analista:

Para escalar fuerte con **publicidad pagada** (Meta/Google), normalmente quiero ver:

- LTV/CAC ≥ **3.0x** (idealmente >3.5x)
- Payback period ≤ **6 meses** (máximo 8-9 meses si el capital es muy barato)

Tú estás en **1.06x** y **12.4 meses**. Es uno de los peores casos que veo.

---

### Qué tienes que hacer antes de meter $10k:

1. **Bajar el churn** drásticamente (idealmente a 3-4% mensual).
2. Subir el precio (a $49 o $59) o añadir un plan anual con descuento.
3. Mejorar el margen bruto si es posible.
4. Probar a bajar el CAC (creatives, audiences, offer, landing).

**Con los números actuales, cada dólar que metas en ads te está destruyendo valor.**

¿Quieres que te arme el modelo completo con sensibilidad (qué churn y qué precio necesitas para poder escalar seguro)? Te lo armo en 30 segundos.