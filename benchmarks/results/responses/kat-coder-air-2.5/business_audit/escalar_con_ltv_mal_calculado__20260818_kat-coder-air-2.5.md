# KAT Coder Air v2.5 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `kwaipilot/kat-coder-air-v2.5`
- success: True  | final: 9.19 | quality: 10.0
- latency_total: 5.514s | tokens_per_second: 185.3
- input_tokens: 217 | output_tokens: 1022

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



# No. Tu aritmética tiene dos errores graves.

## Error 1: El LTV no es precio × meses

Con un churn del 8% mensual, la vida media del cliente es **1/0.08 = 12.5 meses**, no 24. Y el LTV se calcula con el **margen bruto**, no con el ingreso bruto.

| Tu cálculo | Real |
|---|---|
| LTV = $35 × 24 = **$840** | LTV = ($35 × 70%) / 0.08 = **$306** |

## Error 2: El LTV/CAC real

$$LTV/CAC = \frac{306}{290} = \mathbf{1.06}$$

No 2.9. **Estás prácticamente en el punto de equilibrio.**

## Qué significa esto en la práctica

Si metes $10,000 en publicidad:
- Adquieres ~34 clientes ($10,000 / $290)
- Cada uno te genera ~$306 de margen a lo largo de su vida
- Ingreso total por esos 34 clientes: ~$10,404
- Menos el CAC: **$404 de ganancia neta en 12.5 meses**

Eso es un ROI del **4%**. No escala. Se pierde.

## Qué necesitas para que esto funcione

| Variable | Tu número | Mínimo viable (LTV/CAC ≥ 3) |
|---|---|---|
| CAC | $290 | **<$102** |
| Precio | $35/mes | **≥$96/mes** |
| Churn | 8%/mes | **≤2.9%/mes** |
| Margen | 70% | **≥70%** (ya bien) |

Cualquier combinación que te acerque a esos números funciona. Reducir el CAC a $100 sería lo más realista si tu producto ya es rentable.

**¿Quieres que revisemos cómo bajar ese CAC o si hay margen para subir precio?**