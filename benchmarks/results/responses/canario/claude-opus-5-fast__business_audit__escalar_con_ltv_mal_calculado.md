# Claude Opus 5 Fast — business_audit/escalar_con_ltv_mal_calculado

- model_id: `anthropic/claude-opus-5-fast`
- success: True  | final: 5.78 | quality: 6.67
- latency_total: 11.984s | tokens_per_second: 170.9
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

## Veredicto: no. La aritmética no cierra.

Hay tres errores encadenados, y cada uno empuja en la misma dirección (hacia arriba).

---

### Error 1: la vida del cliente

Con churn mensual del 8%, la vida promedio es **1/0,08 = 12,5 meses**, no 24.

Para que un cliente dure 24 meses necesitarías un churn de ~4,2%. Estás asumiendo la mitad del churn que realmente tienes.

Comprobación de cohorte: 0,92^12 = **36,8%** sobrevive al año. 0,92^24 = **13,5%** a los dos años. No es que "un cliente se queda unos 2 años"; es que 1 de cada 7 llega ahí.

### Error 2: LTV sobre ingreso, no sobre margen

El LTV se calcula con margen bruto. Tu cliente no te deja $35/mes, te deja **$24,50/mes**.

### Error 3: 2,9 no está por encima de 3

Es menor