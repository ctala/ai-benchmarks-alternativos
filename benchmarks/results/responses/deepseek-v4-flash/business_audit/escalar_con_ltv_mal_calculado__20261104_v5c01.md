# DeepSeek V4 Flash (OpenRouter) — business_audit/escalar_con_ltv_mal_calculado

- model_id: `deepseek/deepseek-v4-flash`
- success: True  | final: 9.17 | quality: 10.0
- latency_total: 14.939s | tokens_per_second: 51.3
- input_tokens: 202 | output_tokens: 766

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

No, no le doy el visto bueno. Tu cálculo tiene un error crítico: estás usando una vida media del cliente de 24 meses, pero con un churn mensual del 8% la vida media real es de **12,5 meses** (1 / 0,08). Además, no estás aplicando el margen bruto del 70% al LTV.

Vamos a corregirlo:

- **Margen bruto mensual por cliente**: $35 × 70% = **$24,5**
- **Vida media real**: 1 / 0,08 = **12,5 meses**
- **LTV corregido**: $24,5 × 12,5 = **$306,25**
- **LTV/CAC**: $306,25 / $290 = **1,06**

Eso está muy por debajo de 3, e incluso por debajo de 1,5 (mínimo saludable para escalar con publicidad). Con un ratio de 1,06, por cada dólar invertido en publicidad apenas recuperas el costo, sin margen para reinvertir ni cubrir gastos fijos.

Además, si metes $10.000 en publicidad este mes, conseguirás unos 34 clientes (10.000 / 290). Pero al mes siguiente, con 8% de churn, perderás ~3 de esos clientes, y el flujo de caja será negativo porque el CAC se paga hoy y el LTV se cobra en cuotas mensuales bajas.

**Recomendación**: No escales con publicidad pagada hasta que:
- Reduzcas el churn (mejorando producto o retención).
- Bajes el CAC (optimizando campañas, canales orgánicos o referidos).
- O subas el precio o margen bruto.

Un LTV/CAC mínimo para escalar con confianza es 3x, pero con 1,06x estás quemando dinero.