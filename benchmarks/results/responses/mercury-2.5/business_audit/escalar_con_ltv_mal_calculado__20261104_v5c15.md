# Mercury 2.5 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `inception/mercury-2.5`
- success: True  | final: 9.3 | quality: 10.0
- latency_total: 5.834s | tokens_per_second: 401.1
- input_tokens: 223 | output_tokens: 2340

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



No apruebo el plan. La aritmética actual es peligrosa.

Hay dos errores críticos en tu modelo:

1.  **Duración:** Con 8% de churn mensual, la vida promedio es 12.5 meses (1/0.08), no 2 años.
2.  **Margen:** El valor real es el margen, no el precio. Contribución mensual = $35 × 70% = $24.50.

**Recálculo:**
*   Valor total del cliente (LTV) = $24.50 × 12.5 = $306.
*   Ratio LTV/CAC = $306 / $290 ≈ 1.06.

Esto significa que apenas recuperas la inversión al adquirir al cliente. Dado que el tiempo de retorno es de casi 12 meses, muchos se irán antes de llegar ahí. Escalar con esto quemará caja.

**Sugerencia:** Baja el churn o el CAC antes de invertir. Necesitas un ratio superior a 3 para escalar seguro.