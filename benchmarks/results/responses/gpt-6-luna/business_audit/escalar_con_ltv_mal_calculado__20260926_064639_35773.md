# GPT-6 Luna — business_audit/escalar_con_ltv_mal_calculado

- model_id: `openai/gpt-6-luna`
- success: True  | final: 9.01 | quality: 10.0
- latency_total: 16.902s | tokens_per_second: 123.3
- input_tokens: 186 | output_tokens: 2084

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

**No metería los $10.000 de golpe con estos números.** El cálculo de LTV mezcla ingresos con duración y no descuenta el margen bruto.

Con un churn mensual constante del 8%:

- **Vida media esperada:** \(1 / 0,08 = 12,5\) meses, no 24. Solo cerca del **13,5%** de los clientes seguiría activo al mes 24.
- **LTV de ingresos:** \(35 / 0,08 = \$437,50\).
- **LTV de margen bruto:** \(\$437,50 \times 70\% = \$306,25\).
- **LTV de margen bruto / CAC:** \(\$306,25 / \$290 = 1,06\), no 2,9.

Eso deja apenas **$16,25 de margen bruto esperado por cliente** después de recuperar el CAC, antes de gastos fijos, descuentos, coste del capital o cualquier deterioro del CAC al escalar. Con $10.000 de gasto comprarías unos 34 clientes y esperarías solo alrededor de **$560 de contribución total** a lo largo de toda su vida, bajo esos supuestos.

Además, aunque el payback simple de un cliente que permanece activo sería \(290 / (35 \times 70\%) \approx 11,8\) meses, ese cálculo ignora el churn. Al incorporar la retención, la contribución acumulada esperada de la cohorte tardaría unos **35–36 meses** en recuperar el CAC; para entonces quedaría activo alrededor del 5% de los clientes.

**Mi recomendación:** no escales fuerte todavía. Valida el churn de las cohortes adquiridas por pago y el CAC marginal con una prueba limitada, aumentando el presupuesto por etapas y fijando un límite de pérdida. Ser rentable hoy no demuestra que la próxima tanda de clientes pagados también lo será.