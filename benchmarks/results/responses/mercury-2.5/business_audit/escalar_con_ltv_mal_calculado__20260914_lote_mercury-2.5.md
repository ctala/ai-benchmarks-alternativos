# Mercury 2.5 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `inception/mercury-2.5`
- success: True  | final: 9.27 | quality: 10.0
- latency_total: 5.394s | tokens_per_second: 504.3
- input_tokens: 225 | output_tokens: 2720

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



No apruebo el plan. La matemática actual es riesgosa:

1. **Suposición de vida:** Con un churn del 8% mensual, la vida promedio del cliente es de 12.5 meses (1 ÷ 0.08), no 24. Asumir 2 años infla el LTV artificialmente.
2. **LTV real:** El LTV debe basarse en la contribución de margen, no en el ingreso bruto.
   - Aporte mensual real: $35 × 70% = $24.50.
   - LTV estimado: $24.50 × 12.5 meses ≈ $306.
3. **Viabilidad:** Tu ratio LTV/CAC real es ~1.05. En el negocio, buscas mínimo 3. Además, recuperar el CAC de $290 toma casi 12 meses.

Con ese churn, más de la mitad de los clientes se irán antes de pagar por sí mismos. Meter capital en publicidad ahora quema efectivo.

**Recomendación:** Pausa el gasto. Mejora la retención o reduce el CAC. Solo aprueba el escalamiento cuando tengas un periodo de recuperación menor a 9 meses y un ratio sólido.