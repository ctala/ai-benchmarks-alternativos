# Kimi K2 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `moonshotai/kimi-k2`
- success: True  | final: 8.63 | quality: 10.0
- latency_total: 17.46s | tokens_per_second: 37.3
- input_tokens: 232 | output_tokens: 651

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

No le des. Tu cálculo tiene tres errores que convierten tu "rentabilidad" en quemar dinero.

---

## Error 1: El churn mata tu LTV real

Un churn del 8% mensual no da 24 meses. Da **12,5 meses** de vida promedio (1 ÷ 0,08).

**LTV real:** $35 × 12,5 × 0,70 = **$306**

Ya no es $840. Es menos que tu CAC de $290.

---

## Error 2: Estás usando LTV bruto, no de margen

Incluso si usaras tus 24 meses ficticios, el LTV relevante es el de margen: $840 × 0,70 = $588. Contra $290 de CAC, eso es 2,0x — no 2,9x.

Pero con el churn real: **LTV/CAC = 1,05x**

---

## Error 3: El "más o menos 3" es un piso, no un techo

Con churn alto y CAC pagado, necesitas márgenes de seguridad. A 8% mensual de churn, cualquier fluctuación (competencia, seasonality, fatiga de canal) te vuelve insostenible rápido.

---

## El escenario de tus $10,000

| Métrica | Tu cálculo | Realidad |
|--------|-----------|----------|
| Clientes adquiridos | ~34 | ~34 |
| Costo total | $10,000 | $10,000 |
| LTV generado | ~$28,560 | ~$10,404 |
| **Resultado** | "Gano $18,560" | **Pierdes $6,600** + costo de atención |

---

## ¿Qué necesitas antes de escalar?

| Variable | Tu número | Meta mínima |
|----------|-----------|-------------|
| Churn mensual | 8% | **< 5%** (ideal < 3%) |
| CAC pagado | $290 | **< $220** o LTV > $650 |
| LTV/CAC | ~1,0x | **> 3,0x** con margen real |

---

## Mi recomendación

**No metas los $10,000.** Primero:

1. **Reduce churn:** 8% mensual es una fuga. Entiende por qué se van a los 12 meses.
2. **Baja CAC:** Optimiza funnel, prueba canales orgánicos, mejora conversión.
3. **Sube precio o LTV expandible:** $35 con 70% margen deja poco margen de maniobra.

Con estos números, escalar es acelerar la quema. Quieres que recalcule escenarios con churn reducido o precio más alto?