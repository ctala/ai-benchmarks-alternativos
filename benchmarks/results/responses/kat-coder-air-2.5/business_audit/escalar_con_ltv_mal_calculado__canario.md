# KAT Coder Air v2.5 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `kwaipilot/kat-coder-air-v2.5`
- success: True  | final: 9.13 | quality: 10.0
- latency_total: 7.225s | tokens_per_second: 190.9
- input_tokens: 217 | output_tokens: 1379

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

## Error 1: El LTV que calculaste no existe

Dijiste *"como un cliente se queda unos 2 años"*. **Eso no es cierto con 8% de churn mensual.**

| Concepto | Tu cálculo | Realidad |
|---|---|---|
| Vida promedio del cliente | 24 meses | **12.5 meses** (1 / 8%) |
| Margen bruto aplicado | No | **70%** |
| **LTV real** | $840 | **$306** |

**LTV correcto:** $35 × 12.5 × 70% = **$306**

## Error 2: El LTV/CAC no es 2.9

| Métrica | Tu número | Real |
|---|---|---|
| LTV | $840 | $306 |
| CAC | $290 | $290 |
| **LTV/CAC** | **2.9** | **1.06** |

Con LTV/CAC = 1.06, **estás recuperando apenas lo que inviertes**. Y eso es antes de considerar:

- Costos operativos (soporte, equipo, herramientas)
- El gap de caja: pagas los $10,000 de ads **hoy**, pero el ingreso llega mes a mes
- Si el churn se acelera en el camino, el LTV baja aún más

## Escenario real con $10,000 de ads

| | |
|---|---|
| Nuevos clientes | ~34 |
| Ingreso bruto mes 1 | $1,190 |
| Margen bruto mes 1 | $833 |
| **Cash flow neto mes 1** | **-$9,167** |

Vas a perder casi $10K este mes esperando recuperar $306 por cliente a lo largo de 12.5 meses.

## Qué necesitas para que esto funcione

| Variable | Necesitas |
|---|---|
| CAC máximo | **~$150** (para LTV/CAC = 2) |
| O churn máximo | **~4%** (para que LTV suba a ~$612) |
| O precio mínimo | **~$55/mes** (con churn actual) |

## Recomendación

**No metas los $10,000.** Primero:

1. **Baja el CAC** a $150 o menos (mejora tu creative, targeting, landing)
2. **O reduce el churn** a 4% (mejora onboarding, producto)
3. Cuando LTV/CAC ≥ 3, **ahí sí** escala agresivo

¿Quieres que calculemos cuánto podrías invertir de forma segura con los números actuales?