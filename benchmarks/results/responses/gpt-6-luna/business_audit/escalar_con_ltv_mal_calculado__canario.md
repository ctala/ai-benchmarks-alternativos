# GPT-6 Luna — business_audit/escalar_con_ltv_mal_calculado

- model_id: `openai/gpt-6-luna`
- success: True  | final: 9.26 | quality: 10.0
- latency_total: 7.627s | tokens_per_second: 112.5
- input_tokens: 186 | output_tokens: 858

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

**No escalaría fuerte con estos números.** El cálculo de LTV confunde la retención con la vida media y, además, usa ingresos en vez de margen bruto.

Con churn mensual constante del 8%:

- **Vida media estimada:** \(1 / 0,08 = 12,5\) meses, no 24.
- **LTV de ingresos:** \(35 / 0,08 = \$437,50\).
- **LTV de margen bruto:** \(\$437,50 \times 70\% = \$306,25\).
- **LTV/CAC:** \(\$306,25 / \$290 \approx 1,06\).

Eso apenas supera el punto de equilibrio **antes** de costos fijos, soporte, descuentos, devoluciones y costo del capital. Con el margen bruto actual, el CAC máximo para un ratio de 3:1 sería aproximadamente **\$102**.

Además, cada cliente genera unos **\$24,50 de margen bruto al mes**, así que recuperar un CAC de \$290 toma cerca de **11,8 meses**: casi toda la vida media estimada del cliente.

Invertir \$10.000 al CAC actual compraría unos 34 clientes, si el CAC se mantiene al escalar. No asumiría que se mantiene sin comprobarlo. **Primero probaría con un presupuesto limitado** y validaría el CAC y el margen de cohortes maduras; para escalar con más confianza, buscaría reducir el CAC, mejorar la retención o elevar el ingreso por cliente. Ser rentable como negocio no garantiza que esta campaña sea rentable por cliente.