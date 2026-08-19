# KAT Coder Pro v2.5 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `kwaipilot/kat-coder-pro-v2.5`
- success: True  | final: 8.61 | quality: 10.0
- latency_total: 14.843s | tokens_per_second: 82.6
- input_tokens: 217 | output_tokens: 1226

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



**Pare un momento. Su aritmética tiene un error crítico.**

Usted está calculando el LTV como si el churn no existiera. Con un churn mensual del 8%, la vida promedio de un cliente no es 24 meses, es **12.5 meses** (1 / 0.08).

Además, el LTV debe calcularse sobre el **margen bruto**, no sobre el precio total. Usted no gana $35 por mes, gana $24.50 (70% de $35).

**Recálculo:**

- Ingreso bruto mensual por cliente: $35 × 70% = **$24.50**
- Vida promedio del cliente: 1 / 8% = **12.5 meses**
- **LTV real = $24.50 × 12.5 = $306.25**

**LTV / CAC = $306.25 / $290 ≈ 1.06**

Eso no es 2.9. Es **1.06**. Por cada dólar que invierte en publicidad, recupera apenas $1.06 en margen bruto. No está cubriendo costos operativos, equipo, ni su propio tiempo.

**Payback period:** $290 / $24.50 ≈ **11.8 meses**. Casi un año para recuperar el CAC, mientras el 8% de sus clientes se fuga cada mes.

**Conclusión:** No invierta los $10,000 en publicidad pagada todavía. Con estos números, escalar con paid ads **destruye valor**. Cada cliente nuevo apenas paga su propio costo de adquisición.

**Qué hacer antes de escalar:**

1. **Baje el CAC** (optimice canales, mejore conversión, pruebe orgánico).
2. **Reduzca el churn** (el 8% mensual es muy alto; si lo baja al 4%, el LTV se duplica).
3. **Suba el precio o mejore el margen** (aunque sea un 10-15% de aumento).
4. **Espere a que LTV/CAC ≥ 3** antes de inyectar capital fuerte en ads.

La rentabilidad actual puede venir de clientes orgánicos o tempranos con CAC cercano a cero. No asuma que ese CAC de $290 es sostenible cuando escale. La aritmética no miente: con estos números, el crecimiento pagado lo va a descapitalizar.