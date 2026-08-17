# Claude Opus 5 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 5.77 | quality: 6.67
- latency_total: 29.619s | tokens_per_second: 69.1
- input_tokens: 295 | output_tokens: 2048

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

## Veredicto: no. El plan tiene tres errores que se multiplican.

Y el más chico de los tres es que 2,9 no está "por encima de 3".

---

### Error 1: la vida del cliente

Con churn mensual del 8%, la vida promedio es `1 / 0,08 = 12,5 meses`, no 24.

Verificación por supervivencia de cohorte:

| Mes | % de la cohorte que queda |
|---|---|
| 8 | 51% (vida **mediana** ≈ 8,3 meses) |
| 12 | 37% |
| 24 | **13,5%** |

Asumir "unos 2 años" implica un churn de ~4%, la mitad del real. Solo 1 de cada 7 clientes llega ahí.

### Error