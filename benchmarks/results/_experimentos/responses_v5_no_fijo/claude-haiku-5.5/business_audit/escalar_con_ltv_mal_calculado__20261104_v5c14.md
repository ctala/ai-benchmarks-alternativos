# Claude Haiku 5.5 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 8.99 | quality: 10.0
- latency_total: 12.361s | tokens_per_second: 186.6
- input_tokens: 297 | output_tokens: 2306

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

**No le des. Con estos números, cada cliente que compres por publicidad apenas se paga a sí mismo, y escalar amplifica la pérdida de caja.** Hay dos errores en el cálculo.

**1. La vida del cliente no es 24 meses.** Con 8% de churn mensual, la duración promedio es 1 / 0,08 = **12,5 meses**, no 24. Los 24 meses implicarían un churn de ~4,2%.

**2. El LTV usa ingreso, no margen.** Como el margen bruto es 70%, cada cliente aporta $35 × 0,70 = **$24,50 al mes**.

Recalculado:

- **LTV (margen bruto)** = 24,50 × 12,5 ≈ **$306**
- **LTV/CAC** = 306 / 290 ≈ **1,06**, no 2,9
- **Payback** (ajustado por churn, es decir, cuándo la cohorte completa recupera el CAC): ≈ **35 meses**. Con 290 de CAC y 8% de churn, la cohorte acumula ~$306 de margen en total, así que casi no hay excedente.

**Qué significa con $10.000:**

- Compras ~34 clientes.
- Esa cohorte genera en total unos $10.400 de margen bruto a lo largo de su vida, repartidos en ~3 años.
- Resultado neto esperado: **+$400 en 3 años, antes de costos fijos, impuestos y del costo del dinero**. Es un capital atado durante años para casi ningún retorno.
- Además, el CAC casi nunca se mantiene al escalar: la audiencia más barata se agota primero, así que el CAC marginal sube. Con más gasto, la cohorte queda en negativo.

**Qué tendría que ser verdad para escalar (LTV/CAC ≥ 3 y payback < 12 meses):**

- **Churn** de ~2,8% con CAC de 290 (LTV ≈ 870), o
- **CAC** de ~$100 con el churn actual (LTV ≈ 306), o
- **Precio** más alto o mejor margen. Si el precio sube a ~$55 con el mismo churn y CAC, el LTV pasa de ~306 a ~480: ya ayuda, pero aún no alcanza 3x.

**Lo que haría antes de los $10.000:**

1. **Recalcular el CAC con costo total:** incluye el tiempo del equipo, herramientas y creativos, no solo el gasto en anuncios. Y mide el CAC *incremental* al subir la inversión, no solo el promedio.
2. **Atacar el churn.** 8% mensual es alto para $35/mes. Analiza por qué se van (¿onboarding, precio, producto, cliente equivocado?). Reducirlo a la mitad vale más que cualquier campaña.
3. **Probar con $1.000–2.000** en segmentos distintos y medir CAC y retención de esa cohorte a 60–90 días.
4. **Considerar subir precio** con una prueba A/B. Con margen de 70%, un aumento pequeño tiene mucho efecto.

Si me pasas cómo calculas el CAC (qué gastos incluye, si es blended o solo pagado) y la retención por cohorte de los últimos 6 meses, puedo revisar si el 8% es el churn real o si está inflado por clientes de prueba o de un canal específico.